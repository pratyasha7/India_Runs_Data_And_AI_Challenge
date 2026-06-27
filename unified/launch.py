#!/usr/bin/env python
"""
Redrob Hackathon - Unified Project Launcher

Single entry point for the entire Redrob Candidate Ranking System.
Provides options to run backend, sandbox, benchmark, validation, and submission generation.
"""

import sys
import os
import subprocess
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    PROJECT_NAME, PROJECT_VERSION, HACKATHON_NAME,
    SANDBOX_DIR, ENGINE_DIR, SUBMISSIONS_DIR,
    get_project_info
)


def print_banner():
    """Print the project banner."""
    print("=" * 70)
    print(f"  {PROJECT_NAME}")
    print(f"  {HACKATHON_NAME}")
    print(f"  Version {PROJECT_VERSION}")
    print("=" * 70)


def print_menu():
    """Print the main menu."""
    print("\nSelect an option:")
    print("  1. Run Backend (Ranking Engine)")
    print("  2. Run Sandbox (Streamlit Frontend)")
    print("  3. Run Benchmark")
    print("  4. Validate Project")
    print("  5. Generate Submission")
    print("  6. View Project Info")
    print("  7. Exit")
    print("-" * 70)


def run_backend():
    """Run the Version 1 ranking engine."""
    print("\n[INFO] Starting Backend Ranking Engine...")
    try:
        from run_backend import run_ranking_engine
        result = run_ranking_engine()
        if result:
            print("[SUCCESS] Backend execution completed successfully")
        else:
            print("[ERROR] Backend execution failed")
        return result
    except Exception as e:
        print(f"[ERROR] Failed to run backend: {e}")
        return False


def run_sandbox():
    """Launch the Streamlit sandbox."""
    print("\n[INFO] Starting Streamlit Sandbox...")
    try:
        from run_sandbox import launch_sandbox
        launch_sandbox()
    except Exception as e:
        print(f"[ERROR] Failed to launch sandbox: {e}")
        return False


def run_benchmark():
    """Run the benchmark script."""
    print("\n[INFO] Starting Benchmark...")
    try:
        sys.path.insert(0, str(UNIFIED_DIR / "scripts"))
        from benchmark import run_benchmark
        result = run_benchmark()
        if result:
            print("[SUCCESS] Benchmark completed successfully")
        else:
            print("[ERROR] Benchmark failed")
        return result
    except Exception as e:
        print(f"[ERROR] Failed to run benchmark: {e}")
        return False


def validate_project():
    """Run the project validation."""
    print("\n[INFO] Starting Project Validation...")
    try:
        from verify_project import validate_project
        result = validate_project()
        if result:
            print("[SUCCESS] Project validation passed")
        else:
            print("[WARNING] Project validation found issues")
        return result
    except Exception as e:
        print(f"[ERROR] Failed to validate project: {e}")
        return False


def generate_submission():
    """Generate the submission CSV."""
    print("\n[INFO] Starting Submission Generation...")
    try:
        sys.path.insert(0, str(UNIFIED_DIR / "scripts"))
        from generate_submission import generate_submission
        result = generate_submission()
        if result:
            print("[SUCCESS] Submission generated successfully")
        else:
            print("[ERROR] Submission generation failed")
        return result
    except Exception as e:
        print(f"[ERROR] Failed to generate submission: {e}")
        return False


def show_project_info():
    """Display project information."""
    info = get_project_info()
    print("\n" + "=" * 70)
    print("PROJECT INFORMATION")
    print("=" * 70)
    for key, value in info.items():
        print(f"  {key.replace('_', ' ').title()}: {value}")
    print("=" * 70)


def main():
    """Main function for the unified launcher."""
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == "1":
                run_backend()
            elif choice == "2":
                run_sandbox()
            elif choice == "3":
                run_benchmark()
            elif choice == "4":
                validate_project()
            elif choice == "5":
                generate_submission()
            elif choice == "6":
                show_project_info()
            elif choice == "7":
                print("\n[INFO] Exiting...")
                break
            else:
                print("[WARNING] Invalid choice. Please enter a number between 1 and 7.")
        
        except KeyboardInterrupt:
            print("\n\n[INFO] Interrupted by user. Exiting...")
            break
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")
        
        print()


if __name__ == "__main__":
    main()