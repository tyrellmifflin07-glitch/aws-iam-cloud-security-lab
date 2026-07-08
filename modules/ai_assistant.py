import streamlit as st
import pandas as pd


def show():
    st.title("🤖 Project 12 — AI-Powered IAM/GRC Assistant")
    st.markdown("**Live Application · Python · Claude API · Streamlit Cloud**")
    st.markdown("---")

    st.subheader("🌐 Live Application")
    st.markdown("### [Launch the AI GRC Assistant →](https://iam-grc-assistant.streamlit.app)")
    st.markdown("💻 [View Source on GitHub](https://github.com/tyrellmifflin07-glitch/iam-grc-assistant)")

    st.markdown("---")
    st.subheader("What It Does")
    st.markdown("""
    A deployed, production AI application with two capabilities:

    **IAM Risk Assessment** — Upload user access data and receive automated
    risk detection, enterprise risk taxonomy classification (Cyber, Technology,
    Data, AI, Third-Party), control mapping across seven frameworks
    (NIST 800-53, PCI-DSS, SOC 2, HIPAA, COSO, COBIT, DORA), and AI-generated
    audit reports with thematic risk analysis.

    **AI Adoption Risk Advisor** — Describe a proposed AI use case and receive
    a structured second-line risk assessment with likelihood/impact ratings,
    recommended controls with first-line ownership, and a formal
    Approve / Approve with Conditions / Defer recommendation.
    """)

    st.markdown("---")
    st.subheader("Scalability — Stress Tested")
    scale_data = {
        "Users": ["1,000", "10,000", "50,000", "100,000"],
        "Analysis Time": ["< 0.01s", "< 0.01s", "0.02s", "0.05s"],
        "Findings Processed": ["232", "2,502", "12,316", "24,925"]
    }
    st.dataframe(pd.DataFrame(scale_data), use_container_width=True, hide_index=True)
    st.caption("AI narrator uses intelligent aggregation — statistical summaries plus prioritized Critical/High detail — enabling executive-quality reports at any dataset size.")

    st.markdown("---")
    st.subheader("Engineering Concepts Demonstrated")
    st.markdown("""
    - **AI/LLM Integration** — Claude API with structured prompt engineering
    - **Scalable architecture** — token-aware aggregation for large datasets
    - **Enterprise risk taxonomy** — ERM-aligned finding classification
    - **Multi-framework compliance mapping** — 7 frameworks, article-level detail
    - **Secure secrets management** — environment-based API key handling
    - **CI/CD** — GitHub-to-Streamlit-Cloud automated deployment
    """)    