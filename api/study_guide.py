from fastapi import APIRouter, Depends
from services.study_guide_service import StudyGuideServiceDependency
from models.study_guide import StudyGuide

router = APIRouter()

@router.get("/study-guide/", dependencies=[Depends(verify_token)])
def get_study_guide(
    topic: str, 
    level: str, 
    style: str, 
    study_guide_service: StudyGuideServiceDependency,
    token: dict = Depends(verify_token)
):
    user_id = token["sub"]
    return study_guide_service.get_study_guide(user_id, topic, level, style)

@router.post("/study-guide", dependencies=[Depends(verify_token)])
def save_study_guide(
    study_guide: StudyGuide, 
    study_guide_service: StudyGuideServiceDependency,
    token: dict = Depends(verify_token)
):
    user_id = token["sub"]
    return study_guide_service.save_study_guide(user_id, study_guide)

@router.delete("/study-guide/", dependencies=[Depends(verify_token)])
def delete_study_guide(
    topic: str, 
    level: str, 
    style: str, 
    study_guide_service: StudyGuideServiceDependency,
    token: dict = Depends(verify_token)
):
    user_id = token["sub"]
    return study_guide_service.delete_study_guide(user_id, topic, level, style)