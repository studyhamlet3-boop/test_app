from src.data.auth_db import insert_user_db
from src.data.auth_db import get_user_info_by_email
from .gen_token import create_token

async def register_user(email: str, password: str): # returns token, raises UserAlreadyExistsError
    await insert_user_db(email,password) # can rise an exception

    user = await get_user_info_by_email(email)
    if user:
        user_id = user['id']
    else: raise Exception("The db has issues with finding the id")

    token = create_token(user_id, [])
    if not token:
        raise Exception("Token generation failed")
    return token