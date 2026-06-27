# Sandbox Guide

## Overview

The Streamlit sandbox provides a professional, interactive dashboard for demonstrating the Redrob Candidate Ranking System. It allows users to upload datasets, run the ranking engine, and view results through a web interface.

## Features

- **Professional Dashboard**: Clean, modern UI with metric cards
- **File Upload**: Support for JSONL, JSON, and compressed JSONL files
- **Real-time Progress**: Live execution status with stage-by-stage updates
- **Results Display**: Sortable dataframe with ranked candidates
- **Execution Metrics**: Detailed performance statistics
- **CSV Download**: Export ranked results as submission.csv

## Architecture

```
sandbox/
|
+-- app.py                      # Main Streamlit application
+-- components/
|   +-- upload.py               # File upload component
|   +-- results.py              # Results display component
|   +-- metrics.py              # Execution metrics component
|   +-- footer.py               # Footer component
+-- utils/
|   +-- runner.py               # Pipeline execution utility
|   +-- validator.py            # Dataset validation utility
|   +-- file_handler.py         # File handling utility
|   +-- csv_reader.py           # CSV reading utility
+-- sample_data/
|   +-- sample_candidates.json  # Sample dataset
+-- assets/                     # Static assets
+-- requirements.txt            # Python dependencies
+-- .streamlit/
    +-- config.toml             # Streamlit configuration
```

## Running the Sandbox

### Method 1: Using Unified Launcher (Recommended)

```bash
# From project root
python unified/launch.py

# Select option 2: Run Sandbox
```

### Method 2: Using Sandbox Runner

```bash
# From project root
python unified/run_sandbox.py
```

### Method 3: Manual Launch

```bash
# Navigate to sandbox directory
cd sandbox

# Launch Streamlit
streamlit run app.py
```

### Method 4: Custom Port

```bash
# Launch on custom port
python unified/run_sandbox.py 8502
```

## Accessing the Sandbox

After launching, open your web browser and navigate to:

```
http://localhost:8501
```

## Using the Sandbox

### Step 1: Upload Dataset

1. Click on the file upload area
2. Select a JSONL, JSON, or JSONL.gz file
3. Wait for validation and upload confirmation

**File Requirements**:
- Maximum 100 candidates
- Maximum 10MB file size
- Valid JSONL/JSON format

### Step 2: Generate Rankings

1. Click the "Generate Rankings" button
2. Watch the real-time progress indicators
3. Wait for the pipeline to complete

**Progress Stages**:
- Loading Dataset
- Parsing Candidates
- Running Quality Controller
- Running Semantic Matcher
- Running Behavioral Multiplier
- Generating Rankings
- Writing CSV
- Completed

### Step 3: View Results

1. Review the ranked candidates in the results table
2. Sort by rank, score, or candidate ID
3. Inspect the reasoning for each candidate

### Step 4: Download Results

1. Click the "Download submission.csv" button
2. Save the file to your local machine

## Components

### Upload Component (`components/upload.py`)

Handles file upload and validation:
- Accepts JSONL, JSON, and JSONL.gz files
- Validates file format and size
- Stores uploaded file in session state
- Displays upload confirmation

### Results Component (`components/results.py`)

Displays ranking results:
- Shows execution metrics
- Displays sortable dataframe
- Provides download button for CSV

### Metrics Component (`components.metrics.py`)

Shows execution statistics:
- Total candidates processed
- Candidates passed/rejected
- Execution time
- Throughput
- System information

### Footer Component (`components/footer.py`)

Displays project information:
- Project name and version
- System requirements
- Resource links

## Utilities

### Runner (`utils/runner.py`)

Executes the ranking pipeline:
- Imports Version 1 engine modules
- Processes candidates
- Generates rankings
- Returns results

### Validator (`utils/validator.py`)

Validates uploaded datasets:
- Checks file format
- Validates candidate structure
- Ensures required fields
- Returns validation results

### File Handler (`utils/file_handler.py`)

Manages file operations:
- Saves uploaded files to temporary location
- Handles gzip decompression
- Cleans up temporary files

### CSV Reader (`utils/csv_reader.py`)

Reads and parses CSV files:
- Reads submission.csv
- Provides summary statistics
- Formats data for display

## Configuration

### Streamlit Configuration (`.streamlit/config.toml`)

```toml
[theme]
primaryColor = "#3b82f6"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8fafc"
textColor = "#1e293b"
font = "sans serif"

[server]
headless = true
port = 8501
enableCORS = false
enableXsrfProtection = true

[browser]
gatherUsageStats = false
```

### Customizing Appearance

Edit `.streamlit/config.toml` to change:
- Colors and fonts
- Server settings
- Browser behavior

## Dependencies

### Requirements (`requirements.txt`)

```
streamlit>=1.28.0
pandas>=2.0.0
```

### Installing Dependencies

```bash
pip install -r requirements.txt
```

## Deployment

### Streamlit Cloud Deployment

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Add Streamlit sandbox"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to share.streamlit.io
   - Sign in with GitHub
   - Click "New app"

3. **Configure Deployment**
   - Repository: `your-username/TASK15`
   - Branch: `main`
   - Main file path: `sandbox/app.py`

4. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete

### Environment Variables

No environment variables are required for basic operation.

## Troubleshooting

### Issue: Sandbox won't start
**Cause**: Streamlit not installed
**Solution**: Run `pip install -r sandbox/requirements.txt`

### Issue: Import errors
**Cause**: Python path not configured
**Solution**: Run from project root or use unified launcher

### Issue: File upload fails
**Cause**: Invalid file format or size
**Solution**: Check file format and size (max 10MB, 100 candidates)

### Issue: Ranking fails
**Cause**: Invalid dataset structure
**Solution**: Ensure dataset follows required schema

### Issue: Slow performance
**Cause**: Large dataset or system resources
**Solution**: Reduce dataset size or check system resources

## Customization

### Adding New Components

1. Create new file in `components/` directory
2. Import in `app.py`
3. Add to main layout

### Modifying UI

Edit `app.py` to:
- Change layout
- Add new sections
- Modify styling

### Extending Functionality

Edit utility files in `utils/` to:
- Add new validation rules
- Modify ranking logic (not recommended - use Version 1 engine)
- Add new output formats

## Best Practices

1. **Keep dependencies updated**
2. **Validate datasets before upload**
3. **Use sample data for testing**
4. **Check execution logs for errors**
5. **Download results regularly**

## Support

For issues or questions:
- Check the troubleshooting section
- Review the documentation in `unified/docs/`
- Run validation script: `python unified/scripts/validate.py`