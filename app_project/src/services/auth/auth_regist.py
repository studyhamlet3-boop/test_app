from src.data.auth_db import insert_user_db
from .gen_token import create_token

async def register_user(email: str, password: str): # returns token, raises UserAlreadyExistsError
    await insert_user_db(email,password) # can rise an exception
    token = create_token(email) # needs to be changed to user_id
    return token