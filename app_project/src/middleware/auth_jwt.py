from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


async def auth_jwt_middleware(request: Request, call_next):

    public_paths = ["/login", "/register"]

    if request.url.path in public_paths:
        return await call_next(request)

    token = request.cookies.get("access_token")

    if token is None:
        return JSONResponse(
            status_code=409,
            content={"detail": "Unauthorized"}
        )

    return await call_next(request)