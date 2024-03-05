import threading, time, pyautogui, random
from utils.options import save_settings

def anti_afk(self, module, timer, randomize):
    while self.module_states.get(module):
        timer = timer + random.randint(-randomize, randomize)
        timer = 1 if timer < 1 else timer

        time.sleep(timer)
        pyautogui.keyDown("w")
        pyautogui.keyUp("w")
        pyautogui.keyDown("s")
        pyautogui.keyUp("s")

def thread_antiafk(self, module, timer, randomize):
    threading.Thread(target=anti_afk, args=(self, module, timer, randomize), daemon=True).start()

def selfdestruct(self, _, delete_everything, safe_cleanup):
    save_settings(self, self.json_file)
    self.root.destroy()
    if delete_everything:
        # delete all config files
        # delete the program itself
        pass
    if safe_cleanup:
        # check for tmp-files and other stuff
        pass