# Expected Output

## Overview

This document describes the expected output files and their formats when running the Redrob Candidate Ranking System.

## Output Files

### 1. submission.csv

**Location**: `unified/outputs/submissions/submission.csv`

**Format**: CSV (Comma-Separated Values)

**Columns**:
| Column | Type | Description |
|--------|------|-------------|
| `candidate_id` | Integer | Unique candidate identifier |
| `rank` | Integer | Ranking position (1-100) |
| `score` | Float | Final composite score |
| `reasoning` | String | Personalized explanation for selection |

**Example**:
```csv
candidate_id,rank,score,reasoning
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer with proven expertise in Elasticsearch, FAISS. Aligns perfectly with the founding engineer criteria, matching both technical and high-energy platform signals."
1002,2,1.4532,"Highly recommended founding candidate with 5.0 years of experience. Demonstrated success in Pinecone, Embeddings at product-scale; backed by strong platform responsiveness and an optimal 30-day notice period."
1003,3,1.3200,"Top-tier ML Engineer holding 6.0 years of experience. Strong background in TensorFlow, Embeddings; highly active platform signals and immediate availability make them an outstanding fit."
```

**Row Count**: 100 (or less if fewer candidates pass screening)

**File Size**: Approximately 50-100KB

### 2. ranking.log

**Location**: `unified/outputs/logs/ranking.log`

**Format**: Plain text

**Example**:
```
Redrob Hackathon - Submission Generation Log
==================================================

Input file: sandbox/sample_data/sample_candidates.json
Output file: unified/outputs/submissions/submission.csv
Candidates processed: 5
Candidates passed screening: 4
Top candidates selected: 4
File size: 512 bytes
```

### 3. benchmark.txt

**Location**: `unified/outputs/reports/benchmark.txt`

**Format**: Plain text

**Example**:
```
Redrob Hackathon - Benchmark Report
==================================================

Candidates Processed: 5
Execution Time: 0.02 seconds
Throughput: 250.00 candidates/second
Memory Efficient: Yes (streaming)
CPU Only: Yes
Deterministic: Yes
```

### 4. validation.txt

**Location**: `unified/outputs/reports/validation.txt`

**Format**: Plain text

**Example**:
```
Redrob Hackathon - Validation Report
==================================================

Total checks: 4
Passed: 4
Failed: 0

All validations passed successfully.
```

## Output Format Details

### submission.csv Format

#### Header Row
```csv
candidate_id,rank,score,reasoning
```

#### Data Rows
```csv
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer..."
1002,2,1.4532,"Highly recommended founding candidate..."
```

#### Reasoning Format

Reasoning text is enclosed in double quotes and may contain:
- Commas
- Periods
- Special characters
- Line breaks (escaped)

Example:
```csv
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer with proven expertise in Elasticsearch, FAISS. Aligns perfectly with the founding engineer criteria, matching both technical and high-energy platform signals."
```

### Score Format

Scores are floating-point numbers with 4 decimal places:

```
1.6146
1.4532
1.3200
0.9876
0.5432
```

**Range**: 0.0 to 2.0 (theoretically)

**Typical Range**: 0.5 to 1.8

### Rank Format

Ranks are sequential integers starting from 1:

```
1, 2, 3, 4, 5, ..., 98, 99, 100
```

**Note**: Ranks are always consecutive with no gaps.

## Verification

### Verify CSV Format

```python
import csv

with open('unified/outputs/submissions/submission.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    # Check columns
    assert reader.fieldnames == ['candidate_id', 'rank', 'score', 'reasoning']
    
    # Check rows
    rows = list(reader)
    assert len(rows) == 100
    
    # Check data types
    for row in rows:
        int(row['candidate_id'])
        int(row['rank'])
        float(row['score'])
        str(row['reasoning'])
    
    print("CSV format verification passed")
```

### Verify Score Order

```python
import csv

with open('unified/outputs/submissions/submission.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
    # Check scores are in descending order
    for i in range(len(rows) - 1):
        score1 = float(rows[i]['score'])
        score2 = float(rows[i + 1]['score'])
        assert score1 >= score2, f"Score order violated at rows {i+1} and {i+2}"
    
    print("Score order verification passed")
```

### Verify Rank Sequence

```python
import csv

with open('unified/outputs/submissions/submission.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    
    # Check ranks are sequential
    for i, row in enumerate(rows):
        expected_rank = i + 1
        actual_rank = int(row['rank'])
        assert actual_rank == expected_rank, f"Rank mismatch at row {i+1}: expected {expected_rank}, got {actual_rank}"
    
    print("Rank sequence verification passed")
```

## Sample Output Files

### Small Dataset (5 candidates)

**submission.csv**:
```csv
candidate_id,rank,score,reasoning
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer with proven expertise in Elasticsearch, FAISS. Aligns perfectly with the founding engineer criteria, matching both technical and high-energy platform signals."
1004,2,1.4532,"Highly recommended founding candidate with 6.0 years of experience. Demonstrated success in TensorFlow, Embeddings at product-scale; backed by strong platform responsiveness and an optimal 30-day notice period."
1002,3,1.3200,"Top-tier ML Engineer holding 5.0 years of experience. Strong background in Pinecone, Embeddings; highly active platform signals and immediate availability make them an outstanding fit."
1003,4,0.9876,"Solid 3.0-year developer with solid skills in Java, SQL. Excellent technical capabilities, though a slightly longer 60-day notice period is a minor logistical hurdle."
```

**Note**: Only 4 candidates in this example (1 rejected).

### Large Dataset (100 candidates)

**submission.csv**:
- 100 rows
- Ranks 1-100
- Scores in descending order
- Reasoning for each candidate

## Output Interpretation

### Score Interpretation

| Score Range | Interpretation |
|-------------|----------------|
| 1.5 - 2.0 | Exceptional fit |
| 1.2 - 1.5 | Strong fit |
| 1.0 - 1.2 | Good fit |
| 0.8 - 1.0 | Moderate fit |
| 0.5 - 0.8 | Basic fit |
| < 0.5 | Weak fit |

### Rank Interpretation

| Rank Range | Interpretation |
|------------|----------------|
| 1 - 15 | Top tier candidates |
| 16 - 60 | Mid-tier candidates |
| 61 - 100 | Lower-tier candidates |

### Reasoning Interpretation

Reasoning text provides:
- Candidate's years of experience
- Current job title
- Key skills
- Fit assessment
- Any limitations noted

Example breakdown:
```
Exceptional 7.5-year Senior Search Engineer with proven expertise in Elasticsearch, FAISS.
|          |    |                |                    |                      |
Years     Title                    Skills                          Fit assessment
```

## Troubleshooting Output

### Issue: "Empty submission.csv"
**Cause**: No candidates passed screening
**Solution**: Check dataset quality and screening criteria

### Issue: "Less than 100 rows"
**Cause**: Fewer than 100 candidates passed screening
**Solution**: This is normal for small datasets

### Issue: "Scores not in order"
**Cause**: Sorting algorithm issue
**Solution**: Report as bug

### Issue: "Missing reasoning"
**Cause**: Reasoning generation failed
**Solution**: Check candidate data structure

### Issue: "Special characters in reasoning"
**Cause**: CSV escaping issue
**Solution**: Ensure proper CSV quoting

## Best Practices

1. **Always verify output** after generation
2. **Check score order** is descending
3. **Verify rank sequence** is consecutive
4. **Review reasoning** for quality
5. **Backup output files** regularly
6. **Document any anomalies**

## References

- [SUBMISSION_GUIDE.md](../docs/SUBMISSION_GUIDE.md)
- [TESTING_GUIDE.md](../docs/TESTING_GUIDE.md)
- [TROUBLESHOOTING.md](../docs/TROUBLESHOOTING.md)