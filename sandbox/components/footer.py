import streamlit as st
import sys

def render_footer():
    """Render the footer section."""
    st.markdown("---")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        **Redrob Candidate Ranking Sandbox**
        
        Version 1.0
        
        Hackathon Demo
        """)
    
    with col2:
        st.markdown("""
        **System Information:**
        
        Python {}
        
        CPU Only
        """.format(f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"))
    
    with col3:
        st.markdown("""
        **Features:**
        
        Deterministic Ranking
        
        Explainable AI
        """)
    
    with col4:
        st.markdown("""
        **Resources:**
        
        [GitHub Repository]
        
        [Documentation]
        """)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 2rem; padding: 1rem; background: #f8fafc; border-radius: 8px;">
        <p style="margin: 0; color: #64748b; font-size: 0.875rem;">
            Redrob Hackathon - India Runs Data and AI Challenge | CPU-Only Candidate Ranking Engine
        </p>
    </div>
    """, unsafe_allow_html=True)