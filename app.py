from typing import Union

from fastapi import FastAPI
from api.study_guide import router as study_guide_router


app = FastAPI()

app.include_router(study_guide_router)

