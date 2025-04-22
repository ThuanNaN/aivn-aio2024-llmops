import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from functools import lru_cache

load_dotenv()

class Settings(BaseSettings):
    api_key: str = os.getenv("OPENAI_API_KEY")
    api_base: str = os.getenv("OPENAI_API_BASE_URL")
    app_title: str = "LLM API Service"
    app_description: str = "API for LLM operations with different models"
    version: str = "1.0.0"

@lru_cache()
def get_settings():
    return Settings()
