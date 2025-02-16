from fastapi import APIRouter

from infrastructure.open_router.study_guide_repository_implementation import StudyGuideRepositoryDependency

router = APIRouter()

@router.get("/study-guide/{topic}")
def get_study_guide(topic: str, level: str, style: str, study_guide_service: StudyGuideRepositoryDependency):
    return study_guide_service.get_study_guide(topic, level, style)