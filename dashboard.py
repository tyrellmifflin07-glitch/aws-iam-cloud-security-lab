# dashboard.py
# Purpose: AWS IAM & Cloud Security Lab Portfolio Dashboard

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AWS IAM & Cloud Security Lab",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        background-color: #141C26;
        border-right: 2px solid #00B4D8;
    }
    section[data-testid="stSidebar"] .stMarkdown, 
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p {
        color: #DEE5EE !important;
    }
    section[data-testid="stSidebar"] a {
        color: #00B4D8 !important;
    }
    h1, h2, h3 {
        color: #0E2A47 !important;
    }
    [data-testid="stMetricValue"] {
        color: #00B4D8;
    }
</style>
""", unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.title("🛡️ Lab Navigation")
st.sidebar.markdown("**Tyrell Mifflin**")
st.sidebar.markdown("IAM/GRC Consultant · CEH · CSM")
st.sidebar.markdown("---")

page = st.sidebar.radio("Select a section:", [
    "🏠 Overview",
    "☁️ Project 1 — Cloud Web Infrastructure",
    "🔀 Project 2 — Load Balancer & Network",
    "🪪 Project 3 — Active Directory & IAM",
    "✅ Project 4 — Access Certifications",
    "🎭 Project 5 — Role Engineering",
    "📋 Project 6 — Access Request Workflow",
    "🔄 Project 7 — JML Lifecycle",
    "🔐 Project 8 — Privileged Access",
    "☁️ Project 9 — Entra ID Governance",
    "🗺️ Project 10 — IAM Modernization Roadmap",
    "📋 Project 11 — RAID Log & Risk Register",
    "📁 Project Governance",
    "🤖 Project 12 — AI GRC Assistant (Live App)",
    "📊 Monitoring & Detection",
    "🔗 Links & Contact"
])

st.sidebar.markdown("---")
st.sidebar.markdown("🌐 [Live GRC Tool](https://iam-grc-assistant.streamlit.app)")
st.sidebar.markdown("💻 [GitHub](https://github.com/tyrellmifflin07-glitch)")
st.sidebar.markdown("🔗 [LinkedIn](https://linkedin.com/in/tyrell-mifflin-ceh-csm-85a27583)")

# ── OVERVIEW ──────────────────────────────────────────────
if page == "🏠 Overview":
    st.title("🛡️ AWS IAM & Cloud Security Lab")
    st.subheader("Enterprise-Grade Identity Governance & Cloud Security Portfolio")
    st.markdown("""
    This lab replicates an enterprise AWS environment across **12 completed projects** spanning
    cloud infrastructure, Active Directory identity governance, access certifications,
    privileged access management, security monitoring, and GRC program management.
    """)

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Projects Completed", "12")
    col2.metric("Frameworks Applied", "5")
    col3.metric("IAM Controls Demonstrated", "20+")
    col4.metric("AWS Services Used", "12+")

    st.markdown("---")
    st.subheader("🎯 Cybersecurity Program Dashboard")
    pcol1, pcol2, pcol3, pcol4, pcol5, pcol6 = st.columns(6)
    pcol1.metric("Projects", "1")
    pcol2.metric("Open Risks", "6")
    pcol3.metric("Open Issues", "2")
    pcol4.metric("Milestones", "4")
    pcol5.metric("Completion", "72%")
    pcol6.metric("Exec Status", "🟢 Green")
    st.caption("Full PM artifacts — Charter, RAID Log, Risk Register, Stakeholders, Executive Status — in the 📁 Project Governance section")

    st.markdown("---")
    st.subheader("Capabilities Demonstrated")

    capabilities = {
        "Cloud Infrastructure Security": "EC2, ALB, VPC, Security Groups, network segmentation",
        "Identity & Access Governance": "Active Directory, OUs, RBAC, JML lifecycle, service account governance",
        "AWS IAM Governance": "IAM roles, least privilege, MFA, CloudTrail, Config, GuardDuty, Security Hub",
        "Security Monitoring": "CloudWatch, GuardDuty, Nginx logs, auth.log, external Nmap validation",
        "GRC Program Management": "RAID Log, Risk Register, risk tracking, stakeholder accountability",
        "Governance Frameworks": "Least privilege, defense-in-depth, SoD, access certification, audit readiness"
    }

    for cap, desc in capabilities.items():
        st.markdown(f"**{cap}** — {desc}")

    st.markdown("---")
    st.subheader("Projects at a Glance")

    projects = [
        ("1", "Secure Cloud Web Infrastructure", "EC2 · Nginx · Docker · OWASP Juice Shop", "✅"),
        ("2", "Application Load Balancer & Network Segmentation", "Multi-AZ ALB · Security Groups · VPC", "✅"),
        ("3", "Active Directory & IAM Governance", "AD DS · RBAC · JML · GPOs · Service Accounts", "✅"),
        ("4", "Access Certification & Governance Review", "Quarterly cycles · SoD · Remediation closure", "✅"),
        ("5", "Role Engineering & Birthright Access", "Role matrix · Entitlement standardization", "✅"),
        ("6", "Access Request & Approval Workflow", "Formal request · Approval chain · Evidence", "✅"),
        ("7", "Joiner-Mover-Leaver Lifecycle", "End-to-end provisioning and deprovisioning", "✅"),
        ("8", "Privileged Access & Temporary Elevation", "PAM concepts · JIT access · Session governance", "✅"),
        ("9", "Microsoft Entra ID Cloud Governance", "Cloud RBAC · PIM · Conditional Access", "✅"),
        ("10", "IAM Modernization Roadmap", "SailPoint · CyberArk · Entra ID · 12-month plan", "✅"),
        ("11", "RAID Log & Risk Register", "Risk tracking · Assumptions · Issues · Dependencies", "✅"),
        ("12", "AI GRC Assistant (Live App)", "AI risk analysis · 7 frameworks · Tested to 100K users", "✅"),
    ]

    for num, title, desc, status in projects:
        st.markdown(f"{status} **Project {num} — {title}**  \n{desc}")

    st.markdown("---")
    st.subheader("Frameworks Applied")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- NIST SP 800-53 — AC-2, AC-6, AC-17, PS-4, PM-9")
        st.markdown("- PCI-DSS — Requirements 7, 8, 10, 12")
        st.markdown("- SOC 2 — CC6.2, CC6.3, CC9.2")
    with col2:
        st.markdown("- HIPAA — 45 CFR §164.308, §164.312")
        st.markdown("- ISO 27001 — A.8, A.12")
        st.markdown("- CIS AWS Foundations Benchmark")

# ── PROJECT 1 ──────────────────────────────────────────────
elif page == "☁️ Project 1 — Cloud Web Infrastructure":
    st.title("☁️ Project 1 — Secure Cloud Web Infrastructure")
    st.markdown("**EC2 · Nginx Reverse Proxy · Docker · OWASP Juice Shop**")
    st.markdown("---")

    st.subheader("Objective")
    st.markdown("Design and deploy a hardened cloud-hosted web environment demonstrating secure server provisioning, attack surface reduction, and defense-in-depth architecture using a reverse proxy pattern.")

    st.subheader("What Was Built")
    st.markdown("""
    - Provisioned Ubuntu Server 24.04 EC2 instance with RSA key-pair authentication
    - Configured Security Group with scoped inbound rules — SSH restricted to admin IP only
    - Installed and configured Nginx as reverse proxy
    - Deployed Docker and containerized OWASP Juice Shop
    - Hardened environment by removing public port 3000 — eliminated direct container exposure
    """)

    st.subheader("Final Architecture")
    st.code("Internet → AWS Security Group → Nginx (Port 80/443) → Localhost:3000 → OWASP Juice Shop (Docker)")

    st.subheader("Governance & Security Concepts")
    concepts = {
        "Attack Surface Reduction": "Removed unnecessary public port exposure after validating reverse proxy",
        "Defense-in-Depth": "Layered controls: Security Group → reverse proxy → containerized app",
        "Key-Based Authentication": "RSA key pair for SSH — no password authentication",
        "Network Segmentation": "Public vs internal service exposure via Security Group rules",
        "Containerization Security": "Isolated application runtime via Docker"
    }
    for concept, desc in concepts.items():
        st.markdown(f"**{concept}** — {desc}")

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: SC-7 (Boundary Protection), AC-17 (Remote Access), CM-7 (Least Functionality)")
    st.markdown("- CIS AWS: 5.1 — Security Group rules, 5.4 — SSH access restriction")

# ── PROJECT 2 ──────────────────────────────────────────────
elif page == "🔀 Project 2 — Load Balancer & Network":
    st.title("🔀 Project 2 — Application Load Balancer & Network Segmentation")
    st.markdown("**Multi-AZ ALB · Security Group re-architecture · Backend isolation**")
    st.markdown("---")

    st.subheader("Objective")
    st.markdown("Extend cloud infrastructure with a highly-available ALB while enforcing strict network segmentation between public-facing and backend resources.")

    st.subheader("What Was Built")
    st.markdown("""
    - Validated multi-AZ public subnet configuration for ALB high availability
    - Created dedicated ALB security group permitting public HTTP/HTTPS traffic
    - Deployed internet-facing ALB spanning two availability zones
    - Re-architected EC2 security group to accept traffic only from ALB — closed direct public access
    """)

    st.subheader("Governance & Security Concepts")
    concepts = {
        "Network Segmentation": "Backend EC2 isolated from direct internet — only reachable via ALB",
        "High Availability": "Multi-AZ subnet mapping for resilience",
        "Least Privilege (Infrastructure)": "Security group rules scoped to source security group",
        "Health Monitoring": "Automated health checks ensure traffic routes to healthy targets only",
        "Defense-in-Depth": "Additional control layer between internet and compute"
    }
    for concept, desc in concepts.items():
        st.markdown(f"**{concept}** — {desc}")

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: SC-7, SC-5, SI-3")
    st.markdown("- PCI-DSS: Requirement 1 — Network security controls")

# ── PROJECT 3 ──────────────────────────────────────────────
elif page == "🪪 Project 3 — Active Directory & IAM":
    st.title("🪪 Project 3 — Active Directory & IAM Governance Lab")
    st.markdown("**Domain: ascended.local · RBAC · JML · Service Accounts · GPOs**")
    st.markdown("---")

    st.subheader("Objective")
    st.markdown("Deploy Active Directory, implement RBAC, simulate JML lifecycle management, and enforce enterprise authentication policy baselines.")

    st.subheader("OU Structure")
    st.markdown("Finance · IT · Security · Developers · Service Accounts · Terminated Users")

    st.subheader("RBAC Security Groups")
    groups = {
        "IT_Admins": "Administrative access",
        "Helpdesk": "User support access",
        "Finance_Read": "Read-only finance access",
        "Finance_Modify": "Finance management access",
        "Security_Analysts": "Security operations access"
    }
    for group, purpose in groups.items():
        st.markdown(f"**{group}** — {purpose}")

    st.subheader("Authentication Policy Baseline")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Password History", "24 passwords")
        st.metric("Max Password Age", "90 days")
        st.metric("Min Password Length", "14 characters")
    with col2:
        st.metric("Lockout Threshold", "5 attempts")
        st.metric("Lockout Duration", "15 minutes")
        st.metric("Complexity", "Enabled")

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, AC-3, AC-6, IA-5, PS-4")
    st.markdown("- PCI-DSS: Requirements 7, 8")
    st.markdown("- SOC 2: CC6.2, CC6.3")

# ── PROJECT 4 ──────────────────────────────────────────────
elif page == "✅ Project 4 — Access Certifications":
    st.title("✅ Project 4 — Access Certification & Governance Review Cycle")
    st.markdown("**Quarterly review · SoD enforcement · Remediation closure**")
    st.markdown("---")

    st.subheader("Access Certification Results")
    cert_data = {
        "User": ["Sarah Johnson", "Greg Jackson", "John Smith"],
        "Result": [
            "⚠️ Flagged — IAM-Admin excessive for Finance Manager (SoD concern)",
            "✅ Approved — Security_Analysts access validated",
            "🚫 Deprovisioned — access fully revoked (Leaver)"
        ]
    }
    st.dataframe(pd.DataFrame(cert_data))

    st.subheader("Service Account Governance Review")
    svc_data = {
        "Account": ["svc_backup", "svc_sql", "svc_monitoring"],
        "Result": ["✅ Approved", "✅ Approved", "✅ Approved"]
    }
    st.dataframe(pd.DataFrame(svc_data))

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2(7), AC-6, AU-9")
    st.markdown("- SOC 2: CC6.2, CC6.3")
    st.markdown("- PCI-DSS: Requirement 7.2, 8.1")

# ── PROJECT 5 ──────────────────────────────────────────────
elif page == "🎭 Project 5 — Role Engineering":
    st.title("🎭 Project 5 — Role Engineering & Birthright Access Governance")
    st.markdown("**Role matrix · Birthright entitlements · Entitlement standardization**")
    st.markdown("---")

    st.subheader("Role Engineering Matrix")
    role_data = {
        "Role": ["Finance Analyst", "Finance Manager", "Security Analyst", "Helpdesk Technician"],
        "Birthright Entitlement": ["Finance_Read", "Finance_Modify", "Security_Analysts", "Helpdesk"],
        "User": ["Lisa Brown", "Robert Davis", "Karen White", "Mike Green"]
    }
    st.dataframe(pd.DataFrame(role_data))

    st.subheader("Governance Concepts Demonstrated")
    st.markdown("""
    - Role-Based Access Control (RBAC)
    - Role Engineering
    - Birthright Access
    - Entitlement Management
    - Least Privilege
    - Identity Governance
    - Access Lifecycle Management
    """)

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, AC-3, AC-6")
    st.markdown("- SOC 2: CC6.3")

# ── PROJECT 6 ──────────────────────────────────────────────
elif page == "📋 Project 6 — Access Request Workflow":
    st.title("📋 Project 6 — Access Request & Approval Workflow")
    st.markdown("**Formal request · Manager approval · Least privilege · Evidence collection**")
    st.markdown("---")

    st.subheader("Scenario")
    st.markdown("Formal access request for **Lisa Brown** (Finance Analyst) requesting temporary Finance_Modify access during manager leave of absence.")

    st.subheader("Access Request Record")
    request_data = {
        "Field": ["Requestor", "Access Requested", "Business Justification", "Approver", "IAM Review", "Expiration"],
        "Detail": [
            "Lisa Brown (Finance Analyst)",
            "Finance_Modify (temporary elevation)",
            "Coverage during management leave of absence",
            "Robert Davis (Finance Manager)",
            "Approved — least privilege validated, temporary duration confirmed",
            "30 days from provisioning"
        ]
    }
    st.dataframe(pd.DataFrame(request_data))

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, AC-3, AC-6")
    st.markdown("- SOC 2: CC6.3")
    st.markdown("- PCI-DSS: Requirement 7.2")

# ── PROJECT 7 ──────────────────────────────────────────────
elif page == "🔄 Project 7 — JML Lifecycle":
    st.title("🔄 Project 7 — Joiner-Mover-Leaver Lifecycle Simulation")
    st.markdown("**End-to-end identity lifecycle management**")
    st.markdown("---")

    st.subheader("JML Lifecycle Results")
    jml_data = {
        "Event": ["Joiner", "Mover", "Leaver"],
        "User": ["Greg Jackson", "Sarah Johnson", "John Smith"],
        "Action": [
            "Provisioned to Security_Analysts group",
            "Promoted to Finance Manager — access updated to Finance_Modify",
            "Account disabled · Privileged access removed · Moved to Terminated Users OU"
        ],
        "Result": ["✅ Access granted", "✅ Access modified", "🚫 Access revoked"]
    }
    st.dataframe(pd.DataFrame(jml_data))

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, PS-4, PS-5")
    st.markdown("- PCI-DSS: Requirement 8.1.4, 8.2.6")
    st.markdown("- SOC 2: CC6.2, CC6.3")
    st.markdown("- HIPAA: 45 CFR §164.308(a)(3)(ii)(C)")

# ── PROJECT 8 ──────────────────────────────────────────────
elif page == "🔐 Project 8 — Privileged Access":
    st.title("🔐 Project 8 — Privileged Access & Temporary Elevation Governance")
    st.markdown("**PAM concepts · JIT access · Session governance · Least privilege enforcement**")
    st.markdown("---")

    st.subheader("Objective")
    st.markdown("Demonstrate privileged access governance including just-in-time elevation, session monitoring concepts, and standing privilege reduction.")

    st.subheader("Governance Controls Demonstrated")
    st.markdown("""
    - Just-In-Time (JIT) privileged access provisioning concepts
    - Time-bound access with automatic expiration
    - Privileged session monitoring and logging
    - MFA enforcement for privileged accounts
    - Standing privilege elimination
    - Approval workflow for privileged elevation requests
    """)

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, AC-6, AC-17, IA-2")
    st.markdown("- PCI-DSS: Requirement 7.2, 8.2")
    st.markdown("- SOC 2: CC6.3, CC6.6")

# ── PROJECT 9 ──────────────────────────────────────────────
elif page == "☁️ Project 9 — Entra ID Governance":
    st.title("☁️ Project 9 — Microsoft Entra ID Cloud Identity Governance")
    st.markdown("**Cloud RBAC · PIM · Conditional Access · Least privilege**")
    st.markdown("---")

    st.subheader("What Was Implemented")
    st.markdown("""
    - Assigned Security Administrator (not Global Administrator) to Karen White — least privilege role alignment
    - Configured eligible (not permanent) Security Administrator role with 8-hour time-bound activation via PIM
    - Evaluated Conditional Access policies — blocked login from Russia on unknown device at 2:00 AM
    - Mapped enterprise IAM tool responsibilities across Entra ID, SailPoint, and CyberArk
    """)

    st.subheader("Key Governance Decisions")
    decisions = {
        "Role Assignment": "Security Administrator vs Global Administrator — documented least privilege rationale",
        "PIM Configuration": "Eligible role with 8-hour window and automatic expiry — eliminates standing privilege",
        "Conditional Access": "Blocked Mike Green — MFA, managed device, and approved-country policy violations"
    }
    for decision, detail in decisions.items():
        st.markdown(f"**{decision}** — {detail}")

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: AC-2, AC-6, IA-2, AC-17")
    st.markdown("- SOC 2: CC6.3, CC6.6")

# ── PROJECT 10 ──────────────────────────────────────────────
elif page == "🗺️ Project 10 — IAM Modernization Roadmap":
    st.title("🗺️ Project 10 — IAM Modernization Roadmap")
    st.markdown("**SailPoint · CyberArk · Entra ID · 12-month phased plan**")
    st.markdown("---")

    st.subheader("Tool Responsibility Matrix")
    tools = {
        "Tool": ["Microsoft Entra ID", "SailPoint IdentityNow", "CyberArk PAM"],
        "Primary Function": ["Authentication · Cloud identity", "IGA · Access certification", "PAM · Credential vaulting"],
        "Governance Layer": ["Identity provider", "Governance & compliance", "Privileged access control"]
    }
    st.dataframe(pd.DataFrame(tools))

    st.subheader("12-Month Roadmap")
    roadmap = {
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Focus": [
            "Discovery — inventory identities, roles, and entitlements",
            "Role engineering · SoD analysis · Access certification baseline",
            "Automation · KPI/KRI reporting · Governance dashboards",
            "PAM expansion · NHI governance · Entra ID Governance rollout"
        ]
    }
    st.dataframe(pd.DataFrame(roadmap))

# ── PROJECT 11 ──────────────────────────────────────────────
elif page == "📋 Project 11 — RAID Log & Risk Register":
    st.title("📋 Project 11 — RAID Log & Risk Register")
    st.markdown("**Entra ID Implementation · Risk · Assumptions · Issues · Dependencies**")
    st.markdown("---")

    st.subheader("Project Context")
    st.markdown("""
    During the Microsoft Entra ID implementation for the Finance Department,
    a formal RAID Log and Risk Register were maintained to track governance
    decisions, emerging risks, and dependencies — replicating enterprise
    GRC program management practices.
    """)

    st.markdown("---")
    st.subheader("📊 Risk Register")

    risk_data = {
        "ID": ["R001", "R002", "R003", "R004", "R005"],
        "Risk": [
            "MFA rollout may lock out Finance users",
            "Incorrect RBAC assignments post-migration",
            "Active Directory Connect sync failure",
            "Legacy applications incompatible with Entra ID",
            "MFA adoption delays impacting go-live"
        ],
        "Impact": ["High", "High", "Medium", "Medium", "Medium"],
        "Owner": ["IAM Team", "IAM Team", "Infrastructure", "Security", "PM"],
        "Mitigation": [
            "Pilot with 20 users before full rollout",
            "Peer review all role assignments before deployment",
            "Test Azure AD Connect in staging before production",
            "Inventory all applications prior to cutover",
            "Communicate rollout plan 2 weeks in advance"
        ],
        "Status": ["Monitoring", "Open", "Closed", "Open", "Monitoring"]
    }

    df_risk = pd.DataFrame(risk_data)

    def color_status(val):
        if val == "Open":
            return "background-color: #fde8e8; color: #a32d2d"
        elif val == "Closed":
            return "background-color: #eaf3de; color: #3b6d11"
        elif val == "Monitoring":
            return "background-color: #faeeda; color: #854f0b"
        return ""

    def color_impact(val):
        if val == "High":
            return "background-color: #fde8e8; color: #a32d2d"
        elif val == "Medium":
            return "background-color: #faeeda; color: #854f0b"
        return ""

    styled = df_risk.style.map(color_status, subset=["Status"]).map(color_impact, subset=["Impact"])

    st.dataframe(styled, use_container_width=True)

    st.markdown("---")
    st.subheader("📋 RAID Log")

    raid_data = {
        "Type": ["Risk", "Risk", "Assumption", "Assumption", "Issue", "Issue", "Dependency", "Dependency"],
        "ID": ["R001", "R002", "A001", "A002", "I001", "I002", "D001", "D002"],
        "Description": [
            "Users may lose access after Conditional Access rollout",
            "MFA rollout delays may push go-live date",
            "HR provides accurate and current employee data for provisioning",
            "All Finance users have smartphones capable of MFA",
            "Finance user cannot access Salesforce after Entra ID migration",
            "Azure AD Connect sync failed during initial configuration",
            "Networking team must open firewall ports for Azure AD Connect",
            "HR system must export termination data for automated deprovisioning"
        ],
        "Owner": ["IAM Team", "PM", "HR", "IAM Team", "IAM Team", "Infrastructure", "Networking", "HR"],
        "Status": ["Open", "Monitoring", "Confirmed", "Confirmed", "Resolved", "Resolved", "Open", "Open"]
    }

    df_raid = pd.DataFrame(raid_data)

    def color_raid_type(val):
        colors = {
            "Risk": "background-color: #fde8e8; color: #a32d2d",
            "Assumption": "background-color: #e6f1fb; color: #185fa5",
            "Issue": "background-color: #faeeda; color: #854f0b",
            "Dependency": "background-color: #e1f5ee; color: #0f6e56"
        }
        return colors.get(val, "")

    styled_raid = df_raid.style.map(color_raid_type, subset=["Type"])
    st.dataframe(styled_raid, use_container_width=True)

    st.markdown("---")
    st.subheader("Governance Value")
    st.markdown("""
    Maintaining a RAID Log alongside technical implementation demonstrates:
    - **Program-level governance thinking** — not just technical execution
    - **Risk identification and tracking** before issues become incidents
    - **Stakeholder accountability** — every risk and dependency has an owner
    - **Audit readiness** — documented evidence of governance decisions throughout the project
    """)

    st.subheader("Frameworks Mapped")
    st.markdown("- NIST 800-53: PM-9 (Risk Management Strategy), PM-11 (Mission/Business Process Definition)")
    st.markdown("- SOC 2: CC3.1, CC3.2 (Risk Assessment)")
    st.markdown("- PCI-DSS: Requirement 12.3 (Risk Assessment)")
    st.markdown("- ISO 27001: A.8 (Asset Management), A.12 (Operations Security)")

# ── PROJECT GOVERNANCE ──────────────────────────────────────
elif page == "📁 Project Governance":
    st.title("📁 Project Governance — PM Command Center")
    st.markdown("**Project Charter · RAID Log · Risk Register · Stakeholders · Executive Status**")
    st.markdown("---")

    st.subheader("🎯 Cybersecurity Program Dashboard")
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Projects", "1")
    col2.metric("Open Risks", "6")
    col3.metric("Open Issues", "2")
    col4, col5, col6 = st.columns(3)
    col4.metric("Upcoming Milestones", "4")
    col5.metric("Completion", "72%")
    col6.metric("Executive Status", "🟢 Green")

    st.markdown("---")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📜 Project Charter",
        "📋 RAID Log",
        "⚠️ Risk Register",
        "👥 Stakeholders",
        "📊 Executive Status"
    ])

    # ── TAB 1: PROJECT CHARTER ──
    with tab1:
        st.subheader("Project Charter")

        charter = {
            "Field": [
                "Project Name",
                "Sponsor",
                "Project Manager",
                "Objective",
                "Status",
                "Completion"
            ],
            "Detail": [
                "AWS IAM Security Modernization",
                "Chief Information Security Officer",
                "Tyrell Mifflin",
                "Implement enterprise IAM controls using AWS IAM, RBAC, CloudTrail, CloudWatch, Security Hub, and governance best practices",
                "In Progress",
                "72%"
            ]
        }
        st.dataframe(pd.DataFrame(charter), use_container_width=True, hide_index=True)

        st.progress(0.72, text="Overall Project Completion — 72%")

        st.markdown("**Key Milestones**")
        milestones = {
            "Milestone": [
                "IAM policy baseline established",
                "RBAC implementation complete",
                "MFA rollout — all privileged accounts",
                "CloudTrail centralized logging live",
                "Security Hub findings remediation",
                "Access certification cycle 1"
            ],
            "Target": ["Q1", "Q2", "Q2", "Q3", "Q3", "Q4"],
            "Status": ["✅ Complete", "✅ Complete", "🔄 In Progress", "✅ Complete", "🔄 In Progress", "📅 Scheduled"]
        }
        st.dataframe(pd.DataFrame(milestones), use_container_width=True, hide_index=True)

    # ── TAB 2: RAID LOG ──
    with tab2:
        st.subheader("RAID Log")

        raid_gov_data = {
            "Type": ["Risk", "Risk", "Issue", "Issue", "Action", "Action", "Dependency", "Dependency"],
            "ID": ["R-01", "R-02", "I-01", "I-02", "A-01", "A-02", "D-01", "D-02"],
            "Description": [
                "IAM roles configured with overly permissive policies",
                "MFA adoption delays may impact go-live schedule",
                "Security Hub critical finding — CloudTrail configuration gap",
                "Finance user group unable to access reporting application post-RBAC migration",
                "Deploy MFA enforcement policy to all privileged accounts",
                "Complete peer review of all IAM policy documents",
                "HR must provide current employee roster for access recertification",
                "Network team must complete firewall rules for logging pipeline"
            ],
            "Owner": ["IAM Team", "PM", "AWS Admin", "IAM Team", "Security", "IAM Team", "HR", "Network Team"],
            "Priority": ["High", "Medium", "Critical", "High", "High", "Medium", "Medium", "High"],
            "Status": ["Open", "Monitoring", "Open", "Resolved", "In Progress", "In Progress", "Open", "Open"]
        }

        df_raid_gov = pd.DataFrame(raid_gov_data)

        # Filters — exactly how PMs work
        fcol1, fcol2, fcol3 = st.columns(3)
        with fcol1:
            type_filter = st.multiselect("Filter by Type", options=df_raid_gov["Type"].unique(), default=list(df_raid_gov["Type"].unique()))
        with fcol2:
            status_filter = st.multiselect("Filter by Status", options=df_raid_gov["Status"].unique(), default=list(df_raid_gov["Status"].unique()))
        with fcol3:
            priority_filter = st.multiselect("Filter by Priority", options=df_raid_gov["Priority"].unique(), default=list(df_raid_gov["Priority"].unique()))

        search = st.text_input("🔍 Search descriptions")

        filtered = df_raid_gov[
            df_raid_gov["Type"].isin(type_filter) &
            df_raid_gov["Status"].isin(status_filter) &
            df_raid_gov["Priority"].isin(priority_filter)
        ]
        if search:
            filtered = filtered[filtered["Description"].str.contains(search, case=False)]

        def color_gov_type(val):
            colors = {
                "Risk": "background-color: #fde8e8; color: #a32d2d",
                "Issue": "background-color: #faeeda; color: #854f0b",
                "Action": "background-color: #e6f1fb; color: #185fa5",
                "Dependency": "background-color: #e1f5ee; color: #0f6e56"
            }
            return colors.get(val, "")

        def color_gov_priority(val):
            colors = {
                "Critical": "background-color: #a32d2d; color: #ffffff",
                "High": "background-color: #fde8e8; color: #a32d2d",
                "Medium": "background-color: #faeeda; color: #854f0b"
            }
            return colors.get(val, "")

        styled_gov = filtered.style.map(color_gov_type, subset=["Type"]).map(color_gov_priority, subset=["Priority"])
        st.dataframe(styled_gov, use_container_width=True, hide_index=True)

    # ── TAB 3: RISK REGISTER ──
    with tab3:
        st.subheader("Risk Register")

        gov_risk_data = {
            "Risk ID": ["R001", "R002", "R003", "R004", "R005", "R006"],
            "Risk": [
                "Overly permissive IAM policy grants excessive access",
                "CloudTrail disabled in one region — audit gap",
                "No MFA enforcement on privileged accounts",
                "Stale access keys older than 90 days",
                "Root account usage detected",
                "Security group allows unrestricted inbound access"
            ],
            "Likelihood": ["High", "Medium", "High", "Medium", "Low", "Medium"],
            "Impact": ["High", "Critical", "Critical", "High", "Critical", "High"],
            "Mitigation": [
                "Peer review all IAM policies before deployment",
                "Enable organization-wide CloudTrail with S3 log validation",
                "Enforce MFA policy on all privileged and console users",
                "Automated key rotation policy — 90-day maximum",
                "Lock root credentials, enable MFA, alert on any usage",
                "Restrict security groups to known CIDR ranges only"
            ],
            "Owner": ["IAM Team", "AWS Admin", "Security", "IAM Team", "Security", "Cloud Team"],
            "Status": ["Open", "Closed", "Open", "In Progress", "Closed", "In Progress"]
        }

        df_gov_risk = pd.DataFrame(gov_risk_data)

        def color_gov_status(val):
            if val == "Open":
                return "background-color: #fde8e8; color: #a32d2d"
            elif val == "Closed":
                return "background-color: #eaf3de; color: #3b6d11"
            elif val == "In Progress":
                return "background-color: #faeeda; color: #854f0b"
            return ""

        def color_gov_sev(val):
            if val == "Critical":
                return "background-color: #a32d2d; color: #ffffff"
            elif val == "High":
                return "background-color: #fde8e8; color: #a32d2d"
            elif val == "Medium":
                return "background-color: #faeeda; color: #854f0b"
            elif val == "Low":
                return "background-color: #eaf3de; color: #3b6d11"
            return ""

        styled_gov_risk = df_gov_risk.style.map(color_gov_status, subset=["Status"]).map(color_gov_sev, subset=["Likelihood", "Impact"])
        st.dataframe(styled_gov_risk, use_container_width=True, hide_index=True)

        st.markdown("**Risk Summary**")
        rcol1, rcol2, rcol3 = st.columns(3)
        rcol1.metric("Open Risks", "2", delta="-1 this week", delta_color="inverse")
        rcol2.metric("In Progress", "2")
        rcol3.metric("Closed", "2", delta="+2 this month")

    # ── TAB 4: STAKEHOLDERS ──
    with tab4:
        st.subheader("Stakeholder Register")

        stakeholder_data = {
            "Stakeholder": [
                "CISO",
                "IAM Team",
                "Network Team",
                "Cloud Team",
                "Security Operations",
                "Help Desk",
                "HR",
                "Application Owners",
                "Vendor — IAM Platform"
            ],
            "Role": [
                "Executive Sponsor",
                "Implementation Lead",
                "Infrastructure Support",
                "AWS Environment Owner",
                "Monitoring & Response",
                "User Support & Communications",
                "Identity Data Source",
                "Access Approvers",
                "Third-Party Implementation Partner"
            ],
            "Communication": [
                "Weekly steering committee",
                "Daily standups",
                "Weekly sync",
                "Weekly sync",
                "Bi-weekly review",
                "Monthly briefing",
                "As needed — data requests",
                "Certification cycles",
                "Weekly vendor coordination"
            ],
            "Influence": ["High", "High", "Medium", "High", "Medium", "Low", "Medium", "Medium", "Medium"],
            "Interest": ["High", "High", "Medium", "High", "High", "Medium", "Low", "High", "High"]
        }

        df_stake = pd.DataFrame(stakeholder_data)

        def color_level(val):
            if val == "High":
                return "background-color: #e6f1fb; color: #185fa5"
            elif val == "Medium":
                return "background-color: #faeeda; color: #854f0b"
            elif val == "Low":
                return "background-color: #f0f2f6; color: #555555"
            return ""

        styled_stake = df_stake.style.map(color_level, subset=["Influence", "Interest"])
        st.dataframe(styled_stake, use_container_width=True, hide_index=True)

    # ── TAB 5: EXECUTIVE STATUS ──
    with tab5:
        st.subheader("Executive Status Report")
        st.markdown("**Reporting Period: Current Week**")

        scol1, scol2, scol3 = st.columns(3)
        scol1.metric("Overall Status", "🟢 Green")
        scol2.metric("Schedule", "🟢 On Track")
        scol3.metric("Budget", "🟢 On Track")
        scol4, scol5, scol6 = st.columns(3)
        scol4.metric("Scope", "🟢 Stable")
        scol5.metric("Risk", "🟡 Monitoring")
        scol6.metric("Issues", "🔴 1 Critical")

        st.markdown("---")
        st.markdown("### Executive Summary")
        st.markdown("""
        This week the project completed **RBAC implementation** across all in-scope
        business units, marking a major Phase 2 milestone.

        **Security Hub findings were reduced by 35%** following the remediation
        sprint targeting IAM misconfigurations and logging gaps.

        **One critical issue remains open** involving CloudTrail configuration in a
        secondary region — remediation is assigned to the AWS Admin team with a
        target resolution of end of week.

        MFA rollout for privileged accounts is **in progress at 80% adoption**, with
        Help Desk supporting the remaining user migrations.

        Overall, the project **remains on schedule and within budget**, with
        completion tracking at 72% against a Q4 delivery target.
        """)

        st.markdown("### Decisions Needed From Leadership")
        st.markdown("""
        - Approval of extended maintenance window for CloudTrail remediation
        - Sign-off on Q4 access certification scope — all privileged accounts vs full population
        """)

# ── PROJECT 12 ──────────────────────────────────────────────
elif page == "🤖 Project 12 — AI GRC Assistant (Live App)":
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

# ── MONITORING ──────────────────────────────────────────────
elif page == "📊 Monitoring & Detection":
    st.title("📊 Monitoring, Detection & Compliance")
    st.markdown("---")

    services = {
        "CloudTrail": "Full API audit logging — who did what, when, from where",
        "CloudWatch": "Metrics, alarms, and log analysis across all services",
        "GuardDuty": "Threat detection and anomaly alerts — ML-based",
        "AWS Config": "Compliance history and configuration drift detection",
        "Security Hub": "Centralized findings and security posture scoring",
        "S3 Log Storage": "Centralized audit evidence collection and retention",
        "External Nmap": "Attack surface validation and port verification from attacker perspective"
    }

    for service, desc in services.items():
        st.markdown(f"**{service}** — {desc}")

    st.markdown("---")
    st.subheader("Evidence Collected")
    st.markdown("""
    - Running EC2 instances with passed status checks
    - Active Nginx and Docker service confirmations
    - Security Group rule before/after comparison
    - Nmap scan results confirming reduced attack surface
    - AD OU structure and RBAC group assignments
    - JML scenario walkthroughs
    - Access certification cycle documentation
    """)

# ── LINKS ──────────────────────────────────────────────────
elif page == "🔗 Links & Contact":
    st.title("🔗 Links & Contact")
    st.markdown("---")

    st.subheader("Tyrell Mifflin")
    st.markdown("**Principal Cybersecurity & IAM Consultant**")
    st.markdown("New Castle, DE · U.S. Army Veteran (Signal Corps)")
    st.markdown("CEH · CSM · CCSP (Expected 2026)")

    st.markdown("---")
    st.subheader("Portfolio")
    st.markdown("🌐 **Live AI GRC Tool** — [iam-grc-assistant.streamlit.app](https://iam-grc-assistant.streamlit.app)")
    st.markdown("💻 **AI GRC Assistant GitHub** — [github.com/tyrellmifflin07-glitch/iam-grc-assistant](https://github.com/tyrellmifflin07-glitch/iam-grc-assistant)")
    st.markdown("💻 **AWS Lab GitHub** — [github.com/tyrellmifflin07-glitch/aws-iam-cloud-security-lab](https://github.com/tyrellmifflin07-glitch/aws-iam-cloud-security-lab)")
    st.markdown("🔗 **LinkedIn** — [linkedin.com/in/tyrell-mifflin-ceh-csm-85a27583](https://linkedin.com/in/tyrell-mifflin-ceh-csm-85a27583)")

    st.markdown("---")
    st.subheader("Specializations")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("- IAM Governance & Administration")
        st.markdown("- GRC & Compliance Engineering")
        st.markdown("- Cloud Security — AWS & Azure")
        st.markdown("- Active Directory & Entra ID")
    with col2:
        st.markdown("- NIST 800-53 · PCI-DSS · SOC 2 · HIPAA")
        st.markdown("- AI-Powered GRC Tools")
        st.markdown("- Access Certifications & Reviews")
        st.markdown("- Privileged Access Governance")