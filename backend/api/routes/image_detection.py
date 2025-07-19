from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from pydantic import BaseModel
from typing import Optional, List
import json
from utils.image_processor import ImageProcessor
from utils.explainability import ImageExplainer

router = APIRouter()

class ImageResponse(BaseModel):
    is_deepfake: bool
    confidence: float
    explanation: dict
    face_detected: bool
    processing_time: float
    image_url: Optional[str] = None

@router.post("/detect", response_model=ImageResponse)
async def detect_deepfake(
    file: UploadFile = File(...),
    analyze_faces: bool = Form(True)
):
    """
    Detect deepfake in uploaded image using computer vision and explainable AI
    """
    try:
        # Validate file type
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="File must be an image")
        
        # Initialize processors
        processor = ImageProcessor()
        explainer = ImageExplainer()
        
        # Process image and get prediction
        result = processor.predict(file.file, analyze_faces)
        
        # Generate explanations
        explanation = explainer.explain(file.file, result)
        
        return ImageResponse(
            is_deepfake=result["is_deepfake"],
            confidence=result["confidence"],
            explanation=explanation,
            face_detected=result["face_detected"],
            processing_time=result["processing_time"],
            image_url=result.get("image_url")
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")

@router.post("/batch-detect")
async def batch_detect_deepfake(files: List[UploadFile] = File(...)):
    """
    Detect deepfake in multiple images
    """
    try:
        processor = ImageProcessor()
        results = []
        
        for file in files:
            if not file.content_type.startswith('image/'):
                continue
                
            result = processor.predict(file.file)
            results.append({
                "filename": file.filename,
                "is_deepfake": result["is_deepfake"],
                "confidence": result["confidence"],
                "face_detected": result["face_detected"],
                "processing_time": result["processing_time"]
            })
        
        return {"results": results}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing batch: {str(e)}")

@router.get("/stats")
async def get_image_stats():
    """
    Get statistics about image processing
    """
    return {
        "total_processed": 0,
        "deepfake_detected": 0,
        "real_detected": 0,
        "faces_detected": 0,
        "average_confidence": 0.0
    } 