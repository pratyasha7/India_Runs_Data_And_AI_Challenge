# Unified Integration Layer

## Overview

This directory contains the integration layer for the Redrob Candidate Ranking System. It orchestrates the existing projects (Version 1 backend and Streamlit sandbox) without modification.

## Contents

| File/Directory | Purpose |
|----------------|---------|
| `launch.py` | Full-featured entry point with menu options |
| `launcher.py` | Simple launcher (wrapper for launch.py) |
| `run_backend.py` | Backend execution wrapper |
| `run_sandbox.py` | Sandbox launch wrapper |
| `verify_project.py` | Project health checks |
| `project_config.py` | Project configuration (full version) |
| `config.py` | Configuration wrapper (for compatibility) |
| `scripts/` | Helper scripts (setup, validate, benchmark, generate_submission) |
| `docs/` | Comprehensive documentation |
| `configs/` | Configuration files (paths, constants) |
| `outputs/` | Generated outputs (submissions, logs, reports) |
| `examples/` | Example files and documentation |
| `requirements.txt` | Unified layer dependencies |
| `README.md` | This file |

## Architecture

```
unified/
|
+-- launch.py                   # Full-featured entry point
+-- launcher.py                 # Simple launcher (wrapper)
+-- run_backend.py              # Backend runner
+-- run_sandbox.py              # Sandbox runner
+-- verify_project.py           # Project verification
+-- project_config.py           # Project configuration (full)
+-- config.py                   # Configuration wrapper
+-- requirements.txt            # Dependencies
+-- scripts/
|   +-- setup.py                # Project setup
|   +-- validate.py             # Comprehensive validation
|   +-- benchmark.py            # Performance benchmarking
|   +-- generate_submission.py  # Submission generation
+-- docs/
|   +-- ARCHITECTURE.md         # System architecture
|   +-- PROJECT_STRUCTURE.md    # Repository structure
|   +-- LOCAL_SETUP.md          # Local setup guide
|   +-- DATASET_GUIDE.md        # Dataset format guide
|   +-- SANDBOX_GUIDE.md        # Sandbox usage guide
|   +-- BACKEND_GUIDE.md        # Backend usage guide
|   +-- EXECUTION_GUIDE.md      # Execution guide
|   +-- TESTING_GUIDE.md        # Testing guide
|   +-- DEPLOYMENT_GUIDE.md     # Deployment guide
|   +-- SUBMISSION_GUIDE.md     # Submission guide
|   +-- TROUBLESHOOTING.md      # Troubleshooting guide
+-- configs/
|   +-- paths.py                # Path configuration
|   +-- constants.py            # Constants and settings
+-- outputs/
|   +-- submissions/            # Generated submission CSVs
|   +-- logs/                   # Execution logs
|   +-- reports/                # Benchmark and validation reports
+-- examples/
|   +-- sample_execution.md     # Example execution
|   +-- expected_output.md      # Expected output format
```

## How to Use

### Single Entry Point (Full Features)

```bash
python unified/launch.py
```

This provides a menu with options:
1. Run Backend (Ranking Engine)
2. Run Sandbox (Streamlit Frontend)
3. Run Benchmark
4. Validate Project
5. Generate Submission
6. View Project Info
7. Exit

### Simple Launcher (Wrapper)

```bash
python unified/launcher.py
```

This provides a simplified interface that wraps the full launcher.

### Individual Scripts

#### Run Backend

```bash
python unified/run_backend.py
```

#### Run Sandbox

```bash
python unified/run_sandbox.py
```

#### Validate Project

```bash
python unified/verify_project.py
```

#### Generate Submission

```bash
python unified/scripts/generate_submission.py
```

#### Run Benchmark

```bash
python unified/scripts/benchmark.py
```

## Scripts

### setup.py

Creates necessary directories and checks dependencies.

```bash
python unified/scripts/setup.py
```

### validate.py

Runs comprehensive validation of the project.

```bash
python unified/scripts/validate.py
```

### benchmark.py

Runs performance benchmarks on the ranking engine.

```bash
python unified/scripts/benchmark.py
```

### generate_submission.py

Generates the final submission.csv file.

```bash
python unified/scripts/generate_submission.py
```

## Configuration

### project_config.py

Defines project paths, metadata, and configuration.

### configs/paths.py

Defines all file and directory paths used in the project.

### configs/constants.py

Defines project constants and configuration values.

## Documentation

All documentation is located in the `docs/` directory:

| File | Description |
|------|-------------|
| ARCHITECTURE.md | System architecture and design |
| PROJECT_STRUCTURE.md | Repository structure overview |
| LOCAL_SETUP.md | Local development setup guide |
| DATASET_GUIDE.md | Dataset format and placement |
| SANDBOX_GUIDE.md | Streamlit frontend guide |
| BACKEND_GUIDE.md | Ranking engine guide |
| EXECUTION_GUIDE.md | How to run the system |
| TESTING_GUIDE.md | Testing procedures |
| DEPLOYMENT_GUIDE.md | Deployment instructions |
| SUBMISSION_GUIDE.md | Hackathon submission guide |
| TROUBLESHOOTING.md | Common issues and solutions |

## Outputs

### submissions/

Contains generated submission.csv files.

### logs/

Contains execution logs.

### reports/

Contains benchmark and validation reports.

## Integration Principles

This layer must never duplicate:
- AI logic
- Scoring
- Behavioral processing
- Semantic matching
- Fraud detection
- Ranking

It should simply orchestrate the existing implementations.

The Version 1 backend remains the single source of truth.

The Streamlit sandbox remains the presentation layer.

The unified folder becomes the project management and integration layer.

## Dependencies

- Python 3.10+
- Streamlit (for sandbox)
- Pandas (for sandbox)

## References

- [README](../README.md)
- [Documentation](docs/)
- [Scripts](scripts/)

## License

This project was built for the Redrob Hackathon competition.