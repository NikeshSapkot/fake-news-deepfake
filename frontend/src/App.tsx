import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import TextDetection from './pages/TextDetection';
import ImageDetection from './pages/ImageDetection';
import Analysis from './pages/Analysis';
import About from './pages/About';

const App: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50 flex flex-col">
      <Header />
      <main className="w-full max-w-7xl mx-auto px-4 py-8 flex-grow">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/text" element={<TextDetection />} />
          <Route path="/image" element={<ImageDetection />} />
          <Route path="/analysis" element={<Analysis />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={
            <div className="text-center py-12">
              <h1 className="text-2xl font-bold text-gray-900 mb-4">Page Not Found</h1>
              <p className="text-gray-600 mb-6">The page you're looking for doesn't exist.</p>
              <Link to="/" className="btn-primary">
                Go to Dashboard
              </Link>
            </div>
          } />
        </Routes>
      </main>
      <Footer />
    </div>
  );
};

export default App; 