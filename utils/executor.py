import time

last_key_press_time = 0.0
spam_delay = 0.25

def toggle_and_execute(self, module):
    global last_key_press_time
    current_time = time.time()

    if current_time - last_key_press_time >= spam_delay: # prevent spamming
        last_key_press_time = current_time
        try:
            new_state = not self.module_states.get(module, False)
            button = self.toggle_buttons[module]
            command = self.modules[module]["command"]
            params = get_params(self, self.modules[module]["params"], module)

            try:
                button.config(image=self.on if new_state else self.off)
            except:
                pass  # Ignore any errors during image configuration

            self.module_states[module] = new_state

            if new_state:
                command(self, module, *params)

        except Exception as e:
            print(f"Exception: {e} with module {module}") # If options page has not been opened yet, module cant be loaded

def retoggle(self, module):
    # TODO not the nicest solution
    if self.module_states.get(module):
        button = self.toggle_buttons[module]
        self.module_states[module] = False
        button.config(image=self.off)
        time.sleep(0.1)
        toggle_and_execute(self, module)
        
def get_params(self, funs, module):
    params = []
    number = 0
    prev_fun = None  # variable to store the previous function name
    for fun_name in funs:
        # check if the function exists as a method of this class
        if hasattr(self, fun_name) and callable(getattr(self, fun_name)):
            # get the function object using its name
            fun = getattr(self, fun_name)
            # check if this is the first iteration or if the current function is different from the previous one
            if prev_fun is None or fun_name != prev_fun:
                number = 0  # reset index amount to 0
            prev_fun = fun_name  # update the previous function name
            # call the function with the module parameter
            result = fun(module, number)
            params.append(result)
            number = number + 1
        else:
            print(f"Function '{fun_name}' not found in the class.")
    return params