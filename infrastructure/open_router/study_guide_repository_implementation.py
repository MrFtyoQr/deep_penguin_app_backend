from typing import Annotated
import json

from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.deepseek_service import DeepseekService
from models.study_guide import StudyGuide


class StudyGuideRepositoryImplementation(StudyGuideRepository):
    def __init__(self, deepseek_service: DeepseekService):
        self.deepseek_service = deepseek_service

    def get_study_guide(self, topic: str, level: str, style: str) -> StudyGuide:
        study_guide_txt = self.deepseek_service.generate_study_guide(topic, level, style)

        try:
            study_guide_data = json.loads(study_guide_txt)
            return StudyGuide(**study_guide_data)
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(f"Invalid response from Gemini API: {e}")


def get_study_guide_repository(
    deepseek_service: Annotated[DeepseekService, Depends()]
) -> StudyGuideRepository:
    return StudyGuideRepositoryImplementation(deepseek_service)


StudyGuideRepositoryDependency = Annotated[
    StudyGuideRepository, Depends(get_study_guide_repository)
]
