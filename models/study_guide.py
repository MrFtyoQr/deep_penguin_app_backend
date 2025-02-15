from pydantic import BaseModel

from models.question import Question

class StudyGuide(BaseModel):
    text: str
    questions: list[Question]