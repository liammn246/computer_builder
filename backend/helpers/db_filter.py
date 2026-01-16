from fastapi import Depends
from schemas.parts import PartSpecificationSchema
from models.parts import GPU, CPU
from database.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated

db_dependency = Annotated[Session, Depends(get_db)]

def filter_cpu(constraints: PartSpecificationSchema, db: db_dependency) -> list[CPU]:
    cpu_list = db.query(CPU)
    if constraints.cpu_name:
        cpu_list = cpu_list.filter(CPU.name == constraints.cpu_name)
        return cpu_list.all()
    filters = {
        "name": constraints.cpu_name,
        "brand": constraints.cpu_brand,
        # "socket": constraints.socket,
    }
    for field, value in filters.items():
        if value:
            cpu_list = cpu_list.filter(getattr(CPU, field) == value)
    cpus = cpu_list.all()
    return cpus

def filter_gpu(constraints: PartSpecificationSchema, db: db_dependency) -> list[GPU]:
    gpu_list = db.query(GPU)
    if constraints.gpu_name:
        gpu_list = gpu_list.filter(GPU.name == constraints.gpu_name)
        return gpu_list.all()
    filters = {
        "name": constraints.gpu_name,
        "brand": constraints.gpu_brand,
        # "vram": constraints.ram_size,
    }
    for field, value in filters.items():
        if value:
            gpu_list = gpu_list.filter(getattr(GPU, field) == value)
    gpus = gpu_list.all()
    return gpus