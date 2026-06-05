from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
from src.data import genai_cont_db
from src.data.genai_cont_db import ChatEntry


env_loaded = load_dotenv(dotenv_path="/Users/hhalmlet/Developer/myapp/.env")

if not env_loaded:
    raise FileNotFoundError(
        "Missing configuration: No '.env' file found in the project root directory."
   )
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)


def prepare_gemini_history(chat_entries: list[ChatEntry], new_prompt: str):
    contents = []

    # 1. Convert DB Pydantic objects into Gemini's expected roles
    for entry in chat_entries:
        contents.append(
            types.Content(
                role="user",
                parts=[types.Part.from_text(text=entry.prompt)]
            )
        )
        contents.append(
            types.Content(
                role="model",
                parts=[types.Part.from_text(text=entry.response)]
            )
        )
    
    # 2. Append the brand new prompt at the very end
    contents.append(
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=new_prompt)]
        )
    )
    
    return contents

#----------------GenAi Handle Function(Returns a Async Generator)
async def ask_gemini(prompt: str):
    fetched_history = await genai_cont_db.fetch_all() # Fetch the chat history from the database
    forwarded_contents = prepare_gemini_history(fetched_history, prompt)

    # Use the .aio property for async calls
    return await client.aio.models.generate_content_stream( # It uses a "Push" mechanism called an Asynchronous Iterator.
        model="gemini-2.5-flash",
        contents=forwarded_contents
    )
    
    # async for chunk in await client.aio.models.generate_content_stream( # It uses a "Push" mechanism called an Asynchronous Iterator.
    #     model="gemini-2.5-flash",
    #     contents=prompt
    # ):
    #     # Extract text and yield it immediately
    #     yield chunk.text

