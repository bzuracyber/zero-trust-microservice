# 🗂 Plan of Action & Milestones – Mission Data Exchange Zero Trust Microservice Lab

## Purpose
Tracks known security weaknesses, planned remediation actions, and milestones for completion.

| Weakness ID | Description | NIST Control | Risk Level | Planned Action | Milestone Date | Status |
|-------------|-------------|--------------|------------|----------------|----------------|--------|
| POAM‑001 | Keycloak admin account uses default password in lab | IA‑5 | High | Configure strong admin password; store in secure vault | 2025‑09‑15 | Open |
| POAM‑002 | No automated backup for OPA policies | CP‑9 | Medium | Implement Git‑based policy repo with CI sync | 2025‑09‑20 | Open |
| POAM‑003 | TLS certs are self‑signed in lab | SC‑12 | Low | Integrate with lab CA or Let's Encrypt staging | 2025‑09‑25 | Open |
| POAM‑004 | Limited audit log retention (7 days) | AU‑11 | Medium | Extend retention to 90 days in SIEM config | 2025‑09‑30 | Open |

**Note:** Dates are illustrative for lab purposes; in production, align with AO‑approved timelines.
