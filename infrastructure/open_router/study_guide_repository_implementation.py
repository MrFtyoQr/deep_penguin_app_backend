from typing import Annotated
import json

from fastapi import Depends
from data.study_guide_repository import StudyGuideRepository
from infrastructure.open_router.gemini_service import GeminiService
from infrastructure.database.mongodb import study_guides_collection
from models.study_guide import StudyGuide

class StudyGuideRepositoryImplementation(StudyGuideRepository):
    def __init__(self, gemini_service: GeminiService):
        self.gemini_service = gemini_service

    def get_study_guide(self, user_id: str, topic: str, level: str, style: str) -> StudyGuide:
        existing_guide = study_guides_collection.find_one({"user_id": user_id, "topic": topic, "level": level, "style": style}, {"_id": 0})
        if existing_guide:
            return StudyGuide(**existing_guide)

        study_guide_txt = self.gemini_service.generate_study_guide(topic, level, style)

        try:
            study_guide_data = json.loads(study_guide_txt)
            study_guide_data["user_id"] = user_id
            study_guide = StudyGuide(**study_guide_data)
            self.save_study_guide(study_guide)
            return study_guide
        except (json.JSONDecodeError, TypeError) as e:
            raise ValueError(f"Invalid response from Gemini API: {e}")
        
    def save_study_guide(self, study_guide: StudyGuide) -> str:
        result = study_guides_collection.insert_one(study_guide.dict())
        return str(result.inserted_id)

    def delete_study_guide(self, user_id: str, topic: str, level: str, style: str) -> bool:
        result = study_guides_collection.delete_one({"user_id": user_id, "topic": topic, "level": level, "style": style})
        return result.deleted_count > 0

def get_study_guide_repository(
    gemini_service: Annotated[GeminiService, Depends()]
) -> StudyGuideRepository:
    return StudyGuideRepositoryImplementation(gemini_service)

StudyGuideRepositoryDependency = Annotated[
    StudyGuideRepository, Depends(get_study_guide_repository)
]
