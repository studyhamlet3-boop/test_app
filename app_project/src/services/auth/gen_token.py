import jwt
import uuid
from datetime import datetime, timedelta, timezone
from typing import Sequence
from exceptions import InvalidTokenError, TokenExpiredError
import os

SECRET_KEY = os.getenv("SECRET_KEY")


#?Old Token
# def create_token(user_id):
#     payload = {
#         "sub": str(user_id),
#         "exp": datetime.now(timezone.utc) + timedelta(hours=2) # Expires in 2 hours
#     }
# token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")    
#     return token

ACCESS_TTL = timedelta(minutes=30)

def create_token(user_id: str, roles: Sequence[str]) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": user_id,
        "roles": list(roles),
        "type": "access",   # stops refresh tokens being used as access tokens #? whats the difference?
        "iat": now,
        "exp": now + ACCESS_TTL,
        "iss": "Soma",
        "aud": "Soma Regist",
        "jti": str(uuid.uuid4()),   #! DB support required
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256") #? settings.jwt_secret instead of SECRET_KEY


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=["HS256"],
            issuer="Soma",
            audience="Soma Regist",
            options={"require": ["iat", "exp", "iss", "sub", "aud", "jti"]})
        return payload

    except jwt.ExpiredSignatureError:
        raise TokenExpiredError
    except jwt.InvalidTokenError:
        raise InvalidTokenError
    except jwt.MissingRequiredClaimError:
        raise InvalidTokenError