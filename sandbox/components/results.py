import streamlit as st
import pandas as pd
import os

def render_results_section(results):
    """Render the results section with ranked candidates."""
    st.markdown('<div class="section-header">Results - Top Ranked Candidates</div>', unsafe_allow_html=True)
    
    if 'rankings' in results and len(results['rankings']) > 0:
        # Create DataFrame from results
        df = pd.DataFrame(results['rankings'])
        
        # Display metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Candidates Processed", results.get('total_processed', 0))
        
        with col2:
            st.metric("Candidates Passed", results.get('passed_screening', 0))
        
        with col3:
            st.metric("Top Score", f"{results.get('top_score', 0):.4f}")
        
        with col4:
            st.metric("Average Score", f"{results.get('average_score', 0):.4f}")
        
        st.markdown("---")
        
        # Results table
        st.markdown("**Ranked Candidates:**")
        
        # Sortable dataframe
        st.dataframe(
            df[['rank', 'candidate_id', 'score', 'reasoning']],
            column_config={
                "rank": st.column_config.NumberColumn("Rank", width="small"),
                "candidate_id": st.column_config.NumberColumn("Candidate ID", width="small"),
                "score": st.column_config.NumberColumn("Score", format="%.4f", width="medium"),
                "reasoning": st.column_config.TextColumn("Reasoning", width="large")
            },
            use_container_width=True,
            height=400
        )
        
        # Download button
        st.markdown("---")
        st.markdown("**Download Results:**")
        
        if 'output_file' in results and os.path.exists(results['output_file']):
            with open(results['output_file'], 'r') as f:
                csv_content = f.read()
            
            st.download_button(
                label="Download submission.csv",
                data=csv_content,
                file_name="submission.csv",
                mime="text/csv",
                key="download_csv"
            )
        else:
            st.warning("Output file not found. Please run the ranking pipeline first.")
    else:
        st.info("No results available. Please run the ranking pipeline first.")