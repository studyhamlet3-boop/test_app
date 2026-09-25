import jwt
from datetime import datetime, timedelta, timezone
from exceptions import InvalidTokenError, TokenExpiredError
from dotenv import load_dotenv
import os

SECRET_KEY = os.getenv("SECRET_KEY")

def create_token(user_id):
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=2) # Expires in 2 hours
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token

def decode_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError
    except jwt.InvalidTokenError:
        raise InvalidTokenError