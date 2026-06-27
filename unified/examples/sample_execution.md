# Sample Execution

## Overview

This document provides a complete example of executing the Redrob Candidate Ranking System from start to finish.

## Prerequisites

- Python 3.10 or higher
- pip package manager
- Git (optional)

## Step 1: Setup Environment

```bash
# Clone repository (if not already done)
git clone https://github.com/your-username/TASK15.git
cd TASK15

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r sandbox/requirements.txt
```

## Step 2: Verify Setup

```bash
# Run project verification
python unified/verify_project.py
```

Expected output:
```
[SUCCESS] All 6 checks passed
[SUCCESS] Project is ready for use
```

## Step 3: Run Backend

### Option A: Using Unified Launcher

```bash
python unified/launch.py
# Select option 1: Run Backend
```

### Option B: Direct Execution

```bash
python unified/run_backend.py
```

### Option C: Using Sample Data

```bash
# Run with sample data (included)
python unified/run_backend.py sandbox/sample_data/sample_candidates.json
```

Expected output:
```
[INFO] Running ranking engine...
[INFO] Input: sandbox/sample_data/sample_candidates.json
[INFO] Output: unified/outputs/submissions/submission.csv
[SUCCESS] Ranking engine completed
```

## Step 4: Run Sandbox

### Option A: Using Unified Launcher

```bash
python unified/launch.py
# Select option 2: Run Sandbox
```

### Option B: Direct Execution

```bash
python unified/run_sandbox.py
```

### Option C: Manual Launch

```bash
cd sandbox
streamlit run app.py
```

Expected output:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501
```

## Step 5: Use Sandbox

1. Open browser to `http://localhost:8501`
2. Click "Upload your candidate dataset"
3. Select `sandbox/sample_data/sample_candidates.json`
4. Click "Generate Rankings"
5. Wait for processing to complete
6. Review results in the table
7. Click "Download submission.csv"

## Step 6: Generate Submission

```bash
# Generate submission CSV
python unified/scripts/generate_submission.py
```

Expected output:
```
[SUCCESS] Submission generated successfully
[INFO] File: unified/outputs/submissions/submission.csv
[INFO] Rows: 100
```

## Step 7: Validate Submission

```bash
# Run validation
python unified/scripts/validate.py
```

Expected output:
```
[SUCCESS] All 4 validations passed
```

## Step 8: Run Benchmark

```bash
# Run performance benchmark
python unified/scripts/benchmark.py
```

Expected output:
```
BENCHMARK RESULTS
==================================================
Candidates Processed: 5
Execution Time: 0.02 seconds
Throughput: 250.00 candidates/second
==================================================
```

## Complete Script

Here's a complete script that runs all steps:

```bash
#!/bin/bash
# run_complete.sh

echo "=== Redrob Candidate Ranking System ==="

# Setup
echo "Setting up environment..."
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r sandbox/requirements.txt

# Verify
echo "Verifying setup..."
python unified/verify_project.py

# Run backend
echo "Running backend..."
python unified/run_backend.py

# Generate submission
echo "Generating submission..."
python unified/scripts/generate_submission.py

# Validate
echo "Validating submission..."
python unified/scripts/validate.py

# Run benchmark
echo "Running benchmark..."
python unified/scripts/benchmark.py

echo "=== Complete ==="
```

## Expected Files

After execution, you should have:

```
TASK15/
|
+-- unified/outputs/
    +-- submissions/
    |   +-- submission.csv          # Generated submission
    +-- logs/
    |   +-- ranking.log             # Execution logs
    +-- reports/
        +-- benchmark.txt           # Benchmark results
        +-- validation.txt          # Validation report
```

## Troubleshooting

### Issue: "Python not found"
**Solution**: Ensure Python 3.10+ is installed and in PATH

### Issue: "Module not found"
**Solution**: Run `pip install -r sandbox/requirements.txt`

### Issue: "File not found"
**Solution**: Ensure you're in the TASK15 directory

### Issue: "Permission denied"
**Solution**: Check file permissions or run as administrator

## Next Steps

1. Review the generated submission.csv
2. Explore the sandbox interface
3. Read the documentation in `unified/docs/`
4. Deploy to Streamlit Cloud
5. Prepare for hackathon submission