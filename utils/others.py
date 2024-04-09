import webbrowser, sys, os, pyautogui, random, time, keyboard

def open_web(url):
    webbrowser.open_new(url)

def resource(relative_path):
    base_path = getattr(
        sys,
        '_MEIPASS',
        os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def get_file_path(filename):
    # Get the directory of the executable or the script
    if getattr(sys, 'frozen', False):  # If the application is frozen (compiled)
        # If frozen, use sys._MEIPASS to get the base directory
        base_dir = sys._MEIPASS
        file_path = os.path.join(base_dir, filename)
    else:
        # If running in a script, use the directory of the script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(base_dir)
        file_path = os.path.join(parent_dir, "assets", filename)
    
    return file_path

def set_settings(self):
    # TODO: Goofy code, needs to be reworked
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