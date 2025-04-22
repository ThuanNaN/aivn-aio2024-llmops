from typing import List
from pydantic import BaseModel

class MedicalQARequest(BaseModel):
    question: str
    choices: List[str]

class MedicalQAResponse(BaseModel):
    content: str