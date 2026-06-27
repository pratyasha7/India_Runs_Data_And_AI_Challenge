import streamlit as st

def render_metrics_section(results):
    """Render the execution metrics section."""
    st.markdown('<div class="section-header">Execution Summary</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Processing Metrics:**
        """)
        st.metric("Total Candidates", results.get('total_processed', 0))
        st.metric("Passed Screening", results.get('passed_screening', 0))
        st.metric("Rejected", results.get('rejected', 0))
    
    with col2:
        st.markdown("""
        **Performance Metrics:**
        """)
        st.metric("Execution Time", f"{results.get('execution_time', 0):.2f} seconds")
        st.metric("Candidates/Second", f"{results.get('throughput', 0):.1f}")
        st.metric("Output File", "submission.csv")
    
    with col3:
        st.markdown("""
        **System Information:**
        """)
        st.metric("Ranking Mode", "CPU Only")
        st.metric("Deterministic", "Yes")
        st.metric("Version", "1.0")
    
    # Expandable execution logs
    with st.expander("View Execution Logs"):
        if 'logs' in results:
            for log in results['logs']:
                st.code(log, language=None)
        else:
            st.info("No execution logs available.")