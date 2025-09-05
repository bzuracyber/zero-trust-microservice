# 🔐 Zero Trust Microservice Lab: Keycloak + OPA + FastAPI

This lab demonstrates a hybrid Zero Trust architecture using:

- **Keycloak** for authentication and identity federation  
- **Open Policy Agent (OPA)** for policy-based access control  
- **FastAPI** as the microservice backend  

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

## 🛠️ Setup Instructions

### 1. Clone the Repo

git clone https://github.com/yourusername/zero-trust-lab.git
cd zero-trust-lab

### 2. Start Keycloak

docker run -p 8080:8080 \
  -e KEYCLOAK_ADMIN=admin \
  -e KEYCLOAK_ADMIN_PASSWORD=admin \
  quay.io/keycloak/keycloak:latest start-dev

- Access Keycloak at http://localhost:8080
- Create a realm, client (fastapi-client), and user
- Set client to use confidential access type
- Note the client_id, client_secret, and realm name

### 3. Start OPA Server

opa run --server --log-level debug --set=decision_logs.console=true

- OPA listens on http://localhost:8181
- Create a policy file policy.rego:

package authz

default allow = false

allow {
  input.method == "GET"
  input.path == "/data"
  input.user == "alice"
}

Load it into OPA:

curl -X PUT --data-binary @policy.rego \ localhost:8181/v1/policies/authz

### 4. FastAPI App
  Install dependencies:

    pip install fastapi uvicorn python-jose requests

   Create main.py:
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

  uvicorn main:app --reload

## 🔍 Testing the Flow
Get a token from Keycloak using your client credentials

Call FastAPI with the token:

  curl -H "Authorization: Bearer <your_token>" http://localhost:8000/data

## 📁 Project Structure
  zero-trust-lab/
  ├── main.py
  ├── policy.rego
  ├── README.md

## 🧪 Extensions
Add role-based access control in Rego
Integrate Keycloak groups and roles
Use FastAPI middleware for token introspection
Add logging and audit trails

## 🧠 Concepts Demonstrated
Component	Role in Zero Trust
Keycloak	Identity Provider (IdP)
OPA	Policy Decision Point (PDP)
FastAPI	Policy Enforcement Point (PEP)

## 📚 References
Keycloak Docs
OPA Docs
FastAPI Docs

