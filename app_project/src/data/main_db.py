from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncpg
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Users/hhalmlet/Developer/myapp/.env")
db_pool = None

class Database:
    pool = None

    @classmethod
    async def init_pool(cls): # Initiates the pool

        if cls.pool is None:
            cls.pool = await asyncpg.create_pool(
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            host=os.getenv('DB_HOST'),
            min_size=2,
            max_size=10
            )

    @classmethod
    async def clean_db(cls):
        async with cls.pool.acquire() as conn:
            await conn.execute('DELETE FROM chat_logs') # Clear all records from the chat_logs table

    #TMP function
    @classmethod
    async def close_pool(cls):
        if cls.pool:
            await cls.pool.close()
            print("Database connection pool closed safely.")

@asynccontextmanager
async def lifespan_db(app: FastAPI):
    await Database.init_pool()
    await Database.clean_db()
    yield
    await Database.close_pool()