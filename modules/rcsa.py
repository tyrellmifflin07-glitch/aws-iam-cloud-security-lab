import streamlit as st
import pandas as pd


def show():
    st.title("📊 Operational Risk — RCSA")
    st.markdown("**Risk & Control Self-Assessment · Control Testing · Residual Risk · Action Plans**")
    st.markdown("---")

    st.subheader("Executive RCSA Dashboard")

    rcsa_data = {
        "Risk ID": ["RCSA-001", "RCSA-002", "RCSA-003", "RCSA-004", "RCSA-005", "RCSA-006"],
        "Business Process": [
            "Identity Governance",
            "Privileged Access Management",
            "Cloud Security Monitoring",
            "Vendor Access Management",
            "Change Management",
            "Incident Response"
        ],
        "Risk Statement": [
            "Users retain access after role changes or termination",
            "Privileged accounts may have excessive standing access",
            "Cloud activity may not be fully logged or reviewed",
            "Third-party users may retain unnecessary system access",
            "Unauthorized changes may be introduced without approval",
            "Security incidents may not be escalated within required timeframes"
        ],
        "Inherent Risk": ["High", "Critical", "High", "High", "Medium", "High"],
        "Key Control": [
            "Quarterly access certification and JML review",
            "PIM/JIT access, MFA, approval workflow, and session logging",
            "CloudTrail, GuardDuty, Security Hub, and CloudWatch monitoring",
            "Vendor access reviews and contract-based access expiration",
            "CAB approval and documented change evidence",
            "Incident response runbook and escalation matrix"
        ],
        "Control Effectiveness": ["Partially Effective", "Effective", "Partially Effective", "Needs Improvement", "Effective", "Partially Effective"],
        "Residual Risk": ["Medium", "Medium", "Medium", "High", "Low", "Medium"],
        "Owner": ["IAM Team", "Security", "Cloud Team", "Vendor Management", "ITSM Lead", "SOC Manager"],
        "Action Plan": [
            "Automate terminated-user access removal evidence",
            "Expand PAM coverage to service accounts",
            "Implement monthly log review attestation",
            "Create vendor access expiration dashboard",
            "Maintain change evidence repository",
            "Test IR escalation workflow quarterly"
        ],
        "Status": ["Open", "In Progress", "Open", "Open", "Closed", "In Progress"]
    }

    df_rcsa = pd.DataFrame(rcsa_data)

    total_risks = len(df_rcsa)
    high_residual = len(df_rcsa[df_rcsa["Residual Risk"].isin(["High", "Critical"])])
    open_actions = len(df_rcsa[df_rcsa["Status"].isin(["Open", "In Progress"])])
    effective_controls = len(df_rcsa[df_rcsa["Control Effectiveness"] == "Effective"])

    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Operational Risks", total_risks)
    k2.metric("High Residual Risks", high_residual)
    k3.metric("Open Action Plans", open_actions)
    k4.metric("Effective Controls", effective_controls)

    st.markdown("---")
    st.subheader("RCSA Risk Register")

    f1, f2, f3 = st.columns(3)
    with f1:
        process_filter = st.multiselect(
            "Business Process",
            df_rcsa["Business Process"].unique(),
            default=list(df_rcsa["Business Process"].unique())
        )
    with f2:
        residual_filter = st.multiselect(
            "Residual Risk",
            df_rcsa["Residual Risk"].unique(),
            default=list(df_rcsa["Residual Risk"].unique())
        )
    with f3:
        status_filter = st.multiselect(
            "Status",
            df_rcsa["Status"].unique(),
            default=list(df_rcsa["Status"].unique())
        )

    filtered_rcsa = df_rcsa[
        df_rcsa["Business Process"].isin(process_filter) &
        df_rcsa["Residual Risk"].isin(residual_filter) &
        df_rcsa["Status"].isin(status_filter)
    ]

    def color_risk(val):
        colors = {
            "Critical": "background-color: #a32d2d; color: #ffffff",
            "High": "background-color: #fde8e8; color: #a32d2d",
            "Medium": "background-color: #faeeda; color: #854f0b",
            "Low": "background-color: #eaf3de; color: #3b6d11"
        }
        return colors.get(val, "")

    def color_effectiveness(val):
        colors = {
            "Effective": "background-color: #eaf3de; color: #3b6d11",
            "Partially Effective": "background-color: #faeeda; color: #854f0b",
            "Needs Improvement": "background-color: #fde8e8; color: #a32d2d"
        }
        return colors.get(val, "")

    styled_rcsa = (
        filtered_rcsa.style
        .map(color_risk, subset=["Inherent Risk", "Residual Risk"])
        .map(color_effectiveness, subset=["Control Effectiveness"])
    )

    st.dataframe(styled_rcsa, use_container_width=True, hide_index=True)

    with st.expander("📐 Risk Scoring Methodology"):
        st.markdown("""
        **Residual Risk Calculation Model**

        Residual risk is derived from inherent risk, reduced according to
        assessed control effectiveness:

        | Control Effectiveness | Residual Reduction |
        |---|---|
        | Effective | Inherent reduced by 2 levels |
        | Partially Effective | Inherent reduced by 1 level |
        | Needs Improvement | No reduction — residual equals inherent |

        **Rating scale:** Low → Medium → High → Critical

        **Examples from this register:**
        - RCSA-002: Critical inherent + Effective controls → **Medium** residual
        - RCSA-004: High inherent + Needs Improvement → **High** residual (no credit for weak controls)

        Methodology aligned to COSO ERM risk assessment principles and
        NIST 800-53 RA-3. Control effectiveness ratings are validated through
        first-line self-assessment with second-line challenge.
        """)

    st.markdown("---")
    st.subheader("Executive Risk Narrative")
    st.info("""
    Residual operational risk remains **Medium overall**, with the highest exposure concentrated in
    vendor access management and identity governance. The primary risk drivers are incomplete automation
    for access removal evidence, limited service account PAM coverage, and manual vendor access expiration tracking.
    Recommended next steps are to expand privileged access governance, strengthen access review evidence,
    and implement recurring control attestations.
    """)

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: PM-9, RA-3, CA-7, AC-2, AC-6")
    st.markdown("- SOC 2: CC3.1, CC3.2, CC6.2, CC6.3")
    st.markdown("- COSO: Risk Assessment and Control Activities")
    st.markdown("- COBIT: APO12 Risk Management, DSS05 Security Services")