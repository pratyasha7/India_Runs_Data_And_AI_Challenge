# Troubleshooting Guide

## Overview

This guide provides solutions for common issues encountered when using the Redrob Candidate Ranking System.

## Common Issues

### 1. Python Version Issues

#### Issue: "Python version not supported"
```
[ERROR] Python 3.9 (requires 3.10 - 3.12)
```

**Cause**: Python version is too old or too new.

**Solution**:
```bash
# Check Python version
python --version

# Install Python 3.10 or higher
# Download from https://www.python.org/downloads/

# Verify installation
python --version
```

### 2. Import Errors

#### Issue: "Module not found"
```
ModuleNotFoundError: No module named 'quality_controller'
```

**Cause**: Python path not configured correctly.

**Solution**:
```python
import sys
sys.path.insert(0, 'MODEL/India_Runs_Data_And_AI_Challenge')

# Now import
from quality_controller import is_clean_candidate
```

Or use the unified launcher:
```bash
python unified/launch.py
```

#### Issue: "Import error in sandbox"
```
ImportError: cannot import name 'run_ranking_pipeline' from 'utils.runner'
```

**Cause**: Sandbox utilities not in Python path.

**Solution**:
```bash
# Run from project root
cd TASK15
python unified/run_sandbox.py

# Or add to path
sys.path.insert(0, 'sandbox/utils')
```

### 3. File Not Found Issues

#### Issue: "Dataset not found"
```
FileNotFoundError: [Errno 2] No such file or directory: 'candidates.jsonl'
```

**Cause**: Input file missing or wrong path.

**Solution**:
```bash
# Check if file exists
ls -la datasets/

# Use full path
python unified/run_backend.py /full/path/to/candidates.jsonl

# Or place file in expected location
cp /path/to/candidates.jsonl datasets/
```

#### Issue: "Submission CSV not found"
```
FileNotFoundError: [Errno 2] No such file or directory: 'submission.csv'
```

**Cause**: Submission not generated yet.

**Solution**:
```bash
# Generate submission first
python unified/scripts/generate_submission.py

# Or run backend
python unified/run_backend.py
```

### 4. Permission Issues

#### Issue: "Permission denied"
```
PermissionError: [Errno 13] Permission denied: 'submission.csv'
```

**Cause**: File permissions or file in use.

**Solution**:
```bash
# Check file permissions
ls -la submission.csv

# Make writable
chmod +w submission.csv

# Or delete and regenerate
rm submission.csv
python unified/scripts/generate_submission.py
```

### 5. Format Issues

#### Issue: "Invalid JSON"
```
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

**Cause**: Malformed JSON in input file.

**Solution**:
```bash
# Validate JSON
python -c "import json; json.load(open('your_file.jsonl'))"

# Or use JSON validator
cat your_file.jsonl | python -m json.tool
```

#### Issue: "Invalid CSV format"
```
csv.Error: iterator should return strings, not bytes
```

**Cause**: File encoding issue.

**Solution**:
```python
# Specify encoding
with open('file.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
```

### 6. Streamlit Issues

#### Issue: "Streamlit not installed"
```
ModuleNotFoundError: No module named 'streamlit'
```

**Cause**: Streamlit not installed.

**Solution**:
```bash
# Install Streamlit
pip install streamlit

# Or install all requirements
pip install -r sandbox/requirements.txt
```

#### Issue: "Port already in use"
```
OSError: [Errno 98] Address already in use
```

**Cause**: Another process using the same port.

**Solution**:
```bash
# Use different port
streamlit run app.py --server.port 8502

# Or kill process using the port
lsof -i :8501
kill -9 <PID>
```

#### Issue: "Sandbox won't start"
```
Error: Unrecognized command: 'run'
```

**Cause**: Wrong command syntax.

**Solution**:
```bash
# Correct command
streamlit run app.py

# Not
streamlit run.py
```

### 7. Runtime Issues

#### Issue: "Execution timeout"
```
TimeoutError: Execution exceeded time limit
```

**Cause**: Dataset too large or system too slow.

**Solution**:
```bash
# Reduce dataset size
head -n 1000 large_dataset.jsonl > small_dataset.jsonl

# Or increase timeout
python unified/run_backend.py --timeout 300
```

#### Issue: "Memory error"
```
MemoryError: Unable to allocate memory
```

**Cause**: Insufficient system memory.

**Solution**:
```bash
# Check memory usage
free -h

# Close other applications
# Or use a machine with more memory
```

### 8. Validation Issues

#### Issue: "Validation failed"
```
[ERROR] Missing required fields
```

**Cause**: Dataset missing required fields.

**Solution**:
```python
# Check required fields
required_fields = ['candidate_id', 'profile', 'skills']

# Validate your data
for candidate in candidates:
    for field in required_fields:
        if field not in candidate:
            print(f"Missing field: {field}")
```

#### Issue: "Too many candidates"
```
[ERROR] Too many candidates: 150 (maximum allowed is 100)
```

**Cause**: Dataset exceeds limit.

**Solution**:
```bash
# Reduce dataset size
head -n 100 candidates.jsonl > candidates_100.jsonl

# Or modify limit in project_config.py
MAX_CANDIDATES = 200  # Not recommended
```

### 9. Deployment Issues

#### Issue: "Streamlit Cloud deployment failed"
```
Error: Could not find app.py
```

**Cause**: Wrong main file path.

**Solution**:
1. Check main file path in Streamlit Cloud settings
2. Ensure path is `sandbox/app.py`
3. Verify file exists in repository

#### Issue: "Missing dependencies on Streamlit Cloud"
```
ModuleNotFoundError: No module named 'pandas'
```

**Cause**: Dependencies not in requirements.txt.

**Solution**:
```bash
# Check requirements.txt
cat sandbox/requirements.txt

# Add missing dependencies
echo "pandas>=2.0.0" >> sandbox/requirements.txt

# Push changes
git add .
git commit -m "Add missing dependency"
git push
```

### 10. Performance Issues

#### Issue: "Slow execution"
```
Execution time: 120 seconds (expected <30 seconds)
```

**Cause**: Large dataset or inefficient code.

**Solution**:
```bash
# Profile execution
python -m cProfile -o profile.stats unified/run_backend.py

# Analyze profile
python -m pstats profile.stats

# Optimize bottlenecks
```

#### Issue: "High memory usage"
```
Memory usage: 500MB (expected <100MB)
```

**Cause**: Loading entire dataset into memory.

**Solution**:
```python
# Use streaming instead of loading all
with open('dataset.jsonl', 'r') as f:
    for line in f:
        candidate = json.loads(line)
        process(candidate)
```

## Debugging Techniques

### Enable Debug Mode

```bash
# Run with verbose output
python -u unified/run_backend.py 2>&1 | tee debug.log

# Enable Python debugging
python -m pdb unified/run_backend.py
```

### Check Logs

```bash
# View execution logs
cat unified/outputs/logs/ranking.log

# View error logs
cat unified/outputs/reports/validation.txt
```

### Profile Execution

```bash
# Profile time
time python unified/run_backend.py

# Profile memory
python -m memory_profiler unified/run_backend.py

# Profile CPU
python -m cProfile unified/run_backend.py
```

### Test Individual Components

```python
# Test quality controller
from quality_controller import is_clean_candidate
print(is_clean_candidate(test_candidate))

# Test semantic matcher
from semantic_matcher import calculate_relevance_score
print(calculate_relevance_score(test_candidate))

# Test behavioral multiplier
from behavioral_multiplier import calculate_behavioral_multiplier
print(calculate_behavioral_multiplier(test_candidate))
```

## Recovery Procedures

### Corrupted Output

```bash
# Delete corrupted output
rm unified/outputs/submissions/submission.csv

# Regenerate
python unified/scripts/generate_submission.py
```

### Broken Environment

```bash
# Recreate virtual environment
rm -rf venv
python -m venv venv
venv\Scripts\activate
pip install -r sandbox/requirements.txt
```

### Missing Files

```bash
# Restore from git
git checkout HEAD -- path/to/missing/file

# Or regenerate
python unified/scripts/setup.py
```

## Prevention

### Best Practices

1. **Use virtual environments** for isolation
2. **Validate inputs** before processing
3. **Check file permissions** before writing
4. **Monitor resource usage** during execution
5. **Backup important files** regularly
6. **Test changes** before deployment
7. **Read error messages** carefully
8. **Check documentation** for solutions

### Regular Maintenance

```bash
# Update dependencies
pip install --upgrade -r sandbox/requirements.txt

# Clean temporary files
find . -name "*.tmp" -delete

# Verify project integrity
python unified/verify_project.py
```

## Getting Help

### Documentation

- [README.md](README.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [EXECUTION_GUIDE.md](EXECUTION_GUIDE.md)
- [TESTING_GUIDE.md](TESTING_GUIDE.md)

### Community

- GitHub Issues
- Stack Overflow
- Discord/Slack channels

### Support

- Email: support@example.com
- Office hours: TBD

## Reporting Issues

When reporting issues, include:

1. **Error message** (full traceback)
2. **Steps to reproduce**
3. **Expected behavior**
4. **Actual behavior**
5. **Environment details** (OS, Python version, etc.)
6. **Sample data** (if applicable)

Example issue report:

```markdown
**Error Message**
```
ModuleNotFoundError: No module named 'quality_controller'
```

**Steps to Reproduce**
1. Clone repository
2. Create virtual environment
3. Install dependencies
4. Run `python unified/run_backend.py`

**Expected Behavior**
Backend should execute successfully.

**Actual Behavior**
Import error occurs.

**Environment**
- OS: Windows 10
- Python: 3.9.7
- Streamlit: 1.28.0

**Sample Data**
Using included sample_candidates.json
```