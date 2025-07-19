@echo off
echo 🚀 Starting deployment process...

REM Check if we're in the right directory
if not exist "frontend\package.json" (
    echo ❌ Error: Please run this script from the project root directory
    pause
    exit /b 1
)

REM Navigate to frontend directory
cd frontend

echo 📦 Installing dependencies...
call npm install

if %errorlevel% neq 0 (
    echo ❌ Error: Failed to install dependencies
    pause
    exit /b 1
)

echo 🔨 Building the project...
call npm run build

if %errorlevel% neq 0 (
    echo ❌ Error: Build failed
    pause
    exit /b 1
)

echo ✅ Build completed successfully!
echo.
echo 📁 Your build files are ready in: frontend\build\
echo.
echo 🌐 Next steps for free hosting:
echo 1. Go to netlify.com and sign up (free)
echo 2. Click 'New site from Git'
echo 3. Connect your GitHub account
echo 4. Select this repository
echo 5. Set build command: cd frontend ^&^& npm install ^&^& npm run build
echo 6. Set publish directory: frontend/build
echo 7. Click 'Deploy site'
echo.
echo 🎉 Your website will be live in minutes!
echo.
echo Developed by nikeshsapkota 🚀
pause 