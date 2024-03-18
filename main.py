from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.5"
    title = "Chione"
    dev = "by marshall"
    web = "https://github.com/vs-marshall/Chione"
    app = GUI(version, title, dev, web)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS I DONT CARE ABOUT:
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test).
# BUG: If "only in menu" is toggled, this automatically means "only in focus".
# BUG: Modules have to be opened in the tab once, to be able to be toggled.
# BUG: Always on top is buggy if minecraft is in fullscreen.
# BUG: GUI flickers white sometimes when switching tabs.

# TODO-List for Release v0.2.0:
    # GUI:
    # TODO: Create custom checkboxes, to make the gui look better.

    # Modules:
    # TODO: What to do with strafing, unhappy with its current state.
    # TODO: Add three options to Sprint Reset: W, S and Crouch
    # TODO: Add clicker patterns, like jitter, butterfly, etc.
    # TODO: Add sound to autoclicker