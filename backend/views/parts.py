from fastapi import APIRouter, Depends, HTTPException
from schemas.parts import GPUCreateSchema, CPUCreateSchema
from models.parts import GPU, CPU
from database.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated

parts_router = APIRouter(prefix="/parts")
db_dependency = Annotated[Session, Depends(get_db)]

@parts_router.post("/gpu")
def create_gpu(request: GPUCreateSchema, db: db_dependency):
    existing = db.query(GPU).filter(GPU.name == request.name).first()
    if existing:
        raise HTTPException(
            status_code=409,
            detail="GPU already exists"
        )
    gpu = GPU(**request.model_dump()) # model_dump() turns the object into a dict, ** turns keys into arguments
    db.add(gpu)
    db.commit()
    return gpu
    
@parts_router.post("/cpu")
def create_cpu(request: CPUCreateSchema, db: db_dependency):
    existing = db.query(CPU).filter(CPU.name == request.name).first()
    if existing:
        raise HTTPException(
            status_code=409,
            detail="CPU already exists"
        )
    cpu = CPU(**request.model_dump())
    db.add(cpu)
    db.commit()
    return cpu

@parts_router.get("/cpus")
def fetch_cpus(db: db_dependency):
    cpus = db.query(CPU).all()
    return cpus

@parts_router.get("/gpus")
def fetch_gpus(db: db_dependency):
    gpus = db.query(GPU).all()
    return gpus