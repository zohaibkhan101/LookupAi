# ai_core.py
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")  # Use YOLOv8 nano for best speed

def detect_objects(frame):
    results = model.predict(source=frame, conf=0.5, verbose=False)
    labels = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            labels.append(label)

    return list(set(labels))
