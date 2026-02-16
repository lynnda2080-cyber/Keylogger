# Keylogger

This  is a tool designed to record every key pressed on a keyboard and save the data into a local text file. This project explores how background listeners work and how to handle low-level keyboard events in Python.

✨ Features
Modern UI: Developed with a "VS Code" dark theme using CustomTkinter.

Real-Time Monitoring: Captures standard characters and special keys (Space, Enter, etc.).

Background Execution: Uses a non-blocking listener to record keys while the GUI remains responsive.

Auto-Save: Automatically generates a key_log.txt file on the user's Desktop.

Status Indicators: Visual feedback showing whether the logger is Idle, Active, or Saved.

🛠️ Technical Stack
Language: Python 3.x

GUI Framework: CustomTkinter (Modernized Tkinter)

Library: pynput (for monitoring keyboard events)

Module: os (for cross-platform file path handling)

⚠️ ETHICAL WARNING
For Educational Purposes Only. This software is created for learning purposes within a controlled internship environment. Unauthorized use of this tool to monitor a computer without the explicit consent of the owner is illegal and unethical. By using this code, you agree to use it responsibly.

🚀 Installation & Usage
1. Clone the repository
2. Install Dependencies
Make sure you have pip installed, then run:

3. Run the App
⚙️ How it Works
The application uses two main components:

The Controller: A customtkinter class that manages the window and the "Start/Stop" logic.

The Listener: A pynput.keyboard.Listener that runs in a background thread. It detects on_press events and writes the corresponding key name or character into a file located at ~/Desktop/key_log.txt.
