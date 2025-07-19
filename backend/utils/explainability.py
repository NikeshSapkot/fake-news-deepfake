import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, List, Optional
import json
import base64
import io
from wordcloud import WordCloud
import cv2
from PIL import Image

class TextExplainer:
    def __init__(self):
        """Initialize text explainer for generating explanations"""
        self.feature_names = [
            'fake_indicators', 'credible_indicators', 'exclamation_count',
            'caps_ratio', 'sentiment_score', 'word_count', 'avg_word_length'
        ]

    def explain(self, text: str, result: Dict) -> Dict:
        """Generate explanations for text prediction"""
        explanation = {
            "type": "text",
            "prediction": "fake" if result["is_fake"] else "real",
            "confidence": result["confidence"],
            "key_factors": [],
            "feature_importance": {},
            "recommendations": [],
            "visualization": None
        }
        
        # Extract key factors
        if result.get("features"):
            for feature in result["features"]:
                if "fake_indicators" in feature:
                    explanation["key_factors"].append("Contains suspicious language patterns")
                elif "credible_indicators" in feature:
                    explanation["key_factors"].append("Contains credible source indicators")
                elif "exclamation_count" in feature:
                    explanation["key_factors"].append("Uses excessive exclamation marks")
                elif "caps_ratio" in feature:
                    explanation["key_factors"].append("Uses excessive capitalization")
        
        # Generate feature importance
        fake_score = result.get("fake_score", 0.5)
        explanation["feature_importance"] = {
            "suspicious_language": min(fake_score * 0.4, 1.0),
            "source_credibility": max(0, (1 - fake_score) * 0.3),
            "writing_style": min(fake_score * 0.2, 1.0),
            "sentiment": abs(fake_score - 0.5) * 0.1
        }
        
        # Generate recommendations
        if result["is_fake"]:
            explanation["recommendations"] = [
                "Verify information with multiple credible sources",
                "Check for fact-checking websites",
                "Look for official statements or press releases",
                "Be cautious of sensationalist language"
            ]
        else:
            explanation["recommendations"] = [
                "Content appears credible but always verify independently",
                "Check multiple sources for confirmation",
                "Look for official documentation when possible"
            ]
        
        # Generate word cloud visualization
        try:
            explanation["visualization"] = self._generate_word_cloud(text)
        except:
            explanation["visualization"] = None
        
        return explanation

    def _generate_word_cloud(self, text: str) -> Optional[str]:
        """Generate word cloud visualization"""
        try:
            # Create word cloud
            wordcloud = WordCloud(
                width=400, 
                height=200, 
                background_color='white',
                max_words=50
            ).generate(text)
            
            # Convert to base64
            img_buffer = io.BytesIO()
            plt.figure(figsize=(8, 4))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.tight_layout()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            plt.close()
            
            img_buffer.seek(0)
            img_str = base64.b64encode(img_buffer.getvalue()).decode()
            
            return f"data:image/png;base64,{img_str}"
        except:
            return None

class ImageExplainer:
    def __init__(self):
        """Initialize image explainer for generating explanations"""
        self.artifact_names = [
            'edge_density', 'hue_variance', 'saturation_variance',
            'value_variance', 'symmetry_score'
        ]

    def explain(self, image_file, result: Dict) -> Dict:
        """Generate explanations for image prediction"""
        explanation = {
            "type": "image",
            "prediction": "deepfake" if result["is_deepfake"] else "real",
            "confidence": result["confidence"],
            "key_factors": [],
            "artifact_analysis": {},
            "recommendations": [],
            "visualization": None
        }
        
        # Analyze face artifacts
        face_artifacts = result.get("face_artifacts", [])
        if face_artifacts:
            # Average artifacts across all faces
            avg_artifacts = {}
            for key in face_artifacts[0].keys():
                avg_artifacts[key] = np.mean([artifacts[key] for artifacts in face_artifacts])
            
            explanation["artifact_analysis"] = avg_artifacts
            
            # Generate key factors
            if avg_artifacts.get("edge_density", 0) > 0.1:
                explanation["key_factors"].append("Unusually high edge density detected")
            
            if avg_artifacts.get("hue_variance", 0) > 1000:
                explanation["key_factors"].append("Inconsistent color patterns detected")
            
            if avg_artifacts.get("symmetry_score", 0) > 0.95:
                explanation["key_factors"].append("Unnaturally perfect facial symmetry")
        
        # Face detection analysis
        if result.get("face_detected"):
            explanation["key_factors"].append(f"Detected {result.get('face_count', 0)} face(s) in image")
        else:
            explanation["key_factors"].append("No faces detected in image")
        
        # Generate recommendations
        if result["is_deepfake"]:
            explanation["recommendations"] = [
                "Image shows signs of digital manipulation",
                "Verify image source and authenticity",
                "Check for reverse image search results",
                "Look for inconsistencies in lighting and shadows"
            ]
        else:
            explanation["recommendations"] = [
                "Image appears to be authentic",
                "Still verify with reverse image search",
                "Check image metadata when possible",
                "Consider the source and context"
            ]
        
        # Generate heatmap visualization
        try:
            explanation["visualization"] = self._generate_heatmap(image_file, result)
        except:
            explanation["visualization"] = None
        
        return explanation

    def _generate_heatmap(self, image_file, result: Dict) -> Optional[str]:
        """Generate heatmap visualization highlighting suspicious areas"""
        try:
            # Read and process image
            image_bytes = image_file.read()
            image_file.seek(0)
            
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            # Create heatmap
            heatmap = np.zeros(img_rgb.shape[:2], dtype=np.float32)
            
            # Highlight face areas if detected
            face_artifacts = result.get("face_artifacts", [])
            for i, face in enumerate(face_artifacts):
                # This is a simplified heatmap - in practice, you'd use Grad-CAM or similar
                if face.get("edge_density", 0) > 0.1:
                    # Add some heat to face areas
                    heatmap += 0.3
            
            # Normalize heatmap
            if np.max(heatmap) > 0:
                heatmap = heatmap / np.max(heatmap)
            
            # Create visualization
            plt.figure(figsize=(10, 6))
            
            plt.subplot(1, 2, 1)
            plt.imshow(img_rgb)
            plt.title("Original Image")
            plt.axis('off')
            
            plt.subplot(1, 2, 2)
            plt.imshow(img_rgb)
            plt.imshow(heatmap, alpha=0.6, cmap='hot')
            plt.title("Suspicious Areas Highlighted")
            plt.axis('off')
            
            plt.tight_layout()
            
            # Convert to base64
            img_buffer = io.BytesIO()
            plt.savefig(img_buffer, format='png', bbox_inches='tight', dpi=150)
            plt.close()
            
            img_buffer.seek(0)
            img_str = base64.b64encode(img_buffer.getvalue()).decode()
            
            return f"data:image/png;base64,{img_str}"
        except Exception as e:
            print(f"Heatmap generation failed: {e}")
            return None

class ComprehensiveExplainer:
    def __init__(self):
        """Initialize comprehensive explainer for multi-modal analysis"""
        self.text_explainer = TextExplainer()
        self.image_explainer = ImageExplainer()

    def explain_comprehensive(self, text: Optional[str], image_file, text_result: Dict, image_result: Dict) -> Dict:
        """Generate comprehensive explanations for multi-modal analysis"""
        explanation = {
            "type": "comprehensive",
            "overall_score": 0.0,
            "text_analysis": None,
            "image_analysis": None,
            "cross_modal_insights": [],
            "recommendations": []
        }
        
        # Text analysis
        if text and text_result:
            explanation["text_analysis"] = self.text_explainer.explain(text, text_result)
        
        # Image analysis
        if image_file and image_result:
            explanation["image_analysis"] = self.image_explainer.explain(image_file, image_result)
        
        # Calculate overall score
        text_score = text_result.get("fake_score", 0.5) if text_result else 0.5
        image_score = image_result.get("deepfake_score", 0.5) if image_result else 0.5
        
        # Weighted combination
        if text and image_file:
            explanation["overall_score"] = (text_score * 0.6 + image_score * 0.4)
        elif text:
            explanation["overall_score"] = text_score
        elif image_file:
            explanation["overall_score"] = image_score
        
        # Cross-modal insights
        if text and image_file:
            if text_result.get("is_fake") and image_result.get("is_deepfake"):
                explanation["cross_modal_insights"].append("Both text and image show signs of manipulation")
            elif text_result.get("is_fake") and not image_result.get("is_deepfake"):
                explanation["cross_modal_insights"].append("Text appears suspicious but image seems authentic")
            elif not text_result.get("is_fake") and image_result.get("is_deepfake"):
                explanation["cross_modal_insights"].append("Image shows manipulation but text appears credible")
            else:
                explanation["cross_modal_insights"].append("Both text and image appear authentic")
        
        # Generate comprehensive recommendations
        if explanation["overall_score"] > 0.7:
            explanation["recommendations"] = [
                "High likelihood of fake content detected",
                "Verify all information with multiple sources",
                "Check for official statements or press releases",
                "Use fact-checking websites for verification",
                "Be extremely cautious when sharing this content"
            ]
        elif explanation["overall_score"] > 0.4:
            explanation["recommendations"] = [
                "Some suspicious elements detected",
                "Verify information independently",
                "Check multiple sources for confirmation",
                "Consider the source and context carefully"
            ]
        else:
            explanation["recommendations"] = [
                "Content appears to be authentic",
                "Still verify with independent sources",
                "Check for recent updates or corrections",
                "Consider the overall context and source credibility"
            ]
        
        return explanation 