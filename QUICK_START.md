# 🚀 Quick Start Guide

## Prerequisites

- **Python 3.8+**
- **Node.js 16+**
- **npm or yarn**

## 🎯 One-Click Setup

### Option 1: Automated Setup (Recommended)

```bash
# Run the automated setup script
python run_project.py
```

This will:
- ✅ Check prerequisites
- ✅ Setup backend with virtual environment
- ✅ Install all Python dependencies
- ✅ Setup frontend with npm dependencies
- ✅ Create sample data and models
- ✅ Provide next steps

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend
python -m venv venv
# On Windows: venv\Scripts\activate
# On Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
python main.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 🏃‍♂️ Running the Application

### Start Backend Only
```bash
python run_project.py --backend
```
- 🌐 Server: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs

### Start Frontend Only
```bash
python run_project.py --frontend
```
- 🌐 App: http://localhost:3000

### Start Both (Full Stack)
```bash
python run_project.py --run
```
- 🌐 Frontend: http://localhost:3000
- 🌐 Backend: http://localhost:8000

## 📊 Training Models with Real Datasets

### 1. Download Datasets

**Fake News Datasets:**
- [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
- [LIAR Dataset](https://www.kaggle.com/datasets/ruchi798/liar-dataset)

**Deepfake Datasets:**
- [DeepFake Detection Challenge](https://www.kaggle.com/c/deepfake-detection-challenge)
- [FaceForensics++](https://github.com/ondyari/FaceForensics)

### 2. Run Training

```bash
# Install Jupyter
pip install jupyter

# Start Jupyter
jupyter notebook

# Open the training notebook
notebooks/model_training_with_kaggle.ipynb
```

### 3. Dataset Structure

Place downloaded datasets in the `data/` directory:

```
data/
├── Fake.csv          # Fake news articles
├── True.csv          # Real news articles
├── liar_dataset/     # LIAR dataset
└── deepfake/         # Deepfake images/videos
```

## 🧪 Testing the Application

### Text Analysis
1. Go to http://localhost:3000/text
2. Paste a news article or social media post
3. Click "Analyze Text"
4. View results with explanations

### Image Analysis
1. Go to http://localhost:3000/image
2. Upload an image
3. Click "Analyze Image"
4. View deepfake detection results

### Dashboard
1. Go to http://localhost:3000
2. View real-time statistics
3. Check recent analyses

## 🔧 API Testing

### Test Backend API
```bash
# Health check
curl http://localhost:8000/health

# Text analysis
curl -X POST http://localhost:8000/api/text/detect \
  -H "Content-Type: application/json" \
  -d '{"text": "Your news article here", "language": "en"}'

# Image analysis
curl -X POST http://localhost:8000/api/image/detect \
  -F "file=@your_image.jpg"
```

### API Documentation
Visit http://localhost:8000/docs for interactive API documentation.

## 🐳 Docker Deployment

### Quick Docker Setup
```bash
# Build and run with Docker Compose
docker-compose up --build

# Access the application
# Frontend: http://localhost:3000
# Backend: http://localhost:8000
```

### Manual Docker Build
```bash
# Backend only
docker build -t fake-news-backend .
docker run -p 8000:8000 fake-news-backend

# Frontend only
cd frontend
docker build -t fake-news-frontend .
docker run -p 3000:80 fake-news-frontend
```

## 📁 Project Structure

```
fake-news-deepfake-detector/
├── backend/                 # FastAPI backend
│   ├── main.py             # Main application
│   ├── api/routes/         # API endpoints
│   ├── utils/              # ML processing
│   └── requirements.txt    # Python dependencies
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # UI components
│   │   ├── pages/          # Page components
│   │   └── App.tsx         # Main app
│   ├── package.json        # Node.js dependencies
│   └── tailwind.config.js  # Styling config
├── data/                   # Datasets
├── models/                 # Trained models
├── notebooks/              # Training notebooks
├── run_project.py          # Setup script
├── docker-compose.yml      # Docker setup
└── README.md              # Full documentation
```

## 🎯 Features Available

### ✅ Working Features
- **Text Analysis**: Fake news detection with NLP
- **Image Analysis**: Deepfake detection with CV
- **Explainable AI**: SHAP, LIME, visualizations
- **Real-time Dashboard**: Analytics and insights
- **Modern UI**: Responsive design with animations
- **API Documentation**: Interactive Swagger docs
- **Docker Support**: Containerized deployment

### 🔄 In Development
- **Video Analysis**: Deepfake detection in videos
- **Real-time Processing**: Live content analysis
- **Model Versioning**: A/B testing capabilities
- **Advanced XAI**: More sophisticated explanations

## 🚨 Troubleshooting

### Common Issues

**Backend won't start:**
```bash
# Check Python version
python --version

# Reinstall dependencies
cd backend
pip install -r requirements.txt --force-reinstall
```

**Frontend won't start:**
```bash
# Clear npm cache
npm cache clean --force

# Reinstall dependencies
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Port already in use:**
```bash
# Kill processes on ports
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

### Getting Help

1. **Check logs** in the terminal
2. **Visit API docs** at http://localhost:8000/docs
3. **Check browser console** for frontend errors
4. **Verify file paths** and permissions

## 🎉 Success!

Once everything is running:

1. **Frontend**: http://localhost:3000
2. **Backend API**: http://localhost:8000
3. **API Docs**: http://localhost:8000/docs

### Test the System

1. **Try text analysis** with sample news articles
2. **Upload images** to test deepfake detection
3. **Explore the dashboard** for analytics
4. **Check the API documentation** for endpoints

### Next Steps

1. **Train models** with real datasets
2. **Customize the UI** for your needs
3. **Deploy to production** using Docker
4. **Add more features** like video analysis

---

**🎯 Ready to combat misinformation with AI!** 