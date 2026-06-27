# Testing Guide

## Overview

This guide explains how to test the Redrob Candidate Ranking System, including backend tests, sandbox tests, and submission validation.

## Testing Levels

### Level 1: Unit Tests

Test individual components and functions.

### Level 2: Integration Tests

Test component interactions and data flow.

### Level 3: System Tests

Test complete execution pipeline.

### Level 4: Acceptance Tests

Test against requirements and specifications.

## Backend Testing

### Run Backend Tests

```bash
# Using validation script
python unified/scripts/validate.py

# Using verify project
python unified/verify_project.py
```

### Manual Backend Testing

```python
import sys
sys.path.insert(0, 'MODEL/India_Runs_Data_And_AI_Challenge')

# Test imports
from quality_controller import is_clean_candidate
from semantic_matcher import calculate_relevance_score
from behavioral_multiplier import calculate_behavioral_multiplier
from rank import run_master_ranker

print("All imports successful")

# Test with sample candidate
sample_candidate = {
    "candidate_id": 1001,
    "profile": {
        "current_title": "Software Engineer",
        "years_of_experience": 5.0,
        "location": "Pune",
        "country": "India"
    },
    "skills": [{"name": "Python", "proficiency": "expert", "duration_months": 36, "endorsements": 10}],
    "career_history": [],
    "redrob_signals": {"notice_period_days": 30}
}

# Test quality controller
is_clean = is_clean_candidate(sample_candidate)
print(f"Quality check: {is_clean}")

# Test semantic matcher
relevance_score = calculate_relevance_score(sample_candidate)
print(f"Relevance score: {relevance_score}")

# Test behavioral multiplier
behavioral_mult = calculate_behavioral_multiplier(sample_candidate)
print(f"Behavioral multiplier: {behavioral_mult}")

# Calculate final score
final_score = relevance_score * behavioral_mult
print(f"Final score: {final_score}")
```

### Test Cases

#### Quality Controller Tests

```python
# Test honeypot detection
def test_honeypot_detection():
    honeypot_candidate = {
        "candidate_id": 9999,
        "profile": {"years_of_experience": 2.0},
        "skills": [
            {"name": "Python", "proficiency": "expert", "duration_months": 0, "endorsements": 0},
            {"name": "Java", "proficiency": "expert", "duration_months": 0, "endorsements": 0},
            {"name": "C++", "proficiency": "expert", "duration_months": 0, "endorsements": 0}
        ],
        "career_history": []
    }
    
    from quality_controller import is_clean_candidate
    result = is_clean_candidate(honeypot_candidate)
    assert result == False, "Honeypot should be detected"

# Test service company disqualifier
def test_service_company_disqualifier():
    service_candidate = {
        "candidate_id": 9998,
        "profile": {"years_of_experience": 5.0},
        "skills": [],
        "career_history": [
            {"company": "TCS", "title": "Software Engineer", "duration_months": 24},
            {"company": "Infosys", "title": "Senior Software Engineer", "duration_months": 36}
        ]
    }
    
    from quality_controller import is_clean_candidate
    result = is_clean_candidate(service_candidate)
    assert result == False, "Service company candidate should be disqualified"
```

#### Semantic Matcher Tests

```python
# Test relevance scoring
def test_relevance_scoring():
    candidate = {
        "profile": {
            "headline": "Search Engineer",
            "summary": "Building ranking systems with Elasticsearch and FAISS"
        },
        "skills": [{"name": "Elasticsearch"}],
        "career_history": [
            {"description": "Built ranking systems using collaborative filtering"}
        ]
    }
    
    from semantic_matcher import calculate_relevance_score
    score = calculate_relevance_score(candidate)
    assert 0.0 <= score <= 1.0, f"Score should be between 0.0 and 1.0, got {score}"
```

#### Behavioral Multiplier Tests

```python
# Test behavioral multiplier
def test_behavioral_multiplier():
    candidate = {
        "profile": {"location": "Pune", "country": "India"},
        "redrob_signals": {
            "notice_period_days": 30,
            "willing_to_relocate": True,
            "preferred_work_mode": "hybrid",
            "last_active_date": "2026-06-20",
            "recruiter_response_rate": 0.85,
            "avg_response_time_hours": 12.0
        }
    }
    
    from behavioral_multiplier import calculate_behavioral_multiplier
    multiplier = calculate_behavioral_multiplier(candidate)
    assert multiplier > 0, f"Multiplier should be positive, got {multiplier}"
```

## Sandbox Testing

### Run Sandbox Tests

```bash
# Navigate to sandbox directory
cd sandbox

# Run test script
python test_sandbox.py
```

Expected output:
```
[SUCCESS] All tests passed! The sandbox is ready to use.
```

### Manual Sandbox Testing

```python
# Test imports
from utils.runner import run_ranking_pipeline
from utils.validator import validate_dataset
from utils.file_handler import handle_uploaded_file
from utils.csv_reader import read_submission_csv

print("All sandbox imports successful")

# Test validation
is_valid, result = validate_dataset('sample_data/sample_candidates.json')
print(f"Validation: {is_valid}, {result}")

# Test ranking pipeline
results = run_ranking_pipeline('sample_data/sample_candidates.json')
print(f"Ranking results: {results['total_processed']} candidates processed")
```

### Test Cases

#### File Upload Test

```python
def test_file_upload():
    from utils.file_handler import handle_uploaded_file
    
    # Create mock uploaded file
    class MockFile:
        def __init__(self, name, content):
            self.name = name
            self._content = content
        
        def getbuffer(self):
            return self._content.encode()
    
    # Test JSONL upload
    jsonl_content = '{"candidate_id": 1001, "profile": {}, "skills": []}\n'
    mock_file = MockFile("test.jsonl", jsonl_content)
    
    file_path, error = handle_uploaded_file(mock_file)
    assert error is None, f"Upload should succeed, got error: {error}"
    assert file_path is not None, "File path should not be None"
```

#### Validation Test

```python
def test_validation():
    from utils.validator import validate_dataset
    
    # Test valid dataset
    is_valid, result = validate_dataset('sample_data/sample_candidates.json')
    assert is_valid == True, "Sample data should be valid"
    assert 'candidate_count' in result, "Result should contain candidate_count"
    
    # Test invalid dataset (non-existent file)
    is_valid, result = validate_dataset('nonexistent.jsonl')
    assert is_valid == False, "Non-existent file should fail validation"
```

## Submission Validation

### Validate Generated Submission

```bash
# Using validation script
python unified/scripts/validate.py

# Manual validation
python -c "
import csv

with open('unified/outputs/submissions/submission.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
    # Check required columns
    required_columns = ['candidate_id', 'rank', 'score', 'reasoning']
    assert all(col in reader.fieldnames for col in required_columns), 'Missing columns'
    
    # Check row count
    assert len(rows) == 100, f'Expected 100 rows, got {len(rows)}'
    
    # Check data types
    for row in rows:
        int(row['candidate_id'])
        int(row['rank'])
        float(row['score'])
        str(row['reasoning'])
    
    print('Submission validation passed')
"
```

### Validation Checklist

- [ ] File exists at expected location
- [ ] File is valid CSV format
- [ ] Required columns present: `candidate_id`, `rank`, `score`, `reasoning`
- [ ] Exactly 100 rows (or less if fewer candidates)
- [ ] `candidate_id` is integer
- [ ] `rank` is integer (1-100)
- [ ] `score` is float (0.0-2.0)
- [ ] `reasoning` is non-empty string
- [ ] Scores are in descending order
- [ ] Ranks are sequential (1-100)

## Performance Testing

### Benchmark Execution

```bash
# Run benchmark
python unified/scripts/benchmark.py
```

### Performance Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Execution Time (100 candidates) | <5 seconds | Measure with `time` |
| Execution Time (100K candidates) | <5 minutes | Measure with `time` |
| Memory Usage | <100MB | Monitor with `top` |
| CPU Usage | Single core | Monitor with `top` |
| Output File Size | <1MB | Check with `ls -lh` |

### Load Testing

```bash
# Create large test dataset
python -c "
import json

candidates = []
for i in range(1000):
    candidate = {
        'candidate_id': i,
        'profile': {'years_of_experience': 5.0},
        'skills': [{'name': 'Python', 'proficiency': 'expert', 'duration_months': 36, 'endorsements': 10}],
        'career_history': [],
        'redrob_signals': {'notice_period_days': 30}
    }
    candidates.append(candidate)

with open('large_test.jsonl', 'w') as f:
    for c in candidates:
        f.write(json.dumps(c) + '\n')
"

# Run benchmark on large dataset
time python unified/run_backend.py large_test.jsonl large_submission.csv
```

## Automated Testing

### Create Test Script

```bash
# test_all.sh
#!/bin/bash

echo "Running all tests..."

# Backend tests
echo "Running backend tests..."
python unified/scripts/validate.py
if [ $? -ne 0 ]; then
    echo "Backend tests failed"
    exit 1
fi

# Sandbox tests
echo "Running sandbox tests..."
cd sandbox
python test_sandbox.py
if [ $? -ne 0 ]; then
    echo "Sandbox tests failed"
    exit 1
fi

# Submission validation
echo "Validating submission..."
python unified/scripts/generate_submission.py
python unified/scripts/validate.py
if [ $? -ne 0 ]; then
    echo "Submission validation failed"
    exit 1
fi

echo "All tests passed!"
```

### Continuous Integration

```yaml
# .github/workflows/test.yml
name: Test

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'
      - name: Install dependencies
        run: |
          pip install -r sandbox/requirements.txt
      - name: Run tests
        run: |
          python unified/scripts/validate.py
          cd sandbox && python test_sandbox.py
```

## Test Data

### Sample Test Data

Location: `sandbox/sample_data/sample_candidates.json`

Contains 5 candidates with varying characteristics:
- 1 high-ranking candidate (search expertise)
- 1 mid-ranking candidate (ML experience)
- 1 low-ranking candidate (limited search experience)
- 1 borderline candidate
- 1 rejected candidate (IT services background)

### Creating Test Data

```python
import json

# Create minimal test candidate
minimal_candidate = {
    "candidate_id": 1,
    "profile": {
        "current_title": "Engineer",
        "years_of_experience": 5.0,
        "location": "Pune",
        "country": "India"
    },
    "skills": [],
    "career_history": [],
    "redrob_signals": {}
}

# Create test dataset
with open('test_data.jsonl', 'w') as f:
    f.write(json.dumps(minimal_candidate) + '\n')
```

## Troubleshooting Tests

### Issue: "Import error"
**Cause**: Python path not configured
**Solution**: Add directories to path:
```python
import sys
sys.path.insert(0, 'MODEL/India_Runs_Data_And_AI_Challenge')
sys.path.insert(0, 'sandbox/utils')
```

### Issue: "File not found"
**Cause**: Test data missing
**Solution**: Create test data or use sample data

### Issue: "Assertion error"
**Cause**: Test case failed
**Solution**: Check test data and expected values

### Issue: "Timeout error"
**Cause**: Test taking too long
**Solution**: Reduce test data size or increase timeout

## Best Practices

1. **Test early and often**
2. **Use version control for test data**
3. **Keep tests independent**
4. **Document test cases**
5. **Automate test execution**
6. **Monitor test coverage**
7. **Review test results**
8. **Update tests with code changes**