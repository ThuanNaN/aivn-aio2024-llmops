from typing import List, Dict
from pydantic import BaseModel

class ChatRequest(BaseModel):
    messages: List[Dict[str, str]]
    model: str = "meta-llama/Llama-3.2-1B-Instruct"
    temperature: float = 0
    max_tokens: int = 100

class ChatResponse(BaseModel):
    content: str