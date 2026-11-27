from fastapi import APIRouter, HTTPException, Request, Response
import src.services.genai_handle as genai_handle
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from src.services.auth.auth_login import login_user
from src.services.auth.auth_regist import register_user
from exceptions import UserAlreadyExistsError, invalidCredentials

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

@auth_router.get("/verify")
async def login():
    return {}

@auth_router.post("/login")
async def login(body: regist_info, response: Response):
    try:
        token = await login_user(body.email, body.password)
    except invalidCredentials:
        raise HTTPException(status_code=401, detail="invalid credentials") #! Attention to token

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax"
    )
    return {"success": True}

@auth_router.post("/register")
async def register(body: regist_info, response: Response):
    try:
        token = await register_user(body.email, body.password)

    except UserAlreadyExistsError:
        raise HTTPException(status_code=409, detail="User already exists") # CAN BE UPGRADED "FastAPI: global exception handler" whatever that is

    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        secure=False,
        samesite="lax"
    )

    return {"success": True} #!Clear
