from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_my_user():
    return {"user": "The main interface"}
