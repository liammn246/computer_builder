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

class GPUCreateSchema(BaseModel):
    name: str
    brand: str
    vram: int
    base_clock: float
    boost_clock: float
    tdp: int
    price: float
    release_year: int