#!/usr/bin/env python
"""
Sandbox Runner for Redrob Hackathon

Launches the existing Streamlit sandbox frontend without modification.
"""

import sys
import subprocess
from pathlib import Path

# Add unified directory to path
UNIFIED_DIR = Path(__file__).parent
sys.path.insert(0, str(UNIFIED_DIR))

from project_config import SANDBOX_DIR, SANDBOX_APP, SANDBOX_REQUIREMENTS


def check_streamlit_installed():
    """Check if Streamlit is installed."""
    try:
        import streamlit
        return True
    except ImportError:
        return False


def install_requirements():
    """Install sandbox requirements."""
    print("[INFO] Installing sandbox requirements...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", str(SANDBOX_REQUIREMENTS)
        ])
        print("[SUCCESS] Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Failed to install requirements: {e}")
        return False


def launch_sandbox(port=8501, host="localhost"):
    """
    Launch the Streamlit sandbox.
    
    Args:
        port: Port number for the sandbox
        host: Host address for the sandbox
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Verify sandbox app exists
        if not SANDBOX_APP.exists():
            print(f"[ERROR] Sandbox app not found: {SANDBOX_APP}")
            return False
        
        # Check if Streamlit is installed
        if not check_streamlit_installed():
            print("[WARNING] Streamlit not installed. Installing...")
            if not install_requirements():
                return False
        
        # Launch Streamlit
        print(f"[INFO] Launching Streamlit sandbox...")
        print(f"[INFO] URL: http://{host}:{port}")
        print("[INFO] Press Ctrl+C to stop the server")
        
        # Change to sandbox directory
        original_dir = Path.cwd()
        import os
        os.chdir(SANDBOX_DIR)
        
        # Launch Streamlit
        cmd = [
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", str(port),
            "--server.address", host
        ]
        
        subprocess.run(cmd)
        
        # Restore original directory
        os.chdir(original_dir)
        
        return True
        
    except KeyboardInterrupt:
        print("\n[INFO] Sandbox stopped by user")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to launch sandbox: {e}")
        return False


def main():
    """Main function for sandbox runner."""
    print("=" * 70)
    print("  REDROB HACKATHON - STREAMLIT SANDBOX")
    print("=" * 70)
    
    # Parse command line arguments
    port = 8501
    host = "localhost"
    
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    if len(sys.argv) > 2:
        host = sys.argv[2]
    
    # Launch the sandbox
    success = launch_sandbox(port, host)
    
    if success:
        print("\n[SUCCESS] Sandbox execution completed")
        return 0
    else:
        print("\n[ERROR] Sandbox execution failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())