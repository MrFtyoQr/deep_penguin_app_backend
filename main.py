from typing import Union

from fastapi import FastAPI
from api.study_guide import router as study_guide_router
from api.healthcheck import router as healthcheck_router
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://deep-penguin.vercel.app/"],  # ⚠️ Cambia "*" por el dominio de tu frontend en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos los headers
)

app.include_router(study_guide_router)
app.include_router(healthcheck_router)


