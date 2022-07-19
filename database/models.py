from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database.init_db import Base


# class Admin(Base):
#     __tablename__ = "admins"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True)
#     password = Column(String)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    profile = relationship(
        "UserProfile", cascade="all,delete", back_populates="owner", uselist=False)


class UserProfile(Base):
    __tablename__ = "user_profile"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)
    guardian = Column(String, nullable=False)
    dob = Column(Date, nullable=False)
    address = Column(String, nullable=False)
    contact = Column(String(10), nullable=False)
    user = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User", back_populates="profile")
