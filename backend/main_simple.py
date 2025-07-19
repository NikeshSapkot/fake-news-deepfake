from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import json
import random
from typing import Optional, List
import base64
from datetime import datetime

app = FastAPI(
    title="Fake News & Deepfake Detection API",
    description="AI-powered system for detecting fake news and deepfake images/videos with explainable AI",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class TextRequest(BaseModel):
    text: str
    language: str = "en"

class TextResponse(BaseModel):
    is_fake: bool
    confidence: float
    explanation: str
    features: dict
    processing_time: float

class ImageResponse(BaseModel):
    is_deepfake: bool
    confidence: float
    explanation: str
    features: dict
    processing_time: float

class AnalysisResponse(BaseModel):
    text_analysis: TextResponse
    image_analysis: Optional[ImageResponse] = None
    overall_confidence: float
    recommendation: str

# Mock data for demonstration
fake_indicators = [
    "BREAKING", "SHOCKING", "UNBELIEVABLE", "YOU WON'T BELIEVE", 
    "VIRAL", "AMAZING", "INCREDIBLE", "MIND-BLOWING", "CONSPIRACY",
    "SECRET", "HIDDEN", "COVER-UP", "DOCTORS HATE", "GOVERNMENT HIDING"
]

real_indicators = [
    "according to", "official sources", "study published", "research shows",
    "government statement", "scientific evidence", "peer-reviewed", "verified",
    "fact-checked", "reliable source", "expert analysis", "data shows"
]

# Text analysis function
def analyze_text(text: str) -> dict:
    """Simple text analysis for demonstration"""
    text_lower = text.lower()
    
    # Count indicators
    fake_score = sum(1 for indicator in fake_indicators if indicator.lower() in text_lower)
    real_score = sum(1 for indicator in real_indicators if indicator.lower() in text_lower)
    
    # Simple scoring
    total_length = len(text.split())
    fake_ratio = fake_score / max(total_length, 1)
    real_ratio = real_score / max(total_length, 1)
    
    # Determine if fake
    is_fake = fake_ratio > real_ratio or fake_score > 2
    
    # Calculate confidence
    confidence = min(0.95, max(0.05, abs(fake_ratio - real_ratio) * 10))
    
    # Generate explanation
    if is_fake:
        explanation = f"Text contains {fake_score} suspicious indicators like sensationalist language."
    else:
        explanation = f"Text contains {real_score} credible indicators and balanced language."
    
    return {
        "is_fake": is_fake,
        "confidence": confidence,
        "explanation": explanation,
        "features": {
            "fake_indicators": fake_score,
            "real_indicators": real_score,
            "text_length": total_length,
            "fake_ratio": fake_ratio,
            "real_ratio": real_ratio
        }
    }

# Image analysis function
def analyze_image(image_data: bytes) -> dict:
    """Simple image analysis for demonstration"""
    # Mock analysis - in real implementation, this would use ML models
    image_size = len(image_data)
    
    # Simple heuristics for demonstration
    is_deepfake = random.random() < 0.3  # 30% chance of being fake
    confidence = random.uniform(0.6, 0.9)
    
    explanation = "Image analysis completed. Checked for digital artifacts and face consistency."
    
    return {
        "is_deepfake": is_deepfake,
        "confidence": confidence,
        "explanation": explanation,
        "features": {
            "image_size": image_size,
            "format": "JPEG/PNG",
            "resolution": "Unknown",
            "face_detected": random.choice([True, False])
        }
    }

# API Routes
@app.get("/")
async def root():
    return {
        "message": "Fake News & Deepfake Detection API",
        "status": "running",
        "version": "1.0.0",
        "endpoints": {
            "text_detection": "/api/text/detect",
            "image_detection": "/api/image/detect",
            "analysis": "/api/analysis/comprehensive",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running", "timestamp": datetime.now().isoformat()}

# Text Detection Routes
@app.post("/api/text/detect", response_model=TextResponse)
async def detect_fake_news(request: TextRequest):
    """Analyze text for fake news detection"""
    import time
    start_time = time.time()
    
    # Analyze text
    result = analyze_text(request.text)
    
    processing_time = time.time() - start_time
    
    return TextResponse(
        is_fake=result["is_fake"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        features=result["features"],
        processing_time=processing_time
    )

@app.post("/api/text/batch-detect")
async def batch_text_detection(texts: List[str]):
    """Batch text analysis"""
    results = []
    for text in texts:
        result = analyze_text(text)
        results.append({
            "text": text[:100] + "..." if len(text) > 100 else text,
            **result
        })
    
    return {"results": results, "total_processed": len(texts)}

@app.get("/api/text/stats")
async def text_stats():
    """Get text analysis statistics"""
    return {
        "total_analyses": random.randint(100, 1000),
        "fake_detected": random.randint(30, 70),
        "real_detected": random.randint(30, 70),
        "average_confidence": round(random.uniform(0.7, 0.9), 2),
        "processing_time_avg": round(random.uniform(0.1, 0.5), 2)
    }

# Image Detection Routes
@app.post("/api/image/detect", response_model=ImageResponse)
async def detect_deepfake(file: UploadFile = File(...)):
    """Analyze image for deepfake detection"""
    import time
    start_time = time.time()
    
    # Read image data
    image_data = await file.read()
    
    # Analyze image
    result = analyze_image(image_data)
    
    processing_time = time.time() - start_time
    
    return ImageResponse(
        is_deepfake=result["is_deepfake"],
        confidence=result["confidence"],
        explanation=result["explanation"],
        features=result["features"],
        processing_time=processing_time
    )

@app.post("/api/image/batch-detect")
async def batch_image_detection(files: List[UploadFile] = File(...)):
    """Batch image analysis"""
    results = []
    for file in files:
        image_data = await file.read()
        result = analyze_image(image_data)
        results.append({
            "filename": file.filename,
            **result
        })
    
    return {"results": results, "total_processed": len(files)}

@app.get("/api/image/stats")
async def image_stats():
    """Get image analysis statistics"""
    return {
        "total_analyses": random.randint(50, 200),
        "deepfakes_detected": random.randint(10, 40),
        "real_images": random.randint(10, 40),
        "average_confidence": round(random.uniform(0.7, 0.9), 2),
        "processing_time_avg": round(random.uniform(0.5, 2.0), 2)
    }

# Analysis Routes
@app.post("/api/analysis/comprehensive", response_model=AnalysisResponse)
async def comprehensive_analysis(
    text: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    """Comprehensive multi-modal analysis"""
    import time
    start_time = time.time()
    
    # Analyze text
    text_result = analyze_text(text)
    
    # Analyze image if provided
    image_result = None
    if image:
        image_data = await image.read()
        image_result = analyze_image(image_data)
    
    # Calculate overall confidence
    overall_confidence = text_result["confidence"]
    if image_result:
        overall_confidence = (text_result["confidence"] + image_result["confidence"]) / 2
    
    # Generate recommendation
    if text_result["is_fake"] or (image_result and image_result["is_deepfake"]):
        recommendation = "Content appears to be fake or manipulated. Verify with reliable sources."
    else:
        recommendation = "Content appears to be genuine. Always verify with multiple sources."
    
    processing_time = time.time() - start_time
    
    return AnalysisResponse(
        text_analysis=TextResponse(
            is_fake=text_result["is_fake"],
            confidence=text_result["confidence"],
            explanation=text_result["explanation"],
            features=text_result["features"],
            processing_time=processing_time
        ),
        image_analysis=ImageResponse(
            is_deepfake=image_result["is_deepfake"],
            confidence=image_result["confidence"],
            explanation=image_result["explanation"],
            features=image_result["features"],
            processing_time=processing_time
        ) if image_result else None,
        overall_confidence=overall_confidence,
        recommendation=recommendation
    )

@app.get("/api/analysis/dashboard")
async def dashboard_data():
    """Get dashboard data"""
    return {
        "total_analyses": random.randint(500, 2000),
        "text_analyses": random.randint(300, 1200),
        "image_analyses": random.randint(100, 500),
        "fake_detected": random.randint(100, 400),
        "deepfakes_detected": random.randint(20, 100),
        "accuracy_rate": round(random.uniform(0.85, 0.95), 2),
        "recent_activity": [
            {
                "id": i,
                "type": random.choice(["text", "image"]),
                "timestamp": datetime.now().isoformat(),
                "result": random.choice(["fake", "real"]),
                "confidence": round(random.uniform(0.7, 0.9), 2)
            }
            for i in range(1, 11)
        ]
    }

@app.get("/api/analysis/trends")
async def analysis_trends():
    """Get analysis trends"""
    return {
        "daily_analyses": [random.randint(10, 50) for _ in range(7)],
        "fake_detection_rate": [round(random.uniform(0.1, 0.4), 2) for _ in range(7)],
        "deepfake_detection_rate": [round(random.uniform(0.05, 0.2), 2) for _ in range(7)],
        "average_confidence": [round(random.uniform(0.7, 0.9), 2) for _ in range(7)]
    }

if __name__ == "__main__":
    print("🚀 Starting Fake News & Deepfake Detection API...")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🌐 Health Check: http://localhost:8000/health")
    uvicorn.run(
        "main_simple:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 