"""
AI Document Knowledge Assistant & Q&A App
Main Application Entry Point (Streamlit)
"""

import streamlit as st

def main():
    st.set_page_config(
        page_title="AI Document Knowledge Assistant",
        page_icon="📚",
        layout="wide",
    )

    st.title("📚 AI Document Knowledge Assistant & Q&A")
    st.caption("Week 1 Milestone: Workspace Initialized & Architecture Planned")

    st.info(
        "👋 Welcome! The workspace and foundational documents for Week 1 have been initialized.\n\n"
        "In Week 2 and Week 3, the LangChain retrieval pipeline, OpenAI embeddings, "
        "and FAISS vector database will be connected to enable instant document Q&A with citations."
    )

    with st.sidebar:
        st.header("Project Details")
        st.markdown("**Status:** Week 1 Completed")
        st.markdown("**Target Latency:** < 2.0s")
        st.markdown("**Citation Target:** >= 90%")
        st.divider()
        st.markdown("Developed for DataCrumbs AI Capstone Project")

if __name__ == "__main__":
    main()

