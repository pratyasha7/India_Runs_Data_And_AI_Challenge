#!/usr/bin/env python
"""
Validation Script for Redrob Hackathon

Runs comprehensive validation of the project including backend tests, sandbox tests, and submission validation.
"""

import sys
import os
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    ENGINE_DIR, SANDBOX_DIR, SUBMISSIONS_DIR,
    DEFAULT_SUBMISSION, REPORTS_DIR, DEFAULT_VALIDATION_REPORT
)


def validate_backend():
    """Validate the backend ranking engine."""
    print("\n[1/4] Validating Backend...")
    
    try:
        # Add engine directory to path
        sys.path.insert(0, str(ENGINE_DIR))
        
        # Import modules
        from quality_controller import is_clean_candidate
        from semantic_matcher import calculate_relevance_score
        from behavioral_multiplier import calculate_behavioral_multiplier
        from rank import run_master_ranker
        
        print("  [OK] All backend modules import successfully")
        return True
    except ImportError as e:
        print(f"  [ERROR] Backend import failed: {e}")
        return False


def validate_sandbox():
    """Validate the sandbox frontend."""
    print("\n[2/4] Validating Sandbox...")
    
    try:
        # Check if sandbox app exists
        sandbox_app = SANDBOX_DIR / "app.py"
        if not sandbox_app.exists():
            print(f"  [ERROR] Sandbox app not found: {sandbox_app}")
            return False
        
        # Check if requirements exist
        requirements = SANDBOX_DIR / "requirements.txt"
        if not requirements.exists():
            print(f"  [ERROR] Requirements file not found: {requirements}")
            return False
        
        # Check if Streamlit is installed
        try:
            import streamlit
            print("  [OK] Streamlit is installed")
        except ImportError:
            print("  [WARNING] Streamlit not installed (will be installed on first run)")
        
        print("  [OK] Sandbox structure validated")
        return True
    except Exception as e:
        print(f"  [ERROR] Sandbox validation failed: {e}")
        return False


def validate_submission():
    """Validate the submission CSV if it exists."""
    print("\n[3/4] Validating Submission...")
    
    submission_path = DEFAULT_SUBMISSION
    
    if not submission_path.exists():
        print("  [INFO] No submission.csv found (will be generated on first run)")
        return True
    
    try:
        import csv
        
        with open(submission_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        # Check required columns
        required_columns = ['candidate_id', 'rank', 'score', 'reasoning']
        if not all(col in reader.fieldnames for col in required_columns):
            missing = [col for col in required_columns if col not in reader.fieldnames]
            print(f"  [ERROR] Missing columns: {missing}")
            return False
        
        # Check row count
        if len(rows) != 100:
            print(f"  [WARNING] Expected 100 rows, found {len(rows)}")
        
        # Check data types
        for i, row in enumerate(rows[:5]):  # Check first 5 rows
            try:
                int(row['candidate_id'])
                int(row['rank'])
                float(row['score'])
                str(row['reasoning'])
            except (ValueError, KeyError) as e:
                print(f"  [ERROR] Invalid data at row {i+1}: {e}")
                return False
        
        print(f"  [OK] Submission validated: {len(rows)} rows")
        return True
    except Exception as e:
        print(f"  [ERROR] Submission validation failed: {e}")
        return False


def validate_outputs():
    """Validate output directories."""
    print("\n[4/4] Validating Output Directories...")
    
    required_dirs = [SUBMISSIONS_DIR, REPORTS_DIR]
    
    for dir_path in required_dirs:
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  [OK] {dir_path}")
        except Exception as e:
            print(f"  [ERROR] Failed to create {dir_path}: {e}")
            return False
    
    return True


def run_validation():
    """Run all validation checks."""
    print("=" * 70)
    print("  REDROB HACKATHON - COMPREHENSIVE VALIDATION")
    print("=" * 70)
    
    results = []
    
    # Run validations
    results.append(validate_backend())
    results.append(validate_sandbox())
    results.append(validate_submission())
    results.append(validate_outputs())
    
    # Summary
    print("\n" + "=" * 70)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"  [SUCCESS] All {total} validations passed")
        print("=" * 70)
        
        # Save validation report
        try:
            REPORTS_DIR.mkdir(parents=True, exist_ok=True)
            with open(DEFAULT_VALIDATION_REPORT, 'w') as f:
                f.write("Redrob Hackathon - Validation Report\n")
                f.write("=" * 50 + "\n\n")
                f.write(f"Total checks: {total}\n")
                f.write(f"Passed: {passed}\n")
                f.write(f"Failed: {total - passed}\n\n")
                f.write("All validations passed successfully.\n")
            print(f"\n[INFO] Validation report saved to: {DEFAULT_VALIDATION_REPORT}")
        except Exception as e:
            print(f"\n[WARNING] Failed to save validation report: {e}")
        
        return True
    else:
        print(f"  [WARNING] {passed}/{total} validations passed")
        print("=" * 70)
        return False


def main():
    """Main function for validation script."""
    success = run_validation()
    
    if success:
        print("\n[SUCCESS] Project validation completed successfully")
        return 0
    else:
        print("\n[WARNING] Project validation found some issues")
        return 1


if __name__ == "__main__":
    sys.exit(main())