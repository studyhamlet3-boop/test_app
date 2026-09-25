from fastapi import Request, HTTPException
from src.services.auth.gen_token import create_token, decode_token
from fastapi.responses import JSONResponse
from exceptions import InvalidTokenError, TokenExpiredError

# JWT authentication middleware: Requires an "access_token" cookie for most routes.
# Bypasses token validation for public paths like /login and /register.

async def auth_jwt_middleware(request: Request, call_next):

    public_paths = ["/auth/login", "/auth/register"]

    if request.url.path in public_paths:
        return await call_next(request)

    token = request.cookies.get("access_token")

    if token is None:
        return JSONResponse(
            status_code=409,
            content={"detail": "Unauthorized"}
        )

    try :
        payload = decode_token(token)
    except InvalidTokenError:
        return JSONResponse(
            status_code=498,
            content={"detail": "Invalid token"}
        )
    except TokenExpiredError:
        return JSONResponse(
            status_code=498,
            content={"detail": "Token expired"}
        )
    
    request.state.user_id = payload.get("sub")  # Store user_id in request state for downstream use

    response = await call_next(request)
    return response