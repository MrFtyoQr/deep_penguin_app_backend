from pydantic import BaseModel

from models.question import Question

class StudyGuide(BaseModel):
    user_id: str
    text: str
    questions: list[Question]