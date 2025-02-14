from pydantic import BaseModel

class QuestionOption(BaseModel):
    index: int
    text: str