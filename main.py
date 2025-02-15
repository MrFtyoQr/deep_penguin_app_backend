from typing import Union

from fastapi import FastAPI
import uvicorn
from api.study_guide import router as study_guide_router
from api.healthcheck import router as healthcheck_router


app = FastAPI()

app.include_router(study_guide_router)
app.include_router(healthcheck_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0')

