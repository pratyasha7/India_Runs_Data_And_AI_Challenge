# Backend Guide

## Overview

The Version 1 ranking engine is a purely rule-based, CPU-only candidate ranking pipeline. It evaluates job candidates and ranks the Top 100 candidates for a founding engineer role at a search/retrieval systems company.

## Architecture

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

## Modules

### rank.py (Master Orchestrator)

**Purpose**: Main entry point that orchestrates the entire pipeline.

**Functions**:
- `run_master_ranker()`: Main execution function
- `generate_dynamic_reasoning()`: Generates candidate reasoning

**Execution Flow**:
1. Reads candidates from JSONL file (streaming)
2. Passes each candidate through quality gatekeeper
3. Computes base relevance score
4. Applies behavioral multiplier
5. Calculates final score
6. Sorts candidates deterministically
7. Selects Top 100
8. Generates reasoning
9. Writes submission.csv

### quality_controller.py (Fraud Detection)

**Purpose**: Filters out synthetic/fake candidates and IT consulting-only profiles.

**Functions**:
- `is_clean_candidate()`: Main validation function
- `run_honeypot_audit()`: Performs 6 fraud checks
- `check_service_company_disqualifier()`: Filters IT consulting profiles

**Honeypot Checks**:
1. Expert/Advanced skills with zero duration
2. Too many advanced skills with low average duration
3. Career history months exceeding stated YoE
4. YoE inflation vs. chronological timeline
5. High skill claims with zero endorsements
6. Platform behavioral paradoxes

**Service Company Blocklist**:
```
TCS, Infosys, Wipro, Accenture, Cognizant, Capgemini,
HCL, Tech Mahindra, L&T, LNT, Mindtree, Cognizant Technology Solutions
```

### semantic_matcher.py (Relevance Scoring)

**Purpose**: Scores candidates on a 0.0-1.0 scale using weighted keyword matching.

**Dimensions**:
| Dimension | Max Points | Weight |
|-----------|------------|--------|
| IR/Search Experience | 0.40 | 40% |
| Vector DB/Embeddings | 0.25 | 25% |
| Evaluation Metrics | 0.20 | 20% |
| Desirable ML | 0.15 | 15% |

**Adjustments**:
- Seniority boost/penalty: ±0.10
- Non-coding title penalty: -0.15
- Out-of-domain penalty: max -0.15

### behavioral_multiplier.py (Signal Adjustments)

**Purpose**: Computes multiplicative modifier based on platform behavioral signals.

**Signals**:
| Signal | Range | Effect |
|--------|-------|--------|
| Location/Relocation | 0.1 - 1.2 | Local India boost, abroad penalty |
| Notice Period | 0.5 - 1.25 | Quick joiner boost, long notice penalty |
| Activity Recency | 0.4 - 1.2 | Active boost, ghost penalty |
| Responsiveness | 0.5 - 1.15 | Fast reply boost, unresponsive penalty |

**Final Score Formula**:
```
Final Score = Relevance Score (0.0-1.0) × Behavioral Multiplier (0.1-1.575)
```

## Running the Backend

### Method 1: Using Unified Launcher

```bash
# From project root
python unified/launch.py

# Select option 1: Run Backend
```

### Method 2: Using Backend Runner

```bash
# From project root
python unified/run_backend.py
```

### Method 3: Direct Execution

```bash
# Navigate to engine directory
cd MODEL/India_Runs_Data_And_AI_Challenge

# Run ranking engine
python rank.py
```

### Method 4: Custom Input/Output

```bash
# Specify input and output files
python unified/run_backend.py /path/to/input.jsonl /path/to/output.csv
```

## Input/Output

### Input Format

**JSONL Format** (recommended):
```json
{"candidate_id": 1001, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}}
```

**JSON Format**:
```json
[
  {"candidate_id": 1001, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}}
]
```

### Output Format

**CSV Format**:
```csv
candidate_id,rank,score,reasoning
1001,1,1.6146,"Exceptional 7.5-year Senior Search Engineer with proven expertise in Elasticsearch, FAISS..."
1002,2,1.4532,"Highly recommended founding candidate with 5.0 years of experience..."
```

## Performance

### Benchmarks

| Metric | Value |
|--------|-------|
| Candidates Processed | 100,000 |
| Execution Time | <5 minutes |
| Memory Usage | Streaming (low) |
| CPU Usage | Single core |
| Dependencies | Zero external packages |

### Optimization

- **Streaming**: Processes candidates line-by-line
- **Deterministic**: Consistent results across runs
- **CPU-only**: No GPU required
- **Zero dependencies**: Python standard library only

## Testing

### Run Backend Tests

```bash
# From project root
python unified/scripts/validate.py
```

### Manual Testing

```python
import sys
sys.path.insert(0, 'MODEL/India_Runs_Data_And_AI_Challenge')

from rank import run_master_ranker

# Run ranking engine
run_master_ranker()
```

## Troubleshooting

### Issue: "Module not found"
**Cause**: Python path not configured
**Solution**: Add engine directory to path:
```python
import sys
sys.path.insert(0, 'MODEL/India_Runs_Data_And_AI_Challenge')
```

### Issue: "candidates.jsonl not found"
**Cause**: Input file missing
**Solution**: Place dataset in engine directory or specify path

### Issue: "Permission denied"
**Cause**: File permissions
**Solution**: Check file permissions and directory access

### Issue: "Memory error"
**Cause**: Dataset too large
**Solution**: Reduce dataset size or increase system memory

## Development Guidelines

### Do Not Modify

The following files should not be modified:
- `rank.py`
- `quality_controller.py`
- `semantic_matcher.py`
- `behavioral_multiplier.py`

### Safe to Modify

- Documentation files
- Test scripts
- Configuration files
- Integration layer (unified/)

## API Reference

### rank.py

```python
def run_master_ranker():
    """
    Main ranking function.
    
    Reads candidates from 'candidates.jsonl',
    processes through pipeline,
    writes 'submission.csv'.
    """

def generate_dynamic_reasoning(candidate, rank, score):
    """
    Generate reasoning for a candidate.
    
    Args:
        candidate: Candidate dictionary
        rank: Final rank position
        score: Final score
    
    Returns:
        str: Reasoning text
    """
```

### quality_controller.py

```python
def is_clean_candidate(candidate):
    """
    Check if candidate passes quality screening.
    
    Args:
        candidate: Candidate dictionary
    
    Returns:
        bool: True if clean, False otherwise
    """
```

### semantic_matcher.py

```python
def calculate_relevance_score(candidate):
    """
    Calculate relevance score for candidate.
    
    Args:
        candidate: Candidate dictionary
    
    Returns:
        float: Score between 0.0 and 1.0
    """
```

### behavioral_multiplier.py

```python
def calculate_behavioral_multiplier(candidate):
    """
    Calculate behavioral multiplier for candidate.
    
    Args:
        candidate: Candidate dictionary
    
    Returns:
        float: Multiplier value
    """
```

## References

- [Project Architecture](ARCHITECTURE.md)
- [Dataset Guide](DATASET_GUIDE.md)
- [Execution Guide](EXECUTION_GUIDE.md)
- [Troubleshooting](TROUBLESHOOTING.md)