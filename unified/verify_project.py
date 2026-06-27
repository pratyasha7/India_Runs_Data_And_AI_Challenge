#!/usr/bin/env python
"""
Project Verification for Redrob Hackathon

Checks project health, required files, dependencies, and configuration.
"""

import sys
import os
import platform
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import (
    PYTHON_VERSION_MIN, PYTHON_VERSION_MAX,
    REQUIRED_FILES, REQUIRED_DIRS,
    ENGINE_DIR, SANDBOX_DIR, UNIFIED_DIR,
    SUBMISSIONS_DIR, LOGS_DIR, REPORTS_DIR,
    get_project_info
)


def check_python_version():
    """Check if Python version is compatible."""
    current = sys.version_info[:2]
    min_ver = PYTHON_VERSION_MIN
    max_ver = PYTHON_VERSION_MAX
    
    if min_ver <= current <= max_ver:
        return True, f"Python {current[0]}.{current[1]}"
    else:
        return False, f"Python {current[0]}.{current[1]} (requires {min_ver[0]}.{min_ver[1]} - {max_ver[0]}.{max_ver[1]})"


def check_required_files():
    """Check if all required files exist."""
    missing = []
    for file_path in REQUIRED_FILES:
        if not Path(file_path).exists():
            missing.append(str(file_path))
    return len(missing) == 0, missing


def check_required_directories():
    """Check if all required directories exist."""
    missing = []
    for dir_path in REQUIRED_DIRS:
        if not Path(dir_path).exists():
            missing.append(str(dir_path))
    return len(missing) == 0, missing


def check_dependencies():
    """Check if required packages are installed."""
    required_packages = ['streamlit', 'pandas']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing.append(package)
    
    return len(missing) == 0, missing


def check_dataset():
    """Check if dataset files exist."""
    from project_config import (
        CANDIDATES_JSONL, CANDIDATES_JSONL_GZ, SAMPLE_CANDIDATES_JSON
    )
    
    datasets = []
    if CANDIDATES_JSONL.exists():
        datasets.append("candidates.jsonl")
    if CANDIDATES_JSONL_GZ.exists():
        datasets.append("candidates.jsonl.gz")
    if SAMPLE_CANDIDATES_JSON.exists():
        datasets.append("sample_candidates.json")
    
    # Also check sandbox sample data
    sandbox_sample = SANDBOX_DIR / "sample_data" / "sample_candidates.json"
    if sandbox_sample.exists():
        datasets.append("sandbox/sample_data/sample_candidates.json")
    
    return len(datasets) > 0, datasets


def check_permissions():
    """Check if directories are writable."""
    test_dirs = [SUBMISSIONS_DIR, LOGS_DIR, REPORTS_DIR]
    non_writable = []
    
    for dir_path in test_dirs:
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            test_file = dir_path / ".write_test"
            test_file.write_text("test")
            test_file.unlink()
        except Exception:
            non_writable.append(str(dir_path))
    
    return len(non_writable) == 0, non_writable


def validate_project():
    """
    Run all project validations.
    
    Returns:
        bool: True if all validations pass, False otherwise
    """
    print("=" * 70)
    print("  PROJECT VALIDATION")
    print("=" * 70)
    
    results = []
    
    # Check Python version
    print("\n[1/6] Checking Python version...")
    success, info = check_python_version()
    status = "PASS" if success else "FAIL"
    print(f"  [{status}] {info}")
    results.append(success)
    
    # Check required files
    print("\n[2/6] Checking required files...")
    success, missing = check_required_files()
    status = "PASS" if success else "FAIL"
    if success:
        print(f"  [{status}] All {len(REQUIRED_FILES)} required files found")
    else:
        print(f"  [{status}] Missing {len(missing)} files:")
        for f in missing:
            print(f"    - {f}")
    results.append(success)
    
    # Check required directories
    print("\n[3/6] Checking required directories...")
    success, missing = check_required_directories()
    status = "PASS" if success else "FAIL"
    if success:
        print(f"  [{status}] All {len(REQUIRED_DIRS)} required directories found")
    else:
        print(f"  [{status}] Missing {len(missing)} directories:")
        for d in missing:
            print(f"    - {d}")
    results.append(success)
    
    # Check dependencies
    print("\n[4/6] Checking dependencies...")
    success, missing = check_dependencies()
    status = "PASS" if success else "FAIL"
    if success:
        print(f"  [{status}] All required packages installed")
    else:
        print(f"  [{status}] Missing {len(missing)} packages:")
        for p in missing:
            print(f"    - {p}")
    results.append(success)
    
    # Check dataset
    print("\n[5/6] Checking dataset files...")
    success, datasets = check_dataset()
    status = "PASS" if success else "FAIL"
    if success:
        print(f"  [{status}] Found {len(datasets)} dataset(s):")
        for d in datasets:
            print(f"    - {d}")
    else:
        print(f"  [{status}] No dataset files found")
    results.append(success)
    
    # Check permissions
    print("\n[6/6] Checking directory permissions...")
    success, non_writable = check_permissions()
    status = "PASS" if success else "FAIL"
    if success:
        print(f"  [{status}] All directories are writable")
    else:
        print(f"  [{status}] {len(non_writable)} directories not writable:")
        for d in non_writable:
            print(f"    - {d}")
    results.append(success)
    
    # Summary
    print("\n" + "=" * 70)
    passed = sum(results)
    total = len(results)
    
    if all(results):
        print(f"  [SUCCESS] All {total} checks passed")
        print("=" * 70)
        return True
    else:
        print(f"  [WARNING] {passed}/{total} checks passed")
        print("=" * 70)
        return False


def main():
    """Main function for project verification."""
    success = validate_project()
    
    if success:
        print("\n[SUCCESS] Project is ready for use")
        return 0
    else:
        print("\n[WARNING] Project has some issues that may need attention")
        return 1


if __name__ == "__main__":
    sys.exit(main())