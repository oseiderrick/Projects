from fastapi import APIRouter, Depends, HTTPException, Response
from pydantic import BaseModel, EmailStr
from passlib.hash import bcrypt
from datetime import datetime, timedelta
import jwt

JWT_SECRET = "dev-secret-change-me"
JWT_ALG = "HS256"
COOKIE_NAME = "access_token"
EXPIRES_MIN = 60 * 12  # 12h

router = APIRouter(prefix="/auth", tags=["auth"])

# naive in-memory users for demo; replace with DB in production
_USERS = {}

class Register(BaseModel):
    email: EmailStr
    password: str

class Login(BaseModel):
    email: EmailStr
    password: str

def create_token(sub: str):
    payload = {"sub": sub, "exp": datetime.utcnow() + timedelta(minutes=EXPIRES_MIN)}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

@router.post("/register")
def register(body: Register):
    if body.email in _USERS:
        raise HTTPException(status_code=400, detail="Email already exists")
    _USERS[body.email] = bcrypt.hash(body.password)
    return {"ok": True}

@router.post("/login")
def login(body: Login, response: Response):
    if body.email not in _USERS or not bcrypt.verify(body.password, _USERS[body.email]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_token(body.email)
    response.set_cookie(COOKIE_NAME, token, httponly=True, secure=False, samesite="lax", max_age=3600*12, path="/")
    return {"ok": True}

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(COOKIE_NAME, path="/")
    return {"ok": True}

def get_current_user(token: str | None):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
