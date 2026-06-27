# Architecture

## System Overview

The Redrob Candidate Ranking System is a purely rule-based, CPU-only candidate ranking pipeline built in Python with zero external dependencies. The system evaluates job candidates and ranks the Top 100 candidates for a founding engineer role at a search/retrieval systems company.

## High-Level Architecture

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

## Component Architecture

### 1. Version 1 Ranking Engine

The backend ranking engine consists of four main modules:

#### rank.py (Master Orchestrator)
- Main entry point that orchestrates the entire pipeline
- Reads candidates from JSONL file (streaming, memory-efficient)
- Passes each candidate through the quality gatekeeper
- Computes base relevance score via semantic matcher
- Applies behavioral multiplier
- Calculates final score: `relevance_score × behavioral_multiplier`
- Sorts candidates deterministically (score descending, candidate_id ascending for ties)
- Selects Top 100 candidates
- Generates dynamic, non-templated reasoning
- Writes submission.csv

#### quality_controller.py (Fraud Detection & Gating)
- Filters out synthetic/fake candidates and IT consulting-only profiles
- Performs 6 honeypot audit checks:
  1. Expert/Advanced skills with zero duration
  2. Too many advanced skills with low average duration
  3. Career history months exceeding stated YoE
  4. YoE inflation vs. chronological timeline
  5. High skill claims with zero endorsements
  6. Platform behavioral paradoxes
- Service company disqualifier for IT consulting firms

#### semantic_matcher.py (Relevance Scoring)
- Scores candidates on a 0.0-1.0 scale using weighted keyword matching
- 5 dimensions:
  - Dimension A: IR/Search Experience (Max +0.40)
  - Dimension B: Vector DB & Embeddings (Max +0.25)
  - Dimension C: Evaluation Metrics (Max +0.20)
  - Dimension D: Desirable ML Skills (Max +0.15)
  - Seniority Alignment Boost/Penalty
- Non-coding title penalty
- Out-of-domain red flag penalty

#### behavioral_multiplier.py (Signal Adjustments)
- Computes multiplicative modifier based on 4 platform behavioral signals:
  - Location/Relocation Fit
  - Notice Period
  - Platform Activity Recency
  - Recruiter Responsiveness

### 2. Streamlit Sandbox (Frontend)

The frontend sandbox provides a professional dashboard for demonstrating the ranking engine:

#### Components
- **upload.py**: File upload component for JSONL/JSON datasets
- **results.py**: Results display with sortable dataframe
- **metrics.py**: Execution metrics and statistics
- **footer.py**: Project information footer

#### Utilities
- **runner.py**: Pipeline execution utility
- **validator.py**: Dataset validation utility
- **file_handler.py**: File handling utility
- **csv_reader.py**: CSV reading utility

### 3. Unified Integration Layer

The unified layer orchestrates the existing projects without modification:

#### Entry Points
- **launch.py**: Single entry point with menu options
- **run_backend.py**: Backend execution wrapper
- **run_sandbox.py**: Sandbox launch wrapper
- **verify_project.py**: Project health checks

#### Scripts
- **setup.py**: Project setup and dependency checks
- **validate.py**: Comprehensive validation
- **benchmark.py**: Performance benchmarking
- **generate_submission.py**: Submission generation

## Data Flow

1. **Input**: Candidate dataset (JSONL/JSON format)
2. **Processing**:
   - Quality screening (fraud detection)
   - Relevance scoring (semantic matching)
   - Behavioral adjustments (multiplier)
   - Ranking and selection (Top 100)
3. **Output**: submission.csv with ranked candidates

## Performance Characteristics

- **CPU-only execution**: No GPU required
- **Memory-efficient streaming**: Processes candidates line-by-line
- **Deterministic ranking**: Consistent results across runs
- **Fast execution**: <30 seconds for 100 candidates
- **Zero external dependencies**: Python standard library only

## Security Considerations

- No network calls during ranking
- No authentication required
- Temporary files only (auto-cleanup)
- No sensitive data storage
- Read-only access to input files

## Scalability

- Current: Handles up to 100 candidates
- Design: Streaming architecture supports larger datasets
- Limitation: Deterministic sorting requires full dataset in memory
- Future: Could be extended with database backend