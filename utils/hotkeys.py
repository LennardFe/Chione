from tkinter.messagebox import showinfo
from utils.others import get_file_path
from utils.others import resource
from utils.executor import *
from config.setup import *
import tkinter as tk
import re

def set_hotkey(self, button, module):
    self.hotkeys_enabled = False
    popup = tk.Toplevel()
    popup.title("Set Hotkey")
    popup.geometry("400x200")
    popup.configure(bg=CONTENT_COLOR)
    popup.iconbitmap(resource(get_file_path("icon.ico")))
    popup.resizable(False, False)
    popup.attributes("-topmost", True)  # Ensure the popup stays on top

    def set_hotkey(event):
        key = event.keysym
        if key == "Escape":
            self.modules[module]["hotkey"] = "None"
            button.config(text="Bind Hotkey")
            popup.destroy()
        elif key.isalnum() and len(key) == 1: # Only letters and numbers allowed
            if check_if_already_in_use(self, key):
                showinfo("Error", "This hotkey is already in use.")
                popup.focus_force()
                return
            
            self.modules[module]["hotkey"] = key
            button.config(text=(f"Key: [{(key).upper()}]"))
            popup.destroy()
        else:
            showinfo("Error", "Only letters and numbers are allowed for hotkeys.")
            popup.focus_force()

        self.hotkeys_enabled = True

    def on_closing():
        self.hotkeys_enabled = True
        popup.destroy()

    # Make sure that hotkeys are enabled when the popup is closed
    popup.protocol("WM_DELETE_WINDOW", on_closing)

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

def check_if_already_in_use(self, key):
    for module, data in self.modules.items():
        if data["hotkey"] != False:
            if "hotkey" in data and data["hotkey"].lower() == key.lower():
                return True
    return False

def get_controls(self, action_key, default):
    key = self.buttons.get(action_key, default)
    if key == "None" or key is None:
        return default
    
    if isinstance(key, str):
        key = re.sub(r'^\[|\]$', '', key)
        return key
    else:
        key_text = key.cget("text")
        key_text = re.sub(r'^\[|\]$', '', key_text)
        return key_text
    
def check_special_chars(key):
    # Goofy solution, the problem is tkinter and pyautogui use different names for the same key
    if key == "Control": return "ctrl"
    elif key == "Caps": return "capslock"
    else: return key 