import React from 'react';
import { motion } from 'framer-motion';
import { Shield, Brain, Eye, Zap, Users, Globe } from 'lucide-react';

const About: React.FC = () => {
  const features = [
    {
      icon: Brain,
      title: 'Advanced AI',
      description: 'State-of-the-art machine learning models for accurate detection'
    },
    {
      icon: Eye,
      title: 'Computer Vision',
      description: 'Deep learning algorithms to detect image and video manipulation'
    },
    {
      icon: Shield,
      title: 'Explainable AI',
      description: 'Transparent explanations of why content was flagged as fake'
    },
    {
      icon: Zap,
      title: 'Real-time Analysis',
      description: 'Fast processing with results in seconds'
    },
    {
      icon: Users,
      title: 'User-friendly',
      description: 'Intuitive interface for easy content analysis'
    },
    {
      icon: Globe,
      title: 'Multi-language',
      description: 'Support for multiple languages and content types'
    }
  ];

  const technologies = [
    'BERT & RoBERTa for NLP',
    'XceptionNet for Computer Vision',
    'SHAP & LIME for Explainability',
    'OpenCV for Image Processing',
    'FastAPI for Backend',
    'React & TypeScript for Frontend'
  ];

  return (
    <div className="max-w-4xl mx-auto space-y-12">
      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="text-center"
      >
        <h1 className="text-4xl font-bold text-gray-900 mb-6">About Our Project</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          We're building the future of content verification with AI-powered fake news and deepfake detection.
          Our mission is to combat misinformation and promote digital literacy.
        </p>
      </motion.div>

      {/* Mission Statement */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.1 }}
        className="card bg-gradient-to-r from-primary-50 to-blue-50"
      >
        <div className="text-center">
          <Shield className="h-12 w-12 text-primary-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Mission</h2>
          <p className="text-lg text-gray-700 leading-relaxed">
            To provide accessible, accurate, and transparent tools for detecting fake news and deepfakes, 
            empowering users to make informed decisions about the content they consume and share online.
          </p>
        </div>
      </motion.div>

      {/* Features Grid */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.2 }}
      >
        <h2 className="text-3xl font-bold text-gray-900 text-center mb-8">Key Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.1 + index * 0.1 }}
                className="card text-center hover:shadow-lg transition-shadow duration-200"
              >
                <Icon className="h-8 w-8 text-primary-600 mx-auto mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </motion.div>
            );
          })}
        </div>
      </motion.div>

      {/* Technology Stack */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.3 }}
        className="card"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Technology Stack</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {technologies.map((tech, index) => (
            <div key={index} className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <div className="w-2 h-2 bg-primary-600 rounded-full"></div>
              <span className="text-gray-700">{tech}</span>
            </div>
          ))}
        </div>
      </motion.div>

      {/* How It Works */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.4 }}
        className="card"
      >
        <h2 className="text-2xl font-bold text-gray-900 mb-6">How It Works</h2>
        <div className="space-y-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold">
              1
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 mb-2">Content Input</h3>
              <p className="text-gray-600">
                Users upload images or paste text content that they want to verify for authenticity.
              </p>
            </div>
          </div>
          
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold">
              2
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 mb-2">AI Analysis</h3>
              <p className="text-gray-600">
                Our advanced machine learning models analyze the content for patterns, artifacts, and inconsistencies.
              </p>
            </div>
          </div>
          
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-primary-600 text-white rounded-full flex items-center justify-center font-bold">
              3
            </div>
            <div>
              <h3 className="font-semibold text-gray-900 mb-2">Explainable Results</h3>
              <p className="text-gray-600">
                Users receive detailed explanations of why content was flagged, with confidence scores and recommendations.
              </p>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Contact/Info */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.5 }}
        className="card bg-gray-50"
      >
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Get Started</h2>
          <p className="text-gray-600 mb-6">
            Ready to start detecting fake news and deepfakes? Try our tools today!
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <button className="btn-primary">
              Try Text Detection
            </button>
            <button className="btn-secondary">
              Try Image Detection
            </button>
          </div>
        </div>
      </motion.div>
    </div>
  );
};

export default About; 