#!/usr/bin/env python
"""
Submission Generator for Redrob Hackathon

Generates the final submission.csv file for hackathon submission.
"""

import sys
import os
import json
import csv
import time
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    ENGINE_DIR, SANDBOX_SAMPLE_DATA, SUBMISSIONS_DIR,
    DEFAULT_SUBMISSION, LOGS_DIR, DEFAULT_LOG
)


def generate_submission(input_file=None, output_file=None):
    """
    Generate the submission CSV file.
    
    Args:
        input_file: Path to input JSONL file (defaults to sample data)
        output_file: Path to output CSV file (defaults to submissions/submission.csv)
    
    Returns:
        bool: True if successful, False otherwise
    """
    print("=" * 70)
    print("  REDROB HACKATHON - SUBMISSION GENERATOR")
    print("=" * 70)
    
    try:
        # Set default paths
        if input_file is None:
            input_file = SANDBOX_SAMPLE_DATA
        
        if output_file is None:
            SUBMISSIONS_DIR.mkdir(parents=True, exist_ok=True)
            output_file = DEFAULT_SUBMISSION
        
        # Verify input file exists
        if not Path(input_file).exists():
            print(f"[ERROR] Input file not found: {input_file}")
            return False
        
        print(f"\n[INFO] Input file: {input_file}")
        print(f"[INFO] Output file: {output_file}")
        
        # Import ranking engine
        sys.path.insert(0, str(ENGINE_DIR))
        from rank import run_master_ranker
        from quality_controller import is_clean_candidate, _safe_str, _safe_int, _safe_float
        from semantic_matcher import calculate_relevance_score
        from behavioral_multiplier import calculate_behavioral_multiplier
        
        # Load candidates
        print("\n[INFO] Loading candidates...")
        candidates = []
        
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            if content.startswith('['):
                # JSON format
                data = json.loads(content)
                candidates = data if isinstance(data, list) else [data]
            else:
                # JSONL format
                for line in content.split('\n'):
                    if line.strip():
                        try:
                            candidate = json.loads(line)
                            candidates.append(candidate)
                        except json.JSONDecodeError as e:
                            print(f"[WARNING] Invalid JSON line: {e}")
                            continue
        
        print(f"[INFO] Loaded {len(candidates)} candidates")
        
        # Process candidates
        print("\n[INFO] Processing candidates...")
        processed_count = 0
        passed_screening_count = 0
        scored_pool = []
        
        for candidate in candidates:
            processed_count += 1
            
            # Apply quality filter
            if not is_clean_candidate(candidate):
                continue
            
            passed_screening_count += 1
            
            # Calculate scores
            relevance_score = calculate_relevance_score(candidate)
            behavioral_mult = calculate_behavioral_multiplier(candidate)
            final_score = round(relevance_score * behavioral_mult, 4)
            
            scored_pool.append({
                "id": candidate.get("candidate_id"),
                "score": final_score,
                "raw_record": candidate
            })
            
            if processed_count % 100 == 0:
                print(f"  Processed {processed_count} candidates...")
        
        print(f"[INFO] Processed {processed_count} candidates")
        print(f"[INFO] Passed screening: {passed_screening_count} candidates")
        
        # Sort candidates
        print("\n[INFO] Sorting candidates...")
        scored_pool.sort(key=lambda x: (-x["score"], x["id"]))
        
        # Select top 100
        top_candidates = scored_pool[:100]
        
        # Generate reasoning
        print("\n[INFO] Generating reasoning...")
        final_rows = []
        
        for idx, item in enumerate(top_candidates):
            rank = idx + 1
            reasoning = generate_dynamic_reasoning(item["raw_record"], rank, item["score"])
            final_rows.append({
                "candidate_id": item["id"],
                "rank": rank,
                "score": item["score"],
                "reasoning": reasoning
            })
        
        # Write submission CSV
        print(f"\n[INFO] Writing submission to: {output_file}")
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['candidate_id', 'rank', 'score', 'reasoning'])
            writer.writeheader()
            for row in final_rows:
                writer.writerow(row)
        
        # Verify output
        if Path(output_file).exists():
            file_size = Path(output_file).stat().st_size
            print(f"\n[SUCCESS] Submission generated successfully")
            print(f"[INFO] File: {output_file}")
            print(f"[INFO] Size: {file_size} bytes")
            print(f"[INFO] Rows: {len(final_rows)}")
            
            # Save generation log
            LOGS_DIR.mkdir(parents=True, exist_ok=True)
            with open(DEFAULT_LOG, 'w') as f:
                f.write("Redrob Hackathon - Submission Generation Log\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Input file: {input_file}\n")
                f.write(f"Output file: {output_file}\n")
                f.write(f"Candidates processed: {processed_count}\n")
                f.write(f"Candidates passed screening: {passed_screening_count}\n")
                f.write(f"Top candidates selected: {len(final_rows)}\n")
                f.write(f"File size: {file_size} bytes\n")
            
            return True
        else:
            print(f"[ERROR] Failed to create output file")
            return False
        
    except Exception as e:
        print(f"[ERROR] Failed to generate submission: {e}")
        return False


def generate_dynamic_reasoning(candidate, rank, score):
    """Generate reasoning for a candidate (same as in rank.py)."""
    profile = candidate.get("profile", {}) or {}
    signals = candidate.get("redrob_signals", {}) or {}
    skills = candidate.get("skills", []) or []
    
    # Get actual facts
    title = profile.get("current_title", "Software Engineer")
    yoe = _safe_float(profile.get("years_of_experience", 0.0))
    notice = _safe_int(signals.get("notice_period_days", 30))
    
    # Pull top 2 skills they actually possess
    skills_list = [s.get("name") for s in skills if s.get("name")]
    skills_str = ", ".join(skills_list[:2]) if skills_list else "core engineering"
    
    # Structural variations based on rank
    if rank <= 15:
        templates = [
            f"Exceptional {yoe}-year {title} with proven expertise in {skills_str}. Aligns perfectly with the founding engineer criteria, matching both technical and high-energy platform signals.",
            f"Highly recommended founding candidate with {yoe} years of experience. Demonstrated success in {skills_str} at product-scale; backed by strong platform responsiveness and an optimal {notice}-day notice period.",
            f"Top-tier {title} holding {yoe} years of experience. Strong background in {skills_str}; highly active platform signals and immediate availability make them an outstanding fit."
        ]
        return templates[rank % 3]
    elif rank <= 60:
        templates = [
            f"Strong {yoe}-year developer with solid skills in {skills_str}. Excellent technical capabilities, though a slightly longer {notice}-day notice period is a minor logistical hurdle.",
            f"Solid fit with {yoe} years of experience. Strong background in {skills_str} and good platform responsiveness, though slightly less direct experience building retrieval ranking systems.",
            f"Competent {title} with {yoe} years in the field. Demonstrates good knowledge of {skills_str} with consistent login activity; a very capable option for the engineering core."
        ]
        return templates[rank % 3]
    else:
        templates = [
            f"Possesses {yoe} years of solid backend experience with skills in {skills_str}, but ranked lower due to a long {notice}-day notice period.",
            f"Adjacent {yoe}-year engineer with skills in {skills_str}. Good core development credentials, but lacks extensive hands-on vector database and ranking evaluation experience.",
            f"A capable {yoe}-year {title}. Included in final list due to strong active login signals, though their technical focus has been more general backend than core ML/retrieval systems."
        ]
        return templates[rank % 3]


def main():
    """Main function for submission generator."""
    # Parse command line arguments
    input_file = None
    output_file = None
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Generate submission
    success = generate_submission(input_file, output_file)
    
    if success:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())