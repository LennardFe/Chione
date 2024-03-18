import threading, time, pyautogui, random, os, sys
from utils.options import get_user_path
from utils.options import save_settings
from utils.hotkeys import get_controls

def anti_afk(self, module, timer, randomize):
    while self.module_states.get(module):
        timer = timer + random.randint(-randomize, randomize)
        timer = 1 if timer < 1 else timer

        time.sleep(timer)
        pyautogui.keyDown(get_controls(self, "Controls_2", "W"))
        pyautogui.keyUp(get_controls(self, "Controls_2", "W"))
        pyautogui.keyDown(get_controls(self, "Controls_4", "S"))
        pyautogui.keyUp(get_controls(self, "Controls_4", "S"))

def thread_antiafk(self, module, timer, randomize):
    threading.Thread(target=anti_afk, args=(self, module, timer, randomize), daemon=True).start()

def selfdestruct(self, _, delete_everything):
    if delete_everything:
        os.remove(get_user_path(self.json_file))
        os.remove(os.path.dirname(sys.argv[0]))
        self.root.destroy()
    else:
        save_settings(self, self.json_file)
        self.root.destroy()