"""
Redrob Hackathon - Configuration Wrapper

This is a wrapper for the project configuration.
For full configuration, use project_config.py directly.
"""

import sys
import os

# Add unified directory to path
UNIFIED_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, UNIFIED_DIR)

# Import all configuration from project_config
from project_config import *

# For compatibility with the guide
__all__ = [
    'PROJECT_NAME', 'PROJECT_VERSION', 'HACKATHON_NAME', 'TEAM_NAME',
    'PYTHON_VERSION_MIN', 'PYTHON_VERSION_MAX',
    'MAX_CANDIDATES', 'MAX_FILE_SIZE_MB', 'MAX_RUNTIME_SECONDS',
    'get_version', 'get_project_info'
]

def get_version():
    """Return the project version."""
    return PROJECT_VERSION

def get_project_info():
    """Return project information dictionary."""
    return {
        'name': PROJECT_NAME,
        'version': PROJECT_VERSION,
        'hackathon': HACKATHON_NAME,
        'team': TEAM_NAME,
        'python_min': f'{PYTHON_VERSION_MIN[0]}.{PYTHON_VERSION_MIN[1]}',
        'python_max': f'{PYTHON_VERSION_MAX[0]}.{PYTHON_VERSION_MAX[1]}',
    }