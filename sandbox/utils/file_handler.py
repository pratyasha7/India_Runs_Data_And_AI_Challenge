import os
import tempfile
import gzip
import shutil

def handle_uploaded_file(uploaded_file):
    """
    Handle the uploaded file by saving it to a temporary location.
    
    Args:
        uploaded_file: Streamlit UploadedFile object
        
    Returns:
        tuple: (file_path, error_message)
            - If successful: (file_path, None)
            - If error: (None, error_message)
    """
    try:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp(prefix="redrob_sandbox_")
        
        # Determine file extension
        original_name = uploaded_file.name
        if original_name.endswith('.jsonl.gz'):
            file_ext = '.jsonl.gz'
        elif original_name.endswith('.jsonl'):
            file_ext = '.jsonl'
        elif original_name.endswith('.json'):
            file_ext = '.json'
        else:
            return None, f"Unsupported file format: {original_name}"
        
        # Create temporary file path
        temp_file_path = os.path.join(temp_dir, f"candidates{file_ext}")
        
        # Save the uploaded file
        with open(temp_file_path, 'wb') as f:
            f.write(uploaded_file.getbuffer())
        
        # If it's a gzip file, extract it
        if file_ext == '.jsonl.gz':
            extracted_path = os.path.join(temp_dir, "candidates.jsonl")
            with gzip.open(temp_file_path, 'rb') as f_in:
                with open(extracted_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            
            # Remove the gzip file
            os.remove(temp_file_path)
            temp_file_path = extracted_path
        
        # Store the temp directory path in session state for cleanup
        if 'temp_dirs' not in dir(__import__('streamlit').session_state):
            __import__('streamlit').session_state.temp_dirs = []
        __import__('streamlit').session_state.temp_dirs.append(temp_dir)
        
        return temp_file_path, None
        
    except Exception as e:
        return None, f"Error handling uploaded file: {str(e)}"

def cleanup_temp_files():
    """Clean up temporary files and directories."""
    try:
        import streamlit as st
        
        if 'temp_dirs' in st.session_state:
            for temp_dir in st.session_state.temp_dirs:
                if os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)
            st.session_state.temp_dirs = []
    except Exception:
        # Silently ignore cleanup errors
        pass