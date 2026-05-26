from fastapi import APIRouter, Request
import src.services.genai_handle as genai_handle
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

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

# @router.get("/{random:int}")



