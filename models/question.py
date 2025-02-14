from pydantic import BaseModel

from models.correct_answer import CorrectAnswer
from models.question_option import QuestionOption

class Question(BaseModel):
    text: str
    options: list[QuestionOption]
    correct_answer: CorrectAnswer