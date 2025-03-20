import cv2
import numpy as np

class VirtualWorld:
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.point_color = (255, 191, 0)  # Sky blue in BGR
        self.glow_color = (128, 95, 0)    # Dimmer sky blue for glow effect
        self.line_color = (128, 95, 0)    # Color for wireframe
        self.point_size = 1
        self.glow_size = 3
        
        # Initialize particle system for floating effect
        self.particles = []
        self.max_particles = 50

    def create_virtual_frame(self, faces_data):
        # Create black background with motion blur effect
        frame = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        
        for face_data in faces_data:
            landmarks = face_data['landmarks']
            connections = face_data['connections']
            motion = face_data['motion']
            
            # Draw wireframe connections
            self._draw_wireframe(frame, landmarks, connections)
            
            # Draw glowing landmarks with motion effects
            self._draw_landmarks_with_effects(frame, landmarks, motion)
            
            # Update and draw floating particles
            self._update_particles(motion)
            self._draw_particles(frame)
        
        return frame

    def _draw_wireframe(self, frame, landmarks, connections):
        for connection in connections:
            start_idx = connection[0]
            end_idx = connection[1]
            
            start_point = self._get_pixel_coords(landmarks[start_idx])
            end_point = self._get_pixel_coords(landmarks[end_idx])
            
            cv2.line(frame, start_point, end_point, self.line_color, 1)

    def _draw_landmarks_with_effects(self, frame, landmarks, motion):
        for landmark in landmarks:
            point = self._get_pixel_coords(landmark)
            
            # Draw glow effect
            cv2.circle(frame, point, self.glow_size, self.glow_color, -1)
            
            # Draw main point
            cv2.circle(frame, point, self.point_size, self.point_color, -1)
            
            # Add motion trail
            velocity = motion['velocity']
            if np.any(velocity):
                trail_point = (
                    int(point[0] - velocity[0] * 10),
                    int(point[1] - velocity[1] * 10)
                )
                cv2.line(frame, point, trail_point, self.glow_color, 1)

    def _update_particles(self, motion):
        # Add new particles based on motion
        if len(self.particles) < self.max_particles:
            position = motion['position']
            self.particles.append({
                'position': self._get_pixel_coords(position),
                'velocity': np.random.randn(2) * 2,
                'life': 1.0
            })
        
        # Update existing particles
        for particle in self.particles[:]:
            particle['position'] = (
                int(particle['position'][0] + particle['velocity'][0]),
                int(particle['position'][1] + particle['velocity'][1])
            )
            particle['life'] -= 0.02
            
            if particle['life'] <= 0:
                self.particles.remove(particle)

    def _draw_particles(self, frame):
        for particle in self.particles:
            alpha = particle['life']
            color = tuple(int(c * alpha) for c in self.glow_color)
            cv2.circle(frame, particle['position'], 2, color, -1)

    def _get_pixel_coords(self, landmark):
        return (
            int(landmark[0] * self.width),
            int(landmark[1] * self.height)
        )

    def add_fps_counter(self, frame, fps):
        """Add FPS counter to the frame"""
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2) 