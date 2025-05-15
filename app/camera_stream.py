# camera_stream.py
import cv2
import threading
from .ai_core import detect_objects

class CameraStream:
    def __init__(self, camera_id=0, frame_skip=15):
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.current_frame = None
        self.labels = []
        self.frame_skip = frame_skip
        self.counter = 0
        self.running = True
        self.thread = threading.Thread(target=self.update, daemon=True)
        self.thread.start()

    def update(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue

            self.counter += 1
            if self.counter % self.frame_skip == 0:
                self.labels = detect_objects(frame)

            self.current_frame = frame

    def get_frame(self):
        if self.current_frame is None:
            return None, []
        ret, jpeg = cv2.imencode('.jpg', self.current_frame)
        return jpeg.tobytes(), self.labels

    def stop(self):
        self.running = False
        self.cap.release()
