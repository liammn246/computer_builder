from fastapi import APIRouter, Depends, HTTPException
from schemas.parts import PartSpecificationSchema, PartFilterResponse
from models.parts import GPU, CPU
from database.database import get_db
from sqlalchemy.orm import Session
from typing import Annotated
from helpers.db_filter import filter_cpu, filter_gpu

filter = APIRouter(prefix="")
db_dependency = Annotated[Session, Depends(get_db)]

@filter.post("/filter", response_model=PartFilterResponse)
def filter_parts(constraints: PartSpecificationSchema, db: db_dependency):
    # Must factor in Budget and other aspects later
    filtered_cpus = filter_cpu(constraints, db)
    filtered_gpus = filter_gpu(constraints, db)
    return {
        "cpus": filtered_cpus,
        "gpus": filtered_gpus
    }
