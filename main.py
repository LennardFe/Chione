from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.4"
    title = "Chione"
    dev = "by marshall"
    web = "https://github.com/vs-marshall/Chione"
    app = GUI(version, title, dev, web)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS I DONT CARE ABOUT:
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test).
# BUG: Modules have to be opened in the tab, to be able to be toggled.
# BUG: Always on top is buggy if minecraft is in fullscreen.
# BUG: GUI flickers white sometimes when switching tabs.

# TODO-List for Release v0.2.0:
# TODO: Rework strafing, maybe add as suboption to w-tap, s-tap?
# TODO: Self-Destruct-Button not implemented yet. i forgor
# TODO: Labels for Controls, instead of just tooltips?
# TODO: Implement S-Tap in some form?