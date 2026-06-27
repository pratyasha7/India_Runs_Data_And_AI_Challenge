# Redrob Candidate Ranking System

## India Runs Data and AI Challenge

A **purely rule-based, CPU-only candidate ranking pipeline** built in Python with **zero external dependencies**. The system evaluates job candidates and ranks the **Top 100** candidates for a founding engineer role at a search/retrieval systems company.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Hackathon Overview](#hackathon-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Repository Structure](#repository-structure)
- [Technology Stack](#technology-stack)
- [AI/ML Pipeline](#aiml-pipeline)
- [Sandbox Overview](#sandbox-overview)
- [Installation](#installation)
- [Dataset Placement](#dataset-placement)
- [Running Backend](#running-backend)
- [Running Sandbox](#running-sandbox)
- [Running Tests](#running-tests)
- [Running Validator](#running-validator)
- [Generating Submission](#generating-submission)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Submission Checklist](#submission-checklist)
- [Credits](#credits)
- [License](#license)

---

## Project Overview

This system was built for the **Redrob Hackathon** - an "India Runs Data and AI Challenge". It reads candidates from a JSONL database, scores them through a multi-stage pipeline, and outputs a `submission.csv` with the top 100 ranked candidates including personalized reasoning for each selection.

**Key Constraints Met:**
- Runs end-to-end within **5 minutes on CPU**
- Uses only **Python standard library** (no external packages)
- Processes **100K+ candidates** efficiently via streaming
- **Zero network calls** during ranking
- **Deterministic** results across runs
- **Explainable** reasoning for each selection

---

## Hackathon Overview

**Competition**: Redrob Hackathon - India Runs Data and AI Challenge

**Objective**: Build a candidate ranking system for a founding engineer role at a search/retrieval systems company.

**Requirements**:
- Rank Top 100 candidates from ~100,000 applicants
- CPU-only execution (no GPU)
- Explainable reasoning for each selection
- Deterministic results
- Streamlit sandbox demo

**Our Solution**:
- Pure Python implementation with zero dependencies
- Multi-stage ranking pipeline
- Professional Streamlit frontend
- Comprehensive documentation

---

## Features

### Backend (Version 1 Engine)
- **Fraud Detection**: 6 honeypot checks + service company filtering
- **Relevance Scoring**: 5-dimension weighted keyword matching
- **Behavioral Analysis**: Location, notice period, activity, responsiveness
- **Dynamic Reasoning**: Non-templated, rank-tier-based explanations
- **Streaming Processing**: Memory-efficient line-by-line processing
- **Deterministic Sorting**: Score descending, ID ascending for ties

### Frontend (Streamlit Sandbox)
- **Professional Dashboard**: Clean, modern UI with metric cards
- **File Upload**: Support for JSONL, JSON, and compressed JSONL files
- **Real-time Progress**: Live execution status with stage-by-stage updates
- **Results Display**: Sortable dataframe with ranked candidates
- **Execution Metrics**: Detailed performance statistics
- **CSV Download**: Export ranked results as submission.csv

### Integration (Unified Layer)
- **Single Entry Point**: Easy-to-use launcher with menu options
- **Project Verification**: Automated health checks
- **Benchmarking**: Performance measurement tools
- **Submission Generation**: Automated CSV creation
- **Comprehensive Documentation**: Detailed guides for all aspects

---

## Architecture

### High-Level Architecture

```
User
    |
    v
Streamlit Sandbox (Frontend)
    |
    v
Unified Integration Layer
    |
    v
Version 1 Ranking Engine (Backend)
    |
    +---> Quality Controller (Fraud Detection)
    |
    +---> Semantic Matcher (Relevance Scoring)
    |
    +---> Behavioral Multiplier (Signal Adjustments)
    |
    +---> Ranking Engine (Final Selection)
    |
    v
submission.csv (Output)
```

### Component Architecture

```
rank.py (Master Orchestrator)
    |
    +---> quality_controller.py (Fraud Detection & Gating)
    |       +---> Honeypot Audit (6 checks)
    |       +---> Service Company Disqualifier
    |
    +---> semantic_matcher.py (Relevance Scoring)
    |       +---> Dimension A: IR/Search Experience
    |       +---> Dimension B: Vector DB & Embeddings
    |       +---> Dimension C: Evaluation Metrics
    |       +---> Dimension D: Desirable ML Skills
    |       +---> Seniority Alignment Boost/Penalty
    |
    +---> behavioral_multiplier.py (Signal Adjustments)
            +---> Location/Relocation Fit
            +---> Notice Period
            +---> Platform Activity Recency
            +---> Recruiter Responsiveness
```

---

## Repository Structure

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
|   +-- utils/                      # Utility functions
|   +-- sample_data/                # Sample datasets
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
|   +-- docs/                       # Documentation
|   +-- configs/                    # Configuration files
|   +-- outputs/                    # Generated outputs
|   +-- examples/                   # Example files
|   +-- README.md                   # Unified layer documentation
|
+-- datasets/                       # Input datasets (optional)
|
+-- README.md                       # Root project documentation
```

---

## Technology Stack

| Category | Technology |
|----------|------------|
| **Language** | Python 3.10+ |
| **Frontend** | Streamlit |
| **Data Format** | JSONL (input), CSV (output) |
| **Compute** | CPU-only (no GPU required) |
| **Dependencies** | Zero external packages (backend) |
| **Standard Library** | `json`, `csv`, `re`, `datetime`, `time` |
| **Version Control** | Git |
| **Runtime** | <5 minutes on CPU, 16GB RAM |
| **Deployment** | Streamlit Cloud |

---

## AI/ML Pipeline

### Pipeline Flow

```
┌─────────────────────────────────────────────────────────┐
│                    START: candidates.jsonl               │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 1: Quality Gatekeeping (quality_controller.py)   │
│  ├── Honeypot Audit (6 checks)                          │
│  └── Service Company Disqualifier                       │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 2: Relevance Scoring (semantic_matcher.py)       │
│  ├── Dimension A: IR/Search Experience (+0.40)          │
│  ├── Dimension B: Vector DB/Embeddings (+0.25)          │
│  ├── Dimension C: Evaluation Metrics (+0.20)            │
│  ├── Dimension D: Desirable ML (+0.15)                  │
│  └── Seniority/Title/Domain Adjustments                 │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 3: Behavioral Multiplier (behavioral_multiplier.py)
│  ├── Location/Relocation Fit                            │
│  ├── Notice Period                                      │
│  ├── Platform Activity Recency                          │
│  └── Recruiter Responsiveness                           │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 4: Final Scoring & Ranking                       │
│  Final Score = relevance_score × behavioral_multiplier  │
│  Sort: score DESC, candidate_id ASC (tie-break)         │
│  Select Top 100                                         │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│  STAGE 5: Output Generation                             │
│  ├── Generate dynamic reasoning per candidate           │
│  ├── Rank-tier variations (Top/Mid/Lower)               │
│  └── Write submission.csv                               │
└─────────────────────────────────────────────────────────┘
```

### Scoring Methodology

**Final Score Formula**:
```
Final Score = Relevance Score (0.0-1.0) × Behavioral Multiplier (0.1-1.575)
```

**Relevance Score Breakdown**:

| Dimension | Max Points | Weight |
|-----------|------------|--------|
| IR/Search Experience | 0.40 | 40% |
| Vector DB/Embeddings | 0.25 | 25% |
| Evaluation Metrics | 0.20 | 20% |
| Desirable ML | 0.15 | 15% |
| Seniority Boost/Penalty | ±0.10 | Adjustment |
| Title Penalty | -0.15 | Penalty |
| Domain Penalty | -0.15 | Penalty |

---

## Sandbox Overview

The Streamlit sandbox provides a professional, interactive dashboard for demonstrating the ranking engine.

### Features

- **Professional Dashboard**: Clean, modern UI with metric cards
- **File Upload**: Support for JSONL, JSON, and compressed JSONL files
- **Real-time Progress**: Live execution status with stage-by-stage updates
- **Results Display**: Sortable dataframe with ranked candidates
- **Execution Metrics**: Detailed performance statistics
- **CSV Download**: Export ranked results as submission.csv

### Screenshots

*[Add screenshots here]*

### Usage

1. Upload a candidate dataset
2. Click "Generate Rankings"
3. View results and metrics
4. Download submission.csv

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

### Quick Start

```bash
# Clone repository
git clone https://github.com/your-username/TASK15.git
cd TASK15

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r sandbox/requirements.txt

# Verify installation
python unified/verify_project.py
```

### Detailed Installation

See [unified/docs/LOCAL_SETUP.md](unified/docs/LOCAL_SETUP.md) for complete instructions.

---

## Dataset Placement

### Option 1: Use Sample Data (Recommended for testing)

Sample data is included at:
```
sandbox/sample_data/sample_candidates.json
```

### Option 2: Place Custom Dataset

```bash
# Create datasets directory
mkdir datasets

# Copy your dataset
cp /path/to/your/candidates.jsonl datasets/
```

### Supported Formats

- `.jsonl` (JSON Lines) - Recommended
- `.jsonl.gz` (Compressed JSON Lines)
- `.json` (JSON array)

### Dataset Requirements

- Maximum 100 candidates
- Maximum 10MB file size
- Required fields: `candidate_id`, `profile`, `skills`

See [unified/docs/DATASET_GUIDE.md](unified/docs/DATASET_GUIDE.md) for complete specifications.

---

## Running Backend

### Method 1: Using Unified Launcher (Recommended)

```bash
python unified/launch.py
# Select option 1: Run Backend
```

### Method 2: Using Simple Launcher

```bash
python unified/launcher.py
# Select option 1: Run Backend
```

### Method 3: Using Backend Runner

```bash
python unified/run_backend.py
```

### Method 4: Direct Execution

```bash
cd MODEL/India_Runs_Data_And_AI_Challenge
python rank.py
```

### Method 5: Custom Input/Output

```bash
python unified/run_backend.py /path/to/input.jsonl /path/to/output.csv
```

### Expected Output

```
[SUCCESS] Backend execution completed
```

Files generated:
- `submission.csv` in engine directory
- `unified/outputs/submissions/submission.csv`

See [unified/docs/BACKEND_GUIDE.md](unified/docs/BACKEND_GUIDE.md) for complete details.

---

## Running Sandbox

### Method 1: Using Unified Launcher (Recommended)

```bash
python unified/launch.py
# Select option 2: Run Sandbox
```

### Method 2: Using Simple Launcher

```bash
python unified/launcher.py
# Select option 2: Run Sandbox
```

### Method 3: Using Sandbox Runner

```bash
python unified/run_sandbox.py
```

### Method 4: Manual Launch

```bash
cd sandbox
streamlit run app.py
```

### Access Sandbox

Open browser and navigate to:
```
http://localhost:8501
```

### Usage

1. Upload a candidate dataset
2. Click "Generate Rankings"
3. View results and metrics
4. Download submission.csv

See [unified/docs/SANDBOX_GUIDE.md](unified/docs/SANDBOX_GUIDE.md) for complete details.

---

## Running Tests

### Run All Tests

```bash
# Using validation script
python unified/scripts/validate.py

# Using verify project
python unified/verify_project.py
```

### Run Backend Tests

```bash
cd sandbox
python test_sandbox.py
```

### Run Sandbox Tests

```bash
cd sandbox
python test_sandbox.py
```

### Expected Output

```
[SUCCESS] All tests passed! The sandbox is ready to use.
```

See [unified/docs/TESTING_GUIDE.md](unified/docs/TESTING_GUIDE.md) for complete details.

---

## Running Validator

### Comprehensive Validation

```bash
python unified/scripts/validate.py
```

### Project Health Check

```bash
python unified/verify_project.py
```

### Expected Output

```
[SUCCESS] All validations passed
```

See [unified/docs/TESTING_GUIDE.md](unified/docs/TESTING_GUIDE.md) for complete details.

---

## Generating Submission

### Generate Submission CSV

```bash
python unified/scripts/generate_submission.py
```

### Using Unified Launcher

```bash
python unified/launch.py
# Select option 5: Generate Submission
```

### Expected Output

```
[SUCCESS] Submission generated successfully
[INFO] File: unified/outputs/submissions/submission.csv
[INFO] Rows: 100
```

See [unified/docs/SUBMISSION_GUIDE.md](unified/docs/SUBMISSION_GUIDE.md) for complete details.

---

## Deployment

### Streamlit Cloud Deployment

1. Push repository to GitHub
2. Connect to Streamlit Cloud
3. Configure deployment
4. Deploy

See [unified/docs/DEPLOYMENT_GUIDE.md](unified/docs/DEPLOYMENT_GUIDE.md) for complete instructions.

### Other Deployment Options

- Heroku
- AWS Elastic Beanstalk
- Docker

See [unified/docs/DEPLOYMENT_GUIDE.md](unified/docs/DEPLOYMENT_GUIDE.md) for details.

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| Python version error | Install Python 3.10+ |
| Module not found | Run `pip install -r sandbox/requirements.txt` |
| Dataset not found | Place dataset in `datasets/` directory |
| Permission denied | Check file permissions |
| Streamlit won't start | Install Streamlit: `pip install streamlit` |

See [unified/docs/TROUBLESHOOTING.md](unified/docs/TROUBLESHOOTING.md) for complete troubleshooting guide.

---

## Frequently Asked Questions

### Q: What Python version is required?
A: Python 3.10 or higher is required.

### Q: Do I need a GPU?
A: No, the system is CPU-only.

### Q: How long does execution take?
A: <5 seconds for 100 candidates, <5 minutes for 100,000 candidates.

### Q: Can I use my own dataset?
A: Yes, place it in the `datasets/` directory.

### Q: How do I deploy to Streamlit Cloud?
A: See [unified/docs/DEPLOYMENT_GUIDE.md](unified/docs/DEPLOYMENT_GUIDE.md).

### Q: Is the ranking deterministic?
A: Yes, results are consistent across runs.

### Q: Can I modify the ranking logic?
A: The Version 1 engine should not be modified. See [unified/docs/BACKEND_GUIDE.md](unified/docs/BACKEND_GUIDE.md).

---

## Submission Checklist

### Repository
- [ ] GitHub repository is public
- [ ] All code is committed and pushed
- [ ] Documentation is complete
- [ ] No sensitive data included

### Backend
- [ ] Ranking engine executes successfully
- [ ] Runtime is <5 minutes
- [ ] CPU-only execution
- [ ] No external API calls
- [ ] Deterministic results

### Frontend
- [ ] Streamlit sandbox is deployed
- [ ] Sandbox is functional
- [ ] Sample data is included
- [ ] All features work

### Submission
- [ ] submission.csv is generated
- [ ] CSV follows required format
- [ ] Top 100 candidates included
- [ ] Reasoning is provided for each candidate

### Documentation
- [ ] README.md is complete
- [ ] Architecture is documented
- [ ] Setup instructions are clear
- [ ] Usage guide is provided

---

## Credits

### Team Structure

The codebase references team member roles in comments:

- **Pratyasha's Module:** `quality_controller.py` (Fraud detection & gating)
- **Rohan's Scorer:** `semantic_matcher.py` (Relevance scoring)
- **Suvankar's Multiplier:** `behavioral_multiplier.py` (Behavioral signals)
- **Master Orchestrator:** `rank.py` (Pipeline coordination)

### Acknowledgments

- Redrob for organizing the hackathon
- All team members for their contributions
- The open-source community for tools and inspiration

---

## License

This project was built for the Redrob Hackathon competition.

For inquiries, please contact the development team.

---

## Support

- **Documentation**: See `unified/docs/` directory
- **Issues**: GitHub Issues
- **Email**: support@example.com

---

**Last Updated**: June 2026

**Version**: 1.0.0