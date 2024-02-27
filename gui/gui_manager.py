# Internal Imports - Utils
from utils.hotkeys import set_hotkey, on_key_press
from utils.listener import window_listener
from utils.options import load_settings
from utils.options import save_settings
from utils.process import check_minecraft
from utils.executor import toggle_and_execute
from utils.executor import retoggle
from utils.others import get_file_path
from utils.others import open_web
from utils.others import resource

# Internal Imports - Configs
from config.categories import ModuleCategory
from config.modules import modules
from config.setup import *

# Third-party Library Imports
from pynput import keyboard

# Standard Library Imports
import tkinter as tk
import threading

class GUI: 
    def __init__(self, version, title, dev, web):
        # Initialize attributes
        self.version = version
        self.title = title
        self.dev = dev
        self.web = web
        self.modules = modules
        self.buttons = {}
        self.sliders = {}
        self.checkboxs = {}
        self.toggle_buttons = {}
        self.module_states = {module: False for module in self.modules}

        # Declare json file path for saving and loading setting
        self.json_file = resource(get_file_path("options.json"))

        # Create the Tkinter root window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.minsize(MIN_SIZE_W, MIN_SIZE_H)
        self.root.geometry(WINDOW_SIZE)
        self.root.configure(bg=CONTENT_COLOR)
        self.root.iconbitmap(resource(get_file_path("icon.ico")))
        self.root.protocol("WM_DELETE_WINDOW", lambda: save_settings(self, self.json_file))

        # Load GUI assets
        self.on = tk.PhotoImage(file=resource(get_file_path("on.png")))
        self.off = tk.PhotoImage(file=resource(get_file_path("off.png")))

        # Set up keyboard listener
        self.listener = keyboard.Listener(on_press=lambda key: on_key_press(self, key))
        self.listener.start()

        # Set up window listener
        self.focused_process = None
        self.only_on_active = True
        threading.Thread(target=window_listener, args=(self,), daemon=True).start()

        # Set up menu listener
        self.currently_in_menu = False

        # Load settings
        load_settings(self, self.json_file)

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        self.create_version_frame()
        self.create_menu_frame()
        self.create_content_title_frame()
        self.create_content_frame()

    def create_version_frame(self):
        version_frame = tk.Frame(self.root, bg=CONTENT_COLOR)
        version_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Creatin dividing line
        line_canvas = tk.Canvas(version_frame, height=1, bg=FEATURE_COLOR, highlightthickness=0)
        line_canvas.pack(fill=tk.X)

        # Creating version label
        version_label = tk.Label(version_frame, text=f"version {self.version}", fg=FONT_COLOR, font=(FONT, 8), bg=CONTENT_COLOR)
        version_label.pack(side="left", anchor="sw", padx=5, pady=5)

        # Creating dev label
        dev_label = tk.Label(version_frame, text=f"{self.dev}", fg=FONT_COLOR, font=(FONT, 8), bg=CONTENT_COLOR)
        dev_label.pack(side="right", anchor="se", padx=5, pady=5)
        dev_label.bind("<Button-1>", lambda e: open_web(self.web))

    def create_menu_frame(self):
        menu_frame = tk.Frame(self.root, bg=MENU_COLOR)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Creating client name label
        client_name_label = tk.Label(menu_frame, text=self.title, fg=FEATURE_COLOR, font=(FONT, 20, "bold"), bg=MENU_COLOR)
        client_name_label.pack(pady=(3, 0), padx=5, anchor=tk.CENTER)

        # Creating option buttons
        self.option_buttons = []
        for option in ModuleCategory:
            button = self.create_option_button(menu_frame, option)
            self.option_buttons.append(button)

    def create_option_button(self, parent, option):
        button = tk.Button(parent, bg=MENU_COLOR, fg=FONT_COLOR, font=(FONT, FONT_SIZE_OPTIONS), relief=RELIEF_BASIC, text=option, activebackground=PRESS_COLOR, command=lambda opt=option: self.option_content(opt)) 
        if option == "⚙️ Settings":
            button.pack(fill=tk.X, pady=0, ipady=10, side=tk.BOTTOM)
        else:
            button.pack(fill=tk.X, pady=0, ipady=10, side=tk.TOP)
        return button

    def create_content_title_frame(self):
        content_title_frame = tk.Frame(self.root, bg=CONTENT_COLOR)
        content_title_frame.pack(side=tk.TOP, fill=tk.X)

        # Creating title label
        self.content_title_label = tk.Label(content_title_frame, fg=FONT_COLOR, font=(FONT, FONT_SIZE_TITLE), bg=CONTENT_COLOR)
        self.content_title_label.pack(expand=True, anchor=tk.CENTER, pady=(11, 0))

    def create_content_frame(self):
        self.content_frame = tk.Frame(self.root, bg=CONTENT_COLOR, bd=2, relief=RELIEF_BASIC)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Creating status label
        status_text, status_color = check_minecraft()
        status_label = tk.Label(self.content_frame, text=status_text, fg=status_color, font=(FONT, 12, "bold"), bg=CONTENT_COLOR)
        status_label.pack(expand=True, anchor="center")

    def option_content(self, option):
        self.reset_button_colors()
        self.reset_content_frame()

        for button in self.option_buttons:
            if button.cget("text") == option:
                button.config(bg=PRESS_COLOR) # change button pressed color
                self.content_title_label.config(text=option) # change content title

        # filter modules based on the selected option's category
        modules_for_option = {name: module_info for name, module_info in self.modules.items() if module_info.get("category") == option}

        # create widgets for filtered modules
        self.create_widgets_for_modules(modules_for_option)
            
    def reset_button_colors(self):
        for button in self.option_buttons:
            button.config(bg=MENU_COLOR)  # reset background color of all buttons

    def reset_content_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.forget()  # remove all widgets from the content frame

    def create_widgets_for_modules(self, modules):
        for module in modules:
            self.create_child_widgets(module)

    def create_child_widgets(self, module):
        module_frame = tk.Frame(self.content_frame, bg=CONTENT_COLOR, borderwidth=8, relief=RELIEF_FRAME)
        module_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, anchor=tk.CENTER, pady=(4, 0))

        self.create_title_label(module_frame, module)
        self.create_label(module_frame, module)
        self.create_button(module_frame, module)
        self.create_slider(module_frame, module)
        self.create_check_box(module_frame, module)
        self.create_hotkey_button(module_frame, module)
        self.create_toggle_button(module_frame, module)

    def create_title_label(self, parent, module):
        title_label = tk.Label(parent, text=self.modules.get(module)["name"], width=WIDTH, fg=FONT_COLOR, font=(FONT, FONT_SIZE_SUBTITLE, "bold"), bg=CONTENT_COLOR)
        title_label.pack(side=tk.TOP, pady=(CONTENT_PAD_Y, 0), padx=2*CONTENT_PAD_X) # adjust x padding here so the modules are all the same width

    def create_label(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("label"):
            for x in range(module_name.get("label")):

                label_text = module_name.get(f"label_text{x+1}")
                label = tk.Label(parent, text=label_text, fg=FONT_COLOR, font=(FONT, FONT_SIZE_CONTENT), bg=CONTENT_COLOR, wraplength=LENGTH, width=WIDTH)
                label.pack(pady=CONTENT_PAD_Y)

    def create_slider(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("slider"):
            for x in range(module_name.get("slider")):
                
                name = f"{module}_{x}"
                slider_min = module_name.get(f"slider_min{x+1}")
                slider_max = module_name.get(f"slider_max{x+1}")
                slider_text = module_name.get(f"slider_text{x+1}")
                slider_step = module_name.get(f"slider_step{x+1}")
                slider_default = module_name.get(f"slider_default{x+1}")

                slider = tk.Scale(parent, bg=CONTENT_COLOR, fg=FONT_COLOR, relief=RELIEF_BASIC, highlightthickness=0, font=(FONT, FONT_SIZE_CONTENT), label=slider_text, from_=slider_min, to=slider_max, orient=tk.HORIZONTAL, resolution=slider_step)
                slider.bind("<ButtonRelease-1>", (lambda _: retoggle(self, module)))
                slider.pack(side=tk.TOP, fill=tk.X, expand=True, anchor=tk.CENTER, padx=2*CONTENT_PAD_X)

                if name in self.sliders and self.sliders[name] is not None:
                    if isinstance(self.sliders[name], (int, float)):
                        slider.set(self.sliders[name])
                    else:
                        slider.set(self.sliders[name].get())
                else:
                    slider.set(slider_default)

                self.sliders[name] = slider # keep track of all sliders to access them later
           
    def get_slider_value(self, module, x):
        return self.sliders[f"{module}_{x}"].get()

    def create_check_box(self, parent, module):
        if self.modules.get(module).get("checkbox"):
            for x in range(self.modules.get(module).get("checkbox")):

                name = f"{module}_{x}"
                checkbox_text = self.modules.get(module).get(f"checkbox_text{x+1}")
                checkbox_var = tk.BooleanVar()

                checkbox = tk.Checkbutton(parent, text=checkbox_text, font=(FONT, FONT_SIZE_CONTENT), variable=checkbox_var, bg=CONTENT_COLOR, fg=FONT_COLOR, selectcolor=CONTENT_COLOR, relief=RELIEF_BASIC, highlightthickness=0, command=lambda: retoggle(self, module))            
                checkbox.pack(fill=tk.BOTH, side=tk.TOP, expand=True, anchor=tk.CENTER, pady=CONTENT_PAD_Y, padx=2*CONTENT_PAD_X)

                if name in self.checkboxs and self.checkboxs[name] is not None:
                    if isinstance(self.checkboxs[name], bool):
                        checkbox_var.set(self.checkboxs[name])
                    else:
                        checkbox_var.set(self.checkboxs[name].get())
                else:
                    checkbox_var.set(False)
    
                self.checkboxs[name] = checkbox_var # keep track of all checkbuttons to access them later

    def get_checkbox_value(self, module, x):
        return self.checkboxs[f"{module}_{x}"].get()
    
    def create_button(self, parent, module):
        # currently only adjusted for controls module
        module_name = self.modules.get(module)
        if module_name.get("button") and not module_name.get("hotkey"):
            for x in range(module_name.get("button")):
                name = f"{module}_{x}"
                button = module_name.get(f"button{x+1}")

                text = button["button_text"]
                value = button["value"]
                full_text = f"{text}: {value}"
                command = module_name.get("command") 

                button = tk.Button(parent, bg=CONTENT_COLOR, font=(FONT, FONT_SIZE_CONTENT), fg=FONT_COLOR, relief=RELIEF_FANCY, text=full_text, activebackground=PRESS_COLOR, command=lambda name=name, text=text, key=value: command(self, module, name, text, key))
                button.pack(fill=tk.BOTH, side=tk.TOP, expand=True, anchor=tk.CENTER, pady=2*CONTENT_PAD_Y, padx=2*CONTENT_PAD_X)

                if name in self.buttons and self.buttons[name] is not None:
                    if isinstance(self.buttons[name], str):
                        button.config(text=f"{text}: [{self.buttons[name]}]")
                    else:
                        button.config(text=self.buttons[name].cget("text"))

                self.buttons[name] = button # keep track of all buttons to access them later

    def create_hotkey_button(self, parent, module):
        if self.modules.get(module).get("hotkey"):
            hotkey_text = f"Key: [{(self.modules.get(module).get('hotkey')).upper()}]" if self.modules.get(module).get("hotkey") and self.modules.get(module).get("hotkey") != "None" else "Bind Hotkey"
            button = tk.Button(parent, bg=CONTENT_COLOR, font=(FONT, FONT_SIZE_CONTENT), fg=FONT_COLOR, relief=RELIEF_FANCY, text=hotkey_text, activebackground=PRESS_COLOR, command=lambda: set_hotkey(self, button, module))
            button.pack(fill=tk.BOTH, side=tk.TOP, expand=True, anchor=tk.CENTER, pady=CONTENT_PAD_Y, padx=2*CONTENT_PAD_X)

    def create_toggle_button(self, parent, module):
        if self.modules.get(module).get("toggle"):
            image = self.on if self.module_states.get(module) else self.off
            toggle_button = tk.Button(parent, image=image, bg=CONTENT_COLOR, relief=RELIEF_BASIC, bd=0, activebackground=CONTENT_COLOR, command=lambda: toggle_and_execute(self, module))
            toggle_button.pack(pady=(CONTENT_PAD_Y, 2*CONTENT_PAD_X))
        
            self.toggle_buttons[module] = toggle_button # keep track of all buttons to access them later