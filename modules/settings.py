from utils.hotkeys import check_special_chars
from utils.options import get_user_path
from utils.others import get_file_path
from utils.others import resource
import threading, time, win32gui, os
from config.setup import *
import tkinter as tk

def active_window(self, _, var):
    while var:
        if self.focused_process is not None:
            self.currently_in_foreground = "java" in self.focused_process.lower()
        time.sleep(0.1)
    self.currently_in_foreground = True
    
def thread_window(self, _, var):
    threading.Thread(target=active_window, args=(self, _, var), daemon=True).start()

def active_menu(self, _, var):
    while var:
        cursorInfo = win32gui.GetCursorInfo()[1]
        # goofy way to check if the user is in a menu, copied from another repo
        if cursorInfo > 50000 and cursorInfo < 100000:
            self.currently_in_menu = True
        else:
            self.currently_in_menu = False

        time.sleep(0.1)
    self.currently_in_menu = False

def thread_menu(self, _, var):
    threading.Thread(target=active_menu, args=(self, _, var), daemon=True).start()

def hide_taskbar(self, _, var):
    self.root.overrideredirect(var)

def dis_tooltips(self, _, var):
    self.tooltips_enabled = not var

def on_top(self, _, var):
    self.root.attributes("-topmost", var)

def reset_settings(self, _, button_name=None, text_value=None):
    try:
        os.remove(get_user_path(self.json_file))
        self.root.destroy()
    except FileNotFoundError:
        pass

def set_controls(self, _, button_name, text_value):
    popup = tk.Toplevel()
    popup.title(f"Set new Key")
    popup.geometry("400x200")
    popup.configure(bg=CONTENT_COLOR)
    popup.iconbitmap(resource(get_file_path("icon.ico")))
    popup.resizable(False, False)
    popup.attributes("-topmost", True)

    def set_key(event):
        key = event.keysym
        if key == "Escape":
            self.buttons[button_name].config(text=f"None")
            popup.destroy()
        else:
            key = key.split('_')[0]
            key = check_special_chars(key)
            self.buttons[button_name].config(text=f"[{key.upper()}]")
            popup.destroy()

    popup.bind("<KeyPress>", set_key)

    label = tk.Label(popup, text=f"Press a key", font=(FONT, 12), fg=FONT_COLOR, bg=CONTENT_COLOR)
    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    popup.focus_force()