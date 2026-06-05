import src.models.gemini_client as gemini_client
import src.data.genai_cont_db as genai_cont_db

# yields the stream.
# manages db storage of the conversation history.
async def genai_req(prompt: str):
    full_response = ""

#-----------Get And Read The Generator----------------
    async for chunk in await gemini_client.ask_gemini(prompt):

#-----------Capture The Whole Stream----------------

        full_response += chunk.text
        yield chunk.text
    
#-----------Create the ChatEntry object----------------
    tmp_obj = genai_cont_db.ChatEntry(prompt=prompt, response=full_response)

#-----------DB querry----------------
    await genai_cont_db.run(tmp_obj)