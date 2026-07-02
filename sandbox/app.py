import streamlit as st
import sys
import os

# Add parent directory to path here that is the model
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'MODEL', 'India_Runs_Data_And_AI_Challenge'))

from components.upload import render_upload_section
from components.results import render_results_section
from components.metrics import render_metrics_section
from components.footer import render_footer
from utils.runner import run_ranking_pipeline
from utils.validator import validate_dataset
from utils.file_handler import handle_uploaded_file


st.set_page_config(
    page_title="Redrob Candidate Ranking Sandbox",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1e3a5f 0%, #2d5a87 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 2rem;
    }
    .badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    .badge-version {
        background: #10b981;
        color: white;
    }
    .badge-cpu {
        background: #3b82f6;
        color: white;
    }
    .badge-deterministic {
        background: #8b5cf6;
        color: white;
    }
    .metric-card {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1.5rem;
        text-align: center;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1e293b;
    }
    .metric-label {
        font-size: 0.875rem;
        color: #64748b;
        margin-top: 0.5rem;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #1e293b;
        margin-bottom: 1rem;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid #e2e8f0;
    }
    .pipeline-step {
        background: #f1f5f9;
        border-left: 4px solid #3b82f6;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 0 8px 8px 0;
    }
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #2563eb 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        font-weight: 600;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
    }
    .stButton > button:disabled {
        background: #94a3b8;
        cursor: not-allowed;
    }

    /* --- CUSTOM VISIBLE VERTICAL SCROLLBAR STYLING --- */
    [data-testid="stDataFrame"] ::-webkit-scrollbar, 
    [data-testid="stDataFrame"] * ::-webkit-scrollbar {
        width: 10px !important;
        height: 10px !important;
    }
    [data-testid="stDataFrame"] ::-webkit-scrollbar-thumb,
    [data-testid="stDataFrame"] * ::-webkit-scrollbar-thumb {
        background: #cccccc !important;
        border-radius: 5px !important;
    }
    [data-testid="stDataFrame"] ::-webkit-scrollbar-thumb:hover,
    [data-testid="stDataFrame"] * ::-webkit-scrollbar-thumb:hover {
        background: #999999 !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5rem;">Redrob Candidate Ranking Sandbox</h1>
        <p style="margin: 0.5rem 0 1rem 0; opacity: 0.9;">India Runs Data and AI Challenge - Hackathon Demo</p>
        <div>
            <span class="badge badge-version">Version 1</span>
            <span class="badge badge-cpu">CPU Only</span>
            <span class="badge badge-deterministic">Deterministic</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header">Project Overview</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **AI/ML Candidate Ranking Engine** - A purely rule-based, CPU-only candidate ranking pipeline built in Python with zero external dependencies. The system evaluates job candidates and ranks the **Top 100** candidates for a founding engineer role at a search/retrieval systems company.
        
        **Key Features:**
        - Zero external packages (Python standard library only)
        - CPU-only execution (no GPU required)
        - Deterministic ranking with tie-breaking
        - Explainable reasoning for each selection
        - Memory-efficient streaming processing
        """)
    
    with col2:
        st.markdown("""
        **Pipeline Summary:**
        1. Quality Controller (Fraud Detection)
        2. Semantic Matcher (Relevance Scoring)
        3. Behavioral Multiplier (Signal Adjustments)
        4. Ranking Engine (Final Selection)
        5. Output Generation (CSV Export)
        """)
    
    st.markdown("---")
    

    st.markdown('<div class="section-header">Pipeline Visualization</div>', unsafe_allow_html=True)
    
    pipeline_steps = [
        ("Candidate Dataset", "Upload JSONL file with candidate records"),
        ("Quality Controller", "Filter honeypots and IT services profiles"),
        ("Semantic Matcher", "Calculate relevance scores across 5 dimensions"),
        ("Behavioral Multiplier", "Apply location, notice, activity, responsiveness signals"),
        ("Ranking Engine", "Sort and select Top 100 candidates"),
        ("submission.csv", "Generate ranked output with reasoning")
    ]
    
    cols = st.columns(len(pipeline_steps))
    for i, (step, description) in enumerate(pipeline_steps):
        with cols[i]:
            st.markdown(f"""
            <div class="pipeline-step">
                <strong>{step}</strong>
                <p style="font-size: 0.75rem; color: #64748b; margin: 0.5rem 0 0 0;">{description}</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    
    render_upload_section()
    
    
    st.markdown('<div class="section-header">Run Ranking</div>', unsafe_allow_html=True)
    
    if 'uploaded_file' in st.session_state and st.session_state.uploaded_file is not None:
        if st.button("Generate Rankings", key="run_ranking"):
            with st.spinner("Processing candidates..."):
                
                results = run_ranking_pipeline(st.session_state.uploaded_file)
                st.session_state.results = results
                st.rerun()
    else:
        st.info("Please upload a candidate dataset first to enable ranking.")
    
    
    if 'results' in st.session_state and st.session_state.results is not None:
        st.markdown("---")
        render_results_section(st.session_state.results)
        
        
        render_metrics_section(st.session_state.results)
    
    
    render_footer()

if __name__ == "__main__":
    main()