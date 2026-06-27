import streamlit as st
import os
from utils.validator import validate_dataset
from utils.file_handler import handle_uploaded_file

def render_upload_section():
    """Render the dataset upload section."""
    st.markdown('<div class="section-header">Dataset Upload</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **Upload your candidate dataset:**
        - Supported formats: `.jsonl`, `.jsonl.gz`, `.json`
        - Maximum candidates: 100
        - Each candidate should follow the Redrob data schema
        """)
        
        uploaded_file = st.file_uploader(
            "Choose a candidate dataset file",
            type=["jsonl", "gz", "json"],
            help="Upload a JSONL file with candidate records. Maximum 100 candidates allowed."
        )
        
        if uploaded_file is not None:
            # Process the uploaded file
            processed_file, error = handle_uploaded_file(uploaded_file)
            
            if error:
                st.error(f"Error processing file: {error}")
            else:
                # Validate the dataset
                is_valid, validation_result = validate_dataset(processed_file)
                
                if is_valid:
                    st.session_state.uploaded_file = processed_file
                    st.session_state.candidate_count = validation_result['candidate_count']
                    st.success(f"✓ Successfully uploaded {validation_result['candidate_count']} candidates")
                else:
                    st.error(f"Validation error: {validation_result}")
    
    with col2:
        st.markdown("""
        **File Requirements:**
        - Valid JSONL format (one JSON object per line)
        - Required fields: `candidate_id`, `profile`, `skills`
        - Optional fields: `career_history`, `redrob_signals`
        - Maximum file size: 10MB
        """)
        
        # Show sample data info
        if os.path.exists("sample_data/sample_candidates.json"):
            st.info("Sample data available in `sample_data/sample_candidates.json`")
