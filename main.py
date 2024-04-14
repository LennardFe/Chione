from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.7"
    title = "Chione"
    dev = "by marshall"
    app = GUI(version, title, dev)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS
# BUG: If blockhit is high, the cps will be lower than the set cps. (Blockhit delays further clicks)
# BUG: If "only in menu" is toggled, this indireclty means "only in game" is toggled too.
# BUG: All modules automatically wont work in Chione itself, to keep the proram always usable. 
    # The user has to click out of Chione to loose focus, then the modules will work.
# BUG: Only letters and numbers are allowed work for hotkeys. (no special characters)
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test).
# BUG: Modules have to be opened in the tab once, to be able to be toggled.
# BUG: Always on top is kinda buggy if minecraft is in fullscreen.
    

# Remove shaking on desktop, because no clicks are made since no window found.
# After breaking block, blockhit wont work for a few seconds. idk why.
# Weird delay for hits, when breaking blocks and allowing to eat.