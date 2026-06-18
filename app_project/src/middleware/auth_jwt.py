from fastapi import Request
from fastapi.responses import JSONResponse

async def auth_jwt_middleware(request: Request, call_next):

    public_paths = ["/login", "/register"]
    if request.url.path in public_paths:
        return await call_next(request)

    auth_header = request.headers.get("Authorization")
    if auth_header is None or not auth_header.startswith("Bearer "):
        return JSONResponse(status_code=401, content={"message": "Unauthorized"})
    token = auth_header.split(" ")[1]
    return await call_next(request)