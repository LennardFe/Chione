from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.2"
    title = "Chione"
    dev = "by marshall"
    web = "https://github.com/vs-marshall/Chione"
    app = GUI(version, title, dev, web)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS I DONT CARE ABOUT:
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test).
# BUG: If you spam the hotkeys, some moduls break and keys get stuck.
# BUG: Modules have to be opened in the tab, to be able to be toggled.
# BUG: GUI flickers white sometimes when switching tabs.

# TODO-List for Full Release v1.0.0:
# TODO: Options to set keys, like sprint to user binding --> nearly done, currently loading not working 
# TODO: Rework strafing, maybe add as suboption to w-tap, s-tap?
# TODO: AC - Convert BlockHit Checkbox to a slider?
# TODO: Add delay to hotkey, to prevent spamming
# TODO: Implement S-Tap in some form?
# TODO: Add sounds for AutoClicker