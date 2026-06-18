from fastapi import FastAPI
from src.controllers.simple_controller import router as simple_router
from src.controllers.simple_root import router as root_router
from src.data.main_db import lifespan_db
from contextlib import asynccontextmanager
# middleware import
from fastapi.middleware.cors import CORSMiddleware
from src.middleware.logger_mid import log_request
# Temporary imports

@asynccontextmanager
async def lifespan(app: FastAPI): #lifespan function
    async with lifespan_db(app): #Gemini context memory DB lifespan handle
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(root_router)
app.include_router(simple_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)


