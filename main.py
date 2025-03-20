import cv2
import time
import numpy as np
from face_detection import FaceLandmarkDetector
from virtual_world import VirtualWorld

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    
    # Initialize detector and virtual world
    detector = FaceLandmarkDetector()
    virtual_world = VirtualWorld(width=640, height=480)
    
    # FPS calculation variables
    prev_time = time.time()
    fps = 0
    
    # Audio setup (if you want to add sound reactivity)
    # import pyaudio
    # audio = pyaudio.PyAudio()
    # stream = audio.open(format=pyaudio.paFloat32, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            
            # Detect facial landmarks and get motion data
            faces_data = detector.detect_landmarks(frame)
            
            # Create virtual world frame with effects
            virtual_frame = virtual_world.create_virtual_frame(faces_data)
            
            # Calculate and display FPS
            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time
            virtual_world.add_fps_counter(virtual_frame, fps)
            
            # Display result
            cv2.imshow('Virtual Face Landmarks', virtual_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    finally:
        cap.release()
        detector.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 