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

async def run(obj: ChatEntry):
    # Connect using .env
    conn = await asyncpg.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        host=os.getenv('DB_HOST')
    )
    
    # Pass the record_id variable into the query
    await conn.execute(
        '''
        INSERT INTO chat_logs (prompt, response) 
        VALUES ($1, $2)
        ''',
        obj.prompt,
        obj.response
    )

    await conn.close()