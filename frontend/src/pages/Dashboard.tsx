import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { Shield, FileText, Image, BarChart3, AlertTriangle, CheckCircle } from 'lucide-react';

const Dashboard: React.FC = () => {
  const stats = [
    {
      title: 'Total Analyses',
      value: '1,250',
      change: '+12%',
      icon: BarChart3,
      color: 'text-blue-600',
      bgColor: 'bg-blue-100'
    },
    {
      title: 'Fake Detected',
      value: '180',
      change: '+8%',
      icon: AlertTriangle,
      color: 'text-red-600',
      bgColor: 'bg-red-100'
    },
    {
      title: 'Deepfake Detected',
      value: '45',
      change: '+15%',
      icon: Image,
      color: 'text-orange-600',
      bgColor: 'bg-orange-100'
    },
    {
      title: 'Accuracy Rate',
      value: '92%',
      change: '+2%',
      icon: CheckCircle,
      color: 'text-green-600',
      bgColor: 'bg-green-100'
    }
  ];

  const quickActions = [
    {
      title: 'Text Detection',
      description: 'Analyze news articles and social media posts',
      icon: FileText,
      path: '/text',
      color: 'bg-blue-500'
    },
    {
      title: 'Image Detection',
      description: 'Detect deepfakes in images and videos',
      icon: Image,
      path: '/image',
      color: 'bg-purple-500'
    },
    {
      title: 'Comprehensive Analysis',
      description: 'Full analysis of text and image content',
      icon: Shield,
      path: '/analysis',
      color: 'bg-green-500'
    }
  ];

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-900 mb-4">
          AI-Powered Fake News & Deepfake Detection
        </h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Combat misinformation with our advanced machine learning system. 
          Analyze text and images with explainable AI insights.
        </p>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => {
          const Icon = stat.icon;
          return (
            <div key={index} className="card">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                  <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
                  <p className="text-sm text-green-600">{stat.change} from last month</p>
                </div>
                <div className={`p-3 rounded-lg ${stat.bgColor}`}>
                  <Icon className={`h-6 w-6 ${stat.color}`} />
                </div>
              </div>
            </div>
          );
        })}
      </div>

      {/* Quick Actions */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Quick Actions</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {quickActions.map((action, index) => {
            const Icon = action.icon;
            return (
              <Link
                key={index}
                to={action.path}
                className="card hover:shadow-lg transition-shadow duration-200 group"
              >
                <div className="flex items-center space-x-4">
                  <div className={`p-3 rounded-lg ${action.color} text-white group-hover:scale-110 transition-transform duration-200`}>
                    <Icon className="h-6 w-6" />
                  </div>
                  <div>
                    <h3 className="text-lg font-semibold text-gray-900">{action.title}</h3>
                    <p className="text-gray-600">{action.description}</p>
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
      </div>

      {/* Recent Activity */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900 mb-6">Recent Activity</h2>
        <div className="card">
          <div className="space-y-4">
            {[
              { type: 'text', result: 'fake', confidence: 0.85, time: '2 minutes ago' },
              { type: 'image', result: 'deepfake', confidence: 0.78, time: '5 minutes ago' },
              { type: 'text', result: 'real', confidence: 0.92, time: '10 minutes ago' },
              { type: 'image', result: 'real', confidence: 0.88, time: '15 minutes ago' }
            ].map((activity, index) => (
              <div key={index} className="flex items-center justify-between py-3 border-b border-gray-100 last:border-b-0">
                <div className="flex items-center space-x-3">
                  <div className={`p-2 rounded-lg ${
                    activity.result === 'fake' || activity.result === 'deepfake' 
                      ? 'bg-red-100 text-red-600' 
                      : 'bg-green-100 text-green-600'
                  }`}>
                    {activity.type === 'text' ? <FileText className="h-4 w-4" /> : <Image className="h-4 w-4" />}
                  </div>
                  <div>
                    <p className="font-medium text-gray-900">
                      {activity.type === 'text' ? 'Text Analysis' : 'Image Analysis'}
                    </p>
                    <p className="text-sm text-gray-600">
                      Detected as {activity.result} ({Math.round(activity.confidence * 100)}% confidence)
                    </p>
                  </div>
                </div>
                <span className="text-sm text-gray-500">{activity.time}</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard; 