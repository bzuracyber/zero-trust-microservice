# 🎯 Control Tailoring Matrix – Mission Data Exchange Zero Trust Microservice Lab

## Purpose
This matrix maps the lab’s technical implementation to **NIST SP 800‑53 Rev. 5** control families, tailored for a **Moderate** impact SBU system in a DoD mission partner context.

| Control ID | Control Name | Implementation in Lab | Evidence / Artifact |
|------------|--------------|-----------------------|---------------------|
| AC‑2 | Account Management | User accounts managed in Keycloak realm; admin approval required | Keycloak realm export, `Mission_Profile.md` |
| AC‑3 | Access Enforcement | OPA policies enforce ABAC/RBAC decisions | `policy.rego`, OPA decision logs |
| AC‑6 | Least Privilege | Policies grant minimal access per role/user | `policy.rego`, Control Tailoring Matrix |
| IA‑2 | Identification & Authentication | OIDC/JWT authentication via Keycloak | Keycloak config, token validation logs |
| SC‑8 | Transmission Confidentiality | mTLS between services via service mesh | Mesh config, certs |
| SC‑13 | Cryptographic Protection | JWT signing with RS256; TLS 1.2+ | Keycloak public key, TLS configs |
| SI‑4 | System Monitoring | Falco runtime alerts, SIEM integration | Falco rules, SIEM dashboard screenshots |
| RA‑5 | Vulnerability Scanning | Trivy, Terrascan, Semgrep in CI/CD | Scan reports |
| CM‑6 | Configuration Settings | Baseline configs for Keycloak, OPA, FastAPI | Config baseline docs |
| AU‑2 | Audit Events | FastAPI request logs, OPA decision logs | Log samples, SIEM exports |

> **Note:** This is a tailored subset; full control coverage documented in `SSP.md`.
