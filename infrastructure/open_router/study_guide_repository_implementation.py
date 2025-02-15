from typing import Annotated
import json

from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.gemini_service import GeminiService
from models.study_guide import StudyGuide


class StudyGuideRepositoryImplementation(StudyGuideRepository):
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    def get_study_guide(self, topic: str) -> StudyGuide:
        study_guide_txt = self.gemini_service.generate_study_guide(topic)

        try:
            study_guide_data = json.loads(study_guide_txt)
            return StudyGuide(**study_guide_data)
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(f"Invalid response from Gemini API: {e}")


def get_study_guide_repository(
    gemini_service: Annotated[GeminiService, Depends()]
) -> StudyGuideRepository:
    return StudyGuideRepositoryImplementation(gemini_service)


StudyGuideRepositoryDependency = Annotated[
    StudyGuideRepository, Depends(get_study_guide_repository)
]
