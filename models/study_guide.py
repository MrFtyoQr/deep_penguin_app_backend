from pydantic import BaseModel

class StudyGuide(BaseModel):
    text: str
    questions: list[Question]