from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn
from api.routes import text_detection, image_detection, analysis
import os

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

# Include API routes
app.include_router(text_detection.router, prefix="/api/text", tags=["Text Detection"])
app.include_router(image_detection.router, prefix="/api/image", tags=["Image Detection"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])

# Health check endpoint
@app.get("/")
async def root():
    return {
        "message": "Fake News & Deepfake Detection API",
        "status": "running",
        "version": "1.0.0"
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    ) 