import win32gui, win32process, psutil, time
from config.modules import modules

def window_listener(self):
    while True:
        currentWindow = win32gui.GetForegroundWindow()
        self.focused_process = psutil.Process(win32process.GetWindowThreadProcessId(currentWindow)[-1]).name() if currentWindow else None
        self.currently_in_foreground = False if self.focused_process.lower() == "python.exe" or self.focused_process.lower() == "chione.exe" else True # so the user can still use the GUI 
        time.sleep(0.5)

def set_settings(self):
    # TODO: fix this, thats some shit code, i was drunk while writing this
    general_checkboxes = {key: value for key, value in self.checkboxs.items() if key.startswith('General')}
    for key, value in general_checkboxes.items():
        module = key.split('_')[0]
        number = int(key.split('_')[-1]) # careful
        module_name = self.modules.get(module)
        cb_command = module_name.get(f"checkbox_command{number+1}")
        if isinstance(value, bool):
            cb_command(self, module, value)
        else:
            cb_command(self, module, value.get())