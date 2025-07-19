#!/usr/bin/env python3
"""
Simple script to start the Fake News & Deepfake Detection System
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def print_banner():
    print("=" * 60)
    print("🧠 Fake News & Deepfake Detection System")
    print("   Starting the application...")
    print("=" * 60)

def check_backend():
    """Check if backend is running"""
    try:
        import requests
        response = requests.get("http://localhost:8000/health", timeout=2)
        return response.status_code == 200
    except:
        return False

def start_backend():
    """Start the backend server"""
    print("🚀 Starting Backend Server...")
    
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        return False
    
    # Change to backend directory
    os.chdir(backend_dir)
    
    # Start the server
    try:
        print("📡 Backend server starting on http://localhost:8000")
        print("📚 API Documentation: http://localhost:8000/docs")
        subprocess.run([sys.executable, "main_simple.py"])
    except KeyboardInterrupt:
        print("\n⏹️ Backend server stopped")
    
    return True

def open_demo():
    """Open the demo HTML file"""
    demo_file = Path("demo.html")
    if demo_file.exists():
        print("🌐 Opening frontend demo in browser...")
        webbrowser.open(f"file://{demo_file.absolute()}")
        return True
    else:
        print("❌ Demo file not found!")
        return False

def main():
    print_banner()
    
    # Check if backend is already running
    if check_backend():
        print("✅ Backend is already running!")
    else:
        print("🔧 Backend not running. Starting...")
        start_backend()
    
    # Open demo
    open_demo()
    
    print("\n🎉 Project is ready!")
    print("\n📋 Available URLs:")
    print("   Backend API: http://localhost:8000")
    print("   API Docs: http://localhost:8000/docs")
    print("   Frontend Demo: demo.html (opened in browser)")
    
    print("\n🧪 Test the API:")
    print("   curl http://localhost:8000/health")
    print("   curl http://localhost:8000/api/analysis/dashboard")

if __name__ == "__main__":
    main() 