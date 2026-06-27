# Project Structure

## Repository Overview

```
TASK15/
|
+-- MODEL/                          # Version 1 AI/ML Ranking Engine
|   +-- India_Runs_Data_And_AI_Challenge/
|       +-- rank.py                 # Master orchestrator
|       +-- quality_controller.py   # Fraud detection
|       +-- semantic_matcher.py     # Relevance scoring
|       +-- behavioral_multiplier.py # Signal adjustments
|       +-- README.md               # Backend documentation
|
+-- sandbox/                        # Streamlit Frontend
|   +-- app.py                      # Main Streamlit application
|   +-- components/                 # UI components
|   |   +-- upload.py
|   |   +-- results.py
|   |   +-- metrics.py
|   |   +-- footer.py
|   +-- utils/                      # Utility functions
|   |   +-- runner.py
|   |   +-- validator.py
|   |   +-- file_handler.py
|   |   +-- csv_reader.py
|   +-- sample_data/                # Sample datasets
|   |   +-- sample_candidates.json
|   +-- assets/                     # Static assets
|   +-- requirements.txt            # Python dependencies
|   +-- README.md                   # Sandbox documentation
|   +-- .streamlit/                 # Streamlit configuration
|       +-- config.toml
|
+-- unified/                        # Integration Layer
|   +-- launch.py                   # Single entry point
|   +-- run_backend.py              # Backend runner
|   +-- run_sandbox.py              # Sandbox runner
|   +-- verify_project.py           # Project verification
|   +-- project_config.py           # Project configuration
|   +-- scripts/                    # Helper scripts
|   |   +-- setup.py
|   |   +-- validate.py
|   |   +-- benchmark.py
|   |   +-- generate_submission.py
|   +-- docs/                       # Documentation
|   |   +-- ARCHITECTURE.md
|   |   +-- PROJECT_STRUCTURE.md
|   |   +-- LOCAL_SETUP.md
|   |   +-- DATASET_GUIDE.md
|   |   +-- SANDBOX_GUIDE.md
|   |   +-- BACKEND_GUIDE.md
|   |   +-- EXECUTION_GUIDE.md
|   |   +-- TESTING_GUIDE.md
|   |   +-- DEPLOYMENT_GUIDE.md
|   |   +-- SUBMISSION_GUIDE.md
|   |   +-- TROUBLESHOOTING.md
|   +-- configs/                    # Configuration files
|   |   +-- paths.py
|   |   +-- constants.py
|   +-- outputs/                    # Generated outputs
|   |   +-- submissions/
|   |   +-- logs/
|   |   +-- reports/
|   +-- examples/                   # Example files
|   +-- README.md                   # Unified layer documentation
|
+-- datasets/                       # Input datasets (optional)
|   +-- candidates.jsonl
|   +-- candidates.jsonl.gz
|   +-- sample_candidates.json
|
+-- README.md                       # Root project documentation
```

## Directory Purposes

### MODEL/

Contains the Version 1 AI/ML ranking engine. This is the core backend that performs candidate ranking. **Do not modify these files.**

### sandbox/

Contains the Streamlit frontend application. This provides a professional dashboard for demonstrating the ranking engine. **Do not modify these files.**

### unified/

Contains the integration layer that orchestrates the existing projects. This is the only directory where new code should be added.

### datasets/

Optional directory for storing input datasets. The system can also use datasets from other locations.

## File Purposes

### Core Engine Files

| File | Purpose |
|------|---------|
| `rank.py` | Master orchestrator that coordinates the entire pipeline |
| `quality_controller.py` | Fraud detection and candidate screening |
| `semantic_matcher.py` | Relevance scoring based on keyword matching |
| `behavioral_multiplier.py` | Behavioral signal adjustments |

### Frontend Files

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `upload.py` | File upload component |
| `results.py` | Results display component |
| `metrics.py` | Execution metrics component |
| `footer.py` | Footer component |
| `runner.py` | Pipeline execution utility |
| `validator.py` | Dataset validation utility |
| `file_handler.py` | File handling utility |
| `csv_reader.py` | CSV reading utility |

### Integration Files

| File | Purpose |
|------|---------|
| `launch.py` | Single entry point with menu |
| `run_backend.py` | Backend execution wrapper |
| `run_sandbox.py` | Sandbox launch wrapper |
| `verify_project.py` | Project health checks |
| `project_config.py` | Project configuration |
| `setup.py` | Project setup script |
| `validate.py` | Comprehensive validation |
| `benchmark.py` | Performance benchmarking |
| `generate_submission.py` | Submission generation |

## Navigation Guide

### For New Users
1. Start with `README.md` (root)
2. Read `unified/docs/PROJECT_STRUCTURE.md`
3. Follow `unified/docs/LOCAL_SETUP.md`

### For Developers
1. Review `unified/docs/ARCHITECTURE.md`
2. Understand `unified/docs/BACKEND_GUIDE.md`
3. Check `unified/docs/SANDBOX_GUIDE.md`

### For Deployment
1. Follow `unified/docs/DEPLOYMENT_GUIDE.md`
2. Check `unified/docs/SUBMISSION_GUIDE.md`
3. Review `unified/docs/TROUBLESHOOTING.md`

## Key Relationships

```
unified/launch.py
    |
    +---> unified/run_backend.py
    |         |
    |         +---> MODEL/India_Runs_Data_And_AI_Challenge/rank.py
    |
    +---> unified/run_sandbox.py
              |
              +---> sandbox/app.py
```

The unified layer imports and executes the existing modules without modification.