<div align="center">

# 🔥 Fire & Smoke Detection System

**Real-time AI-powered fire & smoke detection with 4 operating modes**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=flat-square)](https://ultralytics.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)

> 🎓 Capstone Project — Deep learning + Computer Vision + Flask Web App

</div>



## Hardware

```
 Jetson Nano B01, Pi Camera V3 
```

## How It Works

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '18px', 'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#94a3b8'}}}%%
flowchart LR
    A(("📷\nCamera")) --> B["🧠 YOLOv8\nInference"] --> C{4 Modes}
    C -- Text --> D["📝 JSON"]
    C -- Capture --> E["📸 PNG"]
    C -- Video --> F["🎬 MP4"]
    C -- Live --> G["📺 MJPEG"]

    style A fill:#0c4a6e,stroke:#7dd3fc,color:#f0f9ff,stroke-width:2px
    style B fill:#92400e,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style C fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style D fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
    style E fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style F fill:#78350f,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style G fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
```

---

## The 4 Modes

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '16px', 'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#64748b'}}}%%
flowchart TB
    CTRL["🎮 Mode Controller — only 1 active"] --> M1 & M2 & M3 & M4

    M1["📝 TEXT — Frame → YOLOv8 → JSON via SSE"]
    M2["📸 CAPTURE — Frame → YOLOv8 + BBox → PNG"]
    M3["🎬 VIDEO — 30s Record → YOLOv8 + BBox → H.264 MP4"]
    M4["📺 LIVE — Continuous → model.track → Trajectory + MJPEG"]

    style CTRL fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style M1 fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
    style M2 fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style M3 fill:#78350f,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style M4 fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
```

<div align="center">

| | 📝 Text | 📸 Capture | 🎬 Video | 📺 Live |
|:--|:--:|:--:|:--:|:--:|
| **Toggle** | `Q` | `D` | `T` | Web UI |
| **Action** | `W` run/pause | `F` snap | `Y` record | Start/Stop btn |
| **Output** | JSON scores | PNG image | MP4 file | MJPEG stream |
| **Tracking** | — | — | — | ✅ |

</div>

---

## Architecture

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '16px', 'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#94a3b8'}}}%%
flowchart LR
    CAM(("📷\nWebcam")) --> FLASK
    SER(("📡\nModem")) --> FLASK

    FLASK["⚙️ Flask :5000\n+ YOLOv8 Engine"] --> MODES

    MODES["📦 text.py | capture.py\nvideo.py | live.py"] --> UI

    UI["🖥️ Browser\nBootstrap 5 + jQuery"]

    style CAM fill:#991b1b,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
    style SER fill:#991b1b,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
    style FLASK fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style MODES fill:#78350f,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style UI fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
```

---

## Project Structure

```
FINAL/
├── main.py                 # Flask entry point + all routes
├── MODES/
│   ├── text.py             # Mode 1 — Text SSE
│   ├── capture.py          # Mode 2 — Image capture
│   ├── video.py            # Mode 3 — Video recording
│   └── live.py             # Mode 4 — Live stream + tracking
├── sys_info.py             # Network diagnostics (serial AT cmds)
├── conv.py                 # YOLOv8 → TensorRT export
├── templates/index.html    # Web UI
├── yolov8n.pt              # Model weights (~6MB)
└── START.bat               # Windows venv launcher
```

---

## Quick Start

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '18px', 'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#64748b'}}}%%
flowchart LR
    A["🔗 Clone"] ==> B["📦 Install"] ==> C["🚀 Run"] ==> D["🌐 Open\nlocalhost:5000"]

    style A fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style B fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style C fill:#92400e,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style D fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
```

```bash
git clone https://github.com/HoangTran1106/cap_B.git
cd cap_B/FINAL

python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate

pip install flask flask-cors ultralytics opencv-python numpy imageio-ffmpeg pyserial keyboard

python main.py
```

Open **http://localhost:5000** — done!

---

## API Summary

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '15px', 'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#475569'}}}%%
flowchart LR
    C(("🖥️\nClient")) --> G & T & I & V & L

    G["🌐 GET / · GET /info\nPOST /mode · POST /set_threshold"]
    T["📝 GET /TextMode/feed\nPOST /TextMode/control"]
    I["📸 GET /CaptureMode/feed\nPOST /CaptureMode/control"]
    V["🎬 GET /VideoMode/getVideo\nPOST /VideoMode/control"]
    L["📺 GET /video_feed\nGET /start_detection\nGET /stop_detection"]

    style C fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style G fill:#581c87,stroke:#d8b4fe,color:#faf5ff,stroke-width:2px
    style T fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
    style I fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style V fill:#78350f,stroke:#fcd34d,color:#fffbeb,stroke-width:2px
    style L fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
```

---

## Config

```python
# main.py
model = YOLO('yolov8n.pt')        # swap for your custom model
conf_threshold = 0.25              # confidence threshold (0.0 – 1.0)
camera = cv2.VideoCapture(0)       # camera index

# MODES/video.py
vid_len = 30                       # recording duration (seconds)
frame_width, frame_height = 640, 480
fps = 30
```

---

<div align="center">

**Built by [Hoang Tran](https://github.com/HoangTran1106)** · 🎓 Capstone Project

⭐ Star this repo if you find it useful!

</div>