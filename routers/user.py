from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from utils import schemas
from dependencies import get_db, verify_password, create_access_token
from database import crud

router = APIRouter(
    prefix='/api/user'
)


@router.get("/")
def index():
    return {
        "message": "User route base point"
    }


@router.post("/register/", response_model=schemas.UserOut)
def register_user(user: schemas.UserIn, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = crud.create_user(db=db, user=user)

    if not new_user:
        raise HTTPException(status_code=400, detail="Could not register user")

    response = {"id": new_user.id, "email": new_user.email,
                "first_name": new_user.first_name, "last_name": new_user.last_name}

    return response


@router.post("/login/")
def login_user(user: schemas.UserLoginIn, db: Session = Depends(get_db)):

    db_user = crud.get_user_by_email(db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    check_password = verify_password(user.password, db_user.password)
    if not check_password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        {"user_id": db_user.id}
    )

    return {"access_token": access_token}


@router.get("/{user_id}/")
def user_profile(user_id: int, db: Session = Depends(get_db)):
    db_user_profile = crud.get_user_profile_by_user_id(db, user_id=user_id)

    if not db_user_profile:
        raise HTTPException(status_code=404, detail="Not found")

    return db_user_profile


@router.delete("/{user_id}/")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user_by_user_id(db, user_id=user_id)

    if not db_user:
        raise HTTPException(
            status_code=404, detail="User with the given id does not exist")

    return {"detail": "User deleted successfully"}
