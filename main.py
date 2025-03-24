from fastapi import FastAPI
from api.study_guide import router as study_guide_router
from api.healthcheck import router as healthcheck_router
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.include_router(study_guide_router)
app.include_router(healthcheck_router)


