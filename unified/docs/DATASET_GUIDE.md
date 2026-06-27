# Dataset Guide

## Overview

The Redrob Candidate Ranking System expects candidate data in specific formats. This guide explains the dataset requirements, formats, and placement.

## Supported Formats

### 1. JSONL (JSON Lines) - Recommended

**File Extension**: `.jsonl`

**Format**: One JSON object per line

**Example**:
```json
{"candidate_id": 1001, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}}
{"candidate_id": 1002, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}}
```

**Advantages**:
- Memory-efficient streaming
- Line-by-line processing
- Easy to inspect and debug

### 2. Compressed JSONL

**File Extension**: `.jsonl.gz`

**Format**: Gzipped JSONL file

**Usage**: Same as JSONL, but compressed for storage efficiency

### 3. JSON Array

**File Extension**: `.json`

**Format**: JSON array of candidate objects

**Example**:
```json
[
  {"candidate_id": 1001, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}},
  {"candidate_id": 1002, "profile": {...}, "skills": [...], "career_history": [...], "redrob_signals": {...}}
]
```

## Candidate Data Schema

Each candidate record must contain the following fields:

### Required Fields

#### candidate_id
- **Type**: Integer
- **Description**: Unique identifier for the candidate
- **Example**: `1001`

#### profile
- **Type**: Object
- **Description**: Candidate's professional profile
- **Required sub-fields**:
  - `anonymized_name`: String (candidate's name)
  - `current_title`: String (current job title)
  - `years_of_experience`: Float (years of professional experience)
  - `location`: String (city/location)
  - `country`: String (country)
  - `headline`: String (professional headline)
  - `summary`: String (professional summary)

#### skills
- **Type**: Array of objects
- **Description**: Candidate's skills
- **Required sub-fields**:
  - `name`: String (skill name)
  - `proficiency`: String (expert/advanced/intermediate)
  - `duration_months`: Integer (months of experience)
  - `endorsements`: Integer (number of endorsements)

### Optional Fields

#### career_history
- **Type**: Array of objects
- **Description**: Work experience history
- **Sub-fields**:
  - `company`: String (company name)
  - `title`: String (job title)
  - `description`: String (job description)
  - `duration_months`: Integer (months employed)
  - `start_date`: String (YYYY-MM-DD format)

#### redrob_signals
- **Type**: Object
- **Description**: Platform behavioral signals
- **Sub-fields**:
  - `signup_date`: String (YYYY-MM-DD)
  - `last_active_date`: String (YYYY-MM-DD)
  - `notice_period_days`: Integer (days)
  - `willing_to_relocate`: Boolean
  - `preferred_work_mode`: String (hybrid/remote/onsite)
  - `recruiter_response_rate`: Float (0.0-1.0)
  - `avg_response_time_hours`: Float (hours)
  - `profile_views_received_30d`: Integer
  - `saved_by_recruiters_30d`: Integer
  - `interview_completion_rate`: Float (0.0-1.0)
  - `offer_acceptance_rate`: Float (0.0-1.0)

## Example Candidate Record

```json
{
  "candidate_id": 1001,
  "profile": {
    "anonymized_name": "Rahul Sharma",
    "current_title": "Senior Search Engineer",
    "years_of_experience": 7.5,
    "location": "Pune",
    "country": "India",
    "headline": "Search & Recommendation Systems Expert",
    "summary": "Building scalable search and ranking systems with expertise in Elasticsearch, FAISS, and collaborative filtering."
  },
  "skills": [
    {
      "name": "Elasticsearch",
      "proficiency": "expert",
      "duration_months": 36,
      "endorsements": 15
    },
    {
      "name": "FAISS",
      "proficiency": "advanced",
      "duration_months": 24,
      "endorsements": 8
    }
  ],
  "career_history": [
    {
      "company": "TechCorp India",
      "title": "Search Engineer",
      "description": "Built ranking systems using FAISS and Elasticsearch for product search.",
      "duration_months": 24,
      "start_date": "2024-03-08"
    }
  ],
  "redrob_signals": {
    "signup_date": "2025-01-15",
    "last_active_date": "2026-06-20",
    "notice_period_days": 30,
    "willing_to_relocate": true,
    "preferred_work_mode": "hybrid",
    "recruiter_response_rate": 0.85,
    "avg_response_time_hours": 12.0,
    "profile_views_received_30d": 45,
    "saved_by_recruiters_30d": 12,
    "interview_completion_rate": 0.7,
    "offer_acceptance_rate": 0.5
  }
}
```

## Dataset Placement

### Option 1: Datasets Directory (Recommended)

Place your dataset in the `datasets/` directory at the project root:

```
TASK15/
|
+-- datasets/
    +-- candidates.jsonl
    +-- candidates.jsonl.gz
    +-- sample_candidates.json
```

### Option 2: Custom Location

You can specify a custom location when running the backend:

```bash
python unified/run_backend.py /path/to/your/candidates.jsonl
```

### Option 3: Sandbox Sample Data

The sandbox includes sample data at:
```
sandbox/sample_data/sample_candidates.json
```

## Dataset Validation

The system validates datasets before processing:

### Validation Rules

1. **File Format**: Must be valid JSONL, JSONL.gz, or JSON
2. **File Size**: Maximum 10MB
3. **Candidate Count**: Maximum 100 candidates
4. **Required Fields**: `candidate_id`, `profile`, `skills` must be present
5. **Data Types**: Fields must match expected types

### Validation Tools

#### Using the Sandbox
The sandbox automatically validates uploaded files.

#### Using the Validator Script
```bash
python unified/scripts/validate.py
```

#### Manual Validation
```python
from unified.utils.validator import validate_dataset

is_valid, result = validate_dataset('path/to/your/file.jsonl')
print(f"Valid: {is_valid}")
print(f"Result: {result}")
```

## Sample Datasets

### Sample Candidates (Included)

Location: `sandbox/sample_data/sample_candidates.json`

Contains 5 sample candidates for testing purposes.

### Creating Your Own Sample

```bash
# Convert full dataset to sample
head -n 100 candidates.jsonl > sample_100.jsonl
```

## Troubleshooting

### Issue: "Invalid JSON at line X"
**Cause**: Malformed JSON in the input file
**Solution**: Validate your JSON format using a JSON linter

### Issue: "Too many candidates"
**Cause**: Dataset exceeds 100 candidate limit
**Solution**: Reduce dataset size or modify limit in `project_config.py`

### Issue: "Missing required fields"
**Cause**: Candidate records missing required fields
**Solution**: Ensure all candidates have `candidate_id`, `profile`, and `skills`

### Issue: "File too large"
**Cause**: File exceeds 10MB limit
**Solution**: Compress file or split into smaller chunks

## Best Practices

1. **Use JSONL format** for better streaming performance
2. **Validate your data** before processing
3. **Keep backups** of your original datasets
4. **Use consistent encoding** (UTF-8)
5. **Include all optional fields** for better ranking accuracy