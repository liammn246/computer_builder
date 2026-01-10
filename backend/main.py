from fastapi import FastAPI
from database.database import Base, engine
from models.parts import CPU, GPU, PSU, Case
from views.parts import parts_router

app = FastAPI()
app.include_router(parts_router)

Base.metadata.create_all(bind=engine)
