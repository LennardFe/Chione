# Internal Imports - Utils
from utils.hotkeys import set_hotkey, on_key_press
from utils.listeners import window_listener
from utils.options import load_settings
from utils.options import save_settings
from utils.executor import toggle_and_execute
from utils.executor import retoggle
from utils.others import get_file_path
from utils.others import set_settings
from utils.others import open_web
from utils.others import resource

# Internal Imports - Configs
from config.categories import ModuleCategory
from config.modules import modules
from config.setup import *

# Internal Imports - GUI
from gui.gui_dropdown import Dropdown
from gui.gui_tooltip import ToolTip

# Third-party Library Imports
from pynput import keyboard

# Standard Library Imports
import tkinter as tk
import threading

class GUI: 
    def __init__(self, version, title, dev):
        # Initialize attributes
        self.version = version
        self.title = title
        self.dev = dev
        self.modules = modules
        self.buttons = {}
        self.sliders = {}
        self.checkboxs = {}
        self.dropdowns = {}
        self.toggle_buttons = {}
        self.hotkeys_enabled = True
        self.tooltips_enabled = True
        self.module_states = {module: False for module in self.modules}

        # Declare json file path for saving and loading setting
        self.json_file = resource(get_file_path("options.json"))

        # Create the Tkinter root window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.minsize(MIN_SIZE_W, MIN_SIZE_H)
        self.root.geometry(WINDOW_SIZE)
        self.root.resizable(False, False)
        self.root.configure(bg=CONTENT_COLOR)
        self.root.iconbitmap(resource(get_file_path("icon.ico")))
        self.root.protocol("WM_DELETE_WINDOW", lambda: save_settings(self, self.json_file))

        # Load GUI assets
        self.on = tk.PhotoImage(file=resource(get_file_path("on.png")))
        self.off = tk.PhotoImage(file=resource(get_file_path("off.png")))
        self.save = tk.PhotoImage(file=resource(get_file_path("save.png")))
        self.load = tk.PhotoImage(file=resource(get_file_path("load.png")))

        # Set up keyboard listener
        self.listener = keyboard.Listener(on_press=lambda key: on_key_press(self, key))
        self.listener.start()

        # Set up window listener
        self.focused_process = None
        self.currently_in_foreground = True
        threading.Thread(target=window_listener, args=(self,), daemon=True).start()

        # Set up menu listener
        self.currently_in_menu = False

        # Load settings
        load_settings(self, self.json_file)

        # Set settings
        set_settings(self)

        # Create GUI widgets
        self.create_widgets()

        # Set default page on startup
        self.option_content(DEFAULT_PAGE)

    def create_widgets(self):
        self.create_version_frame()
        self.create_menu_frame()
        self.create_content_frame()

    def create_version_frame(self):
        # Create version frame
        version_frame = tk.Frame(self.root, 
                                 bg=CONTENT_COLOR)
        version_frame.pack(side=tk.BOTTOM, 
                           fill=tk.X)

        # Create dividing line
        line_canvas = tk.Canvas(version_frame, 
                                height=1, 
                                bg=FEATURE_COLOR, 
                                highlightthickness=0)
        line_canvas.pack(fill=tk.X)

        # Create version label
        version_label = tk.Label(version_frame, 
                                 text=f"version {self.version}", 
                                 fg=FONT_COLOR, 
                                 font=(FONT, FONT_SIZE_CONTENT), 
                                 bg=CONTENT_COLOR)
        version_label.pack(side=tk.LEFT, 
                           anchor=tk.SW, 
                           padx=CONTENT_PAD_X/2, 
                           pady=CONTENT_PAD_Y/2)

        # Create dev label
        dev_label = tk.Label(version_frame, 
                             text=self.dev, 
                             fg=FONT_COLOR, 
                             font=(FONT, 8), 
                             bg=CONTENT_COLOR)
        dev_label.pack(side=tk.RIGHT, 
                       anchor=tk.SE, 
                       padx=CONTENT_PAD_X/2, 
                       pady=CONTENT_PAD_Y/2)

    def create_menu_frame(self):
        # Creating menu frame
        menu_frame = tk.Frame(self.root, 
                              bg=MENU_COLOR)
        menu_frame.pack(side=tk.LEFT,
                        fill=tk.Y)

        # Creating client name label
        client_name_label = tk.Label(menu_frame, 
                                     text=self.title, 
                                     fg=FEATURE_COLOR, 
                                     font=(FONT, FONT_SIZE_BIG_TITLE, "bold"),
                                     bg=MENU_COLOR)
        client_name_label.pack()

        # Creating option buttons
        self.option_buttons = []
        for option in ModuleCategory:
            button = self.create_option_button(menu_frame, option)
            self.option_buttons.append(button)

    def create_option_button(self, parent, option):
        # Creating option button
        button = tk.Button(parent,
                            bg=MENU_COLOR, 
                            fg=FONT_COLOR, 
                            font=(FONT, FONT_SIZE_OPTIONS), 
                            relief=RELIEF_BASIC, 
                            text=option, 
                            activebackground=PRESS_COLOR, 
                            command=lambda opt=option: self.option_content(opt)) 
        
        # Adjusting button placement based on option
        if option == "⚙️ Settings" or option ==  "🔧 Configs":
            button.pack(fill=tk.X, pady=0, ipady=10, side=tk.BOTTOM)
        else:
            button.pack(fill=tk.X, pady=0, ipady=10, side=tk.TOP)
        return button

    def create_content_frame(self):
        # Creating content frame
        self.content_frame = tk.Frame(self.root, 
                                      bg=CONTENT_COLOR, 
                                      bd=2, 
                                      relief=RELIEF_BASIC)
        self.content_frame.pack(side=tk.RIGHT, 
                                fill=tk.BOTH, 
                                expand=True)

    def option_content(self, option):
        # Reset button colors and content frame
        self.reset_button_colors()
        self.reset_content_frame()

        # Change button color
        for button in self.option_buttons:
            if button.cget("text") == option:
                button.config(bg=PRESS_COLOR) # change button pressed color

        # Filter modules based on the selected option's category
        modules_for_option = {name: module_info for name, module_info in self.modules.items() if module_info.get("category") == option}

        # Create overlay frame, to prevent flickering
        overlay_frame = tk.Frame(self.content_frame, bg=CONTENT_COLOR)
        overlay_frame.place(relwidth=1, relheight=1)

        # Create widgets for filtered modules
        self.create_widgets_for_modules(modules_for_option)

        # Raise overlay frame to the top
        overlay_frame.tkraise()

        # Remove the overlay frame after short delay
        self.root.after(150, overlay_frame.destroy)
            
    def reset_button_colors(self):
        for button in self.option_buttons:
            button.config(bg=MENU_COLOR)

    def reset_content_frame(self):
        # Reset content frame and save values
        for widget in self.content_frame.winfo_children():
            for child_widget in widget.winfo_children():
                if isinstance(child_widget, tk.Label):
                    module_name = child_widget['text']
                    self.store_values(module_name, self.sliders, (int, float), tk.Scale)
                    self.store_values(module_name, self.checkboxs, bool, tk.BooleanVar)
                    self.store_values(module_name, self.dropdowns, str, Dropdown)
                    self.store_values(module_name, self.buttons, str, tk.Button)
                    
            widget.destroy()

    def store_values(self, module_name, objects, data_type, obj_type):
        index = 0

        # Store values of objects
        while True:
            obj_name = f"{module_name}_{index}"
            if obj_name not in objects:
                break

            if isinstance(objects[obj_name], data_type):
                objects[obj_name] # If already a value, do nothing
            else: # Override object with value of object
                if obj_type == tk.Scale or obj_type == tk.BooleanVar:
                    objects[obj_name] = objects[obj_name].get()
                elif obj_type == tk.Button:
                    objects[obj_name] = objects[obj_name].cget("text")
                elif obj_type == Dropdown:
                    objects[obj_name] = objects[obj_name].selected_option.get()
            index += 1

    def create_widgets_for_modules(self, modules):
        # Create widgets for each module
        for module in modules:
            self.create_child_widgets(module)

    def create_child_widgets(self, module):
        # Create module frame
        module_frame = tk.Frame(self.content_frame, bg=CONTENT_COLOR, borderwidth=8, relief=RELIEF_FRAME)
        module_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create widgets for module
        self.create_title_label(module_frame, module)
        self.create_label(module_frame, module)
        self.create_slider(module_frame, module)
        self.create_check_box(module_frame, module)
        self.create_dropdown(module_frame, module)
        self.create_button(module_frame, module)

        # Create seperate frame for hotkey and toggle button
        hotkey_toggle_frame = tk.Frame(module_frame, bg=CONTENT_COLOR)	
        hotkey_toggle_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor=tk.S)

        self.create_hotkey_button(hotkey_toggle_frame, module)
        self.create_toggle_button(hotkey_toggle_frame, module)

        # Resize window, after short delay to ensure all widgets are created
        self.root.after(50, self.resize_window)

    def create_title_label(self, parent, module):
        title = self.modules.get(module)["name"]

        # Create title label
        title_label = tk.Label(parent, 
                               text=title, 
                               width=WIDTH, fg=FONT_COLOR, 
                               font=(FONT, FONT_SIZE_SUBTITLE, "bold"), 
                               bg=CONTENT_COLOR)
        title_label.pack(side=tk.TOP, 
                         padx=2*CONTENT_PAD_X,
                         pady=(CONTENT_PAD_Y, 0))

    def create_label(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("label"):
            for x in range(module_name.get("label")):
                label_text = module_name.get(f"label_text{x+1}")

                label = tk.Label(parent, 
                                 text=label_text, 
                                 fg=FONT_COLOR, 
                                 font=(FONT, FONT_SIZE_CONTENT), 
                                 bg=CONTENT_COLOR, 
                                 wraplength=LENGTH, 
                                 width=WIDTH)
                label.pack(fill=tk.BOTH, 
                           expand=True, 
                           pady=CONTENT_PAD_Y)

                if(module_name.get(f"label_link{x+1}")):
                    label.bind("<Button-1>", lambda e, link=f"label_link{x+1}": open_web(module_name.get(link)))
                    
    def create_slider(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("slider"):
            for x in range(module_name.get("slider")):
                
                # Get slider values
                name = f"{module}_{x}"
                slider_min = module_name.get(f"slider_min{x+1}")
                slider_max = module_name.get(f"slider_max{x+1}")
                slider_text = module_name.get(f"slider_text{x+1}")
                slider_step = module_name.get(f"slider_step{x+1}")
                slider_default = module_name.get(f"slider_default{x+1}")
                slider_tooltip = module_name.get(f"slider_tooltip{x+1}")

                # Create slider
                slider = tk.Scale(parent, 
                                  bg=CONTENT_COLOR, 
                                  fg=FONT_COLOR, 
                                  troughcolor=SLIDER_COLOR,
                                  activebackground=FONT_COLOR,
                                  #relief=RELIEF_BASIC,
                                  sliderrelief=RELIEF_BASIC, # unhappy with the design
                                  highlightthickness=0, 
                                  font=(FONT, FONT_SIZE_CONTENT), 
                                  label=slider_text, 
                                  from_=slider_min, 
                                  to=slider_max, 
                                  orient=tk.HORIZONTAL, 
                                  bd=0,
                                  resolution=slider_step)
                
                slider.bind("<ButtonRelease-1>", (lambda _: retoggle(self, module))) # TODO: Can we move this below the pack? 

                slider.pack(side=tk.TOP, 
                            fill=tk.X, 
                            expand=True, 
                            anchor=tk.CENTER,
                            padx=2*CONTENT_PAD_X,
                            pady=CONTENT_PAD_Y/2)

                # Display tooltip information
                ToolTip(slider, slider_tooltip, self.tooltips_enabled)

                # Set slider value to saved value
                if name in self.sliders and self.sliders[name] is not None:
                    slider.set(self.sliders[name])
                else:
                    slider.set(slider_default)

                # Save slider object to access and save value on option change
                self.sliders[name] = slider
           
    def get_slider_value(self, module, x):
        name = f"{module}_{x}"
        if isinstance(self.sliders[name], tk.Scale):
            return self.sliders[name].get()
        else:
            return self.sliders[name]

    def create_check_box(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("checkbox"):
            for x in range(module_name.get("checkbox")):

                # Get checkbox values
                name = f"{module}_{x}"
                checkbox_text = module_name.get(f"checkbox_text{x+1}")
                checkbox_tooltip = module_name.get(f"checkbox_tooltip{x+1}")
                checkbox_var = tk.BooleanVar()

                # Create checkbox
                if module_name.get(f"checkbox_command{x+1}"):
                    cb_command = module_name.get(f"checkbox_command{x+1}")
                    checkbox = tk.Checkbutton(parent, 
                                              text=checkbox_text, 
                                              font=(FONT, FONT_SIZE_CONTENT), 
                                              variable=checkbox_var, 
                                              bg=CONTENT_COLOR, 
                                              fg=FONT_COLOR, 
                                              selectcolor=CONTENT_COLOR, 
                                              relief=RELIEF_BASIC, 
                                              activebackground=PRESS_COLOR, 
                                              highlightthickness=0, 
                                              command=lambda cb=cb_command, 
                                              var=checkbox_var: cb(self, module, var.get()))
                    
                else:
                    checkbox = tk.Checkbutton(parent, 
                                              text=checkbox_text, 
                                              font=(FONT, FONT_SIZE_CONTENT), 
                                              variable=checkbox_var, 
                                              bg=CONTENT_COLOR, 
                                              fg=FONT_COLOR, 
                                              selectcolor=CONTENT_COLOR, 
                                              relief=RELIEF_BASIC, 
                                              activebackground=PRESS_COLOR, 
                                              highlightthickness=0, 
                                              command=lambda: retoggle(self, module))            
                
                checkbox.pack(side=tk.TOP, 
                              fill=tk.BOTH,         
                              expand=True,
                              padx=2*CONTENT_PAD_X,
                              pady=CONTENT_PAD_Y)

                # Display hover information
                ToolTip(checkbox, checkbox_tooltip, self.tooltips_enabled)

                # Set checkbox value to saved value
                if name in self.checkboxs and self.checkboxs[name] is not None:
                    checkbox_var.set(self.checkboxs[name])
                else:
                    checkbox_var.set(False)
    
                # Save checkbox object to access and save value on option change
                self.checkboxs[name] = checkbox_var

    def get_checkbox_value(self, module, x):
        name = f"{module}_{x}"
        if isinstance(self.checkboxs[name], tk.BooleanVar):
            return self.checkboxs[name].get()
        else:
            return self.checkboxs[name]
    
    def create_dropdown(self, parent, module):
        module_name = self.modules.get(module)
        if module_name.get("dropdown"):
            for x in range(module_name.get("dropdown")):
                name = f"{module}_{x}"
                label = module_name.get(f"dropdown_label{x+1}")
                values = module_name.get(f"dropdown_values{x+1}")
                tooltip = module_name.get(f"dropdown_tooltip{x+1}")

                dropdown_border = tk.Frame(parent, 
                                    bg=PRESS_COLOR,
                                    highlightbackground=PRESS_COLOR,
                                    highlightthickness=2,
                                    bd=0)

                dropdown = Dropdown(dropdown_border, 
                                    label, 
                                    values,
                                    relief=RELIEF_BASIC,
                                    command=lambda: retoggle(self, module))
                
                dropdown_border.pack(side=tk.TOP, 
                                    fill=tk.X, 
                                    expand=True, 
                                    padx=2*CONTENT_PAD_X,
                                    pady=CONTENT_PAD_Y)

                dropdown.pack(side=tk.TOP, 
                              fill=tk.BOTH,
                              expand=True)

                ToolTip(dropdown, tooltip, self.tooltips_enabled)

                # Set dropdown value to saved value
                if name in self.dropdowns and self.dropdowns[name] is not None and self.dropdowns[name] in values:
                    dropdown.selected_option.set(self.dropdowns[name])
                    dropdown.dropdown_button.config(text=f"{self.dropdowns[name]} ↓") # Move this to Dropdown class?
                
                # Save dropdown object to access and save value on option change
                self.dropdowns[name] = dropdown

    def get_dropdown_value(self, module, x):
        return self.dropdowns[f"{module}_{x}"].selected_option.get()

    def create_button(self, parent, module):
        # TODO: Refactor this function
        module_name = self.modules.get(module)
        if module_name.get("button"):
            for x in range(module_name.get("button")):

                # Get button name
                name = f"{module}_{x}"

                # Create button frame
                button_border = tk.Frame(parent, 
                                           bg=PRESS_COLOR,
                                           highlightbackground=PRESS_COLOR,
                                           highlightthickness=2,
                                           bd=0)

                # Get label values / if label exists
                if module_name.get(f"button_label{x+1}"):
                    button_label = module_name.get(f"button_label{x+1}")
                    label = tk.Label(parent, 
                                     text=button_label, 
                                     fg=FONT_COLOR, 
                                     font=(FONT, FONT_SIZE_CONTENT), 
                                     bg=CONTENT_COLOR, 
                                     wraplength=LENGTH, 
                                     width=WIDTH)
                    
                    label.pack(fill=tk.BOTH, 
                               expand=True)

                # Get button values / image or text, kinda hardcoded for load and save config
                if(module_name.get(f"button_img{x+1}")):
                    image = self.load if module_name.get(f"button_img{x+1}") == "Load" else self.save
                    b_command = module_name.get(f"button_command{x+1}") 

                    button_border_sl = tk.Frame(parent, 
                                                bg=FEATURE_COLOR,
                                                highlightbackground=FEATURE_COLOR,
                                                highlightthickness=2,
                                                bd=0)

                    button = tk.Button(button_border_sl, 
                                       image=image, 
                                       bg=CONTENT_COLOR, 
                                       relief=RELIEF_BASIC, 
                                       activebackground=CONTENT_COLOR, 
                                       bd=0, 
                                       command=lambda: b_command(self, module))
                    
                    button_border_sl.pack(side=tk.BOTTOM,
                                          padx=2*CONTENT_PAD_X,
                                          pady=2*CONTENT_PAD_Y)

                    button.pack(side=tk.BOTTOM)

                else: # Currently only used in controls and reset button
                    button_text = module_name.get(f"button_text{x+1}")
                    button_command = module_name.get(f"button_command{x+1}")
                    button = tk.Button(button_border, 
                                       bg=CONTENT_COLOR, 
                                       font=(FONT, FONT_SIZE_CONTENT), 
                                       fg=FONT_COLOR, 
                                       relief=RELIEF_BASIC, 
                                       text=button_text, 
                                       activebackground=PRESS_COLOR, 
                                       command=lambda bt=button_text, name=name: button_command(self, module, name, bt))
                    
                    button_border.pack(side=tk.TOP,
                                       fill=tk.X, 
                                       expand=True,
                                       padx=4*CONTENT_PAD_X, # 4* here -> to differentiate between the settings and the content
                                       pady=(0, CONTENT_PAD_Y)) # 0 here -> mainly so the controls are close to the corresponding label

                    button.pack(side=tk.TOP, 
                                fill=tk.X,  # only x fill, to differentiate between the settings and the content
                                expand=True)

                # Display hover information / if tooltip exists
                if module_name.get(f"button_tooltip{x+1}"):
                    button_tooltip = module_name.get(f"button_tooltip{x+1}")
                    ToolTip(button, button_tooltip, self.tooltips_enabled) 

                # Set button value to saved value
                if name in self.buttons and self.buttons[name] is not None:
                    button.config(text=f"{self.buttons[name]}")

                # Save button object to access and save value on option change
                self.buttons[name] = button 

    def create_hotkey_button(self, parent, module):
        if self.modules.get(module).get("hotkey", False):
            hotkey_text = f"Key: [{(self.modules.get(module).get('hotkey')).upper()}]" if self.modules.get(module).get("hotkey") and self.modules.get(module).get("hotkey") != "None" else "Bind Hotkey"
            
            button_border = tk.Frame(parent, 
                                     bg=PRESS_COLOR,
                                     highlightbackground=PRESS_COLOR,
                                     highlightthickness=2,
                                     bd=0)

            button = tk.Button(button_border, 
                               bg=CONTENT_COLOR, 
                               font=(FONT, FONT_SIZE_CONTENT), 
                               fg=FONT_COLOR, 
                               relief=RELIEF_BASIC, 
                               text=hotkey_text, 
                               activebackground=PRESS_COLOR, 
                               command=lambda: set_hotkey(self, button, module))
            
            button_border.pack(side=tk.LEFT, 
                               fill=tk.BOTH, 
                               expand=True, 
                               padx=(2*CONTENT_PAD_X, CONTENT_PAD_X/2),
                               pady=CONTENT_PAD_Y)

            button.pack(side=tk.LEFT,
                        fill=tk.BOTH, 
                        expand=True)
            
            # Prevent button from resizing, after short delay to ensure on first load
            button_border.after(50, button_border.pack_propagate, False)
            button.after(50, button.pack_propagate, False)

    def create_toggle_button(self, parent, module):
        if self.modules.get(module).get("toggle"):
            image = self.on if self.module_states.get(module) else self.off

            toggle_border = tk.Frame(parent, 
                                     bg=FEATURE_COLOR,
                                     highlightbackground=FEATURE_COLOR,
                                     highlightthickness=2,
                                     bd=0)

            toggle_button = tk.Button(toggle_border, 
                                      image=image, 
                                      bg=CONTENT_COLOR, 
                                      relief=RELIEF_BASIC, 
                                      activebackground=CONTENT_COLOR, 
                                      bd=0, 
                                      command=lambda: toggle_and_execute(self, module))
            
            toggle_border.pack(side=tk.LEFT, 
                               padx=(CONTENT_PAD_X/2, 2*CONTENT_PAD_X),
                               pady=CONTENT_PAD_Y)
            
            toggle_button.pack(side=tk.LEFT)
        
            self.toggle_buttons[module] = toggle_button # Keep track of all buttons to access them later

    def resize_window(self):
        # Get old window size
        old_width = self.root.winfo_width()
        old_height = self.root.winfo_height()

        # Get new requested window size
        new_width = self.root.winfo_reqwidth() + 10  # Add puffer of 10 units
        new_height = self.root.winfo_reqheight() + 10  # Add puffer of 10 units

        # Check if new size is smaller than the old size
        if old_width is None or old_height is None or new_width > old_width or new_height > old_height:
            # Only increase the smaller dimension, keeping the larger one unchanged
            new_width = max(new_width, old_width)
            new_height = max(new_height, old_height)
            self.root.geometry(f"{new_width}x{new_height}")