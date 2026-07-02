import re
from datetime import datetime

# Quick list of major IT consulting/services firms to check against 
SERVICE_COMPANIES = {
    "tcs", "infosys", "wipro", "accenture", "cognizant", "capgemini", 
    "hcl", "tech mahindra", "l&t", "lnt", "mindtree", "cognizant technology solutions"
}

# DEFENSIVE HELPERS (Preventing crashes if fields are missing or corrupted) 

def _safe_str(val) -> str:
    """Convert values to a trimmed string and handle None values gracefully."""
    if val is None:
        return ""
    return str(val).strip()

def _safe_int(val, default=0) -> int:
    """
    Convert input to integer. 
    Handles string-based values like '90 days' or 'immediate' safely using regex [30].
    """
    if val is None:
        return default
    val_str = str(val).strip()
    
    # Extract the first group of digits (e.g. "90 days" -> "90")
    match = re.search(r'\d+', val_str)
    if match:
        try:
            return int(match.group())
        except (ValueError, TypeError):
            pass
            
    # Handle descriptive text entries
    if "immediate" in val_str.lower() or "join now" in val_str.lower():
        return 0
        
    try:
        return int(float(val))
    except (ValueError, TypeError):
        return default

def _safe_float(val, default=0.0) -> float:
    """Convert input to float safely, falling back to 0.0 on type errors."""
    if val is None:
        return default
    try:
        return float(val)
    except (ValueError, TypeError):
        return default

# HONEYPOT AUDITS (Spotting impossible synthetic profile data)

def run_honeypot_audit(candidate) -> bool:
    """
    Runs our 6 anti-fraud checks [4]. 
    Returns True if we detect any fake or logically impossible stats [4].
    """
    profile = candidate.get("profile", {}) or {}
    signals = candidate.get("redrob_signals", {}) or {}
    skills = candidate.get("skills", []) or []
    history = candidate.get("career_history", []) or []  # Points to "career_history"
    
    # Stated YoE is nested inside the profile dictionary [3]
    raw_yoe = _safe_float(profile.get("years_of_experience", 0.0))
    yoe_months = raw_yoe * 12

    # Check 1: Flag if they claim to be highly skilled but have 0 months of experience using it 
    expert_zero = sum(
        1 for s in skills 
        if _safe_str(s.get("proficiency")).lower() in ["expert", "advanced"] 
        and _safe_int(s.get("duration_months"), 1) == 0
    )
    if expert_zero >= 3:
        return True

    # Check 2: Flag if they list many expert skills but average less than a year of experience per skill 
    expert_skills = [
        s for s in skills 
        if _safe_str(s.get("proficiency")).lower() in ["expert", "advanced"]
    ]
    if len(expert_skills) > 8:
        avg_exp_dur = sum(_safe_int(s.get("duration_months"), 0) for s in expert_skills) / len(expert_skills)
        if avg_exp_dur < 12.0:  # Less than an average of 1 year per expert skill
            return True

    # Check 3: Compare total duration of all jobs against their overall stated Years of Experience 
    total_worked_months = sum(_safe_int(job.get("duration_months"), 0) for job in history)
    if yoe_months > 0 and total_worked_months > (yoe_months * 1.85):
        return True

    # Check 4: Compare stated experience years against their actual chronological career span 
    timeline_yoe = total_worked_months / 12.0
    evidence_yoe_sources = [timeline_yoe]
    
    if history:
        try:
            years = []
            for job in history:
                start = _safe_str(job.get("start_date", ""))
                # Pull out the 4-digit start years from their job dates
                start_match = re.search(r"\b(19\d\d|20\d\d)\b", start)
                if start_match:
                    years.append(int(start_match.group(1)))
            if years:
                # Calculate chronological span (using the current year 2026 as our ceiling)
                evidence_yoe_sources.append(2026 - min(years))
        except Exception:
            pass

    max_evidence = max(evidence_yoe_sources) if evidence_yoe_sources else 0.0
    if raw_yoe > 0 and (raw_yoe - max_evidence) > 4.0:
        return True  # Stated experience is way higher than their actual timeline supports

    # Check 5: Flag if they claim advanced skills but have zero platform endorsements 
    expert_no_end = sum(
        1 for s in skills 
        if _safe_str(s.get("proficiency")).lower() in ["expert", "advanced"] 
        and _safe_int(s.get("endorsements"), 0) == 0
    )
    if len(skills) > 0 and (expert_no_end / len(skills)) > 0.5 and len(expert_skills) >= 4:
        return True

    # Check 6: Check for platform telemetry anomalies 
    # A user cannot be active on the platform before their signup date
    try:
        signup = datetime.strptime(_safe_str(signals.get("signup_date", "")), "%Y-%m-%d")
        last_active = datetime.strptime(_safe_str(signals.get("last_active_date", "")), "%Y-%m-%d")
        if signup > last_active:
            return True  # Cannot login before signing up
    except (ValueError, TypeError):
        pass

    # A profile cannot be bookmarked more times than it was viewed
    views = _safe_int(signals.get("profile_views_received_30d", 0))
    saves = _safe_int(signals.get("saved_by_recruiters_30d", 0))
    if saves > views:
        return True  # Cannot save more than was viewed

    # A candidate cannot accept an offer if they completed zero interviews
    if _safe_float(signals.get("offer_acceptance_rate", -1.0)) > 0.0 and _safe_float(signals.get("interview_completion_rate", 0.0)) == 0.0:
        return True  # Cannot accept offers with 0% interview completion

    return False

#  SERVICE COMPANY BLOCKER (Ensuring product/startup experience) 

def check_service_company_disqualifier(candidate) -> bool:
    """
    Check if the candidate has only worked at IT outsourcing/consulting firms [3]. 
    We keep them if they have at least one product company [3].
    """
    history = candidate.get("career_history", []) or []  # Points to "career_history"
    if not history:
        return True  # If they have no listed jobs, we cannot verify product/startup experience

    all_service = True
    for job in history:
        company_name = _safe_str(job.get("company", "")).lower()
        # Check if the company name is on our consulting blocker list 
        is_service = any(service in company_name for service in SERVICE_COMPANIES)
        if not is_service:
            all_service = False
            break  # Found a product-focused company! They are clear to proceed 

    return all_service

#  MASTER GATEKEEPER

def is_clean_candidate(candidate) -> bool:
    """
    Main screening function [4]. 
    Returns True if the candidate passes both the fraud audits and the industry filters [4].
    """
    # First, filter out any impossible bot profiles 
    if run_honeypot_audit(candidate):
        return False
    
    # Next, filter out candidates who have exclusively worked at service firms 
    if check_service_company_disqualifier(candidate):
        return False

    return True