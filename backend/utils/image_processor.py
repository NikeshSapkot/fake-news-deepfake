import time
import cv2
import numpy as np
from typing import Dict, Optional
from PIL import Image
import io
import face_recognition
from deepface import DeepFace
import tensorflow as tf
from tensorflow.keras.applications import Xception
from tensorflow.keras.preprocessing import image as keras_image

class ImageProcessor:
    def __init__(self):
        """Initialize the image processor with CV models"""
        self.device = 'cuda' if tf.config.list_physical_devices('GPU') else 'cpu'
        
        # Initialize face detection
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        # Initialize Xception model for deepfake detection
        try:
            self.xception_model = Xception(weights='imagenet', include_top=False, pooling='avg')
        except:
            self.xception_model = None
        
        # Deepfake detection thresholds
        self.face_confidence_threshold = 0.5
        self.deepfake_threshold = 0.6
        
        # Image preprocessing parameters
        self.target_size = (224, 224)
        self.max_faces = 5

    def preprocess_image(self, image_file) -> np.ndarray:
        """Preprocess image for analysis"""
        try:
            # Read image from file
            image_bytes = image_file.read()
            image_file.seek(0)  # Reset file pointer
            
            # Convert to numpy array
            nparr = np.frombuffer(image_bytes, np.uint8)
            img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            if img is None:
                raise ValueError("Could not decode image")
            
            # Convert BGR to RGB
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            
            return img_rgb
        except Exception as e:
            raise ValueError(f"Error preprocessing image: {str(e)}")

    def detect_faces(self, img: np.ndarray) -> list:
        """Detect faces in the image"""
        faces = []
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
        # Detect faces using OpenCV
        face_locations = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )
        
        for (x, y, w, h) in face_locations:
            face_img = img[y:y+h, x:x+w]
            faces.append({
                'bbox': (x, y, w, h),
                'face_img': face_img,
                'confidence': 0.8  # Default confidence for OpenCV detection
            })
        
        # Also try face_recognition library for better accuracy
        try:
            face_locations_fr = face_recognition.face_locations(img)
            face_encodings = face_recognition.face_encodings(img, face_locations_fr)
            
            for i, (top, right, bottom, left) in enumerate(face_locations_fr):
                face_img = img[top:bottom, left:right]
                faces.append({
                    'bbox': (left, top, right-left, bottom-top),
                    'face_img': face_img,
                    'encoding': face_encodings[i] if i < len(face_encodings) else None,
                    'confidence': 0.9
                })
        except Exception as e:
            print(f"Face recognition failed: {e}")
        
        return faces[:self.max_faces]  # Limit number of faces

    def extract_image_features(self, img: np.ndarray) -> Dict:
        """Extract features from image for deepfake detection"""
        features = {}
        
        # Basic image statistics
        features['width'] = img.shape[1]
        features['height'] = img.shape[0]
        features['channels'] = img.shape[2]
        
        # Color statistics
        features['mean_r'] = np.mean(img[:, :, 0])
        features['mean_g'] = np.mean(img[:, :, 1])
        features['mean_b'] = np.mean(img[:, :, 2])
        features['std_r'] = np.std(img[:, :, 0])
        features['std_g'] = np.std(img[:, :, 1])
        features['std_b'] = np.std(img[:, :, 2])
        
        # Texture features (simplified)
        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        features['brightness'] = np.mean(gray)
        features['contrast'] = np.std(gray)
        
        # Edge density
        edges = cv2.Canny(gray, 50, 150)
        features['edge_density'] = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
        
        return features

    def analyze_face_artifacts(self, face_img: np.ndarray) -> Dict:
        """Analyze face for deepfake artifacts"""
        artifacts = {}
        
        # Resize face for analysis
        face_resized = cv2.resize(face_img, self.target_size)
        
        # Check for unnatural edges
        gray_face = cv2.cvtColor(face_resized, cv2.COLOR_RGB2GRAY)
        edges = cv2.Canny(gray_face, 50, 150)
        artifacts['edge_density'] = np.sum(edges > 0) / (edges.shape[0] * edges.shape[1])
        
        # Check for color inconsistencies
        hsv = cv2.cvtColor(face_resized, cv2.COLOR_RGB2HSV)
        artifacts['hue_variance'] = np.var(hsv[:, :, 0])
        artifacts['saturation_variance'] = np.var(hsv[:, :, 1])
        artifacts['value_variance'] = np.var(hsv[:, :, 2])
        
        # Check for unnatural symmetry
        left_half = gray_face[:, :gray_face.shape[1]//2]
        right_half = cv2.flip(gray_face[:, gray_face.shape[1]//2:], 1)
        
        if left_half.shape == right_half.shape:
            symmetry_diff = np.mean(np.abs(left_half.astype(float) - right_half.astype(float)))
            artifacts['symmetry_score'] = 1.0 - (symmetry_diff / 255.0)
        else:
            artifacts['symmetry_score'] = 0.5
        
        return artifacts

    def predict(self, image_file, analyze_faces: bool = True) -> Dict:
        """Predict whether image contains deepfakes"""
        start_time = time.time()
        
        try:
            # Preprocess image
            img = self.preprocess_image(image_file)
            
            # Extract general image features
            features = self.extract_image_features(img)
            
            # Detect faces
            faces = self.detect_faces(img) if analyze_faces else []
            
            # Initialize deepfake score
            deepfake_score = 0.0
            face_artifacts = []
            
            # Analyze each face for artifacts
            for face in faces:
                artifacts = self.analyze_face_artifacts(face['face_img'])
                face_artifacts.append(artifacts)
                
                # Calculate artifact score
                artifact_score = 0.0
                
                # High edge density might indicate manipulation
                if artifacts['edge_density'] > 0.1:
                    artifact_score += 0.2
                
                # Unnatural color variance
                if artifacts['hue_variance'] > 1000 or artifacts['saturation_variance'] > 500:
                    artifact_score += 0.3
                
                # Perfect symmetry might indicate deepfake
                if artifacts['symmetry_score'] > 0.95:
                    artifact_score += 0.2
                
                deepfake_score = max(deepfake_score, artifact_score)
            
            # Use Xception model if available
            if self.xception_model and len(faces) > 0:
                try:
                    # Use the largest face for analysis
                    largest_face = max(faces, key=lambda x: x['face_img'].shape[0] * x['face_img'].shape[1])
                    face_img = largest_face['face_img']
                    
                    # Preprocess for Xception
                    face_pil = Image.fromarray(face_img)
                    face_pil = face_pil.resize(self.target_size)
                    x = keras_image.img_to_array(face_pil)
                    x = np.expand_dims(x, axis=0)
                    x = tf.keras.applications.xception.preprocess_input(x)
                    
                    # Extract features
                    features_xception = self.xception_model.predict(x)
                    
                    # Simple classification based on feature statistics
                    feature_mean = np.mean(features_xception)
                    feature_std = np.std(features_xception)
                    
                    # Unusual feature patterns might indicate deepfake
                    if feature_std > 0.5 or feature_mean < -0.1:
                        deepfake_score = max(deepfake_score, 0.4)
                
                except Exception as e:
                    print(f"Xception analysis failed: {e}")
            
            # Normalize score
            deepfake_score = max(0.0, min(1.0, deepfake_score))
            
            processing_time = time.time() - start_time
            
            return {
                "is_deepfake": deepfake_score > self.deepfake_threshold,
                "confidence": deepfake_score if deepfake_score > self.deepfake_threshold else 1 - deepfake_score,
                "deepfake_score": deepfake_score,
                "face_detected": len(faces) > 0,
                "face_count": len(faces),
                "face_artifacts": face_artifacts,
                "processing_time": processing_time,
                "image_features": features
            }
        
        except Exception as e:
            raise ValueError(f"Error processing image: {str(e)}")

    def get_artifact_importance(self, face_artifacts: list) -> Dict:
        """Get importance of different artifacts in the prediction"""
        if not face_artifacts:
            return {}
        
        # Average artifacts across all faces
        avg_artifacts = {}
        for key in face_artifacts[0].keys():
            avg_artifacts[key] = np.mean([artifacts[key] for artifacts in face_artifacts])
        
        importance = {}
        for artifact, value in avg_artifacts.items():
            if artifact == 'edge_density':
                importance[artifact] = value * 0.2 if value > 0.1 else 0
            elif artifact == 'hue_variance':
                importance[artifact] = value * 0.3 if value > 1000 else 0
            elif artifact == 'symmetry_score':
                importance[artifact] = value * 0.2 if value > 0.95 else 0
            else:
                importance[artifact] = 0
        
        return importance 