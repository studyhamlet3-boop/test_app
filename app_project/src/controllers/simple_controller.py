from fastapi import APIRouter, HTTPException, Request
import src.services.genai_handle as genai_handle
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from src.services.auth.auth_regist import register_user
from exceptions import UserAlreadyExistsError

class regist_info(BaseModel):
    email: str
    password: str

class UserRequest(BaseModel):
    prompt: str


router = APIRouter(prefix="/users")

@router.get("")
def get_my_user():
    return {"user": "This is the User unterface"}

@router.post("/res")
async def ask_gemini(request: UserRequest):
    return StreamingResponse(
        genai_handle.genai_req(request.prompt), 
        media_type="text/event-stream"
    )


auth_router = APIRouter(prefix="/auth")

@auth_router.post("/login")
async def login(request: Request):
    return {"message": "Login successful"}

@auth_router.post("/register")
async def register(request: regist_info): # work in progress(need to change email to user_id for JWT creation) returns token, catches UserAlreadyExistsError
    try:
        return await register_user(request)
    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail="User already exists") # CAN BE UPGRADED "FastAPI: global exception handler" whatever that is
