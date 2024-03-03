from utils.options import load_logic
from utils.options import save_logic
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd

def save_config(self, _):
    self.hotkeys_enabled = False

    filetypes = (
        ('JSON files', '*.json'),
    )

    filename = fd.asksaveasfilename(
        title='Save Configuration',
        defaultextension='.json',
        filetypes=filetypes
    )

    if filename:
        save_logic(self, filename)
        title = "Config - Success"
        message = f"Config saved to: {filename}"
    else:
        title = "Config - Error"
        message = "No file saved."

    self.hotkeys_enabled = True

    showinfo(
        title=title,
        message=message
    )

def load_config(self, _):
    self.hotkeys_enabled = False

    filetypes = (
        ('JSON files', '*.json'),
    )

    filename = fd.askopenfilename(
        title='Load Configuration',
        initialdir='/',
        filetypes=filetypes)
        
    if filename:
        load_logic(self, filename)
        title = f"Config - Success"
        message = f"Config loaded from: {filename}"
    else:
        title = "Config - Error"
        message = "No file selected."

    self.hotkeys_enabled = True

    showinfo(
        title=title,
        message=message
    )