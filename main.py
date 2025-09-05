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
