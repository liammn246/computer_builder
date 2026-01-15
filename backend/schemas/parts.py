from pydantic import BaseModel

class CPUCreateSchema(BaseModel):
    name: str
    brand: str
    cores: int
    threads: int
    base_clock: float
    boost_clock: float
    socket: str
    price: float
    integrated_graphics: bool
    release_year: int

class CPUOptionSchema(BaseModel):
    id: int
    name: str

class CPUOut(CPUCreateSchema):
    id: int

class GPUCreateSchema(BaseModel):
    name: str
    brand: str
    vram: int
    base_clock: float
    boost_clock: float
    tdp: int
    price: float
    release_year: int
    
class GPUOptionSchema(BaseModel):
    id: int
    name: str

class GPUOut(GPUCreateSchema):
    id: int

class PartSpecificationSchema(BaseModel):
    cpu_name: str | None = None
    gpu_name: str | None = None
    cpu_brand: str | None = None
    gpu_brand: str | None = None
    ram_size: int | None = None
    budget: float | None = None

class PartFilterResponse(BaseModel):
    cpus: list[CPUOut]
    gpus: list[GPUOut]
