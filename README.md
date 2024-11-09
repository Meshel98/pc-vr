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

### Highlights:
- Emojis for visual appeal.
- Organized sections for readability.
- Example commands formatted as code blocks.
- A professional structure for developers exploring your repository.

Feel free to replace placeholders (`your-username`, `your.email@example.com`, etc.) with your actual information!

![Skärmbild (393)](https://github.com/user-attachments/assets/340adb24-dfb1-46b1-9e9f-3af2adc94f31)
