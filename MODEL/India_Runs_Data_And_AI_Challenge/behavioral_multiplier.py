from datetime import datetime

# Reusing the robust string, int, and float parsers from Pratyasha's module to prevent duplicate code
from quality_controller import _safe_str, _safe_int, _safe_float

def calculate_behavioral_multiplier(candidate) -> float:
    """
    Process platform behavioral signals to calculate a final score multiplier (0.1 to 2.07) [3].
    Adjusts score based on Location/Relocation, Notice Period, Activity, and Responsiveness [3].
    """
    profile = candidate.get("profile", {}) or {}
    signals = candidate.get("redrob_signals", {}) or {}
    
    multiplier = 1.0

    # Noida/Pune Location & Relocation Filter
    # JD requires hybrid/onsite in Pune/Noida. We prioritize local candidates or those willing to move,
    # and heavily downweight candidates stuck abroad who refuse to relocate
    loc = _safe_str(profile.get("location")).lower()
    country = _safe_str(profile.get("country")).lower()
    
    willing_to_relocate = bool(signals.get("willing_to_relocate", False))
    preferred_work_mode = _safe_str(signals.get("preferred_work_mode")).lower()

    # Indian tech hubs welcomed in the JD
    indian_tech_hubs = ["noida", "pune", "delhi", "mumbai", "hyderabad", "bangalore", "gurgaon"]
    is_local_india = any(city in loc for city in indian_tech_hubs) or "india" in country

    if is_local_india:
        multiplier *= 1.2
    elif willing_to_relocate and preferred_work_mode in ["hybrid", "flexible", "onsite"]:
        multiplier *= 1.1
    else:
        multiplier *= 0.1

    # --- Notice Period Modifiers ---
    # JD prefers sub-30 day notice, buyouts are supported up to 30 days, and 30+ days have a higher bar
    notice = _safe_int(signals.get("notice_period_days", 180))
    if notice <= 30:
        multiplier *= 1.25
    elif 31 <= notice <= 60:
        multiplier *= 1.0
    elif 61 <= notice <= 90:
        # 61-90 days is typical in India but represents a slow pipeline, so we apply a slight penalty
        multiplier *= 0.8
    else:
        multiplier *= 0.5

    # Platform Activity Recency
    # Perfect resumes don't matter if they are "ghosts" who haven't logged in for months.
    try:
        last_active_str = _safe_str(signals.get("last_active_date", ""))
        last_active = datetime.strptime(last_active_str, "%Y-%m-%d")
        
        # Challenge timeline anchor: June 24, 2026
        days_inactive = (datetime(2026, 6, 24) - last_active).days
        
        if days_inactive <= 14:
            multiplier *= 1.2
        elif 15 <= days_inactive <= 45:
            multiplier *= 1.0
        elif 46 <= days_inactive <= 90:
            multiplier *= 0.7
        else:
            multiplier *= 0.4
    except (ValueError, TypeError):
        multiplier *= 0.5

    # Recruiter Responsiveness 
    resp_rate = _safe_float(signals.get("recruiter_response_rate", 0.0))
    resp_time = _safe_float(signals.get("avg_response_time_hours", 72.0))
    
    if resp_rate > 0.75 and resp_time < 24.0:
        multiplier *= 1.15
    elif resp_rate < 0.20 or resp_time > 120.0:
        multiplier *= 0.5

    return round(multiplier, 4)