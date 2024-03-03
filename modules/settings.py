import threading, time, win32gui
from config.setup import *

def active_window(self, module):
    while self.module_states.get(module):
        if self.focused_process is not None:
            # maybe add this as an argument instead of hardcoding it
            if "java" in self.focused_process.lower():
                self.currently_in_foreground = True
            else:
                self.currently_in_foreground = False
        else:
            self.currently_in_foreground = False

        time.sleep(0.5)
    self.currently_in_foreground = True
    
def thread_window(self, module):
    threading.Thread(target=active_window, args=(self, module), daemon=True).start()

def active_menu(self, module):
    while self.module_states.get(module):
        cursorInfo = win32gui.GetCursorInfo()[1]
        # goofy way to check if the user is in a menu, copied from another repo
        if cursorInfo > 50000 and cursorInfo < 100000:
            self.currently_in_menu = True
        else:
            self.currently_in_menu = False
        
        time.sleep(0.2)
    self.currently_in_menu = False

def thread_menu(self, module):
    threading.Thread(target=active_menu, args=(self, module), daemon=True).start()