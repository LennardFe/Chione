import threading, time, win32gui
from config.setup import *
import tkinter as tk

def active_window(self, module):
    while self.module_states.get(module):
        if self.focused_process is not None:
            if "java" in self.focused_process.lower():
                self.only_on_active = True
            else:
                self.only_on_active = False
        else:
            self.only_on_active = False

        time.sleep(0.5)
    self.only_on_active = True
    
def thread_window(self, module):
    threading.Thread(target=active_window, args=(self, module), daemon=True).start()

def active_menu(self, module):
    while self.module_states.get(module):
        cursorInfo = win32gui.GetCursorInfo()[1]
        if cursorInfo > 50000 and cursorInfo < 100000:
            self.currently_in_menu = True
        else:
            self.currently_in_menu = False
        
        time.sleep(0.2)
    self.currently_in_menu = False

def thread_menu(self, module):
    threading.Thread(target=active_menu, args=(self, module), daemon=True).start()

def controls(self, module, name, text, old_key):
    popup = tk.Toplevel()
    popup.title(f"Set Key for {text}")
    popup.geometry("400x200")
    popup.configure(bg=CONTENT_COLOR)
    #popup.iconbitmap("assets\icon.ico")
    popup.resizable(False, False)
    popup.attributes("-topmost", True)  # ensure the popup stays on top

    def set_key(event):
        key = event.keysym
        if key == "Escape":
            self.buttons[name].config(text=f"{text}: None")
            popup.destroy()
        else:
            self.buttons[name].config(text=f"{text}: [{key.upper()}]")
            popup.destroy()

    popup.bind("<KeyPress>", set_key)

    label = tk.Label(popup, text=f"Press a key for {text}", font=(FONT, 12), fg=FONT_COLOR, bg=CONTENT_COLOR)
    label.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    popup.focus_force()