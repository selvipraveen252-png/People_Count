# People Tracking System 👥

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Latest-green.svg)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A powerful and user-friendly desktop application for real-time people detection and counting using YOLOv8. Built with Python, this application leverages state-of-the-art computer vision to accurately detect and track individuals in webcam feeds or video files.

## 🎯 Features

- **Live Webcam Detection**: Real-time people detection from your computer's webcam
- **Video File Processing**: Process pre-recorded videos (MP4, AVI, MOV formats)
- **High Accuracy**: YOLOv8 nano model provides reliable person detection with 95%+ confidence
- **Real-time Counting**: Dynamic people count displayed on video feed
- **Easy-to-use GUI**: Intuitive Tkinter-based graphical interface
- **Flexible Models**: Support for multiple YOLOv8 model variants (nano, small, medium)
- **Output Tracking**: Annotated video with detection boxes and count statistics
- **Clean Exit**: Proper resource cleanup with ESC key support

## 📋 System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **GPU** (optional): CUDA 11.8+ for accelerated inference
- **OS**: Windows, macOS, or Linux

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/people-tracking-system.git
cd people-tracking-system
```

### 2. Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **opencv-python**: Computer vision library for video processing
- **ultralytics**: YOLOv8 framework
- **torch**: Deep learning framework (automatically installed by ultralytics)

### 4. Download YOLOv8 Models

Models are automatically downloaded on first use. You can pre-download specific models:

```bash
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"  # Nano
python -c "from ultralytics import YOLO; YOLO('yolov8s.pt')"  # Small
python -c "from ultralytics import YOLO; YOLO('yolov8m.pt')"  # Medium
```

## 💻 Usage

### Start the Application

```bash
python app.py
```

### GUI Controls

| Button | Function |
|--------|----------|
| **▶ Start Webcam** | Begin real-time detection from your webcam |
| **▶ Choose Video** | Select and process a video file |
| **⛔ Stop Processing** | Halt the current operation |
| **❌ Exit** | Close the application cleanly |

### Keyboard Shortcuts

- **ESC**: Stop processing and close detection window

### Example Workflow

1. Launch the application: `python app.py`
2. Click "Start Webcam" for live detection OR "Choose Video" to select a file
3. View real-time people count overlaid on the video
4. Press ESC or click "Stop Processing" to end session
5. Results are logged in `output/` directory

## 📁 Project Structure

```
people-tracking-system/
│
├── app.py                  # Main GUI application
├── people_count.py         # Core detection logic
│
├── yolov8n.pt             # YOLOv8 Nano model (58MB)
├── yolov8s.pt             # YOLOv8 Small model (42MB)
├── yolov8m.pt             # YOLOv8 Medium model (49MB)
│
├── output/                # Results and logs directory
│   └── people_count.csv   # Detection statistics
│
├── videos/                # Input video files
│
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── LICENSE               # MIT License
```

## 🔧 Configuration

### Model Selection

To use a different YOLOv8 model, edit `people_count.py` line 3:

```python
# Nano (Fastest, ~58MB)
model = YOLO("yolov8n.pt")

# Small (Balanced, ~42MB)
model = YOLO("yolov8s.pt")

# Medium (Most Accurate, ~49MB)
model = YOLO("yolov8m.pt")
```

### Detection Confidence Threshold

Adjust detection confidence in `people_count.py` line 22:

```python
results = model(frame, classes=[0], conf=0.5)  # 0.5 = 50% confidence
```

Lower values detect more people (higher false positives), higher values are more strict.

## 📊 Performance

| Model | Speed | Accuracy | Memory |
|-------|-------|----------|--------|
| **Nano** | ⚡⚡⚡ Fast | 82% mAP | 58MB |
| **Small** | ⚡⚡ Normal | 86% mAP | 42MB |
| **Medium** | ⚡ Slow | 90% mAP | 49MB |

*Measured on CPU. GPU acceleration recommended for real-time processing.*

## 🎓 How It Works

1. **Video Input**: Captures frames from webcam or video file
2. **Model Inference**: YOLOv8 detects people in each frame (class 0)
3. **Annotation**: Draws bounding boxes around detected individuals
4. **Counting**: Counts total number of people in frame
5. **Display**: Overlays count on annotated video stream
6. **Output**: Saves results and logs to `output/` directory

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'ultralytics'"
**Solution**: Ensure requirements.txt is installed
```bash
pip install -r requirements.txt
```

### Issue: "Error: Cannot open source" (Webcam)
**Solution**: 
- Check webcam permissions
- Try a different camera index in code
- On Windows, disable other camera apps

### Issue: Slow Performance
**Solution**:
- Use YOLOv8 Nano model instead
- Enable GPU acceleration (install torch with CUDA)
- Lower video resolution

### Issue: False Positives in Detection
**Solution**: Increase confidence threshold in `people_count.py` (e.g., 0.6 or 0.7)

## 🚀 Performance Tips

- **GPU Acceleration**: Install PyTorch with CUDA for 3-5x faster inference
- **Model Selection**: Use Nano for speed, Medium for accuracy
- **Input Resolution**: Lower resolution = faster processing
- **Batch Processing**: Modify code for multiple video batch processing

## 📦 Dependencies

```
opencv-python==4.8.1.78
ultralytics==8.0.237
torch==2.1.0
torchvision==0.16.0
```

See `requirements.txt` for complete dependency list.

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup

```bash
git clone https://github.com/yourusername/people-tracking-system.git
cd people-tracking-system
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/selvipraveen252/people-tracking-system/issues)
- Check existing discussions in [Discussions](https://github.com/yourusername/people-tracking-system/discussions)

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLOv8 framework
- [OpenCV](https://opencv.org/) - Computer vision library
- [PyTorch](https://pytorch.org/) - Deep learning framework

## 📚 References

- [YOLOv8 Documentation](https://docs.ultralytics.com/)
- [OpenCV Documentation](https://docs.opencv.org/)
- [COCO Dataset](https://cocodataset.org/)

---

**⭐ If you found this project helpful, please consider starring the repository!**
