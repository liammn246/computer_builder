from fastapi import FastAPI
from database.database import Base, engine
import models.models

app = FastAPI()
Base.metadata.create_all(bind=engine)