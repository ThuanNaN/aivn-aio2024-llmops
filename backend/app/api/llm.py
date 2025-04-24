from langchain_openai import ChatOpenAI
from app.core.config import get_settings

settings = get_settings()

sentiment_chat_llm = ChatOpenAI(
    openai_api_key=settings.api_key,
    openai_api_base=settings.api_base,
    model="vsf-lora",
    temperature=0,
    max_tokens=16
)


medqa_chat_llm = ChatOpenAI(
    openai_api_key=settings.api_key,
    openai_api_base=settings.api_base,
    model="medqa-lora",
    temperature=0,
    max_tokens=64
)
