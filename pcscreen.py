import cv2
import numpy as np
from flask import Flask, Response, redirect
import pyautogui
import threading
import time
import mss

app = Flask(__name__)

latest_frame = None
capture_lock = threading.Lock()
scale_factor = 1.0

def capture_screen():
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        img = np.array(sct.grab(monitor))
        img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        if scale_factor != 1.0:
            img_bgr = cv2.resize(img_bgr, (int(monitor["width"] * scale_factor), int(monitor["height"] * scale_factor)))
        mouse_x, mouse_y = pyautogui.position()
        cursor_radius = 10
        cursor_color = (0, 0, 255)
        cv2.circle(img_bgr, (mouse_x, mouse_y), cursor_radius, cursor_color, thickness=-1)
        return img_bgr

def duplicate_screen(screen):
    duplicated_screen = np.hstack((screen, screen))
    _, jpeg = cv2.imencode('.jpg', duplicated_screen, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    return jpeg.tobytes()

def capture_thread():
    global latest_frame
    while True:
        frame = capture_screen()
        with capture_lock:
            latest_frame = frame
        time.sleep(0.03)

@app.route('/video_feed')
def video_feed():
    def generate():
        while True:
            with capture_lock:
                frame = latest_frame
            if frame is not None:
                duplicated_frame = duplicate_screen(frame)
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + duplicated_frame + b'\r\n\r\n')
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return redirect("/video_feed")

if __name__ == '__main__':
    threading.Thread(target=capture_thread, daemon=True).start()
    app.run(host='0.0.0.0', port=5000, debug=False)
