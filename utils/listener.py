import win32gui, win32process, psutil, time

def window_listener(self):
    while True:
        currentWindow = win32gui.GetForegroundWindow()
        self.focused_process = psutil.Process(win32process.GetWindowThreadProcessId(currentWindow)[-1]).name() if currentWindow else None
        self.currently_in_foreground = False if self.focused_process == "python.exe" else True # so the user can still use the GUI 
        time.sleep(0.5)