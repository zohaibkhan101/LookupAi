# app/routes.py
from flask import Blueprint, render_template, Response, request
from .camera_stream import CameraStream

main = Blueprint('main', __name__)

# Default camera
camera = CameraStream(camera_id=0)

@main.route('/')
def index():
    return render_template('index.html', caption="Starting...")

@main.route('/video_feed')
def video_feed():
    def generate():
        while True:
            frame, labels = camera.get_frame()
            if frame is None:
                continue
            text = ', '.join(labels)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@main.route('/set_camera/<int:cam_id>')
def set_camera(cam_id):
    global camera
    camera.stop()
    camera = CameraStream(camera_id=cam_id)
    return "Camera changed"
