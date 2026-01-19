from sqlalchemy import Column, Integer, String, Float, Boolean
from database.database import Base

class CPU(Base):
    __tablename__ = "cpus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    brand = Column(String, nullable=False)  # AMD, INTEL

    cores = Column(Integer)
    threads = Column(Integer)

    base_clock = Column(Float)   # GHz
    boost_clock = Column(Float)  # GHz

    socket = Column(String)

    performance_score = Column(Float, nullable=True)
    tdp_watts = Column(Integer, nullable=True)

    price_usd = Column(Float)
    integrated_graphics = Column(Boolean, default=False)

    release_year = Column(Integer)


class GPU(Base):
    __tablename__ = "gpus"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    brand = Column(String, nullable=False)  # NVIDIA, AMD, INTEL

    vram_gb = Column(Integer)

    performance_score = Column(Float, nullable=True)
    value_score = Column(Float, nullable=True)

    tdp_watts = Column(Integer, nullable=True)

    price_usd = Column(Float)
    release_year = Column(Integer)

    pcie_version = Column(Float, nullable=True)
    length_mm = Column(Integer, nullable=True)


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
