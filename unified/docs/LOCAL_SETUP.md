# Local Setup Guide

This guide will help you set up the Redrob Candidate Ranking System on your local machine.

## Prerequisites

- Python 3.10 or higher
- Git (for cloning the repository)
- pip (Python package installer)

## Step 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/your-username/TASK15.git

# Navigate to the project directory
cd TASK15
```

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

## Step 3: Install Requirements

```bash
# Install sandbox requirements
pip install -r sandbox/requirements.txt
```

## Step 4: Verify Installation

```bash
# Run project verification
python unified/verify_project.py
```

Expected output:
```
[SUCCESS] All 6 checks passed
[SUCCESS] Project is ready for use
```

## Step 5: Place Dataset

Place your dataset in one of these locations:

### Option A: Use Sample Data (Recommended for testing)
The sample data is already included in `sandbox/sample_data/sample_candidates.json`.

### Option B: Place Custom Dataset
```bash
# Create datasets directory
mkdir datasets

# Copy your dataset
cp /path/to/your/candidates.jsonl datasets/
```

Supported formats:
- `.jsonl` (JSON Lines)
- `.jsonl.gz` (Compressed JSON Lines)
- `.json` (JSON array)

## Step 6: Run Backend

```bash
# Run the ranking engine
python unified/run_backend.py
```

Or use the unified launcher:
```bash
# Launch the menu
python unified/launch.py

# Select option 1: Run Backend
```

## Step 7: Run Sandbox

```bash
# Launch the Streamlit sandbox
python unified/run_sandbox.py
```

Or manually:
```bash
cd sandbox
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

## Step 8: Generate Submission

```bash
# Generate submission.csv
python unified/scripts/generate_submission.py
```

The submission will be saved to `unified/outputs/submissions/submission.csv`.

## Step 9: Validate Submission

```bash
# Run comprehensive validation
python unified/scripts/validate.py
```

## Step 10: Run Benchmark

```bash
# Run performance benchmark
python unified/scripts/benchmark.py
```

## Directory Structure After Setup

```
TASK15/
|
+-- venv/                          # Virtual environment (created)
|
+-- datasets/                      # Dataset directory (created)
|   +-- candidates.jsonl           # Your dataset
|
+-- unified/
    +-- outputs/
        +-- submissions/
        |   +-- submission.csv     # Generated output
        +-- logs/
        |   +-- ranking.log        # Execution logs
        +-- reports/
            +-- benchmark.txt      # Benchmark results
            +-- validation.txt     # Validation report
```

## Quick Start Commands

```bash
# Complete setup in one go
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r sandbox/requirements.txt
python unified/verify_project.py
python unified/launch.py
```

## Verification

After setup, verify everything works:

```bash
# Check project health
python unified/verify_project.py

# Run the test script
cd sandbox
python test_sandbox.py
```

Expected output:
```
[SUCCESS] All tests passed! The sandbox is ready to use.
```

## Next Steps

1. **Explore the sandbox**: Upload a dataset and generate rankings
2. **Read the documentation**: Check `unified/docs/` for detailed guides
3. **Deploy to Streamlit Cloud**: Follow `unified/docs/DEPLOYMENT_GUIDE.md`
4. **Prepare submission**: Follow `unified/docs/SUBMISSION_GUIDE.md`

## Common Issues

### Python Version Error
```
[ERROR] Python 3.9 (requires 3.10 - 3.12)
```
**Solution**: Install Python 3.10 or higher.

### Missing Dependencies
```
[MISSING] streamlit
[MISSING] pandas
```
**Solution**: Run `pip install -r sandbox/requirements.txt`

### Dataset Not Found
```
[INFO] No dataset files found
```
**Solution**: Place your dataset in `datasets/` directory.

For more issues, see `unified/docs/TROUBLESHOOTING.md`.