from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "postgresql://eonebonbpohpcb:a6f6a88d189acb3328f2351787c7c6b7252a52bd2c1dd208b6cc2461ed8832ed@ec2-44-206-197-71.compute-1.amazonaws.com/d6gbqaarpqfm2a"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123456789@localhost/univcomm"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
