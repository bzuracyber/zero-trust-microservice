# Mission Data Exchange – Zero Trust Microservice Architecture

## Scenario
You are tasked with designing and accrediting a secure, containerized microservice platform for a fictional DoD mission partner network.  
The system must:

- Handle **Sensitive But Unclassified (SBU)** mission data
- Enforce **continuous authentication and authorization**
- Remain **resilient under attack**
- Produce **RMF‑ready documentation** throughout the lifecycle

---

## Core Components

### 1. API Gateway & Service Mesh
- Envoy or Istio for **mTLS** between services
- **JWT/OIDC** authentication via Keycloak
- Policy enforcement with **OPA/Rego**

### 2. Microservices
- **Data Ingest Service** – receives mission data from external partner
- **Data Processing Service** – applies classification rules
- **Data Access Service** – serves authorized users

### 3. Security Tooling
- **Static**: Semgrep, Trivy, Terrascan
- **Dynamic**: OWASP ZAP, k6 for load testing
- **Runtime**: Falco for anomaly detection

### 4. Supply Chain Assurance
- SBOM generation (Syft/Grype)
- Vulnerability scanning in CI/CD

### 5. Continuous Monitoring
- SIEM integration (Splunk or OpenSearch)
- Automated compliance checks in pipeline

---

## RMF Step Alignment

| **RMF Step** | **Lab Activity** | **Artifact Produced** |
|--------------|------------------|-----------------------|
| **Categorize** | Define mission profile, data types, CIA impact | Mission Profile doc, Data Flow Diagram |
| **Select** | Tailor NIST SP 800‑53 controls + Zero Trust overlay | Control Tailoring Matrix |
| **Implement** | Build microservices with Zero Trust patterns | Secure Architecture Diagram, Config Baselines |
| **Assess** | Run static/dynamic/runtime tests | Test Reports, Vulnerability Scan Results |
| **Authorize** | Present risk posture to fictional AO | Risk Assessment Report, POA&M |
| **Monitor** | Automate scans, log analysis, change tracking | Continuous Monitoring Plan, Updated SSP |

---

## Purpose of This Lab
This lab is designed to simulate a **full RMF lifecycle** in a Zero Trust microservice environment, producing both **technical implementations** and **compliance artifacts**.  
It serves as a hands‑on training platform for engineers, ISSEs, and security architects working in **DoD and regulated environments**.

---

## 🧠 Why This Stack?

Zero Trust means “never trust, always verify.” This lab shows how to:

- Authenticate users via OAuth2/OIDC  
- Authorize requests using external policy enforcement  
- Decouple identity and policy logic from your app  

---

## 🚀 Architecture Overview

[User] → [Keycloak] → [FastAPI] → [OPA] → [Policy Decision]


- Keycloak issues JWT tokens  
- FastAPI validates tokens and sends request context to OPA  
- OPA evaluates policies and returns allow/deny  
- FastAPI enforces the decision  

---

## 🛠️ Lab Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/bzuracyber/zero-trust-microservice.git

cd zero-trust-microservice
```

### 2. Start Keycloak

```bash
docker run -p 8080:8080 `
-e KEYCLOAK_ADMIN=admin `
-e KEYCLOAK_ADMIN_PASSWORD=admin `
quay.io/keycloak/keycloak:latest start-dev
```

- Access Keycloak at http://localhost:8080
- Create a realm, client (fastapi-client), and user
- Set client to use confidential access type
- Note the client_id, client_secret, and realm name

### 3. Start OPA Server

 ```bash
opa run --server --log-level debug --set=decision_logs.console=true
```
- OPA listens on http://localhost:8181
- Create a policy file policy.rego:

# OPA policy language
    package authz

     default allow = false

         allow {
             input.method == "GET"
            input.path == "/data"
            input.user == "alice"
           }

Load it into OPA:

 ```bash
 curl -X PUT --data-binary @policy.rego \ localhost:8181/v1/policies/authz
```

### 4. FastAPI App
  Install dependencies:

 ```bash
 pip install fastapi uvicorn python-jose requests
```
   Create main.py:
   
    # Python code
    from fastapi import FastAPI, Depends, HTTPException, Request
    from fastapi.security import OAuth2PasswordBearer
    import requests
    from jose import jwt

    app = FastAPI()
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    KEYCLOAK_PUBLIC_KEY = "your-public-key"
    OPA_URL = "http://localhost:8181/v1/data/authz/allow"

    def verify_token(token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, KEYCLOAK_PUBLIC_KEY, algorithms=["RS256"])
            return payload
        except Exception:
            raise HTTPException(status_code=401, detail="Invalid token")

    @app.get("/data")
    def get_data(user=Depends(verify_token), request: Request = None):
        input_data = {
            "input": {
                "method": request.method,
                "path": request.url.path,
                "user": user["preferred_username"]
            }
        }
        response = requests.post(OPA_URL, json=input_data)
        if response.json().get("result"):
            return {"message": "Access granted"}
        raise HTTPException(status_code=403, detail="Access denied")

Run the app:

```bash
uvicorn main:app --reload
```

## 🔍 Testing the Flow
Get a token from Keycloak using your client credentials

Call FastAPI with the token:

```bash
curl -H "Authorization: Bearer <your_token>" http://localhost:8000/data
```

## 📁 Project Structure
```text
zero-trust-lab/
├── main.py
├── policy.rego
├── README.md
```


## 🧪 Extensions
Add role-based access control in Rego
Integrate Keycloak groups and roles
Use FastAPI middleware for token introspection
Add logging and audit trails

## 🧠 Concepts Demonstrated

| Component | Role in Zero Trust              |
|-----------|---------------------------------|
| Keycloak  | Identity Provider (IdP)         |
| OPA       | Policy Decision Point (PDP)     |
| FastAPI   | Policy Enforcement Point (PEP)  |


## 📚 References
- Keycloak Docs
- OPA Docs
- FastAPI Docs

