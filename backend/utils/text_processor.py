import time
import re
import numpy as np
from typing import Dict, List, Optional
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        """Initialize the text processor with NLP models"""
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Initialize BERT model for fake news detection
        try:
            self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
            self.model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)
            self.model.to(self.device)
        except:
            # Fallback to a simpler model if BERT is not available
            self.model = None
            self.tokenizer = None
        
        # Initialize sentiment analysis pipeline
        try:
            self.sentiment_analyzer = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment-latest")
        except:
            self.sentiment_analyzer = None
        
        # Load stopwords
        self.stop_words = set(stopwords.words('english'))
        
        # Fake news indicators
        self.fake_indicators = [
            'fake', 'hoax', 'conspiracy', 'unverified', 'rumor', 'allegedly',
            'supposedly', 'claimed', 'anonymous source', 'insider', 'exclusive',
            'breaking', 'shocking', 'you won\'t believe', 'doctors hate',
            'clickbait', 'viral', 'trending', 'must see', 'amazing'
        ]
        
        # Credible source indicators
        self.credible_indicators = [
            'study', 'research', 'official', 'government', 'university',
            'peer-reviewed', 'journal', 'published', 'verified', 'confirmed',
            'fact-checked', 'reliable', 'credible', 'expert', 'scientist'
        ]

    def preprocess_text(self, text: str) -> str:
        """Preprocess text for analysis"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and extra whitespace
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text

    def extract_features(self, text: str) -> Dict:
        """Extract linguistic and semantic features from text"""
        features = {}
        
        # Basic text statistics
        features['length'] = len(text)
        features['word_count'] = len(text.split())
        features['avg_word_length'] = np.mean([len(word) for word in text.split()]) if text.split() else 0
        
        # Sentiment analysis
        if self.sentiment_analyzer:
            try:
                sentiment = self.sentiment_analyzer(text[:512])[0]
                features['sentiment'] = sentiment['label']
                features['sentiment_score'] = sentiment['score']
            except:
                features['sentiment'] = 'neutral'
                features['sentiment_score'] = 0.5
        else:
            # Fallback sentiment analysis
            blob = TextBlob(text)
            features['sentiment'] = 'positive' if blob.sentiment.polarity > 0 else 'negative' if blob.sentiment.polarity < 0 else 'neutral'
            features['sentiment_score'] = abs(blob.sentiment.polarity)
        
        # Fake news indicators
        fake_count = sum(1 for indicator in self.fake_indicators if indicator in text.lower())
        features['fake_indicators'] = fake_count
        
        # Credible source indicators
        credible_count = sum(1 for indicator in self.credible_indicators if indicator in text.lower())
        features['credible_indicators'] = credible_count
        
        # Exclamation marks and caps
        features['exclamation_count'] = text.count('!')
        features['caps_ratio'] = sum(1 for c in text if c.isupper()) / len(text) if text else 0
        
        return features

    def predict(self, text: str, language: str = "en") -> Dict:
        """Predict whether text is fake news"""
        start_time = time.time()
        
        # Preprocess text
        processed_text = self.preprocess_text(text)
        
        # Extract features
        features = self.extract_features(processed_text)
        
        # Simple rule-based prediction (fallback)
        fake_score = 0.0
        
        # Adjust score based on features
        if features['fake_indicators'] > 0:
            fake_score += 0.3 * features['fake_indicators']
        
        if features['credible_indicators'] > 0:
            fake_score -= 0.2 * features['credible_indicators']
        
        if features['exclamation_count'] > 2:
            fake_score += 0.1
        
        if features['caps_ratio'] > 0.3:
            fake_score += 0.1
        
        # Normalize score
        fake_score = max(0.0, min(1.0, fake_score))
        
        # Use BERT model if available
        if self.model and self.tokenizer:
            try:
                inputs = self.tokenizer(processed_text[:512], return_tensors="pt", truncation=True, padding=True)
                inputs = {k: v.to(self.device) for k, v in inputs.items()}
                
                with torch.no_grad():
                    outputs = self.model(**inputs)
                    probabilities = torch.softmax(outputs.logits, dim=1)
                    fake_score = probabilities[0][1].item()
            except Exception as e:
                print(f"BERT prediction failed: {e}")
        
        processing_time = time.time() - start_time
        
        return {
            "is_fake": fake_score > 0.5,
            "confidence": fake_score if fake_score > 0.5 else 1 - fake_score,
            "fake_score": fake_score,
            "features": list(features.keys()),
            "processing_time": processing_time,
            "text_length": len(text)
        }

    def get_feature_importance(self, text: str) -> Dict:
        """Get importance of different features in the prediction"""
        features = self.extract_features(text)
        
        importance = {}
        for feature, value in features.items():
            if feature == 'fake_indicators':
                importance[feature] = value * 0.3
            elif feature == 'credible_indicators':
                importance[feature] = -value * 0.2
            elif feature == 'exclamation_count':
                importance[feature] = value * 0.1 if value > 2 else 0
            elif feature == 'caps_ratio':
                importance[feature] = value * 0.1 if value > 0.3 else 0
            else:
                importance[feature] = 0
        
        return importance 