#!/usr/bin/env python3
"""
Fake News & Deepfake Detection System - Complete Setup and Run Script
This script sets up the entire project, downloads datasets, and runs the application.
"""

import os
import sys
import subprocess
import json
from pathlib import Path

def print_banner():
    """Print project banner"""
    print("=" * 80)
    print("🧠 Fake News & Deepfake Detection System")
    print("   AI-powered system with Explainable AI")
    print("=" * 80)

def check_prerequisites():
    """Check if required software is installed"""
    print("🔍 Checking prerequisites...")
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        return False
    
    # Check Node.js
    try:
        result = subprocess.run(['node', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Node.js is not installed")
            return False
        print(f"✅ Node.js version: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ Node.js is not installed")
        return False
    
    # Check npm
    try:
        result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ npm is not installed")
            return False
        print(f"✅ npm version: {result.stdout.strip()}")
    except FileNotFoundError:
        print("❌ npm is not installed")
        return False
    
    print("✅ All prerequisites are satisfied!")
    return True

def setup_backend():
    """Setup the backend"""
    print("\n🔧 Setting up backend...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return False
    
    # Create virtual environment
    venv_dir = backend_dir / "venv"
    if not venv_dir.exists():
        print("📦 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], cwd=backend_dir)
    
    # Determine activation script
    if os.name == 'nt':  # Windows
        python_path = venv_dir / "Scripts" / "python.exe"
        pip_path = venv_dir / "Scripts" / "pip.exe"
    else:  # Unix/Linux/Mac
        python_path = venv_dir / "bin" / "python"
        pip_path = venv_dir / "bin" / "pip"
    
    # Install dependencies
    print("📦 Installing Python dependencies...")
    requirements_file = backend_dir / "requirements.txt"
    if requirements_file.exists():
        subprocess.run([str(pip_path), "install", "-r", str(requirements_file)])
        print("✅ Backend dependencies installed")
    else:
        print("❌ requirements.txt not found")
        return False
    
    return True

def setup_frontend():
    """Setup the frontend"""
    print("\n🎨 Setting up frontend...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found")
        return False
    
    # Install npm dependencies
    print("📦 Installing Node.js dependencies...")
    package_json = frontend_dir / "package.json"
    if package_json.exists():
        subprocess.run(["npm", "install"], cwd=frontend_dir)
        print("✅ Frontend dependencies installed")
    else:
        print("❌ package.json not found")
        return False
    
    return True

def create_sample_data():
    """Create sample data for testing"""
    print("\n📝 Creating sample data for testing...")
    
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Sample fake news data
    fake_data = {
        'text': [
            'BREAKING: You won\'t believe what happened next! Shocking revelation!',
            'Anonymous insider reveals shocking conspiracy theory!',
            'Viral video shows amazing transformation that doctors hate!',
            'This unbelievable story will blow your mind!',
            'Secret information that they don\'t want you to know!'
        ],
        'subject': ['fake_news'] * 5,
        'date': ['2024-01-15'] * 5
    }
    
    # Sample real news data
    real_data = {
        'text': [
            'This is a credible news article with factual information and proper sources.',
            'According to official government sources, the event occurred yesterday.',
            'The study published in Nature journal shows significant findings.',
            'Research conducted by Harvard University reveals important data.',
            'Official statement from the White House regarding the policy change.'
        ],
        'subject': ['real_news'] * 5,
        'date': ['2024-01-15'] * 5
    }
    
    # Save sample data
    import pandas as pd
    
    fake_df = pd.DataFrame(fake_data)
    real_df = pd.DataFrame(real_data)
    
    fake_df.to_csv(data_dir / "Fake.csv", index=False)
    real_df.to_csv(data_dir / "True.csv", index=False)
    
    print("✅ Sample data created")

def create_sample_models():
    """Create sample models for testing"""
    print("\n🤖 Creating sample models...")
    
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    # Create sample model metadata
    model_metadata = {
        'text_classifier': {
            'type': 'bert',
            'accuracy': 0.92,
            'model_path': 'bert_fake_news_model',
            'version': '1.0.0',
            'training_date': '2024-01-15'
        },
        'image_classifier': {
            'type': 'xception',
            'accuracy': 0.89,
            'model_path': 'xception_deepfake_model',
            'version': '1.0.0',
            'training_date': '2024-01-15'
        }
    }
    
    metadata_file = models_dir / "model_metadata.json"
    with open(metadata_file, 'w') as f:
        json.dump(model_metadata, f, indent=2)
    
    print("✅ Sample models created")

def start_backend():
    """Start the backend server"""
    print("\n🚀 Starting backend server...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found")
        return False
    
    # Determine Python path
    venv_dir = backend_dir / "venv"
    if os.name == 'nt':  # Windows
        python_path = venv_dir / "Scripts" / "python.exe"
    else:  # Unix/Linux/Mac
        python_path = venv_dir / "bin" / "python"
    
    if not python_path.exists():
        print("❌ Virtual environment not found. Please run setup first.")
        return False
    
    try:
        print("🌐 Backend server starting on http://localhost:8000")
        print("📚 API documentation will be available at http://localhost:8000/docs")
        subprocess.run([str(python_path), "main.py"], cwd=backend_dir)
    except KeyboardInterrupt:
        print("\n⏹️  Backend server stopped")
    
    return True

def start_frontend():
    """Start the frontend development server"""
    print("\n🎨 Starting frontend development server...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found")
        return False
    
    try:
        print("🌐 Frontend server starting on http://localhost:3000")
        subprocess.run(["npm", "start"], cwd=frontend_dir)
    except KeyboardInterrupt:
        print("\n⏹️  Frontend server stopped")
    
    return True

def main():
    """Main function"""
    print_banner()
    
    # Check prerequisites
    if not check_prerequisites():
        print("\n❌ Prerequisites not met. Please install required software.")
        return
    
    # Setup backend
    if not setup_backend():
        print("\n❌ Backend setup failed.")
        return
    
    # Setup frontend
    if not setup_frontend():
        print("\n❌ Frontend setup failed.")
        return
    
    # Create sample data
    create_sample_data()
    
    # Create sample models
    create_sample_models()
    
    # Show next steps
    print("\n🎉 Setup complete!")
    print("\n📋 Next steps:")
    print("  1. Start backend: python run_project.py --backend")
    print("  2. Start frontend: python run_project.py --frontend")
    print("  3. Run training: python run_project.py --train")
    print("  4. Run both: python run_project.py --run")
    
    # Check command line arguments
    if len(sys.argv) > 1:
        if "--backend" in sys.argv:
            start_backend()
        elif "--frontend" in sys.argv:
            start_frontend()
        elif "--train" in sys.argv:
            print("\n📓 To run training:")
            print("  1. Install Jupyter: pip install jupyter")
            print("  2. Start Jupyter: jupyter notebook")
            print("  3. Open: notebooks/model_training_with_kaggle.ipynb")
        elif "--run" in sys.argv:
            print("\n🚀 Starting both servers...")
            print("⚠️  This will open two terminal windows")
            print("   Backend: http://localhost:8000")
            print("   Frontend: http://localhost:3000")
            
            # Start backend in background
            import threading
            backend_thread = threading.Thread(target=start_backend)
            backend_thread.daemon = True
            backend_thread.start()
            
            # Start frontend
            start_frontend()

if __name__ == "__main__":
    # Import pandas for sample data creation
    try:
        import pandas as pd
    except ImportError:
        print("❌ pandas is required. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pandas"])
        import pandas as pd
    
    main() 