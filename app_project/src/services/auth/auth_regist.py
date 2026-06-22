from src.data.auth_db import insert_user_db
from src.controllers.simple_controller import regist_info
from gen_token import create_token

async def register_user(cred: regist_info): # returns token, raises UserAlreadyExistsError
    await insert_user_db(cred) # can rise an exception
    token = create_token(cred.email) # needs to be changed to user_id
    return {"token": token}