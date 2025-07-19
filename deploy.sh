#!/bin/bash

echo "🚀 Starting deployment process..."

# Check if we're in the right directory
if [ ! -f "frontend/package.json" ]; then
    echo "❌ Error: Please run this script from the project root directory"
    exit 1
fi

# Navigate to frontend directory
cd frontend

echo "📦 Installing dependencies..."
npm install

if [ $? -ne 0 ]; then
    echo "❌ Error: Failed to install dependencies"
    exit 1
fi

echo "🔨 Building the project..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Error: Build failed"
    exit 1
fi

echo "✅ Build completed successfully!"
echo ""
echo "📁 Your build files are ready in: frontend/build/"
echo ""
echo "🌐 Next steps for free hosting:"
echo "1. Go to netlify.com and sign up (free)"
echo "2. Click 'New site from Git'"
echo "3. Connect your GitHub account"
echo "4. Select this repository"
echo "5. Set build command: cd frontend && npm install && npm run build"
echo "6. Set publish directory: frontend/build"
echo "7. Click 'Deploy site'"
echo ""
echo "🎉 Your website will be live in minutes!"
echo ""
echo "Developed by nikeshsapkota 🚀" 