import win32gui, win32process, psutil, time

def window_listener(self):
    while True:
        currentWindow = win32gui.GetForegroundWindow()
        self.focused_process = psutil.Process(win32process.GetWindowThreadProcessId(currentWindow)[-1]).name() if currentWindow else None
        self.currently_in_foreground = False if self.focused_process is None or self.focused_process.lower() == "python.exe" or self.focused_process.lower() == "chione.exe" else True
        time.sleep(0.5)