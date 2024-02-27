import win32gui, win32process, psutil, time

def window_listener(self):
    while True:
        currentWindow = win32gui.GetForegroundWindow()
        self.focused_process = psutil.Process(win32process.GetWindowThreadProcessId(currentWindow)[-1]).name() if currentWindow else None
        time.sleep(0.5)