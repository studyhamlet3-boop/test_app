import asyncio
import asyncpg
from pydantic import BaseModel
import os
from pathlib import Path
from dotenv import load_dotenv


class ChatEntry(BaseModel): # prompt + response
    prompt: str
    response: str
    # created_at: datetime = Field(default_factory=datetime.utcnow)


load_dotenv(dotenv_path="/Users/hhalmlet/Developer/myapp/.env")
db_pool = None


async def init_pool(): #Initiates the pool
    # Connect using .env
    global db_pool
    if db_pool is None:
        print("Initializing database connection pool...")
        db_pool = await asyncpg.create_pool(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST'),
        min_size=2, #minimum 2 cons open
        max_size=10
        )


async def run(obj: ChatEntry):
    async with db_pool.acquire() as conn:
        # Pass the record_id variable into the query
        await conn.execute(
            '''
            INSERT INTO chat_logs (prompt, response)
            VALUES ($1, $2)
            ''',
            obj.prompt,
            obj.response
        )

#TMP function
async def close_pool():
    global db_pool
    if db_pool:
        await db_pool.close()
        print("Database connection pool closed safely.")