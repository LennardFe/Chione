import random, threading, time, win32api, win32gui, win32con

def find_win_pos():
    title = win32gui.FindWindow(None, win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    x, y = win32gui.GetCursorPos()
    rel_x, rel_y = win32gui.ScreenToClient(title, (x, y))

    param = win32api.MAKELONG(rel_x, rel_y)

    return title, param

def click_mouse(title, param, button, bblock = None):
    if not bblock or bblock is None:
        msg_down = win32con.WM_LBUTTONDOWN if button == 'left' else win32con.WM_RBUTTONDOWN
        msg_up = win32con.WM_LBUTTONUP if button == 'left' else win32con.WM_RBUTTONUP
        state = win32con.MK_LBUTTON if button == 'left' else win32con.MK_RBUTTON

        win32api.SendMessage(title, msg_down, state, param)
        win32api.SendMessage(title, msg_up, state, param) 

    else:
        msg_down_bb = win32con.MOUSEEVENTF_LEFTDOWN if button == 'left' else win32con.MOUSEEVENTF_RIGHTDOWN
        win32api.mouse_event(msg_down_bb, 0, 0) 

        #msg_down_bb = win32con.WM_LBUTTONDOWN if button == 'left' else win32con.WM_RBUTTONDOWN
        #win32api.SendMessage(title, msg_down_bb, 0, 0)

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

def interval_calculator(cps, randomize, bblock):
    rand_cps = cps + random.randint(-randomize, randomize)

    # Difference in 1.1 and 0.9 to equalize them, since the execution time varies for the bblock and non-bblock
    if bblock:
        interval = 1.1 / ((rand_cps) if rand_cps > 0 else 1)
        return interval
    else:
        interval = 0.95 / ((rand_cps) if rand_cps > 0 else 1)
        return interval

def leftclick(self, module, clicks_per_second, randomize, shake, blockhit, hold, bblock, button):
    while self.module_states.get(module):
        interval = None
        left_button_state = win32api.GetAsyncKeyState(0x01) & 0x8000
        if self.currently_in_foreground and not self.currently_in_menu:
            if hold and left_button_state:
                interval = interval_calculator(clicks_per_second, randomize, bblock)
                title, param = find_win_pos()
                click_mouse(title, param, button, bblock)
                if (random.randint(1, 200) <= blockhit):  # 200 so it's not too often
                    click_mouse(title, param, "right")
                shake_effect(shake)

            elif not hold:
                interval = interval_calculator(clicks_per_second, randomize, bblock)
                title, param = find_win_pos()
                click_mouse(title, param, button, bblock)
                if random.randint(1, 200) <= blockhit:  # 200 so it's not too often
                    click_mouse(title, param, "right")
                shake_effect(shake)
            
            time.sleep(interval) if interval is not None else time.sleep(0.1)
        else:
            time.sleep(0.1)

    # Stop left holding
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def thread_lclick(self, module, slider, randomize, shake, blockhit, hold, bblock, button="left"):
    threading.Thread(target=leftclick, args=(self, module, slider, randomize, shake, blockhit, hold, bblock, button), daemon=True).start()

def rightclick(self, module, clicks_per_second, randomize, shake, hold, eat, button):
    while self.module_states.get(module):
        interval = None
        right_button_state = win32api.GetAsyncKeyState(0x02) & 0x8000
        if self.currently_in_foreground and not self.currently_in_menu:
            if hold and right_button_state:
                interval = interval_calculator(clicks_per_second, randomize, eat)
                title, param = find_win_pos()
                click_mouse(title, param, button, eat)
                shake_effect(shake)

            elif not hold:
                interval = interval_calculator(clicks_per_second, randomize, eat)
                title, param = find_win_pos()
                click_mouse(title, param, button, eat)
                shake_effect(shake)
            
            time.sleep(interval) if interval is not None else time.sleep(0.1)
        else:
            time.sleep(0.1)

    # Stop right holding
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def thread_rclick(self, module, slider, randomize, shake, hold, eat, button="right"):
    threading.Thread(target=rightclick, args=(self, module, slider, randomize, shake, hold, eat, button), daemon=True).start()