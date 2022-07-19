from fastapi import Header, HTTPException
from database.init_db import SessionLocal
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import timedelta, datetime


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
