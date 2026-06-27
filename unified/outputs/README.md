# Outputs

## Overview

This directory contains generated outputs from the Redrob Candidate Ranking System.

## Contents

| Directory | Purpose |
|-----------|---------|
| `submissions/` | Generated submission CSVs |
| `logs/` | Execution logs |
| `reports/` | Benchmark and validation reports |
| `README.md` | This file |

## Directory Structure

```
outputs/
|
+-- submissions/
|   +-- submission.csv          # Generated submission
|   +-- benchmark_submission.csv # Benchmark output
|
+-- logs/
|   +-- ranking.log             # Execution logs
|   +-- sandbox.log             # Sandbox logs
|
+-- reports/
    +-- benchmark.txt           # Benchmark results
    +-- validation.txt          # Validation report
    +-- error_report.txt        # Error reports
```

## Output Files

### submissions/submission.csv

The main output file containing ranked candidates.

**Format**: CSV with columns `candidate_id`, `rank`, `score`, `reasoning`

**Example**:
```csv
candidate_id,rank,score,reasoning
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer..."
1002,2,1.4532,"Highly recommended founding candidate..."
```

### logs/ranking.log

Execution logs from the ranking engine.

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

### reports/benchmark.txt

Performance benchmark results.

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

### reports/validation.txt

Project validation results.

**Example**:
```
Redrob Hackathon - Validation Report
==================================================

Total checks: 4
Passed: 4
Failed: 0

All validations passed successfully.
```

## Generating Outputs

### Generate Submission

```bash
python unified/scripts/generate_submission.py
```

### Run Benchmark

```bash
python unified/scripts/benchmark.py
```

### Run Validation

```bash
python unified/scripts/validate.py
```

## Output Management

### Cleanup

To clean up old outputs:

```bash
# Remove all outputs
rm -rf unified/outputs/*

# Or remove specific files
rm unified/outputs/submissions/*.csv
rm unified/outputs/logs/*.log
rm unified/outputs/reports/*.txt
```

### Backup

To backup outputs:

```bash
# Create backup
tar -czf outputs_backup.tar.gz unified/outputs/
```

### Archive

To archive old outputs:

```bash
# Move to archive
mkdir archive
mv unified/outputs/submissions/*.csv archive/
```

## Best Practices

1. **Regular cleanup** - Remove old outputs periodically
2. **Backup important outputs** - Keep copies of successful runs
3. **Document outputs** - Note what each output represents
4. **Version control** - Don't commit outputs to git
5. **Monitor disk space** - Outputs can accumulate

## Troubleshooting

### Issue: "Output directory not found"
**Solution**: Run `python unified/scripts/setup.py`

### Issue: "Permission denied"
**Solution**: Check directory permissions

### Issue: "Disk space full"
**Solution**: Clean up old outputs

## References

- [Expected Output](../examples/expected_output.md)
- [Submission Guide](../docs/SUBMISSION_GUIDE.md)
- [Testing Guide](../docs/TESTING_GUIDE.md)

## License

This project was built for the Redrob Hackathon competition.