import src.models.gemini_client as gemini_client
import src.data.genai_cont_db as genai_cont_db
from google.genai import errors

# yields the stream.
# manages db storage of the conversation history.
async def genai_req(prompt: str):
    full_response = ""

#-----------Get And Read The Generator----------------
    try:
        async for chunk in await gemini_client.ask_gemini(prompt):
            full_response += chunk.text
            yield chunk.text
    except errors.APIError as e:
        # Handles API-specific issues (e.g., 429 for high demand, 401/403 for auth)
        print(f"API Error code {e.code}: {e.message}")
    except Exception as e:
        # Handles network drops or other unexpected runtime errors
        print(f"Unexpected error: {e}")

        # Handle the error (e.g., log it, return a default response, etc.)

#-----------Create the ChatEntry object----------------
    tmp_obj = genai_cont_db.ChatEntry(prompt=prompt, response=full_response)

#-----------DB querry----------------
    await genai_cont_db.run(tmp_obj)