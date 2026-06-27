# Execution Guide

## Overview

This guide explains how to execute the Redrob Candidate Ranking System in various modes.

## Execution Modes

### 1. Backend Only

Execute the ranking engine directly without the frontend.

```bash
# Using unified launcher
python unified/launch.py
# Select option 1: Run Backend

# Or using backend runner
python unified/run_backend.py

# Or direct execution
cd MODEL/India_Runs_Data_And_AI_Challenge
python rank.py
```

### 2. Sandbox Only

Launch the Streamlit frontend.

```bash
# Using unified launcher
python unified/launch.py
# Select option 2: Run Sandbox

# Or using sandbox runner
python unified/run_sandbox.py

# Or manual launch
cd sandbox
streamlit run app.py
```

### 3. Full Pipeline

Run both backend and sandbox.

```bash
# Using unified launcher
python unified/launch.py
# Select options 1 and 2 sequentially
```

### 4. Validation Mode

Run comprehensive project validation.

```bash
# Using unified launcher
python unified/launch.py
# Select option 4: Validate Project

# Or using validation script
python unified/scripts/validate.py
```

### 5. Benchmark Mode

Run performance benchmarks.

```bash
# Using unified launcher
python unified/launch.py
# Select option 3: Run Benchmark

# Or using benchmark script
python unified/scripts/benchmark.py
```

### 6. Submission Generation

Generate the final submission CSV.

```bash
# Using unified launcher
python unified/launch.py
# Select option 5: Generate Submission

# Or using submission script
python unified/scripts/generate_submission.py
```

## Execution Flow

### Backend Execution Flow

```
1. Initialize
   |
   v
2. Load Dataset (JSONL/JSON)
   |
   v
3. Process Each Candidate
   |
   +---> Quality Controller (Fraud Detection)
   |
   +---> Semantic Matcher (Relevance Scoring)
   |
   +---> Behavioral Multiplier (Signal Adjustments)
   |
   +---> Calculate Final Score
   |
   v
4. Sort Candidates (Score DESC, ID ASC)
   |
   v
5. Select Top 100
   |
   v
6. Generate Reasoning
   |
   v
7. Write submission.csv
   |
   v
8. Output Statistics
```

### Sandbox Execution Flow

```
1. Launch Streamlit
   |
   v
2. Display Dashboard
   |
   v
3. User Uploads Dataset
   |
   v
4. Validate Dataset
   |
   v
5. User Clicks "Generate Rankings"
   |
   v
6. Execute Ranking Pipeline
   |
   v
7. Display Results
   |
   v
8. User Downloads CSV
```

## Command Line Arguments

### run_backend.py

```bash
python unified/run_backend.py [INPUT_FILE] [OUTPUT_FILE]
```

**Arguments**:
- `INPUT_FILE`: Path to input JSONL/JSON file (optional)
- `OUTPUT_FILE`: Path to output CSV file (optional)

**Examples**:
```bash
# Use defaults
python unified/run_backend.py

# Specify input file
python unified/run_backend.py datasets/candidates.jsonl

# Specify both input and output
python unified/run_backend.py datasets/candidates.jsonl outputs/my_submission.csv
```

### run_sandbox.py

```bash
python unified/run_sandbox.py [PORT] [HOST]
```

**Arguments**:
- `PORT`: Port number (optional, default: 8501)
- `HOST`: Host address (optional, default: localhost)

**Examples**:
```bash
# Use defaults
python unified/run_sandbox.py

# Custom port
python unified/run_sandbox.py 8502

# Custom port and host
python unified/run_sandbox.py 8502 0.0.0.0
```

### generate_submission.py

```bash
python unified/scripts/generate_submission.py [INPUT_FILE] [OUTPUT_FILE]
```

**Arguments**:
- `INPUT_FILE`: Path to input JSONL/JSON file (optional)
- `OUTPUT_FILE`: Path to output CSV file (optional)

## Output Files

### Backend Output

**submission.csv**
- Location: `MODEL/India_Runs_Data_And_AI_Challenge/submission.csv`
- Format: CSV with columns `candidate_id`, `rank`, `score`, `reasoning`
- Rows: 100 (or less if fewer candidates pass screening)

### Sandbox Output

**submission.csv**
- Location: `unified/outputs/submissions/submission.csv`
- Format: Same as backend output
- Access: Download button in sandbox interface

### Log Files

**ranking.log**
- Location: `unified/outputs/logs/ranking.log`
- Content: Execution timestamps and statistics

### Report Files

**benchmark.txt**
- Location: `unified/outputs/reports/benchmark.txt`
- Content: Performance metrics and statistics

**validation.txt**
- Location: `unified/outputs/reports/validation.txt`
- Content: Validation results and checks

## Execution Time

### Expected Runtime

| Operation | Expected Time |
|-----------|---------------|
| Backend (100 candidates) | <5 seconds |
| Backend (100,000 candidates) | <5 minutes |
| Sandbox Launch | <10 seconds |
| Validation | <5 seconds |
| Benchmark | <30 seconds |

### Performance Monitoring

```bash
# Time a command
time python unified/run_backend.py

# Monitor memory usage
python -m memory_profiler unified/run_backend.py
```

## Error Handling

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Input file not found |
| 3 | Invalid input format |
| 4 | Output write error |
| 5 | Import error |

### Logging

All execution logs are saved to:
- `unified/outputs/logs/ranking.log`

### Debug Mode

```bash
# Enable debug output
python -u unified/run_backend.py 2>&1 | tee debug.log
```

## Batch Execution

### Process Multiple Datasets

```bash
#!/bin/bash
# process_all.sh

for file in datasets/*.jsonl; do
    echo "Processing: $file"
    python unified/run_backend.py "$file" "outputs/$(basename $file .jsonl)_submission.csv"
done
```

### Schedule Execution

```bash
# Run daily at 2 AM
0 2 * * * cd /path/to/TASK15 && python unified/run_backend.py
```

## Remote Execution

### SSH Execution

```bash
# Connect to remote server
ssh user@server

# Navigate to project
cd /path/to/TASK15

# Activate virtual environment
source venv/bin/activate

# Run backend
python unified/run_backend.py
```

### Screen/Tmux Session

```bash
# Start screen session
screen -S ranking

# Run backend
python unified/run_backend.py

# Detach: Ctrl+A, D
# Reattach: screen -r ranking
```

## Troubleshooting Execution

### Issue: "Command not found"
**Cause**: Python not in PATH
**Solution**: Use full path to Python or activate virtual environment

### Issue: "Permission denied"
**Cause**: File permissions
**Solution**: Check file permissions and directory access

### Issue: "Timeout error"
**Cause**: Execution taking too long
**Solution**: Reduce dataset size or check system resources

### Issue: "Memory error"
**Cause**: Insufficient memory
**Solution**: Close other applications or increase system memory

## Best Practices

1. **Use virtual environments** for isolation
2. **Validate inputs** before execution
3. **Monitor execution** for large datasets
4. **Check logs** for errors
5. **Backup outputs** regularly
6. **Use deterministic settings** for reproducibility