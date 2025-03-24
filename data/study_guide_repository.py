from abc import ABC, abstractmethod
from models.study_guide import StudyGuide

class StudyGuideRepository(ABC):
    @abstractmethod
    def get_study_guide(self, user_id: str, topic: str, level: str, style: str) -> StudyGuide:
        pass
    
