import mediapipe as mp
import numpy as np
import cv2

class FaceLandmarkDetector:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=3,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        # Define connections for wireframe
        self.FACE_CONNECTIONS = mp.solutions.face_mesh.FACEMESH_TESSELATION

    def detect_landmarks(self, frame):
        """
        Detect facial landmarks and return both landmarks and connections
        Returns: Tuple of (landmarks, connections)
        """
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.face_mesh.process(frame_rgb)
        
        faces_data = []
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                # Get landmarks
                landmarks = np.array([(lm.x, lm.y, lm.z) for lm in face_landmarks.landmark])
                
                # Calculate motion metrics (for effects)
                motion = self._calculate_motion(landmarks)
                
                faces_data.append({
                    'landmarks': landmarks,
                    'connections': self.FACE_CONNECTIONS,
                    'motion': motion
                })
                
        return faces_data

    def _calculate_motion(self, landmarks):
        """Calculate face motion metrics for effects"""
        # Use nose tip as reference point for motion
        nose_tip = landmarks[4]
        return {
            'velocity': np.mean(np.diff(landmarks, axis=0), axis=0),
            'position': nose_tip
        }

    def release(self):
        """Release resources"""
        self.face_mesh.close() 