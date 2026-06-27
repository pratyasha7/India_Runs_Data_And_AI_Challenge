# Deployment Guide

## Overview

This guide explains how to deploy the Redrob Candidate Ranking System to Streamlit Cloud and other platforms.

## Streamlit Cloud Deployment

### Prerequisites

- GitHub repository with the project code
- Streamlit Cloud account (https://share.streamlit.io)
- Python 3.10 or higher

### Step 1: Prepare Repository

Ensure your repository has the following structure:

```
TASK15/
|
+-- sandbox/
|   +-- app.py                      # Main Streamlit app
|   +-- requirements.txt            # Dependencies
|   +-- components/                 # UI components
|   +-- utils/                      # Utilities
|   +-- sample_data/                # Sample data
|   +-- .streamlit/
|       +-- config.toml             # Streamlit config
|
+-- MODEL/                          # Backend engine
|   +-- India_Runs_Data_And_AI_Challenge/
|       +-- rank.py
|       +-- quality_controller.py
|       +-- semantic_matcher.py
|       +-- behavioral_multiplier.py
|
+-- unified/                        # Integration layer
```

### Step 2: Push to GitHub

```bash
# Initialize git repository
git init
git add .
git commit -m "Initial commit"

# Add remote repository
git remote add origin https://github.com/your-username/TASK15.git

# Push to GitHub
git push -u origin main
```

### Step 3: Connect to Streamlit Cloud

1. Go to https://share.streamlit.io
2. Sign in with GitHub
3. Click "New app"

### Step 4: Configure Deployment

Fill in the deployment form:

| Field | Value |
|-------|-------|
| Repository | `your-username/TASK15` |
| Branch | `main` |
| Main file path | `sandbox/app.py` |

### Step 5: Deploy

1. Click "Deploy"
2. Wait for deployment to complete (usually 2-5 minutes)
3. Access your app via the provided URL

### Step 6: Verify Deployment

1. Open the deployed app
2. Upload the sample dataset
3. Generate rankings
4. Download the submission CSV

## Configuration

### Streamlit Configuration

File: `sandbox/.streamlit/config.toml`

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

### Environment Variables

No environment variables are required for basic deployment.

Optional variables:
- `STREAMLIT_SERVER_PORT`: Custom port number
- `STREAMLIT_SERVER_ADDRESS`: Custom host address

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

**Pros**:
- Free for public repositories
- Easy setup
- Automatic deployments
- Built-in monitoring

**Cons**:
- Limited to public repositories (free tier)
- No custom domain (free tier)
- Resource limits

### Option 2: Heroku

```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create your-app-name

# Add buildpack
heroku buildpacks:add heroku/python

# Deploy
git push heroku main

# Open app
heroku open
```

### Option 3: AWS Elastic Beanstalk

```bash
# Install EB CLI
pip install awsebcli

# Initialize EB
eb init

# Create environment
eb create

# Deploy
eb deploy

# Open app
eb open
```

### Option 4: Docker

```dockerfile
# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY sandbox/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy application
COPY sandbox/ ./sandbox/
COPY MODEL/ ./MODEL/
COPY unified/ ./unified/

# Expose port
EXPOSE 8501

# Run application
CMD ["streamlit", "run", "sandbox/app.py"]
```

```bash
# Build Docker image
docker build -t redrob-sandbox .

# Run container
docker run -p 8501:8501 redrob-sandbox
```

## Post-Deployment

### Verify Functionality

1. **Test Upload**: Upload a sample dataset
2. **Test Ranking**: Generate rankings
3. **Test Download**: Download submission.csv
4. **Test Metrics**: Verify execution metrics display

### Monitor Performance

- Check Streamlit Cloud dashboard for metrics
- Monitor error logs
- Review user feedback

### Update Deployment

```bash
# Make changes
git add .
git commit -m "Update feature"

# Push to GitHub
git push origin main

# Streamlit Cloud auto-deploys
```

## Troubleshooting

### Issue: "Application failed to start"
**Cause**: Import error or missing dependency
**Solution**:
1. Check `requirements.txt` includes all dependencies
2. Verify Python version compatibility
3. Check Streamlit Cloud logs

### Issue: "Module not found"
**Cause**: Python path not configured
**Solution**:
1. Ensure `sandbox/app.py` adds correct paths
2. Check directory structure matches expected layout

### Issue: "File not found"
**Cause**: Missing files in deployment
**Solution**:
1. Verify all required files are committed to git
2. Check `.gitignore` doesn't exclude necessary files
3. Ensure sample data is included

### Issue: "Permission denied"
**Cause**: File permissions in deployment
**Solution**:
1. Check file permissions in repository
2. Ensure directories are writable
3. Review Streamlit Cloud documentation

### Issue: "Timeout error"
**Cause**: Application taking too long to start
**Solution**:
1. Optimize startup time
2. Reduce initial data loading
3. Check Streamlit Cloud resource limits

## Best Practices

### Repository Structure

- Keep `sandbox/app.py` as the main entry point
- Include all required dependencies in `requirements.txt`
- Store sample data in `sandbox/sample_data/`
- Use `.streamlit/config.toml` for configuration

### Code Organization

- Separate UI components in `components/`
- Keep utilities in `utils/`
- Import backend engine from `MODEL/`
- Use unified layer for orchestration

### Documentation

- Include README.md in root directory
- Document deployment steps
- Provide troubleshooting guide
- Update documentation with changes

### Monitoring

- Set up error logging
- Monitor performance metrics
- Track user usage
- Review feedback

## Security Considerations

### Data Privacy

- No sensitive data stored in repository
- Temporary files only (auto-cleanup)
- No authentication required
- Read-only access to input files

### Access Control

- Public repository access
- No sensitive endpoints
- No database connections
- No API keys required

### Compliance

- No PII stored
- No tracking without consent
- GDPR compliant (no data collection)
- CCPA compliant (no data selling)

## Cost Optimization

### Streamlit Cloud

- Free for public repositories
- Limited resources on free tier
- Upgrade for private repos

### Other Platforms

- **Heroku**: Free tier available
- **AWS**: Pay-as-you-go
- **Docker**: Free (self-hosted)

## Scaling

### Current Limitations

- 100 candidates maximum
- Single-user execution
- In-memory processing
- No concurrent users

### Future Enhancements

- Database backend for large datasets
- User authentication
- Concurrent execution
- API endpoints
- Caching layer

## Support

### Documentation

- [README.md](README.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

### Issues

- GitHub Issues
- Email support
- Community forums

### Updates

- Regular maintenance
- Bug fixes
- Feature additions
- Performance improvements