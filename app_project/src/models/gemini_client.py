from google import genai
import os
from dotenv import load_dotenv

env_loaded = load_dotenv()
if not env_loaded:
    raise FileNotFoundError(
        "Missing configuration: No '.env' file found in the project root directory."
   )
API_KEY = os.getenv("API_KEY")
client = genai.Client(api_key=API_KEY)
async def ask_gemini(prompt):

    # Use the .aio property for async calls
    async for chunk in await client.aio.models.generate_content_stream( # It uses a "Push" mechanism called an Asynchronous Iterator.
        model="gemini-2.5-flash",
        contents=prompt
    ):
        # Extract text and yield it immediately
        yield chunk.text
