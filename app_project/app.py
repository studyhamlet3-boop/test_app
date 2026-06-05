from fastapi import FastAPI
from src.controllers.simple_controller import router as simple_router
from src.controllers.simple_root import router as root_router
# middleware import
from fastapi.middleware.cors import CORSMiddleware
from src.middleware.logger_mid import log_request
# Temporary imports
from src.data.genai_cont_db import clean_db, init_pool,close_pool

app = FastAPI()

app.include_router(root_router)
app.include_router(simple_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    await init_pool()  # Safely creates the global pool ONCE before any requests arrive
    await clean_db()   # Clear the chat_logs table on startup (optional, for testing purposes)

@app.on_event("shutdown")
async def shutdown_event():
    # Reach out to your global pool and close it cleanly
    await close_pool()
# app.middleware("http")(log_request)


# #1. Define the lifespan setup/teardown wrapper
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # This runs ON STARTUP
#     await init_pool()  
#     yield
#     # This runs ON SHUTDOWN
#     await close_pool() 

# #2. Pass lifespan directly into your FastAPI initialization
# app = FastAPI(lifespan=lifespan)
