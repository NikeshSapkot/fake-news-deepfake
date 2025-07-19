import React, { useState, useCallback } from 'react';
import { motion } from 'framer-motion';
import { useDropzone } from 'react-dropzone';
import { Image, Upload, AlertTriangle, CheckCircle } from 'lucide-react';

const ImageDetection: React.FC = () => {
  const [uploadedImage, setUploadedImage] = useState<File | null>(null);
  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<any>(null);

  const onDrop = useCallback((acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (file) {
      setUploadedImage(file);
      const reader = new FileReader();
      reader.onload = () => {
        setImagePreview(reader.result as string);
      };
      reader.readAsDataURL(file);
    }
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.jpeg', '.jpg', '.png', '.gif', '.bmp']
    },
    multiple: false
  });

  const handleAnalyze = async () => {
    if (!uploadedImage) return;
    
    setIsAnalyzing(true);
    try {
      const formData = new FormData();
      formData.append('file', uploadedImage);
      formData.append('analyze_faces', 'true');
      
      const response = await fetch('/api/image/detect', {
        method: 'POST',
        body: formData,
      });
      
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error analyzing image:', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto space-y-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center"
      >
        <h1 className="text-3xl font-bold text-gray-900 mb-4">Image Detection</h1>
        <p className="text-gray-600">
          Upload images to detect deepfakes and digital manipulation
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
        className="card"
      >
        <div className="space-y-6">
          <div
            {...getRootProps()}
            className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
              isDragActive
                ? 'border-primary-500 bg-primary-50'
                : 'border-gray-300 hover:border-primary-400'
            }`}
          >
            <input {...getInputProps()} />
            <Upload className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            {isDragActive ? (
              <p className="text-primary-600">Drop the image here...</p>
            ) : (
              <div>
                <p className="text-gray-600 mb-2">
                  Drag & drop an image here, or click to select
                </p>
                <p className="text-sm text-gray-500">
                  Supports: JPEG, PNG, GIF, BMP
                </p>
              </div>
            )}
          </div>

          {imagePreview && (
            <div className="text-center">
              <img
                src={imagePreview}
                alt="Preview"
                className="max-w-full h-64 object-contain mx-auto rounded-lg border"
              />
            </div>
          )}

          <button
            onClick={handleAnalyze}
            disabled={!uploadedImage || isAnalyzing}
            className="btn-primary w-full flex items-center justify-center space-x-2 disabled:opacity-50"
          >
            {isAnalyzing ? (
              <>
                <div className="loading-spinner"></div>
                <span>Analyzing...</span>
              </>
            ) : (
              <>
                <Image className="h-4 w-4" />
                <span>Analyze Image</span>
              </>
            )}
          </button>
        </div>
      </motion.div>

      {result && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="card"
        >
          <div className="space-y-6">
            <div className="flex items-center space-x-3">
              {result.is_deepfake ? (
                <AlertTriangle className="h-8 w-8 text-red-600" />
              ) : (
                <CheckCircle className="h-8 w-8 text-green-600" />
              )}
              <div>
                <h3 className="text-xl font-semibold text-gray-900">
                  {result.is_deepfake ? 'Deepfake Detected' : 'Image Appears Authentic'}
                </h3>
                <p className="text-gray-600">
                  Confidence: {Math.round(result.confidence * 100)}%
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Image Analysis</h4>
                <ul className="space-y-1 text-sm text-gray-600">
                  <li>Face detected: {result.face_detected ? 'Yes' : 'No'}</li>
                  {result.face_count && <li>Faces found: {result.face_count}</li>}
                  <li>Processing time: {result.processing_time.toFixed(2)}s</li>
                </ul>
              </div>

              {result.explanation && result.explanation.key_factors && (
                <div>
                  <h4 className="font-medium text-gray-700 mb-2">Key Factors</h4>
                  <ul className="space-y-1 text-sm text-gray-600">
                    {result.explanation.key_factors.map((factor: string, index: number) => (
                      <li key={index}>• {factor}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>

            {result.explanation && result.explanation.recommendations && (
              <div>
                <h4 className="font-medium text-gray-700 mb-2">Recommendations</h4>
                <ul className="list-disc list-inside space-y-1 text-sm text-gray-600">
                  {result.explanation.recommendations.map((rec: string, index: number) => (
                    <li key={index}>{rec}</li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        </motion.div>
      )}
    </div>
  );
};

export default ImageDetection; 