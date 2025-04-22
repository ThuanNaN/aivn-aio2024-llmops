from fastapi import APIRouter
from .sentiment import router as sentiment_router
from .medical_qa import router as medical_qa_router

router = APIRouter()
router.include_router(sentiment_router, tags=["Sentiment Analysis"])
router.include_router(medical_qa_router, tags=["Medical QA"])