from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base

class CPU(Base):
    __tablename__ = "cpus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    brand = Column(String)  # Intel, AMD
    cores = Column(Integer)
    threads = Column(Integer)
    base_clock = Column(Float)  # GHz
    boost_clock = Column(Float)  # GHz
    tdp = Column(Integer)  # Watts
    socket = Column(String)
    price = Column(Float)  # USD
    integrated_graphics = Column(Boolean, default=False)
    release_year = Column(Integer)

class GPU(Base):
    __tablename__ = "gpus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    brand = Column(String)  # NVIDIA, AMD
    vram = Column(Integer)  # GB
    base_clock = Column(Float)
    boost_clock = Column(Float)
    tdp = Column(Integer)  # Watts
    price = Column(Float)  # USD
    release_year = Column(Integer)

class PSU(Base):
    __tablename__ = "psus"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    wattage = Column(Integer)
    efficiency_rating = Column(String)  # e.g., 80+ Gold
    modular = Column(Boolean, default=False)
    price = Column(Float)  # USD
    brand = Column(String)
    release_year = Column(Integer)

class Case(Base):
    __tablename__ = "cases"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    brand = Column(String)
    form_factor = Column(String)  # ATX, MicroATX, Mini-ITX
    gpu_max_length = Column(Integer)  # mm
    cpu_cooler_max_height = Column(Integer)  # mm
    psu_max_length = Column(Integer)  # mm
    price = Column(Float)  # USD
    release_year = Column(Integer)
