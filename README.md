<div align="center">

# 🔥 Fire & Smoke Detection System

**Real-time AI-powered fire & smoke detection with 4 operating modes**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask)](https://flask.palletsprojects.com)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?style=flat-square)](https://ultralytics.com)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org)

> 🎓 Capstone Project — Deep learning + Computer Vision + Flask Web App

</div>

---

## How It Works

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#94a3b8', 'fontSize': '14px'}}}%%
graph LR
    A["📷 Camera"] ==> B["🧠 YOLOv8"]
    B ==> C{"4 Modes"}
    C -->|Text| D["📝 JSON Scores"]
    C -->|Capture| E["📸 Annotated PNG"]
    C -->|Video| F["🎬 30s MP4 Clip"]
    C -->|Live| G["📺 MJPEG Stream"]

    style A fill:#0c4a6e,stroke:#7dd3fc,color:#f0f9ff
    style B fill:#92400e,stroke:#fcd34d,color:#fffbeb
    style C fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff
    style D fill:#14532d,stroke:#86efac,color:#f0fdf4
    style E fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff
    style F fill:#78350f,stroke:#fcd34d,color:#fffbeb
    style G fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2
```

---

## The 4 Modes

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#64748b', 'fontSize': '13px'}}}%%
graph TB
    CTRL["🎮 Mode Controller<br/><i>Only 1 active at a time</i>"]

    CTRL --> M1 & M2 & M3 & M4

    subgraph M1["📝 Text Mode"]
        T1["Read Frame → YOLOv8 → JSON via SSE"]
    end

    subgraph M2["📸 Capture Mode"]
        C1["Read Frame → YOLOv8 + BBox → Save PNG"]
    end

    subgraph M3["🎬 Video Mode"]
        V1["Record 30s → YOLOv8 + BBox → H.264 MP4"]
    end

    subgraph M4["📺 Live Mode"]
        L1["Continuous → model.track() → Trajectory + MJPEG"]
    end

    style CTRL fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style M1 fill:#14532d,stroke:#86efac,color:#f0fdf4
    style M2 fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff
    style M3 fill:#78350f,stroke:#fcd34d,color:#fffbeb
    style M4 fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2
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
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#1e293b', 'primaryTextColor': '#f8fafc', 'lineColor': '#94a3b8', 'fontSize': '13px'}}}%%
graph TB
    subgraph HW["🔌 Hardware"]
        CAM["📷 Webcam"] ~~~ SER["📡 4G Modem"]
    end

    subgraph BACK["⚙️ Flask Backend"]
        direction TB
        APP["🌐 Flask :5000"]
        YOLO["🧠 YOLOv8 Engine"]
        subgraph MODES["📦 Modes"]
            direction LR
            m1["text.py"] ~~~ m2["capture.py"] ~~~ m3["video.py"] ~~~ m4["live.py"]
        end
        SYS["📊 sys_info.py"] ~~~ FF["🎞️ FFmpeg"]
    end

    subgraph FRONT["🖥️ Browser"]
        UI["🌐 Bootstrap 5 + jQuery + SSE"]
    end

    HW ==> BACK ==> FRONT

    style HW fill:#991b1b,stroke:#fca5a5,color:#fef2f2,stroke-width:2px
    style BACK fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff,stroke-width:2px
    style MODES fill:#1e40af,stroke:#60a5fa,color:#eff6ff
    style FRONT fill:#14532d,stroke:#86efac,color:#f0fdf4,stroke-width:2px
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
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#64748b', 'fontSize': '14px'}}}%%
flowchart LR
    A["🔗 Clone"] ==> B["📦 Install"] ==> C["🚀 Run"] ==> D["🌐 Open"]

    style A fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff
    style B fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff
    style C fill:#92400e,stroke:#fcd34d,color:#fffbeb
    style D fill:#14532d,stroke:#86efac,color:#f0fdf4
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

## API at a Glance

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#0f172a', 'primaryTextColor': '#f1f5f9', 'lineColor': '#475569', 'fontSize': '12px'}}}%%
graph LR
    C["🖥️ Client"]

    C --> G & T & I & V & L

    subgraph G["🌐 General"]
        g1["GET /"] ~~~ g2["GET /info"] ~~~ g3["POST /mode"] ~~~ g4["POST /set_threshold"]
    end
    subgraph T["📝 Text"]
        t1["GET /TextMode/feed"] ~~~ t2["POST /TextMode/control"]
    end
    subgraph I["📸 Capture"]
        i1["GET /CaptureMode/feed"] ~~~ i2["POST /CaptureMode/control"]
    end
    subgraph V["🎬 Video"]
        v1["GET /VideoMode/getVideo"] ~~~ v2["POST /VideoMode/control"]
    end
    subgraph L["📺 Live"]
        l1["GET /video_feed"] ~~~ l2["GET /start_detection"] ~~~ l3["GET /stop_detection"]
    end

    style C fill:#4c1d95,stroke:#c4b5fd,color:#f5f3ff,stroke-width:2px
    style G fill:#581c87,stroke:#d8b4fe,color:#faf5ff
    style T fill:#14532d,stroke:#86efac,color:#f0fdf4
    style I fill:#1e3a5f,stroke:#93c5fd,color:#eff6ff
    style V fill:#78350f,stroke:#fcd34d,color:#fffbeb
    style L fill:#7f1d1d,stroke:#fca5a5,color:#fef2f2
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