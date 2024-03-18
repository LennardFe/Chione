import tkinter as tk

def move_window(self, event):
    self.root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))

def new_titlebar(self):
    #TODO: Create custom titlebar
    pass