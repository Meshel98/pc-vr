# 🎥 Screen Mirroring and Duplication Server

A Python-based application for capturing, duplicating, and streaming your computer's screen in real-time over a local network. The server displays a **side-by-side duplication** of the screen and highlights the **mouse cursor** with a red circle for better visibility. 🖥️

---

## ✨ Features

- 📡 **Real-time Screen Capture**: Captures the primary monitor using `mss`.
- 🖼️ **Screen Duplication**: Streams a side-by-side duplication of your screen.
- 🎯 **Mouse Cursor Tracking**: Highlights the mouse cursor with a red circle for clarity.
- 🌐 **Web-based Streaming**: Streams the screen as an MJPEG feed accessible in any web browser.
- 🔧 **Customizable Scale**: Adjust the resolution of the captured screen for performance.

---

## 🛠️ Technologies Used

- **Python Libraries**:
  - `cv2 (OpenCV)` - Image processing and video encoding.
  - `numpy` - Array manipulations.
  - `flask` - Lightweight web server for streaming.
  - `pyautogui` - Mouse cursor tracking.
  - `mss` - High-performance screen capturing.

---

## 🚀 Getting Started

### 1️⃣ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/screen-mirroring-server.git
   cd screen-mirroring-server
Install the required Python dependencies:

bash
Kopiera kod
pip install -r requirements.txt
Contents of requirements.txt:

Kopiera kod
flask
opencv-python
numpy
pyautogui
mss
2️⃣ Usage
Run the application:

bash
Kopiera kod
python server.py
Open your web browser and visit:

arduino
Kopiera kod
http://<your-computer-ip>:5000
Replace <your-computer-ip> with the local IP address of your computer.

🎥 Enjoy the real-time screen duplication!
🔍 Preview
Real-time Screen Feed:
🖥️ Live View: The /video_feed endpoint streams your screen in real-time.
🔄 Side-by-side Duplication: Enhances visibility by duplicating the screen horizontally.
🎯 Mouse Tracking: Highlights the mouse cursor for added clarity.
⚠️ Limitations
High CPU Usage: Continuous screen capture and streaming may consume significant resources.
No Security: The stream is accessible to anyone on the network without authentication.
Browser Compatibility: Ensure your browser supports MJPEG streaming.
🤝 Contributing
Contributions are welcome! Feel free to:

🐛 Report bugs
🚀 Suggest new features
📥 Submit pull requests
📜 License
This project is licensed under the MIT License. See the LICENSE file for more information.

💡 Author
Your Name
📧 Email: your.email@example.com
🌐 GitHub: your-username
📝 Notes
Have fun streaming your screen in real-time! If you encounter issues or have questions, feel free to open an issue in this repository. 😊

markdown
Kopiera kod

### Highlights:
- Emojis for visual appeal.
- Organized sections for readability.
- Example commands formatted as code blocks.
- A professional structure for developers exploring your repository.

Feel free to replace placeholders (`your-username`, `your.email@example.com`, etc.) with your actual information!

![Skärmbild (393)](https://github.com/user-attachments/assets/340adb24-dfb1-46b1-9e9f-3af2adc94f31)
