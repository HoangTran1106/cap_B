from ultralytics import YOLO

model = YOLO("m_100k_250epoch.pt")
model.export(
    format="engine"
)
