from fastapi import FastAPI
from database.database import Base, engine
from models.parts import CPU, GPU, PSU, Case
from views.parts import parts_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(parts_router)

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
