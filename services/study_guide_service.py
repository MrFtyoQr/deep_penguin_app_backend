from typing import Annotated
from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.study_guide_repository_implementation import StudyGuideRepositoryDependency
from models.study_guide import StudyGuide

class StudyGuideService:
    def __init__(self, study_guide_repository: StudyGuideRepository):
        self.study_guide_repository = study_guide_repository

    def get_study_guide_by_title(self, title: str) -> StudyGuide:
        return self.study_guide_repository.get_study_guide(title)
    
def get_study_guide_service(study_guide_repository: StudyGuideRepositoryDependency) -> StudyGuideService:
    return StudyGuideService(study_guide_repository)

StudyGuideServiceDependency = Annotated[
    StudyGuideService, Depends(get_study_guide_service)
]