import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = ""

def create_token(user_id):
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(hours=2) # Expires in 2 hours
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    
    return token