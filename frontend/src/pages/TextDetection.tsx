import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { FileText, Send, AlertTriangle, CheckCircle } from 'lucide-react';

const TextDetection: React.FC = () => {
  const [text, setText] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<any>(null);

  const handleAnalyze = async () => {
    if (!text.trim()) return;
    
    setIsAnalyzing(true);
    try {
      const response = await fetch('/api/text/detect', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text, language: 'en' }),
      });
      
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error analyzing text:', error);
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
        <h1 className="text-3xl font-bold text-gray-900 mb-4">Text Detection</h1>
        <p className="text-gray-600">
          Analyze news articles, social media posts, and other text content for fake news detection
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
        className="card"
      >
        <div className="space-y-4">
          <div>
            <label htmlFor="text-input" className="block text-sm font-medium text-gray-700 mb-2">
              Enter text to analyze
            </label>
            <textarea
              id="text-input"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Paste your text here... (news articles, social media posts, etc.)"
              className="input-field h-32 resize-none"
              disabled={isAnalyzing}
            />
          </div>
          
          <button
            onClick={handleAnalyze}
            disabled={!text.trim() || isAnalyzing}
            className="btn-primary w-full flex items-center justify-center space-x-2 disabled:opacity-50"
          >
            {isAnalyzing ? (
              <>
                <div className="loading-spinner"></div>
                <span>Analyzing...</span>
              </>
            ) : (
              <>
                <Send className="h-4 w-4" />
                <span>Analyze Text</span>
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
              {result.is_fake ? (
                <AlertTriangle className="h-8 w-8 text-red-600" />
              ) : (
                <CheckCircle className="h-8 w-8 text-green-600" />
              )}
              <div>
                <h3 className="text-xl font-semibold text-gray-900">
                  {result.is_fake ? 'Fake News Detected' : 'Content Appears Authentic'}
                </h3>
                <p className="text-gray-600">
                  Confidence: {Math.round(result.confidence * 100)}%
                </p>
              </div>
            </div>

            {result.explanation && (
              <div className="space-y-4">
                <h4 className="text-lg font-medium text-gray-900">Analysis Details</h4>
                
                {result.explanation.key_factors && result.explanation.key_factors.length > 0 && (
                  <div>
                    <h5 className="font-medium text-gray-700 mb-2">Key Factors:</h5>
                    <ul className="list-disc list-inside space-y-1 text-gray-600">
                      {result.explanation.key_factors.map((factor: string, index: number) => (
                        <li key={index}>{factor}</li>
                      ))}
                    </ul>
                  </div>
                )}

                {result.explanation.recommendations && result.explanation.recommendations.length > 0 && (
                  <div>
                    <h5 className="font-medium text-gray-700 mb-2">Recommendations:</h5>
                    <ul className="list-disc list-inside space-y-1 text-gray-600">
                      {result.explanation.recommendations.map((rec: string, index: number) => (
                        <li key={index}>{rec}</li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            )}
          </div>
        </motion.div>
      )}
    </div>
  );
};

export default TextDetection; 