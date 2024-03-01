from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.1"
    title = "Chione"
    dev = "by marshall"
    web = "https://github.com/vs-marshall/Chione"
    app = GUI(version, title, dev, web)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS I DONT CARE ABOUT:
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test)
# BUG: If you spam the hotkeys, some moduls break and keys get stuck.
# BUG: Modules have to be opened in the tab, to be able to be toggled.
# BUG: GUI flickers white sometimes when switching tabs.

# TODO-LIST:
# TODO: Add dropdown menu for selecting process to focus on (currenlty hardcoded to java, works for most clients)
# TODO: Options to set keys, like sprint to user binding --> nearly done, currently loading not working 
# TODO: Split the gui class into multiple files, to make it more readable
# TODO: Rework strafing, maybe add as suboption to w-tap, s-tap?
# TODO: Add hover information for each module
# TODO: Implement S-Tap in some form?