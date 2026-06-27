
import os
from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent
TASK15_DIR = BASE_DIR
MODEL_DIR = TASK15_DIR / "MODEL"
SANDBOX_DIR = TASK15_DIR / "sandbox"
UNIFIED_DIR = TASK15_DIR / "unified"

# Version 1 Engine paths
ENGINE_DIR = MODEL_DIR / "India_Runs_Data_And_AI_Challenge"
ENGINE_RANK = ENGINE_DIR / "rank.py"
ENGINE_QUALITY_CONTROLLER = ENGINE_DIR / "quality_controller.py"
ENGINE_SEMANTIC_MATCHER = ENGINE_DIR / "semantic_matcher.py"
ENGINE_BEHAVIORAL_MULTIPLIER = ENGINE_DIR / "behavioral_multiplier.py"

# Sandbox paths
SANDBOX_APP = SANDBOX_DIR / "app.py"
SANDBOX_REQUIREMENTS = SANDBOX_DIR / "requirements.txt"
SANDBOX_SAMPLE_DATA = SANDBOX_DIR / "sample_data" / "sample_candidates.json"

# Unified paths
SCRIPTS_DIR = UNIFIED_DIR / "scripts"
DOCS_DIR = UNIFIED_DIR / "docs"
CONFIGS_DIR = UNIFIED_DIR / "configs"
OUTPUTS_DIR = UNIFIED_DIR / "outputs"
EXAMPLES_DIR = UNIFIED_DIR / "examples"

# Output paths
SUBMISSIONS_DIR = OUTPUTS_DIR / "submissions"
LOGS_DIR = OUTPUTS_DIR / "logs"
REPORTS_DIR = OUTPUTS_DIR / "reports"

# Default output files
DEFAULT_SUBMISSION = SUBMISSIONS_DIR / "submission.csv"
DEFAULT_LOG = LOGS_DIR / "ranking.log"
DEFAULT_BENCHMARK_REPORT = REPORTS_DIR / "benchmark.txt"
DEFAULT_VALIDATION_REPORT = REPORTS_DIR / "validation.txt"

# Dataset paths (expected locations)
DATASETS_DIR = BASE_DIR / "datasets"
CANDIDATES_JSONL = DATASETS_DIR / "candidates.jsonl"
CANDIDATES_JSONL_GZ = DATASETS_DIR / "candidates.jsonl.gz"
SAMPLE_CANDIDATES_JSON = DATASETS_DIR / "sample_candidates.json"

# Project metadata
PROJECT_NAME = "Redrob Candidate Ranking System"
PROJECT_VERSION = "1.0.0"
HACKATHON_NAME = "India Runs Data and AI Challenge"
TEAM_NAME = "Redrob Hackathon Team"

# Configuration files
CONFIG_FILES = {
    "paths": CONFIGS_DIR / "paths.py",
    "constants": CONFIGS_DIR / "constants.py",
}

# Documentation files
DOC_FILES = {
    "architecture": DOCS_DIR / "ARCHITECTURE.md",
    "project_structure": DOCS_DIR / "PROJECT_STRUCTURE.md",
    "local_setup": DOCS_DIR / "LOCAL_SETUP.md",
    "dataset_guide": DOCS_DIR / "DATASET_GUIDE.md",
    "sandbox_guide": DOCS_DIR / "SANDBOX_GUIDE.md",
    "backend_guide": DOCS_DIR / "BACKEND_GUIDE.md",
    "execution_guide": DOCS_DIR / "EXECUTION_GUIDE.md",
    "testing_guide": DOCS_DIR / "TESTING_GUIDE.md",
    "deployment_guide": DOCS_DIR / "DEPLOYMENT_GUIDE.md",
    "submission_guide": DOCS_DIR / "SUBMISSION_GUIDE.md",
    "troubleshooting": DOCS_DIR / "TROUBLESHOOTING.md",
}

# Required files for project validation
REQUIRED_FILES = [
    ENGINE_RANK,
    ENGINE_QUALITY_CONTROLLER,
    ENGINE_SEMANTIC_MATCHER,
    ENGINE_BEHAVIORAL_MULTIPLIER,
    SANDBOX_APP,
    SANDBOX_REQUIREMENTS,
    SANDBOX_SAMPLE_DATA,
]

# Required directories
REQUIRED_DIRS = [
    MODEL_DIR,
    SANDBOX_DIR,
    UNIFIED_DIR,
    SCRIPTS_DIR,
    DOCS_DIR,
    CONFIGS_DIR,
    OUTPUTS_DIR,
    SUBMISSIONS_DIR,
    LOGS_DIR,
    REPORTS_DIR,
]

# Python version requirements
PYTHON_VERSION_MIN = (3, 10)
PYTHON_VERSION_MAX = (3, 12)

# Runtime requirements
MAX_CANDIDATES = 100
MAX_FILE_SIZE_MB = 10
MAX_RUNTIME_SECONDS = 30

def get_version():
    """Return the project version."""
    return PROJECT_VERSION

def get_project_info():
    """Return project information dictionary."""
    return {
        "name": PROJECT_NAME,
        "version": PROJECT_VERSION,
        "hackathon": HACKATHON_NAME,
        "team": TEAM_NAME,
        "python_min": f"{PYTHON_VERSION_MIN[0]}.{PYTHON_VERSION_MIN[1]}",
        "python_max": f"{PYTHON_VERSION_MAX[0]}.{PYTHON_VERSION_MAX[1]}",
    }