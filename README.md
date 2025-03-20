# Face Landmark Virtual Visualizer

A real-time Python application that transforms facial landmarks into an artistic virtual visualization using MediaPipe and OpenCV. The program detects facial features and displays them as glowing points in a virtual space with dynamic effects.

## ✨ Features

- Real-time facial landmark detection
- Glowing vertex effects with motion trails
- Dynamic particle system
- Wireframe face mesh visualization
- Multi-face support
- Performance monitoring (FPS counter)
- Black background with sky-blue points

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Webcam

### Installation

1. Clone the repository
    ```
    git clone https://github.com/yourusername/face-landmark-visualizer.git
    cd face-landmark-visualizer
    ```

2. Install required packages
    ```
    pip install -r requirements.txt
    ```

### Running the Application

Run the main script:
``` 
python main.py
 ```

### Controls
- Face the camera to see the visualization
- Move your face to create dynamic effects
- Press 'q' to quit



## 🛠️ Technical Details

### Components

#### Face Detection Module
- Uses MediaPipe for facial landmark detection
- Supports tracking multiple faces
- Calculates motion metrics for effects

#### Virtual World Engine
- Renders landmarks as glowing points
- Creates motion trails based on movement
- Implements wireframe visualization
- Manages particle effects

#### Main Application
- Handles webcam input
- Coordinates detection and visualization
- Monitors performance (FPS)

## ⚙️ Dependencies
```
mediapipe>=0.10.0
numpy>=1.21.0
opencv-python>=4.8.0
```

## 💡 Performance Tips

If experiencing performance issues:
- Ensure good lighting conditions
- Reduce camera resolution in `main.py`
- Decrease particle count in `virtual_world.py`
- Update graphics drivers

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- MediaPipe team for face mesh solution
- OpenCV community
- All contributors

## 📧 Contact

Your Name - [@yourusername](https://github.com/yourusername)

Project Link: [https://github.com/yourusername/face-landmark-visualizer](https://github.com/yourusername/face-landmark-visualizer)

---
Made with ❤️ using Python, MediaPipe, and OpenCV
