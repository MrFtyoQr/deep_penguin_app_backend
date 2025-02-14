

from data.study_guide_repository import StudyGuideRepository
from models.study_guide import StudyGuide


class OpenRouterService(StudyGuideRepository):
    def __init__(self):
        pass

    def get_study_guide(self, topic: str) -> StudyGuide:
        return self.study_guide_repository.get_study_guide(topic)
    
