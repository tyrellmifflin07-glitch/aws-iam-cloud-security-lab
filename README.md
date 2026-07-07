# AWS IAM & Cloud Security Lab

**Enterprise-grade Identity & Access Management and Cloud Security home lab built and operated by Tyrell Mifflin.**

Designed to demonstrate hands-on proficiency across cloud infrastructure security, identity governance, access lifecycle management, and continuous security monitoring — directly applicable to IAM Governance, Cloud Security, and GRC Engineering roles.

---

## Lab Overview

This lab replicates an enterprise AWS environment across 10 completed projects spanning cloud infrastructure, Active Directory identity governance, access certifications, privileged access management, and security monitoring.

**Target Roles Demonstrated:** IAM Governance Specialist · Cloud Security Engineer · GRC System Engineer · Information Security Analyst

**Industries Applicable:** Financial Services · Healthcare · Legal · MSP

---

## Architecture

![AWS IAM & Cloud Security Lab Architecture](diagrams/aws_architecture.png)

---

## Capabilities Demonstrated

| Capability | Demonstrated Through |
|---|---|
| Cloud Infrastructure Security | EC2, ALB, VPC, Security Groups, network segmentation |
| Identity & Access Governance | Active Directory, OUs, RBAC, JML lifecycle, service account governance |
| AWS IAM Governance | IAM roles, least privilege, MFA, CloudTrail, Config, GuardDuty, Security Hub |
| Security Monitoring & Operations | CloudWatch, GuardDuty, Nginx logs, auth.log, external Nmap validation |
| Governance Frameworks Applied | Least privilege, defense-in-depth, SoD, access certification, audit readiness |

---

## Projects Completed

| # | Project | Status |
|---|---|---|
| 1 | Secure Cloud Web Infrastructure — EC2, Nginx, Docker, OWASP Juice Shop | ✅ Complete |
| 2 | Application Load Balancer & Network Segmentation | ✅ Complete |
| 3 | Active Directory & IAM Governance Lab | ✅ Complete |
| 4 | Access Certification & Governance Review Cycle | ✅ Complete |
| 5 | Role Engineering & Birthright Access Governance | ✅ Complete |
| 6 | Access Request & Approval Workflow | ✅ Complete |
| 7 | Joiner-Mover-Leaver Lifecycle Simulation | ✅ Complete |
| 8 | Privileged Access & Temporary Elevation Governance | ✅ Complete |
| 9 | Microsoft Entra ID Cloud Identity Governance | ✅ Complete |
| 10 | IAM Modernization Roadmap — SailPoint, CyberArk, Entra ID | ✅ Complete |

---

## Tech Stack

| Layer | Technology |
|---|---|
| Cloud Provider | AWS |
| Compute | EC2 — Ubuntu 24.04, Windows Server |
| Identity | Active Directory, Microsoft Entra ID, AWS IAM |
| Web Security | Docker, Nginx, OWASP Juice Shop |
| Load Balancing | Application Load Balancer (Multi-AZ) |
| Networking | Custom VPC, Public/Private Subnets, Security Groups, Network ACLs |
| Monitoring | CloudTrail, CloudWatch, GuardDuty, AWS Config, Security Hub |
| Log Storage | S3 — Centralized audit evidence |
| Validation | Nmap external scanning |

---

## Identity Governance Highlights

### Active Directory Domain — ascended.local

**OU Structure:**
- Finance, IT, Security, Developers, Service Accounts, Terminated Users

**RBAC Security Groups:**

| Group | Purpose |
|---|---|
| IT_Admins | Administrative access |
| Helpdesk | User support access |
| Finance_Read | Read-only finance access |
| Finance_Modify | Finance management access |
| Security_Analysts | Security operations access |

**Authentication Policy Baseline:**

| Policy | Value |
|---|---|
| Password History | 24 passwords |
| Maximum Password Age | 90 days |
| Minimum Password Length | 14 characters |
| Account Lockout Threshold | 5 attempts |
| Lockout Duration | 15 minutes |

---

### Joiner-Mover-Leaver Lifecycle

| Event | User | Action |
|---|---|---|
| Joiner | Greg Jackson | Provisioned to Security_Analysts group |
| Mover | Sarah Johnson | Promoted to Finance Manager — access updated to Finance_Modify |
| Leaver | John Smith | Account disabled, access revoked, moved to Terminated Users OU |

---

### Access Certification Results

| User | Result |
|---|---|
| Sarah Johnson | Flagged — IAM-Admin entitlement excessive for Finance Manager role (SoD concern) |
| Greg Jackson | Approved — Security_Analysts access validated |
| John Smith | Deprovisioned — access fully revoked |

---

## Monitoring & Detection

- CloudTrail — full API audit logging
- CloudWatch — metrics, alarms, and log analysis
- GuardDuty — threat detection and anomaly alerts
- AWS Config — compliance history and configuration drift
- Security Hub — centralized findings and security posture
- S3 — centralized log storage and audit evidence collection
- External Nmap scanning — attack surface validation and port verification

---

## Frameworks Applied

- NIST SP 800-53 — AC-2, AC-6, AC-17, PS-4
- PCI-DSS — Requirements 7, 8, 10, 12
- SOC 2 — CC6.2, CC6.3, CC9.2
- HIPAA — 45 CFR §164.308, §164.312
- CIS AWS Foundations Benchmark

---

## Built By

**Tyrell Mifflin** — Cybersecurity Architect & IAM/GRC Consultant
New Castle, DE | [LinkedIn](https://linkedin.com/in/tyrell-mifflin-ceh-csm-85a27583) | [GitHub](https://github.com/tyrellmifflin07-glitch)

**Live AI GRC Tool:** [iam-grc-assistant.streamlit.app](https://iam-grc-assistant.streamlit.app)

Certifications: CEH · CSM · CCSP (in progress)
Specializations: IAM Governance · GRC · Cloud Security · AWS · Active Directory · Microsoft Entra ID