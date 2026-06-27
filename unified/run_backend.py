#!/usr/bin/env python
"""
Backend Runner for Redrob Hackathon

Imports and executes the existing Version 1 ranking engine without modification.
"""

import sys
import os
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    ENGINE_DIR, SANDBOX_SAMPLE_DATA, DEFAULT_SUBMISSION,
    SUBMISSIONS_DIR, LOGS_DIR, DEFAULT_LOG
)


def run_ranking_engine(input_file=None, output_file=None):
    """
    Run the Version 1 ranking engine.
    
    Args:
        input_file: Path to input JSONL file (defaults to sample data)
        output_file: Path to output CSV file (defaults to submissions/submission.csv)
    
    Returns:
        bool: True if successful, False otherwise
    """
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
        
        # Add engine directory to path
        sys.path.insert(0, str(ENGINE_DIR))
        
        # Import the existing ranking engine
        from rank import run_master_ranker
        
        # Change to engine directory for proper execution
        original_dir = os.getcwd()
        os.chdir(ENGINE_DIR)
        
        # Run the ranking engine
        print(f"[INFO] Running ranking engine...")
        print(f"[INFO] Input: {input_file}")
        print(f"[INFO] Output: {output_file}")
        
        # Execute the ranking engine
        run_master_ranker()
        
        # Restore original directory
        os.chdir(original_dir)
        
        # Verify output was created
        output_path = Path(output_file)
        if not output_path.exists():
            # Check if output was created in engine directory
            engine_output = ENGINE_DIR / "submission.csv"
            if engine_output.exists():
                # Move to desired location
                import shutil
                SUBMISSIONS_DIR.mkdir(parents=True, exist_ok=True)
                shutil.move(str(engine_output), str(output_file))
                print(f"[INFO] Moved submission to: {output_file}")
        
        print(f"[SUCCESS] Ranking engine completed")
        return True
        
    except Exception as e:
        print(f"[ERROR] Failed to run ranking engine: {e}")
        return False


def main():
    """Main function for backend runner."""
    print("=" * 70)
    print("  REDROB HACKATHON - BACKEND RANKING ENGINE")
    print("=" * 70)
    
    # Parse command line arguments
    input_file = None
    output_file = None
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    # Run the ranking engine
    success = run_ranking_engine(input_file, output_file)
    
    if success:
        print("\n[SUCCESS] Backend execution completed successfully")
        return 0
    else:
        print("\n[ERROR] Backend execution failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())