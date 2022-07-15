from sqlalchemy.orm import Session

from routers import user

from . import models
from utils import schemas

from dependencies import generate_password_hash


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_admin_by_email(db: Session, email: str):
    return db.query(models.Admin).filter(models.Admin.email == email).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


def get_user_profile_by_user_id(db: Session, user_id: int):
    return db.query(models.UserProfile).filter(models.UserProfile.user == user_id).first()


def get_user_by_user_id(db: Session, user_id: int):
    return db.query(models.User).get(user_id)


def delete_user_by_user_id(db: Session, user_id: int):
    db_user = get_user_by_user_id(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user


def get_users(db: Session):
    return db.query(models.User).with_entities(models.User.id, models.User.email).all()


def create_admin(db: Session, admin: schemas.AdminIn):
    hashed_password = generate_password_hash(admin.password)
    db_admin = models.Admin(email=admin.email, password=hashed_password)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin


def create_user(db: Session, user: schemas.UserIn):
    hashed_password = generate_password_hash(user.password)
    db_user = models.User(email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_profile(db: Session, user: schemas.UserIn, user_id: int):
    db_user_detail = models.UserProfile(first_name=user.first_name, last_name=user.last_name, guardian=user. guardian,
                                        dob=user.dob, address=user.address, contact=user.contact, user=user_id)
    db.add(db_user_detail)
    db.commit()
    db.refresh(db_user_detail)
    return db_user_detail
