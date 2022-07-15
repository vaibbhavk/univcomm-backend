from fastapi import Header, HTTPException
from database.init_db import SessionLocal
from passlib.context import CryptContext


def pwd_context():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context

def generate_password_hash(password):
    return pwd_context().hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context().verify(plain_password, hashed_password)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
