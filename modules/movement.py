import pyautogui, keyboard, threading, time, win32api, random

def autosprint(self, module):
    shift_pressed = False
    x = 0

    while self.module_states.get(module):
        if self.only_on_active and not self.currently_in_menu:
            if keyboard.is_pressed('w'):
                pyautogui.keyDown('shift')
                shift_pressed = True
            elif shift_pressed:
                pyautogui.keyUp('shift')
                shift_pressed = False
        elif shift_pressed:
            pyautogui.keyUp('shift')
            time.sleep(0.1)
            shift_pressed = False

        x += 1
        time.sleep(0.01)

def thread_autosprint(self, module): 
    threading.Thread(target=autosprint, args=(self, module)).start()

def wtap(self, module, delay, randomize, hold):
    previous_button_state = 0  # Initialize previous button state

    while self.module_states.get(module):
        if self.only_on_active and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            # Check if state of left button has changed
            if keyboard.is_pressed("w") and ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or (self.module_states.get("LeftClicker") and left_button_state < 0)):
                pyautogui.keyDown("s")
                time.sleep(hold) 
                pyautogui.keyUp("s")

            # Update the previous button state
            previous_button_state = left_button_state

            rand_delay = (delay + random.uniform(-randomize, randomize))
            time.sleep((rand_delay) if rand_delay > 0 else 0.05)
        else:
            time.sleep(0.1)

def thread_wtap(self, module, slider, randomize, hold):
    threading.Thread(target=wtap, args=(self, module, slider, randomize, hold)).start()

def strafing(self, module, delay, randomize, hold):
    previous_button_state = 0  # Initialize previous button state

    while self.module_states.get(module):
        if self.only_on_active and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            # Check if state of left button has changed
            if keyboard.is_pressed("w") and ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or (self.module_states.get("LeftClicker") and left_button_state < 0)):
                key_to_press = random.choice(["a", "d"])  # Randomly select between "a" and "d"
                pyautogui.keyDown(key_to_press)
                time.sleep(hold)
                pyautogui.keyUp(key_to_press)

            # Update the previous button state
            previous_button_state = left_button_state

            rand_delay = (delay + random.uniform(-randomize, randomize))
            time.sleep((rand_delay) if rand_delay > 0 else 0.05)
        else:
            time.sleep(0.1)

def thread_strafing(self, module, delay, randomize, hold):
    threading.Thread(target=strafing, args=(self, module, delay, randomize, hold)).start()