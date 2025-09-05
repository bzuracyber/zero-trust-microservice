# 📄 Mission Profile – Mission Data Exchange Zero Trust Microservice Lab

## 1. System Identification
- **System Name:** Mission Data Exchange Platform (MDEP)
- **System Acronym:** MDEP-ZT
- **System Type:** Containerized Microservice Platform
- **Environment:** Development / Lab Simulation
- **Mission Owner:** Fictional DoD Mission Partner Network
- **System Boundary:** API Gateway, Service Mesh, Microservices (Ingest, Processing, Access), Keycloak IdP, OPA PDP, Data Store

---

## 2. Mission Description
The Mission Data Exchange Platform enables secure, policy‑driven sharing of **Sensitive But Unclassified (SBU)** mission data between DoD mission partners.  
The platform enforces **Zero Trust principles** — continuous authentication, dynamic authorization, and least‑privilege access — while maintaining resilience against cyber threats.

This lab simulates the end‑to‑end lifecycle of such a system, from architecture design through RMF accreditation artifacts.

---

## 3. Mission Objectives
1. **Secure Data Exchange:** Ensure only authenticated and authorized users can access mission data.
2. **Policy‑Driven Control:** Externalize access control logic via OPA/Rego for agility and auditability.
3. **Resilience Under Attack:** Maintain service availability and integrity during simulated threat scenarios.
4. **Compliance Readiness:** Produce RMF‑aligned documentation and evidence for each lifecycle phase.

---

## 4. Data Description
- **Data Types:**  
  - Mission reports (text, JSON)  
  - Operational status updates  
  - Partner metadata  
- **Classification:** Sensitive But Unclassified (SBU)  
- **Impact Levels:**  
  - **Confidentiality:** Moderate  
  - **Integrity:** Moderate  
  - **Availability:** Moderate  

---

## 5. Operational Environment
- **Hosting:** Containerized services (Docker) on lab workstation or cloud sandbox
- **Networking:** Simulated partner network with API Gateway and mTLS between services
- **Identity Management:** Keycloak (OIDC/JWT)
- **Policy Enforcement:** OPA (Rego policies)
- **Monitoring:** SIEM integration (Splunk/OpenSearch)

---

## 6. Stakeholders
| Role | Responsibility |
|------|----------------|
| Mission Owner | Defines operational requirements |
| ISSE | Designs security architecture, maps controls to RMF |
| Developers | Implement microservices and integrations |
| Security Analysts | Conduct static/dynamic/runtime testing |
| Authorizing Official (AO) | Reviews risk posture for accreditation |

---

## 7. Threat Summary
- Credential theft / token replay
- Unauthorized API access
- Supply chain compromise (container images)
- Policy bypass attempts
- Denial of Service (DoS) on API endpoints

---

## 8. Security Controls Overview
- **Access Control:** OIDC authentication, OPA authorization
- **Data Protection:** mTLS, JWT signing, secure config baselines
- **Monitoring:** Falco runtime alerts, SIEM log aggregation
- **Supply Chain:** SBOM generation, vulnerability scanning in CI/CD
- **Testing:** Semgrep, Trivy, Terrascan, OWASP ZAP, k6

---

## 9. RMF Alignment
This mission profile supports the **Categorize** step of the RMF by:
- Defining the system boundary
- Identifying data types and classification
- Documenting mission objectives and operational environment
- Establishing initial threat context

Artifacts produced here will feed into:
- **System Security Plan (SSP)**
- **Control Tailoring Matrix**
- **Risk Assessment Report**

---

## 10. References
- DoDI 8500.01 – Cybersecurity
- DoDI 8510.01 – Risk Management Framework (RMF) for DoD IT
- NIST SP 800‑53 Rev. 5 – Security and Privacy Controls
- NIST SP 800‑37 Rev. 2 – RMF for Information Systems
