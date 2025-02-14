

from typing import Annotated

from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.gemini_service import GeminiService
from models.study_guide import StudyGuide


class StudyGuideRepositoryImplementation(StudyGuideRepository):
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    def get_study_guide(self, topic: str) -> StudyGuide:
        study_guide_txt = self.gemini_service.generate_study_guide(topic)

        return StudyGuide(title=topic, content=study_guide_txt)
        

def get_study_guide_repository(gemini_service: GeminiService) -> StudyGuideRepository:
    return StudyGuideRepositoryImplementation(gemini_service)

StudyGuideRepositoryDependency = Annotated[
    StudyGuideRepositoryImplementation, Depends(get_study_guide_repository)
]
