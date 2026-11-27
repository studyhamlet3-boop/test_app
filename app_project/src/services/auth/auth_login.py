from exceptions import invalidCredentials
from src.data.auth_db import get_user_info_by_email
from .gen_token import create_token

async def login_user(email, password):
    user = await get_user_info_by_email(email)
    if user is None:
        raise invalidCredentials()
    if user['password'] != password:
        raise invalidCredentials()
    if not user['verified']:
        raise invalidCredentials()
    
    token = create_token(user['id'], [])
    return token