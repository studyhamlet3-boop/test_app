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


async def init_pool(): # Initiates the pool
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

async def clean_db():
    async with db_pool.acquire() as conn:
        await conn.execute('DELETE FROM chat_logs') # Clear all records from the chat_logs table

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

async def fetch_all(): # returns ChatEntry object array
    async with db_pool.acquire() as conn:
        records = await conn.fetch('SELECT * FROM chat_logs ORDER BY id DESC LIMIT 10') # Fetch the 10 most recent records
        records = reversed(records)  # Reverse the order to get the most recent entries at the end
        return [ChatEntry(prompt=record['prompt'], response=record['response']) for record in records]

#TMP function
async def close_pool():
    global db_pool
    if db_pool:
        await db_pool.close()
        print("Database connection pool closed safely.")