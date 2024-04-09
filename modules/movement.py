import pyautogui, keyboard, threading, time, win32api, random
from utils.hotkeys import get_controls

def autosprint(self, module):
    shift_pressed = False

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            if keyboard.is_pressed(get_controls(self, "Controls_2", "W")):
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

def get_key_for_mode(mode):
    mapping = {
        "W-Tap": {"control": "Controls_2", "key": "W"},
        "S-Tap": {"control": "Controls_4", "key": "S"},
        "Crouch": {"control": "Controls_1", "key": "CTRL"}
    }
    return mapping.get(mode)

def sprintreset(self, module, delay, randomize, hold, mode):
    previous_button_state = 0 

    control, key = get_key_for_mode(mode).values()

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            hold_lc = self.get_checkbox_value("LeftClicker", 0) # Get if hold left click is enabled, risky since the 0 is hardcoded

            if (keyboard.is_pressed(get_controls(self, "Controls_2", "W")) and                                      # Check if W Key is pressed, always has to be pressed, then one of the following conditions has to be true
                ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or  # Check if the state of the left button has changed
                (self.module_states.get("LeftClicker") and hold_lc and left_button_state < 0) or                    # Alternatively, check if the left button is pressed while left clicker is enabled and hold left click is enabled
                (self.module_states.get("LeftClicker") and not hold_lc))):                                          # Alternatively, check if left clicker is enabled

                if(mode == "W-Tap"): # More complex logic for W-Tap, since we have to workaround the user input
                    keyboard.block_key(get_controls(self, control, key)) # Block the w key to prevent user inputs
                    pyautogui.keyUp(get_controls(self, control, key))
                    time.sleep(hold) 
                    keyboard.unblock_key(get_controls(self, control, key)) # Unblock or no w for you lol
                    if keyboard.is_pressed(get_controls(self, control, key)):  # Make sure the w key is still pressed by the user
                        pyautogui.keyDown(get_controls(self, control, key))
                        
                elif(mode == "S-Tap" or mode == "Crouch"):
                    pyautogui.keyDown(get_controls(self, control, key))
                    time.sleep(hold)
                    pyautogui.keyUp(get_controls(self, control, key))

            # Update the previous button state
            previous_button_state = left_button_state

            # Sleep for a (random) amount of time
            rand_delay = (delay + random.uniform(-randomize, randomize))
            time.sleep((rand_delay) if rand_delay > 0 else 0.05)
        else:
            time.sleep(0.1) # Sleep to reduce CPU usage

def thread_sprintreset(self, module, slider, randomize, hold, mode):
    threading.Thread(target=sprintreset, args=(self, module, slider, randomize, hold, mode), daemon=True).start()

def strafing(self, module, delay, randomize, hold, randomize_direction):
    last_key_pressed = random.choice([get_controls(self, "Controls_3", "a"), get_controls(self, "Controls_5", "d")])
    previous_button_state = 0  

    while self.module_states.get(module):
        if self.currently_in_foreground and not self.currently_in_menu:
            left_button_state = win32api.GetKeyState(0x01)

            hold_lc = self.get_checkbox_value("LeftClicker", 0) # Get if hold left click is enabled, risky since the 0 is hardcoded

            # Check if W Key is pressed and state of left button has changed
            if (keyboard.is_pressed(get_controls(self, "Controls_2", "W")) and                                      # Check if W Key is pressed, always has to be pressed, then one of the following conditions has to be true
                ((((not self.module_states.get("LeftClicker")) and previous_button_state != left_button_state)) or  # Check if the state of the left button has changed
                (self.module_states.get("LeftClicker") and hold_lc and left_button_state < 0) or                    # Alternatively, check if the left button is pressed while left clicker is enabled and hold left click is enabled
                (self.module_states.get("LeftClicker") and not hold_lc))):                                          # Alternatively, check if left clicker is enabled

                if not randomize_direction: # If randomize direction is disabled, strafe in the opposite direction as the last key
                    key_to_press = get_controls(self, "Controls_5", "D") if last_key_pressed == get_controls(self, "Controls_3", "A") else get_controls(self, "Controls_3", "A")
                else:
                    key_to_press = random.choice([get_controls(self, "Controls_3", "a"), get_controls(self, "Controls_5", "d")])

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

def thread_strafing(self, module, delay, randomize, hold, randomize_direction):
    threading.Thread(target=strafing, args=(self, module, delay, randomize, hold, randomize_direction), daemon=True).start()