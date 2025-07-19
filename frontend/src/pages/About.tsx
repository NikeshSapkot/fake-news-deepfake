import React from 'react';
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
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">About Our Project</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          We're building the future of content verification with AI-powered fake news and deepfake detection.
          Our mission is to combat misinformation and promote digital literacy.
        </p>
      </div>

      {/* Mission Statement */}
      <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="text-center">
          <Shield className="h-12 w-12 text-blue-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Our Mission</h2>
          <p className="text-lg text-gray-700 leading-relaxed">
            To provide accessible, accurate, and transparent tools for detecting fake news and deepfakes, 
            empowering users to make informed decisions about the content they consume and share online.
          </p>
        </div>
      </div>

      {/* Features Grid */}
      <div>
        <h2 className="text-3xl font-bold text-gray-900 text-center mb-8">Key Features</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature, index) => {
            const Icon = feature.icon;
            return (
              <div
                key={index}
                className="bg-white rounded-xl shadow-sm border border-gray-200 p-6 text-center hover:shadow-lg transition-shadow duration-200"
              >
                <Icon className="h-8 w-8 text-blue-600 mx-auto mb-4" />
                <h3 className="text-lg font-semibold text-gray-900 mb-2">{feature.title}</h3>
                <p className="text-gray-600">{feature.description}</p>
              </div>
            );
          })}
        </div>
      </div>

      {/* Technology Stack */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Technology Stack</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {technologies.map((tech, index) => (
            <div key={index} className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
              <div className="w-2 h-2 bg-blue-600 rounded-full"></div>
              <span className="text-gray-700">{tech}</span>
            </div>
          ))}
        </div>
      </div>

      {/* How It Works */}
      <div className="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
        <h2 className="text-2xl font-bold text-gray-900 mb-6">How It Works</h2>
        <div className="space-y-6">
          <div className="flex items-start space-x-4">
            <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
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
            <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
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
            <div className="flex-shrink-0 w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center font-bold">
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
      </div>

      {/* Developer Info */}
      <div className="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl shadow-sm border border-gray-200 p-6">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 mb-4">About the Developer</h2>
          <div className="flex items-center justify-center mb-4">
            <div className="w-20 h-20 bg-blue-600 rounded-full flex items-center justify-center text-white text-2xl font-bold">
              NS
            </div>
          </div>
          <h3 className="text-xl font-semibold text-gray-900 mb-2">Nikesh Sapkota</h3>
          <p className="text-gray-600 mb-4 max-w-3xl mx-auto leading-relaxed">
            A passionate developer with a strong interest in Machine Learning, AI, and full-stack web development. 
            I specialize in building responsive, modern web applications using React, Tailwind CSS, and rich UI animations. 
            On the backend, I work with Node.js and Express.js to create robust APIs and scalable architectures.
          </p>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm text-gray-500 mb-6">
            <span>• Full Stack Developer</span>
            <span>• Machine Learning Engineer</span>
            <span>• AI/ML Enthusiast</span>
          </div>
          
          <div className="bg-white rounded-lg p-4 mb-6">
            <h4 className="font-semibold text-gray-900 mb-3">Notable Projects:</h4>
            <ul className="text-left space-y-2 text-gray-600">
              <li>• Cancer detection system using machine learning</li>
              <li>• Mental health analysis platform using NLP and BERT</li>
              <li>• Food management system for restaurants</li>
              <li>• Fake News & Deepfake Detection (Current Project)</li>
            </ul>
          </div>
          
          <p className="text-gray-600 italic">
            "I enjoy blending functionality with elegant design, focusing on clean, minimalist interfaces with powerful features. 
            I'm continuously exploring new technologies and love solving real-world problems through code."
          </p>
        </div>
      </div>

      {/* Contact/Info */}
      <div className="bg-gray-50 rounded-xl shadow-sm border border-gray-200 p-6">
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
      </div>
    </div>
  );
};

export default About; 