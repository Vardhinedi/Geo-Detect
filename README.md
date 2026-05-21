# GeoDetect

AI-powered multimodal geospatial intelligence system for aerial and satellite imagery analysis.

## Features

- YOLO-OBB aerial object detection
- Rotated bounding box vehicle analysis
- Multimodal image understanding
- Local LLM intelligence reporting
- Streamlit intelligence dashboard
- Structured ISR-style summaries
- Geospatial scene analysis
- Detection-to-report intelligence pipeline

---

# System Architecture

Aerial Image
↓
YOLO-OBB Detection
↓
Structured Spatial Data
↓
Multimodal Scene Understanding
↓
LLM Intelligence Fusion
↓
Operational Intelligence Report

---

# Technologies Used

## Computer Vision
- YOLOv8-OBB
- OpenCV
- Ultralytics

## AI / LLM
- Ollama
- Llama 3
- MiniCPM-V

## Frontend
- Streamlit

## Backend
- Python
- Torch
- FastAPI

---

# Project Structure

```bash
satellite-intelligence-system/
│
├── backend/
│   ├── detector.py
│   ├── intelligence.py
│   ├── scene_understanding.py
│   └── scene_test.py
│
├── frontend/
│   └── app.py
│
├── data/
│   ├── output/
│   └── test_image.jpg
│
├── reports/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your-repo-url>
cd satellite-intelligence-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Install Ollama

Download:

https://ollama.com

---

# Pull Required Models

```bash
ollama pull llama3
ollama pull minicpm-v
```

---

# Run The Dashboard

```bash
streamlit run frontend/app.py
```

---

# Current Capabilities

- Dense aerial traffic detection
- Rotated vehicle bounding boxes
- Structured detection analytics
- Local multimodal inference
- Intelligence summary generation
- Urban infrastructure analysis
- Spatial pattern interpretation

---

# Current Limitations

- Scene-level VLM grounding still requires refinement
- No temporal tracking yet
- No geospatial coordinate mapping yet
- No custom-trained aerospace dataset yet

---

# Planned Upgrades

- DOTA/xView custom training
- RT-DETR integration
- Traffic density analytics
- Object tracking
- Video intelligence pipeline
- Geospatial coordinate conversion
- Confidence calibration
- Advanced ISR analytics

---

# Disclaimer

This project is an experimental AI research and engineering system intended for computer vision, geospatial analysis, and multimodal AI experimentation.

It is not intended for operational military or surveillance deployment.

---

# Author

Chetan Phanindra
