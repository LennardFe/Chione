from gui.gui_manager import GUI
from tkinter import *

def main():
    version = "0.1"
    title = "Chione"
    dev = "by marshall"
    web = "https://github.com/vs-marshall/Chione"
    app = GUI(version, title, dev, web)
    app.root.mainloop()

if __name__ == "__main__":
    main()

# TODO: Options to set keys, like sprint etc. --> nearly done, currently loading not working correctly
# TODO: Split the gui class into multiple files, to make it more readable
# TODO: Loading toggelt not working correctly
# TODO: Shaking not working in badlion client
# TODO: Clean up code