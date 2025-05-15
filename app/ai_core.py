# ai_core.py
from ultralytics import YOLO

# Load YOLOv8 nano model once
model = YOLO("yolov8n.pt")  # Make sure yolov8n.pt is downloaded and accessible

def detect_objects(frame):
    """
    Run YOLOv8 object detection on the frame.
    
    Args:
        frame (numpy.ndarray): BGR image from OpenCV camera.
        
    Returns:
        List of detections, each is a dict with:
        - label: object class name
        - confidence: detection confidence (0-1)
        - box: bounding box [x1, y1, x2, y2]
    """
    results = model.predict(source=frame, conf=0.5, verbose=False)

    detections = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = box.conf[0].item()
            xyxy = box.xyxy[0].tolist()
            detections.append({
                "label": label,
                "confidence": conf,
                "box": xyxy
            })

    return detections
