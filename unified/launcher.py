#!/usr/bin/env python
"""
Redrob Hackathon - Simple Launcher

This is a simple wrapper for the unified launch system.
For full functionality, use launch.py directly.
"""

import sys
import os

# Add unified directory to path
UNIFIED_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, UNIFIED_DIR)

def main():
    """Main launcher function."""
    print("=" * 70)
    print("  REDROB HACKATHON - CANDIDATE RANKING SYSTEM")
    print("  Simple Launcher")
    print("=" * 70)
    print()
    print("This launcher provides a simplified interface.")
    print("For full options, run: python launch.py")
    print()
    
    # Import and run the full launcher
    try:
        from launch import main as launch_main
        launch_main()
    except ImportError as e:
        print(f"[ERROR] Failed to import launch module: {e}")
        print("[INFO] Please run from the unified directory")
        return 1
    except Exception as e:
        print(f"[ERROR] Launch failed: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())