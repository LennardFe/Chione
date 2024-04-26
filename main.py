from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1.8"
    title = "Chione"
    dev = "by marshall"
    app = GUI(version, title, dev)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# KNOWN-BUGS
# BUG: If blockhit is high, the cps will be lower than the set cps. (Blockhit delays further clicks)
# BUG: If "only in menu" is toggled, this indireclty means "only in game" is toggled too.
# BUG: All modules automatically wont work in Chione itself, to keep the program always usable. 
    # The user has to click out of Chione to loose focus, then the modules will work.
# BUG: AC-Shaking not working in Badlion-Client (possibly others too, didn't test).
# BUG: Modules have to be opened in the tab once, to be able to be toggled.
# BUG: Weird delay for hits, when breaking blocks and allowing to eat.