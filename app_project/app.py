from fastapi import FastAPI
from src.controllers.simple_controller import router as simple_router
from src.controllers.simple_controller import auth_router as auth_router
from src.controllers.simple_root import router as root_router
from src.data.main_db import lifespan_db
from contextlib import asynccontextmanager

from dotenv import load_dotenv
# middleware import
from src.middleware.auth_jwt import auth_jwt_middleware
from fastapi.middleware.cors import CORSMiddleware
# Temporary imports

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI): #lifespan function
    async with lifespan_db(app): #Gemini context memory DB lifespan handle
        yield

app = FastAPI(lifespan=lifespan)

app.include_router(root_router)
app.include_router(simple_router)
app.include_router(auth_router)

app.middleware("http")(auth_jwt_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],    
    allow_headers=["*"],
)


