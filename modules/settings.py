import threading, time, win32gui, os
from utils.options import get_user_path
from utils.others import reset
from config.setup import *

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

def reset_settings(self, _):
    try:
        os.remove(get_user_path(self.json_file))
        reset(self)
    except FileNotFoundError:
        pass