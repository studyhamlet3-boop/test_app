from fastapi import FastAPI
from src.controllers.simple_controller import router as simple_router
from src.controllers.simple_root import router as root_router
# middleware import
from fastapi.middleware.cors import CORSMiddleware
from src.middleware.logger_mid import log_request


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
# app.middleware("http")(log_request)
