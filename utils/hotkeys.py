from utils.others import get_file_path
from utils.others import resource
from utils.executor import *
from config.setup import *
import tkinter as tk

def set_hotkey(self, button, module):
    popup = tk.Toplevel()
    popup.title("Set Hotkey")
    popup.geometry("400x200")
    popup.configure(bg=CONTENT_COLOR)
    popup.iconbitmap(resource(get_file_path("icon.ico")))
    popup.resizable(False, False)
    popup.attributes("-topmost", True)  # ensure the popup stays on top

    def set_hotkey(event):
        key = event.keysym
        if key == "Escape":
            self.modules[module]["hotkey"] = "None"
            button.config(text="Bind Hotkey")
            popup.destroy()
        else:
            self.modules[module]["hotkey"] = key
            button.config(text=(f"Key: [{(key).upper()}]"))
            popup.destroy()

    popup.bind("<KeyPress>", set_hotkey)

    label = tk.Label(popup, text="Press a key", font=(FONT, 12), fg=FONT_COLOR, bg=CONTENT_COLOR)
    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    popup.focus_force()

def on_key_press(self, key):
    try: # Convert the key to a string representation   
        key_char = key.char
    except AttributeError: # Handle special keys like Shift, Alt, etc.
        key_char = str(key)

    # Check if the pressed key matches any hotkey
    for module, data in self.modules.items():
        if data["hotkey"] != False:
            if "hotkey" in data and data["hotkey"].lower() == key_char.lower():
                if self.hotkeys_enabled:
                    toggle_and_execute(self, module)