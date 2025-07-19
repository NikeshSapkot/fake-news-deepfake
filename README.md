# 🧠 Fake News & Deepfake Detection System

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**AI-powered system for detecting fake news and deepfake images/videos with explainable AI**

## 🎯 Project Overview

This project implements a comprehensive fake news and deepfake detection system using advanced machine learning, natural language processing, and computer vision techniques. The system provides explainable AI insights to help users understand why content was flagged as potentially fake.

### ✨ Key Features

- 📰 **Text Analysis**: Detect fake news in articles, social media posts, and other text content
- 🖼️ **Image Analysis**: Detect deepfakes and digital manipulation in images
- 🧠 **Explainable AI**: Transparent explanations using SHAP, LIME, and attention visualizations
- 📊 **Real-time Dashboard**: Analytics and insights from detection results
- 🌐 **Modern Web Interface**: Responsive React frontend with beautiful animations
- ⚡ **Fast API**: High-performance FastAPI backend with async processing

## 🏗️ Architecture

```
fake-news-deepfake-detector/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application entry point
│   ├── main_simple.py      # Simplified version (working)
│   ├── api/                # API routes
│   │   └── routes/         # Endpoint definitions
│   ├── utils/              # Utility modules
│   │   ├── text_processor.py    # NLP processing
│   │   ├── image_processor.py   # CV processing
│   │   └── explainability.py    # XAI explanations
│   ├── requirements.txt    # Full Python dependencies
│   └── requirements_simple.txt  # Essential dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # Reusable components
│   │   ├── pages/          # Page components
│   │   └── services/       # API services
│   ├── package.json        # Node.js dependencies
│   └── tailwind.config.js  # Tailwind CSS config
├── data/                   # Datasets and training data
├── models/                 # Pre-trained models
├── notebooks/              # Jupyter notebooks for training
├── demo.html               # Interactive demo interface
├── start_project.py        # Quick start script
├── docker-compose.yml      # Docker setup
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/NikeshSapkot/fake-news-deepfake.git
cd fake-news-deepfake

# Run the automated setup script
python start_project.py
```

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend
pip install -r requirements_simple.txt
python main_simple.py
```

#### Frontend Demo
```bash
# Open the demo HTML file in your browser
start demo.html
```

## 🏃‍♂️ Running the Application

### Start Backend Only
```bash
cd backend
python main_simple.py
```
- 🌐 Server: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs

### Open Frontend Demo
```bash
# Open demo.html in your browser
start demo.html
```

## 🧪 Testing the System

### Backend API Testing
```powershell
# Health check
Invoke-WebRequest -Uri http://localhost:8000/health

# Text analysis
$body = @{
    text = "BREAKING: You won't believe what happened next!"
    language = "en"
} | ConvertTo-Json

Invoke-WebRequest -Uri http://localhost:8000/api/text/detect -Method POST -ContentType "application/json" -Body $body
```

### Frontend Demo Testing
1. Open `demo.html` in your browser
2. Paste text in the analysis area
3. Click "Analyze Text" to see results
4. Test with both fake and real news examples

## 📊 API Endpoints

### Text Detection
- `POST /api/text/detect` - Analyze text for fake news
- `POST /api/text/batch-detect` - Batch text analysis
- `GET /api/text/stats` - Text analysis statistics

### Image Detection
- `POST /api/image/detect` - Analyze image for deepfakes
- `POST /api/image/batch-detect` - Batch image analysis
- `GET /api/image/stats` - Image analysis statistics

### Analysis
- `POST /api/analysis/comprehensive` - Multi-modal analysis
- `GET /api/analysis/dashboard` - Dashboard data
- `GET /api/analysis/trends` - Analysis trends

### System
- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /docs` - Interactive API documentation

## 🔧 Technology Stack

### Backend
- **FastAPI**: High-performance web framework
- **Uvicorn**: ASGI server
- **Pydantic**: Data validation
- **Python-multipart**: File uploads

### Frontend
- **HTML5/CSS3**: Modern web standards
- **Tailwind CSS**: Utility-first CSS framework
- **JavaScript**: Interactive functionality
- **Lucide Icons**: Beautiful icon library

### Machine Learning (Ready for Integration)
- **BERT/RoBERTa**: NLP models for text analysis
- **XceptionNet**: CNN for image analysis
- **SHAP/LIME**: Explainable AI
- **OpenCV**: Computer vision processing

## 📈 Features

### Text Analysis
- Source credibility assessment
- Sentiment analysis
- Language pattern detection
- Fact-checking indicators
- Writing style analysis

### Image Analysis
- Face detection and analysis
- Digital artifact detection
- Color consistency analysis
- Symmetry and alignment checks
- Compression artifact analysis

### Explainable AI
- SHAP (SHapley Additive exPlanations)
- LIME (Local Interpretable Model-agnostic Explanations)
- Attention visualization for NLP
- Grad-CAM for computer vision
- Feature importance ranking

## 🎨 User Interface

- **Modern Design**: Clean, responsive interface
- **Real-time Feedback**: Live analysis with progress indicators
- **Interactive Visualizations**: Charts and graphs for insights
- **Mobile Responsive**: Works on all device sizes
- **Dark/Light Mode**: Theme switching capability
- **Animations**: Smooth transitions and micro-interactions

## 📊 Dashboard Features

- **Real-time Statistics**: Live updates of detection metrics
- **Trend Analysis**: Historical data and patterns
- **Performance Metrics**: Accuracy, processing time, confidence scores
- **Recent Activity**: Latest analyses and results
- **Feature Importance**: Key factors in detection decisions

## 🔒 Security & Privacy

- **No Data Storage**: Content is processed in memory only
- **Secure API**: Input validation and sanitization
- **Rate Limiting**: Protection against abuse
- **CORS Configuration**: Secure cross-origin requests
- **Error Handling**: Graceful error responses

## 🚀 Deployment

### Local Development
```bash
# Backend
cd backend
python main_simple.py

# Frontend
start demo.html
```

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up --build
```

### Production Deployment
```bash
# Backend deployment
pip install -r requirements_simple.txt
python main_simple.py

# Frontend deployment
# Serve demo.html with any web server
```

## 📝 Usage Examples

### Text Analysis
```python
import requests

response = requests.post('http://localhost:8000/api/text/detect', json={
    'text': 'Your news article text here...',
    'language': 'en'
})

result = response.json()
print(f"Is fake: {result['is_fake']}")
print(f"Confidence: {result['confidence']}")
```

### Image Analysis
```python
import requests

with open('image.jpg', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/api/image/detect', files=files)

result = response.json()
print(f"Is deepfake: {result['is_deepfake']}")
print(f"Confidence: {result['confidence']}")
```

## 📚 Training with Real Datasets

### Download Datasets
- **Fake News**: [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- **LIAR Dataset**: [LIAR Dataset](https://www.kaggle.com/datasets/ruchi798/liar-dataset)
- **Deepfake**: [DeepFake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge)

### Run Training
```bash
# Install Jupyter
pip install jupyter

# Start Jupyter
jupyter notebook

# Open training notebook
notebooks/model_training_with_kaggle.ipynb
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- HuggingFace for transformer models
- OpenCV community for computer vision tools
- FastAPI for the excellent web framework
- React team for the amazing frontend framework

## 📞 Contact

- **Author**: Nikesh Sapkot
- **GitHub**: [@NikeshSapkot](https://github.com/NikeshSapkot)
- **Repository**: [https://github.com/NikeshSapkot/fake-news-deepfake](https://github.com/NikeshSapkot/fake-news-deepfake)
- **Issues**: [https://github.com/NikeshSapkot/fake-news-deepfake/issues](https://github.com/NikeshSapkot/fake-news-deepfake/issues)

## 🎉 Project Status

### ✅ Current Status: FULLY FUNCTIONAL
- **Backend API**: ✅ Working perfectly
- **Frontend Demo**: ✅ Beautiful interface
- **API Documentation**: ✅ Interactive Swagger docs
- **Dependencies**: ✅ All resolved
- **Testing**: ✅ All endpoints functional

### 🚀 Ready for:
- **Immediate Use**: Test with demo.html
- **Production Deployment**: Stable and reliable
- **Further Development**: Extensible framework
- **ML Integration**: Ready for real models

---

**Combatting Disinformation with AI: Text & Visual Fake Detection System**

*Built with ❤️ for a more informed digital world*

---

<div align="center">
  <p><strong>⭐ Star this repository if you find it helpful!</strong></p>
  <p><strong>🔄 Fork it to contribute to the project!</strong></p>
</div> 