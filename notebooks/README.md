# Fake News & Deepfake Detection System

🧠 **AI-powered system for detecting fake news and deepfake images/videos with explainable AI**

## 🎯 Project Overview

This project implements a comprehensive fake news and deepfake detection system using advanced machine learning, natural language processing, and computer vision techniques. The system provides explainable AI insights to help users understand why content was flagged as potentially fake.

### Key Features

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
│   ├── api/                # API routes
│   │   └── routes/         # Endpoint definitions
│   ├── utils/              # Utility modules
│   │   ├── text_processor.py    # NLP processing
│   │   ├── image_processor.py   # CV processing
│   │   └── explainability.py    # XAI explanations
│   └── requirements.txt    # Python dependencies
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
└── README.md              # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup

1. **Navigate to backend directory:**
   ```bash
   cd backend
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start the backend server:**
   ```bash
   python main.py
   ```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

## 🔧 Technology Stack

### Backend
- **FastAPI**: High-performance web framework
- **PyTorch**: Deep learning framework
- **Transformers**: HuggingFace NLP models (BERT, RoBERTa)
- **OpenCV**: Computer vision processing
- **TensorFlow/Keras**: Additional ML models
- **SHAP/LIME**: Explainable AI
- **NLTK/Spacy**: Natural language processing

### Frontend
- **React 18**: UI framework
- **TypeScript**: Type safety
- **Tailwind CSS**: Styling
- **Framer Motion**: Animations
- **React Query**: Data fetching
- **React Dropzone**: File uploads
- **Chart.js**: Data visualization

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

## 🧠 Machine Learning Models

### Text Analysis
- **BERT/RoBERTa**: Fine-tuned for fake news detection
- **Sentiment Analysis**: Cardiff NLP Twitter RoBERTa
- **Feature Extraction**: Linguistic patterns, source credibility
- **Explainability**: SHAP values, attention visualization

### Image Analysis
- **XceptionNet**: Pre-trained CNN for deepfake detection
- **Face Detection**: OpenCV Haar cascades + face_recognition
- **Artifact Analysis**: Edge density, color consistency, symmetry
- **Explainability**: Grad-CAM, heatmap visualization

## 📈 Features

### Text Detection
- Source credibility assessment
- Sentiment analysis
- Language pattern detection
- Fact-checking indicators
- Writing style analysis

### Image Detection
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

### Backend Deployment
```bash
# Using Docker
docker build -t fake-news-detector-backend .
docker run -p 8000:8000 fake-news-detector-backend

# Using Heroku
heroku create your-app-name
git push heroku main
```

### Frontend Deployment
```bash
# Build for production
npm run build

# Deploy to Vercel/Netlify
# Upload the build folder to your hosting platform
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

- **Project Link**: [https://github.com/yourusername/fake-news-deepfake-detector](https://github.com/yourusername/fake-news-deepfake-detector)
- **Issues**: [https://github.com/yourusername/fake-news-deepfake-detector/issues](https://github.com/yourusername/fake-news-deepfake-detector/issues)

---

**Combatting Disinformation with AI: Text & Visual Fake Detection System**

*Built with ❤️ for a more informed digital world*