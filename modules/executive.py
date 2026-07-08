import streamlit as st
import pandas as pd


def show():
    st.title("🏠 MiffTech Identity & Risk Governance Platform")
    st.subheader("Enterprise IAM · Cloud Security · GRC · AI Risk Intelligence")
    st.markdown("""
    This platform demonstrates how enterprise security programs connect **identity governance,
    cloud security, operational risk, compliance, project governance, and AI-assisted GRC** into
    one executive-ready governance dashboard.

    The detailed project pages remain available in the sidebar as implementation evidence behind
    each platform capability.
    """)

    st.markdown("---")

    st.subheader("Executive Security Scorecard")
    score1, score2, score3, score4, score5, score6 = st.columns(6)
    score1.metric("Identity Security", "96%", delta="+4% maturity")
    score2.metric("Cloud Security", "94%", delta="+3% posture")
    score3.metric("Compliance", "97%", delta="+5 controls")
    score4.metric("Overall Risk", "Medium")
    score5.metric("Critical Findings", "3", delta="-2 remediated", delta_color="inverse")
    score6.metric("Open Actions", "5", delta="-1 this sprint", delta_color="inverse")

    st.caption("Representative executive indicators based on the IAM, cloud security, RCSA, project governance, and AI GRC modules in this portfolio.")

    st.markdown("---")

    st.subheader("Platform Overview")
    st.markdown("""
    **MiffTech Identity & Risk Governance Platform** is a portfolio-grade governance application
    built with Python and Streamlit. It connects technical security implementation with the way
    enterprise teams govern identity, cloud risk, access reviews, privileged access, project risk,
    operational controls, and executive reporting.

    The purpose is to demonstrate not only that security controls can be configured, but also that
    they can be governed, measured, documented, mapped to frameworks, and communicated to leadership.
    """)

    st.markdown("---")

    st.subheader("Platform Capability Map")

    cap1, cap2 = st.columns(2)

    with cap1:
        st.markdown("""
        ### 👤 Identity Governance
        Active Directory, RBAC, access certifications, role engineering, access requests,
        Joiner-Mover-Leaver lifecycle, privileged access, Entra ID governance, and IAM modernization.

        **Supporting evidence:** Projects 3–10

        ### ☁️ Cloud Security
        AWS infrastructure, network segmentation, load balancing, CloudTrail, GuardDuty,
        Security Hub, CloudWatch, and external attack-surface validation.

        **Supporting evidence:** Projects 1–2 and Monitoring & Detection

        ### 📊 Operational Risk
        RCSA, inherent risk, residual risk, control effectiveness, ownership, and remediation action tracking.

        **Supporting evidence:** Operational Risk — RCSA
        """)

    with cap2:
        st.markdown("""
        ### 📁 Project Governance
        Project charter, RAID log, risk register, stakeholder register, milestones,
        executive status reporting, and leadership decision tracking.

        **Supporting evidence:** Project 11 and Project Governance

        ### 🤖 AI Risk Intelligence
        AI-powered IAM risk assessment, AI adoption risk advisory, control mapping,
        thematic risk analysis, and executive-ready reporting.

        **Supporting evidence:** Project 12 — AI GRC Assistant

        ### 📈 Executive Reporting
        Security posture, compliance coverage, open findings, control maturity,
        action plans, and leadership-ready summaries.
        """)

    st.markdown("---")

    st.subheader("Governance Snapshot")
    g1, g2, g3, g4, g5, g6 = st.columns(6)
    g1.metric("Managed Identities", "100K")
    g2.metric("Privileged Accounts", "42")
    g3.metric("Access Reviews", "Complete")
    g4.metric("High Risks", "4")
    g5.metric("Audit Findings", "6")
    g6.metric("Control Coverage", "92%")

    st.markdown("---")

    st.subheader("Compliance & Control Coverage")
    framework_data = {
        "Framework": [
            "NIST 800-53",
            "PCI DSS",
            "SOC 2",
            "HIPAA",
            "ISO 27001",
            "COSO / COBIT"
        ],
        "Coverage Demonstrated": [
            "Access control, audit logging, risk management, least privilege, continuous monitoring",
            "Authentication, least privilege, logging, access reviews, security policy requirements",
            "Security, availability, access control, risk assessment, and vendor governance",
            "Administrative safeguards, technical safeguards, and access management controls",
            "Asset management, access control, operations security, and governance controls",
            "Enterprise risk management, control activities, IT governance, and risk ownership"
        ],
        "Portfolio Evidence": [
            "IAM, RCSA, Monitoring, Project Governance",
            "IAM, Access Reviews, Logging, Cloud Security",
            "Identity Governance, Risk Assessment, Vendor Risk direction",
            "Access Management and Administrative Controls",
            "Cloud Security, IAM Governance, Operations Security",
            "RCSA, Project Governance, AI Risk Advisory"
        ]
    }
    st.dataframe(pd.DataFrame(framework_data), use_container_width=True, hide_index=True)

    st.markdown("---")

    st.subheader("Recent Governance Activity")
    activity_data = {
        "Activity": [
            "MiffTech branding applied across the platform",
            "Operational Risk RCSA module added",
            "Quarterly access certification workflow documented",
            "Privileged access governance controls documented",
            "CloudTrail and Security Hub monitoring validated",
            "AI GRC Assistant integrated as a portfolio capability"
        ],
        "Area": [
            "Platform Branding",
            "Operational Risk",
            "Identity Governance",
            "Privileged Access",
            "Cloud Security",
            "AI Risk Intelligence"
        ],
        "Status": [
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete"
        ]
    }

    st.dataframe(pd.DataFrame(activity_data), use_container_width=True, hide_index=True)

    st.markdown("---")

    st.subheader("Implementation Evidence")
    evidence_data = {
        "Capability": [
            "Cloud Web Infrastructure",
            "Network Segmentation",
            "Active Directory & IAM",
            "Access Certifications",
            "Role Engineering",
            "Access Request Workflow",
            "JML Lifecycle",
            "Privileged Access",
            "Entra ID Governance",
            "IAM Modernization",
            "RAID / Risk Register",
            "AI GRC Assistant",
            "Operational Risk RCSA"
        ],
        "Evidence Location": [
            "Project 1",
            "Project 2",
            "Project 3",
            "Project 4",
            "Project 5",
            "Project 6",
            "Project 7",
            "Project 8",
            "Project 9",
            "Project 10",
            "Project 11 / Project Governance",
            "Project 12",
            "Operational Risk — RCSA"
        ],
        "Status": [
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete",
            "✅ Complete"
        ]
    }

    st.dataframe(pd.DataFrame(evidence_data), use_container_width=True, hide_index=True)