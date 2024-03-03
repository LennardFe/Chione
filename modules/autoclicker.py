import random, threading, time, win32api, win32gui, win32con
from pynput.mouse import Controller

def find_win_pos():
    title = win32gui.FindWindow(None, win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    x, y = win32gui.GetCursorPos()
    rel_x, rel_y = win32gui.ScreenToClient(title, (x, y))

    param = win32api.MAKELONG(rel_x, rel_y)

    return title, param

def click_mouse(title, param, button):
    msg_down = win32con.WM_LBUTTONDOWN if button == 'left' else win32con.WM_RBUTTONDOWN
    msg_up = win32con.WM_LBUTTONUP if button == 'left' else win32con.WM_RBUTTONUP
    state = win32con.MK_LBUTTON if button == 'left' else win32con.MK_RBUTTON

    win32api.SendMessage(title, msg_down, state, param)
    win32api.SendMessage(title, msg_up, state, param)  

def shake_effect(shake):
    if shake == 0:
        return None

    currentPos = win32api.GetCursorPos() 
    
    direction = random.randint(0, 3)
    pixels = random.randint(-shake, shake)
    
    direction_map = {
        0: (1, -1),
        1: (-1, 1),
        2: (1, 1),
        3: (-1, -1)
    }
    
    x_adjust, y_adjust = direction_map[direction]
    new_pos = (currentPos[0] + x_adjust * pixels, currentPos[1] + y_adjust * pixels)
    win32api.SetCursorPos(new_pos)

def leftclick(self, module, clicks_per_second, randomize, shake, hold, blockhit, button):
    last_blockhit_time = 0

    while self.module_states.get(module):
        interval = None
        left_button_state = win32api.GetAsyncKeyState(0x01) & 0x8000        
        if self.currently_in_foreground and not self.currently_in_menu:
            if hold and left_button_state:
                rand_cps = clicks_per_second + random.randint(-randomize, randomize)
                interval = 1 / ((rand_cps) if rand_cps > 0 else 1)
                title, param = find_win_pos()
                click_mouse(title, param, button)
                current_time = time.time()  # Get the current time
                if blockhit and (current_time - last_blockhit_time >= (1 + (random.randint(-1,1))/5)):  # Check if 1 second has elapsed
                    click_mouse(title, param, button="right")
                    last_blockhit_time = current_time
                shake_effect(shake)

            elif not hold:
                interval = random.uniform(0.4, 1.6) / clicks_per_second if randomize else 1 / clicks_per_second
                title, param = find_win_pos()
                click_mouse(title, param, button)
                current_time = time.time() 
                if blockhit and current_time - last_blockhit_time >= 1:  # Check if 1 second has elapsed
                    click_mouse(title, param, button="right")
                    last_blockhit_time = current_time 
                shake_effect(shake)
            
            time.sleep(interval) if interval is not None else time.sleep(0.1)
        else:
            time.sleep(0.1)

def thread_lclick(self, module, slider, randomize, shake, hold, blockhit, button="left"):
    threading.Thread(target=leftclick, args=(self, module, slider, randomize, shake, hold, blockhit, button), daemon=True).start()

def rightclick(self, module, clicks_per_second, randomize, shake, hold, button):
    while self.module_states.get(module):
        interval = None
        right_button_state = win32api.GetAsyncKeyState(0x02)&0x8000
        if self.currently_in_foreground and not self.currently_in_menu:
            if hold and right_button_state:
                rand_cps = clicks_per_second + random.randint(-randomize, randomize)
                interval = 1 / ((rand_cps) if rand_cps > 0 else 1)
                title, param = find_win_pos()
                click_mouse(title, param, button)   
                shake_effect(shake)

            elif not hold:
                interval = random.uniform(0.4, 1.6) / clicks_per_second if randomize else 1 / clicks_per_second
                title, param = find_win_pos()
                click_mouse(title, param, button) 
                shake_effect(shake)
            
            time.sleep(interval) if interval is not None else time.sleep(0.1)

def thread_rclick(self, module, slider, randomize, shake, hold, button="right"):
    threading.Thread(target=rightclick, args=(self, module, slider, randomize, shake, hold, button), daemon=True).start()