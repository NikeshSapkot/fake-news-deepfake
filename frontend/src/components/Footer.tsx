import React from 'react';
import { Link } from 'react-router-dom';
import { Shield, Github, Linkedin, Mail } from 'lucide-react';

const Footer: React.FC = () => {
  return (
    <footer className="bg-gray-900 text-white mt-16">
      <div className="w-full max-w-7xl mx-auto px-4 py-12">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
          {/* Brand Section */}
          <div className="col-span-1 md:col-span-2">
            <div className="flex items-center space-x-2 mb-4">
              <Shield className="h-8 w-8 text-blue-400" />
              <span className="text-xl font-bold">Fake News & Deepfake Detector</span>
            </div>
            <p className="text-gray-300 mb-4 max-w-md">
              Advanced AI-powered tools for detecting fake news and deepfakes. 
              Empowering users to make informed decisions about the content they consume and share online.
            </p>
            <div className="flex space-x-4">
              <a 
                href="https://github.com/NikeshSapkot" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
                aria-label="GitHub Profile"
              >
                <Github className="h-5 w-5" />
              </a>
              <a 
                href="https://linkedin.com/in/nikeshsapkota" 
                target="_blank" 
                rel="noopener noreferrer"
                className="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
                aria-label="LinkedIn Profile"
              >
                <Linkedin className="h-5 w-5" />
              </a>
              <a 
                href="mailto:nikeshsapkota.code@gmail.com" 
                className="text-gray-400 hover:text-white transition-all duration-300 hover:scale-110"
                aria-label="Email Contact"
              >
                <Mail className="h-5 w-5" />
              </a>
            </div>
          </div>

          {/* Quick Links */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <Link to="/" className="text-gray-300 hover:text-white transition-colors duration-200 hover:translate-x-1 inline-block">
                  Dashboard
                </Link>
              </li>
              <li>
                <Link to="/text" className="text-gray-300 hover:text-white transition-colors duration-200 hover:translate-x-1 inline-block">
                  Text Detection
                </Link>
              </li>
              <li>
                <Link to="/image" className="text-gray-300 hover:text-white transition-colors duration-200 hover:translate-x-1 inline-block">
                  Image Detection
                </Link>
              </li>
              <li>
                <Link to="/analysis" className="text-gray-300 hover:text-white transition-colors duration-200 hover:translate-x-1 inline-block">
                  Analysis
                </Link>
              </li>
              <li>
                <Link to="/about" className="text-gray-300 hover:text-white transition-colors duration-200 hover:translate-x-1 inline-block">
                  About
                </Link>
              </li>
            </ul>
          </div>

          {/* Contact Info */}
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact</h3>
            <ul className="space-y-2 text-gray-300">
              <li className="hover:text-white transition-colors duration-200">Email: nikesh.sapkota@example.com</li>
              <li className="hover:text-white transition-colors duration-200">GitHub: github.com/NikeshSapkot</li>
              <li className="hover:text-white transition-colors duration-200">LinkedIn: linkedin.com/in/nikeshsapkota</li>
            </ul>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-gray-800 mt-8 pt-8 flex flex-col md:flex-row justify-between items-center">
          <p className="text-gray-400 text-sm">
            © 2024 Fake News & Deepfake Detector. All rights reserved.
          </p>
          <p className="text-gray-400 text-sm mt-2 md:mt-0">
            Developed by <span className="text-blue-400 font-semibold hover:text-blue-300 transition-colors duration-200">nikeshsapkota</span>
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer; 