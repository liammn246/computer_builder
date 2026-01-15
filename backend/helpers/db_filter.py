from fastapi import Depends
from schemas.parts import PartSpecificationSchema
from models.parts import GPU, CPU
from database.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated

db_dependency = Annotated[Session, Depends(get_db)]

def filter_cpu(constraints: PartSpecificationSchema, db: db_dependency) -> list[CPU]:
    cpu_list = db.query(CPU)
    filters = {
        "name": constraints.cpu_name,
        "brand": constraints.cpu_brand,
        # "socket": constraints.socket,
    }
    for field, value in filters.items():
        if value is not None:
            cpu_list = cpu_list.filter(getattr(CPU, field) == value)
    cpus = cpu_list.all()
    return cpus

def filter_gpu(constraints: PartSpecificationSchema, db: db_dependency) -> list[GPU]:
    gpu_list = db.query(GPU)
    filters = {
        "name": constraints.gpu_name,
        "brand": constraints.gpu_brand,
        # "vram": constraints.ram_size,
    }
    for field, value in filters.items():
        if value is not None:
            gpu_list = gpu_list.filter(getattr(GPU, field) == value)
    gpus = gpu_list.all()
    return gpus