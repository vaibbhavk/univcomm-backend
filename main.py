from fastapi import FastAPI
from database import models, init_db
from routers import user, admin

models.Base.metadata.create_all(bind=init_db.engine)

app = FastAPI()

app.include_router(admin.router)
app.include_router(user.router)
