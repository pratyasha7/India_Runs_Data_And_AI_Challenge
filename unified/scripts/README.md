# Scripts

## Overview

This directory contains helper scripts for the Redrob Candidate Ranking System.

## Contents

| File | Purpose |
|------|---------|
| `setup.py` | Project setup and dependency checks |
| `validate.py` | Comprehensive validation |
| `benchmark.py` | Performance benchmarking |
| `generate_submission.py` | Submission generation |
| `README.md` | This file |

## Scripts

### setup.py

Creates necessary directories and checks dependencies.

```bash
python unified/scripts/setup.py
```

**Features**:
- Creates required directories
- Checks Python version
- Verifies dependencies
- Reports setup status

### validate.py

Runs comprehensive validation of the project.

```bash
python unified/scripts/validate.py
```

**Features**:
- Validates backend modules
- Checks sandbox structure
- Validates submission format
- Verifies output directories
- Generates validation report

### benchmark.py

Runs performance benchmarks on the ranking engine.

```bash
python unified/scripts/benchmark.py
```

**Features**:
- Measures execution time
- Calculates throughput
- Tests with sample data
- Generates benchmark report

### generate_submission.py

Generates the final submission.csv file.

```bash
python unified/scripts/generate_submission.py
```

**Features**:
- Loads candidate dataset
- Processes through ranking pipeline
- Generates reasoning
- Creates submission.csv
- Saves generation log

## Usage

### Running Scripts

```bash
# From project root
python unified/scripts/setup.py
python unified/scripts/validate.py
python unified/scripts/benchmark.py
python unified/scripts/generate_submission.py
```

### Using Unified Launcher

```bash
python unified/launch.py
# Select appropriate option from menu
```

## Dependencies

- Python 3.10+
- Access to Version 1 engine modules
- Access to sandbox modules

## Output

Scripts generate output in:
- `unified/outputs/submissions/` - Submission CSVs
- `unified/outputs/logs/` - Execution logs
- `unified/outputs/reports/` - Reports and benchmarks

## Troubleshooting

### Issue: "Module not found"
**Solution**: Ensure you're running from project root

### Issue: "Permission denied"
**Solution**: Check file permissions

### Issue: "File not found"
**Solution**: Verify paths in project_config.py

## References

- [Execution Guide](../docs/EXECUTION_GUIDE.md)
- [Testing Guide](../docs/TESTING_GUIDE.md)
- [Submission Guide](../docs/SUBMISSION_GUIDE.md)

## License

This project was built for the Redrob Hackathon competition.