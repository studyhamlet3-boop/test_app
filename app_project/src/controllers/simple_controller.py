from fastapi import APIRouter, Request
import src.services.process_user as user_service
import src.models.gemini_client as gemini_client
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
        gemini_client.ask_gemini(request.prompt), 
        media_type="text/event-stream"
    )

@router.get("/{random:int}")
def get_my_user():
    return {"user": "12341234"}


