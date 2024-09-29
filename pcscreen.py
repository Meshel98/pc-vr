import cv2
import numpy as np
from flask import Flask, Response, redirect
import pyautogui
import threading
import time
import mss  # Import mss for faster screen capture

app = Flask(__name__)

# Global variables
latest_frame = None
capture_lock = threading.Lock()

# Full-screen dimensions will be auto-detected using mss
scale_factor = 1.0  # Full resolution capture

# Function to capture the primary screen using mss
def capture_screen():
    with mss.mss() as sct:
        # Capture the full screen (monitor[1] captures the primary screen)
        monitor = sct.monitors[1]
        img = np.array(sct.grab(monitor))

        # Convert BGRA to BGR for OpenCV compatibility
        img_bgr = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

        # Resize image if scale_factor is not 1.0
        if scale_factor != 1.0:
            img_bgr = cv2.resize(img_bgr, (int(monitor["width"] * scale_factor), int(monitor["height"] * scale_factor)))

        # Get the current mouse position
        mouse_x, mouse_y = pyautogui.position()

        # Draw a circle at the mouse position to represent the cursor
        cursor_radius = 10  # Larger cursor size for better visibility
        cursor_color = (0, 0, 255)  # Red color for the cursor
        cv2.circle(img_bgr, (mouse_x, mouse_y), cursor_radius, cursor_color, thickness=-1)

        return img_bgr

# Function to create a duplicated screen view (left and right)
def duplicate_screen(screen):
    # Duplicate the screen by concatenating the same image twice
    duplicated_screen = np.hstack((screen, screen))

    # Encode the image as JPEG with high quality (quality=90)
    _, jpeg = cv2.imencode('.jpg', duplicated_screen, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    return jpeg.tobytes()

# Background thread to capture frames continuously
def capture_thread():
    global latest_frame
    while True:
        frame = capture_screen()
        with capture_lock:
            latest_frame = frame
        time.sleep(0.03)  # Capture rate of approximately 30 FPS

# Route to serve the live screen as a video feed
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

# Default route to redirect to the video feed
@app.route('/')
def index():
    return redirect("/video_feed")

if __name__ == '__main__':
    # Start the capture thread
    threading.Thread(target=capture_thread, daemon=True).start()
    # Run the app on the local IP address at port 5000
    app.run(host='0.0.0.0', port=5000, debug=False)
