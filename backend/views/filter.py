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
    # Step 1: Ensure budget is provided
    if constraints.budget is None:
        return {
            "needs_clarification": "budget",
            "cpus": None,
            "gpus": None
        }

    # Step 2: Fetch all CPUs and GPUs matching initial constraints
    filtered_cpus = filter_cpu(constraints, db)
    filtered_gpus = filter_gpu(constraints, db)

    # Step 3: Calculate value_score dynamically (performance per dollar)
    for cpu in filtered_cpus:
        cpu.value_score = (cpu.performance_score or 0) / max(cpu.price_usd or 1, 1)
    for gpu in filtered_gpus:
        gpu.value_score = (gpu.performance_score or 0) / max(gpu.price_usd or 1, 1)

    # Step 4: Budget splitting
    if constraints.pc_use == "Gaming":
        cpu_budget = constraints.budget * 0.4
        gpu_budget = constraints.budget * 0.6
    elif constraints.pc_use == "Work":
        cpu_budget = constraints.budget * 0.7
        gpu_budget = constraints.budget * 0.3
    else:
        cpu_budget = constraints.budget
        gpu_budget = constraints.budget

    filtered_cpus = [cpu for cpu in filtered_cpus if (cpu.price_usd or 0) <= cpu_budget]
    filtered_gpus = [gpu for gpu in filtered_gpus if (gpu.price_usd or 0) <= gpu_budget]

    # Step 5: Sorting and prioritization
    if constraints.pc_use == "Gaming":
        # GPUs: performance first, value second
        filtered_gpus.sort(
            key=lambda g: (-(g.performance_score or 0), -(g.value_score or 0))
        )
        # CPUs: performance first, value second
        filtered_cpus.sort(
            key=lambda c: (-(c.performance_score or 0), -(c.value_score or 0))
        )
        # Optional: filter out CPUs that would bottleneck top GPU
        top_gpu_score = filtered_gpus[0].performance_score if filtered_gpus else 0
        filtered_cpus = [
            cpu for cpu in filtered_cpus
            if cpu.performance_score / max(top_gpu_score, 1) >= 0.3
        ]

    elif constraints.pc_use == "Work":
        # CPUs: prioritize cores/threads, performance, iGPU, then cheaper
        filtered_cpus.sort(
            key=lambda c: (
                -(c.cores or 0),
                -(c.threads or 0),
                -(c.performance_score or 0),
                (0 if c.integrated_graphics else 1),  # iGPU preferred
                (c.price_usd or 0)
            )
        )
        # GPUs: value first, then cheaper
        filtered_gpus.sort(
            key=lambda g: (-(g.value_score or 0), (g.price_usd or 0))
        )
        # Optional: remove GPU entirely if CPU has iGPU and user wants minimal cost
        if filtered_cpus and filtered_cpus[0].integrated_graphics:
            filtered_gpus = filtered_gpus[:1]  # keep only one low-end GPU suggestion

    else:
        # Default: sort cheapest first
        filtered_cpus.sort(key=lambda c: c.price_usd or 0)
        filtered_gpus.sort(key=lambda g: g.price_usd or 0)

    # Step 6: Return top 3 of each
    return {
        "cpus": filtered_cpus[:3],
        "gpus": filtered_gpus[:3],
        "needs_clarification": None
    }
