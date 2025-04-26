from fastapi import APIRouter, HTTPException
from app.models.sentiment import SentimentRequest, SentimentResponse
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from app.core.template import SENTIMENT_TEMPLATE
from app.api.llm import sentiment_chat_llm
from langsmith import traceable

router = APIRouter()

class SentimentOutputParser(StrOutputParser):
    """Parser that extracts just the sentiment label from the LLM response."""
    
    def parse(self, text: str) -> str:
        if "Sentiment: " in text:
            return text.split("Sentiment: ")[1].strip()
        return text.strip()

@traceable(metadata={"llm": "llama3.2-1b-4bit"})
@router.post("/sentiment", response_model=SentimentResponse)
def analyze_sentiment(request: SentimentRequest):

    prompt = PromptTemplate(template=SENTIMENT_TEMPLATE, input_variables=["input"])

    chain = prompt | sentiment_chat_llm | SentimentOutputParser()
    
    input = {
        "input": request.text
    }
    if request.text == "Error":
        input = {
            "inputs": request.text # Wrong keys to test error alerting
        }
    result = chain.invoke(input)

    return SentimentResponse(content=result)