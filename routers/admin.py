from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from routers import user
from utils import schemas
from dependencies import get_db, verify_password
from database import crud

router = APIRouter()

@router.post("/admin/register", response_model = schemas.AdminOut)
def register_admin(admin: schemas.AdminIn, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
        
    return crud.create_admin(db=db, admin = admin).__dict__

@router.post("/admin/login")
def login_admin(admin: schemas.AdminIn, db: Session = Depends(get_db)):
    db_admin = crud.get_admin_by_email(db, email=admin.email)
    if not db_admin:
        raise HTTPException(status_code = 401, detail = "Invalid credentials")
    check_password = verify_password(admin.password, db_admin.password)
    if not check_password:
        raise HTTPException(status_code = 401, detail = "Invalid credentials")
    
    return {"detail": "Logged in successfully"}

@router.get("/admin/users")
def get_all_users(db: Session = Depends(get_db)):
    user_list = crud.get_users(db)

    if not user_list:
        raise HTTPException(status_code = 400, detail = "Could not get users")
    
    return user_list