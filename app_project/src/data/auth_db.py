from pydantic import BaseModel
from src.data.main_db import Database

class ChatEntry(BaseModel):
    email: str
    password_hash: str

async def run(obj: ChatEntry):
    async with Database.pool.acquire() as conn:
        # Pass the record_id variable into the query
        await conn.execute(
            '''
            INSERT INTO users (email, password_hash)
            VALUES ($1, $2)
            ''',
            obj.email,
            obj.password_hash
        )


