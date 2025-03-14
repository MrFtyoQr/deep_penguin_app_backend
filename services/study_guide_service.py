from typing import Annotated
from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.study_guide_repository_implementation import StudyGuideRepositoryDependency
from models.study_guide import StudyGuide

class StudyGuideService:
    def __init__(self, study_guide_repository: StudyGuideRepository):
        self.study_guide_repository = study_guide_repository

    def get_study_guide(self, user_id: str, topic: str, level: str, style: str) -> StudyGuide:
        return self.study_guide_repository.get_study_guide(user_id, topic, level, style)
    
    def save_study_guide(self, user_id: str, study_guide: StudyGuide) -> str:
        study_guide.user_id = user_id
        return self.study_guide_repository.save_study_guide(study_guide)
    
    def delete_study_guide(self, user_id: str, topic: str, level: str, style: str) -> bool:
        return self.study_guide_repository.delete_study_guide(user_id, topic, level, style)
    
def get_study_guide_service(study_guide_repository: StudyGuideRepositoryDependency) -> StudyGuideService:
    return StudyGuideService(study_guide_repository)

StudyGuideServiceDependency = Annotated[
    StudyGuideService, Depends(get_study_guide_service)
]