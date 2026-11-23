from src.data.auth_db import insert_user_db
from src.data.auth_db import get_user_id_by_email
from .gen_token import create_token

async def register_user(email: str, password: str): # returns token, raises UserAlreadyExistsError
    await insert_user_db(email,password) # can rise an exception
    user_id = await get_user_id_by_email(email)
    token = create_token(user_id, [])
    if not token:
        raise Exception("Token generation failed")
    return token