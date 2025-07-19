import React from 'react';
import { motion } from 'framer-motion';
import { BarChart3, TrendingUp, AlertTriangle, CheckCircle } from 'lucide-react';

const Analysis: React.FC = () => {
  return (
    <div className="max-w-6xl mx-auto space-y-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center"
      >
        <h1 className="text-3xl font-bold text-gray-900 mb-4">Analysis Dashboard</h1>
        <p className="text-gray-600">
          Comprehensive analytics and insights from our detection system
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
        className="grid grid-cols-1 lg:grid-cols-2 gap-8"
      >
        {/* Detection Statistics */}
        <div className="card">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Detection Statistics</h2>
          <div className="space-y-4">
            <div className="flex items-center justify-between p-4 bg-gray-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <BarChart3 className="h-5 w-5 text-blue-600" />
                <span className="font-medium">Total Analyses</span>
              </div>
              <span className="text-2xl font-bold text-gray-900">1,250</span>
            </div>
            
            <div className="flex items-center justify-between p-4 bg-red-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <AlertTriangle className="h-5 w-5 text-red-600" />
                <span className="font-medium">Fake Detected</span>
              </div>
              <span className="text-2xl font-bold text-red-600">180</span>
            </div>
            
            <div className="flex items-center justify-between p-4 bg-orange-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <AlertTriangle className="h-5 w-5 text-orange-600" />
                <span className="font-medium">Deepfake Detected</span>
              </div>
              <span className="text-2xl font-bold text-orange-600">45</span>
            </div>
            
            <div className="flex items-center justify-between p-4 bg-green-50 rounded-lg">
              <div className="flex items-center space-x-3">
                <CheckCircle className="h-5 w-5 text-green-600" />
                <span className="font-medium">Accuracy Rate</span>
              </div>
              <span className="text-2xl font-bold text-green-600">92%</span>
            </div>
          </div>
        </div>

        {/* Performance Metrics */}
        <div className="card">
          <h2 className="text-xl font-semibold text-gray-900 mb-6">Performance Metrics</h2>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium text-gray-700">Text Detection Accuracy</span>
                <span className="text-sm font-medium text-gray-900">94%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div className="bg-blue-600 h-2 rounded-full" style={{ width: '94%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium text-gray-700">Image Detection Accuracy</span>
                <span className="text-sm font-medium text-gray-900">89%</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div className="bg-purple-600 h-2 rounded-full" style={{ width: '89%' }}></div>
              </div>
            </div>
            
            <div>
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm font-medium text-gray-700">Average Processing Time</span>
                <span className="text-sm font-medium text-gray-900">2.3s</span>
              </div>
              <div className="w-full bg-gray-200 rounded-full h-2">
                <div className="bg-green-600 h-2 rounded-full" style={{ width: '77%' }}></div>
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Recent Trends */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.2 }}
        className="card"
      >
        <h2 className="text-xl font-semibold text-gray-900 mb-6">Recent Trends</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div className="text-center p-4 bg-blue-50 rounded-lg">
            <TrendingUp className="h-8 w-8 text-blue-600 mx-auto mb-2" />
            <h3 className="font-semibold text-gray-900">Daily Analyses</h3>
            <p className="text-2xl font-bold text-blue-600">45</p>
            <p className="text-sm text-gray-600">+12% from yesterday</p>
          </div>
          
          <div className="text-center p-4 bg-red-50 rounded-lg">
            <AlertTriangle className="h-8 w-8 text-red-600 mx-auto mb-2" />
            <h3 className="font-semibold text-gray-900">Fake Detected Today</h3>
            <p className="text-2xl font-bold text-red-600">8</p>
            <p className="text-sm text-gray-600">+2 from yesterday</p>
          </div>
          
          <div className="text-center p-4 bg-orange-50 rounded-lg">
            <AlertTriangle className="h-8 w-8 text-orange-600 mx-auto mb-2" />
            <h3 className="font-semibold text-gray-900">Deepfakes Today</h3>
            <p className="text-2xl font-bold text-orange-600">2</p>
            <p className="text-sm text-gray-600">-1 from yesterday</p>
          </div>
        </div>
      </motion.div>

      {/* Top Features */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.3 }}
        className="card"
      >
        <h2 className="text-xl font-semibold text-gray-900 mb-6">Detection Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 className="font-medium text-gray-900 mb-3">Text Analysis Features</h3>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Source credibility assessment</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Sentiment analysis</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Language pattern detection</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Fact-checking indicators</span>
              </li>
            </ul>
          </div>
          
          <div>
            <h3 className="font-medium text-gray-900 mb-3">Image Analysis Features</h3>
            <ul className="space-y-2 text-sm text-gray-600">
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Face detection and analysis</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Artifact detection</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Color consistency analysis</span>
              </li>
              <li className="flex items-center space-x-2">
                <CheckCircle className="h-4 w-4 text-green-600" />
                <span>Symmetry and alignment checks</span>
              </li>
            </ul>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default Analysis; 