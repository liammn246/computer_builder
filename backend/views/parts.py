from fastapi import APIRouter

parts_router = APIRouter(prefix="/parts")

@parts_router.post("/gpu")
def create_gpu():
    ...