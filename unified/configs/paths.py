"""
Path Configuration for Redrob Hackathon

Defines all file and directory paths used in the project.
"""

from pathlib import Path

# Base paths
BASE_DIR = Path(__file__).parent.parent.parent
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

# Documentation files
README_FILES = {
    "root": TASK15_DIR / "README.md",
    "model": MODEL_DIR / "README.md",
    "sandbox": SANDBOX_DIR / "README.md",
    "unified": UNIFIED_DIR / "README.md",
    "docs": DOCS_DIR / "README.md",
    "scripts": SCRIPTS_DIR / "README.md",
    "outputs": OUTPUTS_DIR / "README.md",
    "examples": EXAMPLES_DIR / "README.md",
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