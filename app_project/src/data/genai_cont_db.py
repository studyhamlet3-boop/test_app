from src.data.main_db import Database
from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncpg
from pydantic import BaseModel
import os
from dotenv import load_dotenv


class ChatEntry(BaseModel): # prompt + response
    prompt: str
    response: str
    # created_at: datetime = Field(default_factory=datetime.utcnow)


async def run(obj: ChatEntry):
    async with Database.pool.acquire() as conn:
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
    try:
        async with Database.pool.acquire() as conn:
            records = await conn.fetch('SELECT * FROM chat_logs ORDER BY id DESC LIMIT 10') # Fetch the 10 most recent records
            records = reversed(records)  # Reverse the order to get the most recent entries at the end
            return [ChatEntry(prompt=record['prompt'], response=record['response']) for record in records]
    except Exception as e:
        print(f"Error fetching chat logs: {e}")
        return []
