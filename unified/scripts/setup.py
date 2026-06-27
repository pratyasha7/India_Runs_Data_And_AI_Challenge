#!/usr/bin/env python
"""
Setup Script for Redrob Hackathon

Creates necessary directories and checks dependencies.
"""

import sys
import os
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    REQUIRED_DIRS, SUBMISSIONS_DIR, LOGS_DIR, REPORTS_DIR
)


def create_directories():
    """Create all required directories."""
    print("[INFO] Creating directories...")
    
    for dir_path in REQUIRED_DIRS:
        try:
            Path(dir_path).mkdir(parents=True, exist_ok=True)
            print(f"  [OK] {dir_path}")
        except Exception as e:
            print(f"  [ERROR] Failed to create {dir_path}: {e}")
            return False
    
    return True


def check_python_version():
    """Check Python version."""
    print("\n[INFO] Checking Python version...")
    current = sys.version_info[:2]
    min_ver = (3, 10)
    
    if current >= min_ver:
        print(f"  [OK] Python {current[0]}.{current[1]}")
        return True
    else:
        print(f"  [ERROR] Python {current[0]}.{current[1]} (requires {min_ver[0]}.{min_ver[1]}+)")
        return False


def check_dependencies():
    """Check if required packages are installed."""
    print("\n[INFO] Checking dependencies...")
    
    required_packages = ['streamlit', 'pandas']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  [OK] {package}")
        except ImportError:
            print(f"  [MISSING] {package}")
            missing.append(package)
    
    if missing:
        print(f"\n[INFO] Missing packages: {', '.join(missing)}")
        print("[INFO] Install with: pip install -r sandbox/requirements.txt")
        return False
    
    return True


def setup_project():
    """Run complete project setup."""
    print("=" * 70)
    print("  REDROB HACKATHON - PROJECT SETUP")
    print("=" * 70)
    
    results = []
    
    # Check Python version
    results.append(check_python_version())
    
    # Create directories
    results.append(create_directories())
    
    # Check dependencies
    results.append(check_dependencies())
    
    # Summary
    print("\n" + "=" * 70)
    if all(results):
        print("  [SUCCESS] Setup completed successfully")
        print("=" * 70)
        return True
    else:
        print("  [WARNING] Setup completed with some issues")
        print("=" * 70)
        return False


def main():
    """Main function for setup script."""
    success = setup_project()
    
    if success:
        print("\n[SUCCESS] Project is ready for use")
        print("\nNext steps:")
        print("  1. Place dataset in datasets/ directory")
        print("  2. Run: python unified/launch.py")
        return 0
    else:
        print("\n[WARNING] Please resolve the issues above")
        return 1


if __name__ == "__main__":
    sys.exit(main())