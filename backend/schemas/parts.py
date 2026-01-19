from pydantic import BaseModel
from typing import Optional

class CPUCreateSchema(BaseModel):
    name: str
    brand: str

    cores: int
    threads: int

    base_clock: Optional[float] = None
    boost_clock: Optional[float] = None

    socket: str

    performance_score: Optional[float] = None
    tdp_watts: Optional[int] = None

    price_usd: float
    integrated_graphics: bool = False

    release_year: int


class CPUOptionSchema(BaseModel):
    id: int
    name: str

class CPUOut(CPUCreateSchema):
    id: int
    price_usd: float

class GPUCreateSchema(BaseModel):
    name: str
    brand: str

    vram_gb: int

    performance_score: Optional[float] = None
    value_score: Optional[float] = None

    tdp_watts: Optional[int] = None

    price_usd: float
    release_year: int

    pcie_version: Optional[float] = None
    length_mm: Optional[int] = None

    
class GPUOptionSchema(BaseModel):
    id: int
    name: str

class GPUOut(GPUCreateSchema):
    id: int
    price_usd: float

class PartSpecificationSchema(BaseModel):
    cpu_name: str | None = None
    gpu_name: str | None = None
    cpu_brand: str | None = None
    gpu_brand: str | None = None
    ram_size: int | None = None
    budget: float | None = None
    pc_use: str | None = None

class PartFilterResponse(BaseModel):
    cpus: list[CPUOut] | None = None
    gpus: list[GPUOut] | None = None
    ram: str | None = None
    storage: str | None = None
    needs_clarification: str | None = None
