from fastapi import APIRouter

router = APIRouter()

@router.get("/study-guide/{topic}")
def get_study_guide(topic: str):
    return {"message": "Study guide route is working"}