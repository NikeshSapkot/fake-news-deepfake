from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional, List
import json
from utils.text_processor import TextProcessor
from utils.explainability import TextExplainer

router = APIRouter()

class TextRequest(BaseModel):
    text: str
    language: Optional[str] = "en"

class TextResponse(BaseModel):
    is_fake: bool
    confidence: float
    explanation: dict
    features: List[str]
    processing_time: float

@router.post("/detect", response_model=TextResponse)
async def detect_fake_news(request: TextRequest):
    """
    Detect fake news in text content using NLP and explainable AI
    """
    try:
        # Initialize text processor
        processor = TextProcessor()
        explainer = TextExplainer()
        
        # Process text and get prediction
        result = processor.predict(request.text, request.language)
        
        # Generate explanations
        explanation = explainer.explain(request.text, result)
        
        return TextResponse(
            is_fake=result["is_fake"],
            confidence=result["confidence"],
            explanation=explanation,
            features=result["features"],
            processing_time=result["processing_time"]
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")

@router.post("/batch-detect")
async def batch_detect_fake_news(texts: List[str]):
    """
    Detect fake news in multiple text inputs
    """
    try:
        processor = TextProcessor()
        results = []
        
        for text in texts:
            result = processor.predict(text)
            results.append({
                "text": text,
                "is_fake": result["is_fake"],
                "confidence": result["confidence"],
                "processing_time": result["processing_time"]
            })
        
        return {"results": results}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing batch: {str(e)}")

@router.get("/stats")
async def get_text_stats():
    """
    Get statistics about text processing
    """
    return {
        "total_processed": 0,
        "fake_detected": 0,
        "real_detected": 0,
        "average_confidence": 0.0
    } 