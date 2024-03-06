import pyautogui, keyboard, threading, time, win32api, random
from utils.hotkeys import get_controls

def autosprint(self, module):
    shift_pressed = False

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            if keyboard.is_pressed(get_controls(self, "Controls_1", "W")):
                pyautogui.keyDown(get_controls(self, "Controls_0", "SHIFT"))
                shift_pressed = True
            elif shift_pressed:
                pyautogui.keyUp(get_controls(self, "Controls_0", "SHIFT"))
                shift_pressed = False
        elif shift_pressed:
            pyautogui.keyUp(get_controls(self, "Controls_0", "SHIFT"))
            time.sleep(0.1)
            shift_pressed = False

        # Sleep to reduce CPU usage
        time.sleep(0.01)

def thread_autosprint(self, module): 
    threading.Thread(target=autosprint, args=(self, module), daemon=True).start()

def wtap(self, module, delay, randomize, hold):
    previous_button_state = 0 

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            # Check if W Key is pressed and state of left button has changed
            if keyboard.is_pressed(get_controls(self, "Controls_1", "W")) and ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or (self.module_states.get("LeftClicker") and left_button_state < 0)):
                keyboard.block_key(get_controls(self, "Controls_1", "W")) # Block the w key to prevent user inputs
                pyautogui.keyUp(get_controls(self, "Controls_1", "W"))
                time.sleep(hold) 
                keyboard.unblock_key(get_controls(self, "Controls_1", "W")) # Unblock or no w for you lol
                if keyboard.is_pressed(get_controls(self, "Controls_1", "W")):  # Make sure the w key is still pressed by the user
                    pyautogui.keyDown(get_controls(self, "Controls_1", "W"))

            # Update the previous button state
            previous_button_state = left_button_state

            # Sleep for a (random) amount of time
            rand_delay = (delay + random.uniform(-randomize, randomize))
            time.sleep((rand_delay) if rand_delay > 0 else 0.05)
        else:
            time.sleep(0.1) # Sleep to reduce CPU usage

def thread_wtap(self, module, slider, randomize, hold):
    threading.Thread(target=wtap, args=(self, module, slider, randomize, hold), daemon=True).start()

def strafing(self, module, delay, randomize, hold):
    last_key_pressed = random.choice([get_controls(self, "Controls_2", "a"), get_controls(self, "Controls_4", "d")])
    previous_button_state = 0  

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            # Check if W Key is pressed and state of left button has changed
            if keyboard.is_pressed(get_controls(self, "Controls_1", "W")) and ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or (self.module_states.get("LeftClicker") and left_button_state < 0)):
                key_to_press = get_controls(self, "Controls_4", "D") if last_key_pressed == get_controls(self, "Controls_2", "A") else get_controls(self, "Controls_2", "A")

                pyautogui.keyDown(key_to_press)
                time.sleep(hold)
                pyautogui.keyUp(key_to_press)

                # Update the last pressed key
                last_key_pressed = key_to_press

            # Update the previous button state
            previous_button_state = left_button_state

            # Sleep for a (random) amount of time
            rand_delay = (delay + random.uniform(-randomize, randomize))
            time.sleep((rand_delay) if rand_delay > 0 else 0.05)
        else:
            time.sleep(0.1) # Sleep to reduce CPU usage

def thread_strafing(self, module, delay, randomize, hold):
    threading.Thread(target=strafing, args=(self, module, delay, randomize, hold), daemon=True).start()