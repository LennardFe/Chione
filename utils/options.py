import json, re, os

def get_user_path(json_file):
    filename = os.path.basename(json_file)
    home_directory = os.path.expanduser("~")
    option_path = os.path.join(home_directory, filename)
    return option_path

def load_logic(self, path):
    with open(path, 'r') as file:
        modules_data = json.load(file)

    for module_data in modules_data:
        module_name = module_data.get("name")
        module = self.modules.get(module_name)

        if module:
            module["hotkey"] = module_data.get("hotkey", False)
            sliders_count = module.get("slider", 0)
            checkboxes_count = module.get("checkbox", 0)
            buttons_count = module.get("button", 0)

            for x in range(sliders_count):
                slider_key = f"{module_name}_{x}"
                self.sliders[slider_key] = module_data.get(f"slider_{x}", False)

            for x in range(checkboxes_count):
                checkbox_key = f"{module_name}_{x}"
                self.checkboxs[checkbox_key] = module_data.get(f"checkbox_{x}", False)

            for x in range(buttons_count):
                button_key = f"{module_name}_{x}"
                self.buttons[button_key] = module_data.get(f"button_{x}", False)

        else:
            print(f"Module {module_name} not found in the class.")

def load_settings(self, json_file):
    user_path = get_user_path(json_file)
    
    try:
        load_logic(self, user_path)
    except FileNotFoundError:   # Fallback to original file path
        load_logic(self, json_file)

def save_logic(self, path):
    modules_data = []

    for module_name, module_info in self.modules.items():
        module_data = {
            "name": module_name,
            "hotkey": module_info.get("hotkey", False),
        }

        # Include slider data
        for x in range(module_info.get("slider", 0)):
            slider = self.sliders.get(f"{module_name}_{x}")
            module_data[f"slider_{x}"] = slider if isinstance(slider, (int, float)) else (slider.get() if slider else None)

        # Include checkbox data
        for x in range(module_info.get("checkbox", 0)):
            checkbox = self.checkboxs.get(f"{module_name}_{x}")
            module_data[f"checkbox_{x}"] = checkbox if isinstance(checkbox, bool) else (checkbox.get() if checkbox else None)

        # Check if the module has a button, then include button data
        for x in range(module_info.get("button", 0)):
            button_text = self.buttons.get(f"{module_name}_{x}")
            module_data[f"button_{x}"] = button_text if isinstance(button_text, str) else (re.search(r'\[([^\]]+)\]', button_text.cget("text")).group(1)) if button_text else None

        # Append module data to the list
        modules_data.append(module_data)
    
    # Write module data to the options file
    with open(path, 'w') as file:
        json.dump(modules_data, file, indent=4)

def save_settings(self, json_file):
    user_path = get_user_path(json_file)
    save_logic(self, user_path)
    self.root.destroy()