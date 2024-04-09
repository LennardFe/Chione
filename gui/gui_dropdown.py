from config.setup import *
import tkinter as tk

class Dropdown(tk.Frame):
    def __init__(self, master, display_text, options, relief, command):
        super().__init__(master)
        
        # Set the variables
        self.display_text = f"{display_text} ↓"
        self.options = options
        self.selected_option = tk.StringVar()
        self.relief = relief
        

        # include command
        self.command = command
          
        # Set the default options
        self.config(bg=CONTENT_COLOR)
        self.dropdown_button = tk.Button(self, 
                                         text=self.display_text,
                                         font=(FONT, FONT_SIZE_CONTENT), 
                                         bg=CONTENT_COLOR, 
                                         fg=FONT_COLOR, 
                                         relief=self.relief, 
                                         activebackground=PRESS_COLOR,
                                         command=self.toggle_dropdown)
        
        self.dropdown_button.pack(fill=tk.X, expand=True)

        # Create the top level window
        self.tw = tk.Toplevel(self)
        self.tw.wm_overrideredirect(True)
        self.tw.lift(aboveThis=self.master)
        self.tw.withdraw()

        # Create the dropdown menu as a Listbox
        self.dropdown_menu = tk.Listbox(self.tw, 
                                        selectmode=tk.SINGLE, 
                                        justify="center", 
                                        font=(FONT, FONT_SIZE_CONTENT), 
                                        bg=CONTENT_COLOR, 
                                        height=0, # Set to 0 to allow for dynamic height
                                        fg=FONT_COLOR, 
                                        highlightcolor=PRESS_COLOR,
                                        highlightbackground=PRESS_COLOR,
                                        selectbackground=PRESS_COLOR,
                                        highlightthickness=2,
                                        border=2)
        
        # Insert options into the dropdown menu
        for option in self.options:
            self.dropdown_menu.insert(tk.END, option)

        # Bind the dropdown menu to the on_select method
        self.dropdown_menu.bind('<<ListboxSelect>>', self.on_select)

        # Set the default option
        self.selected_option.set(self.options[0])

        # Close dropdown when window is moved
        root = self.master.winfo_toplevel() 
        root.bind('<Configure>', lambda e: self.remove_top_level())

    def toggle_dropdown(self):
        # Check if the dropdown menu is mapped
        if self.dropdown_menu.winfo_ismapped():
            self.tw.withdraw()
        else:
            x = self.dropdown_button.winfo_rootx() - 2 # -2 because of the new frame sourounding the button
            y = self.dropdown_button.winfo_rooty() + self.dropdown_button.winfo_height()

            # Get the width of the dropdown button
            button_width = self.dropdown_button.winfo_width() + 4 # 4 because of the new frame sourounding the button

            # Get the height of the dropdown menu
            menu_height = self.dropdown_menu.winfo_reqheight()

            # Set dropdown menu width same as button width
            self.tw.geometry(f"{button_width}x{menu_height}+{x}+{y}") 
            self.tw.deiconify()
            self.dropdown_menu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def on_select(self, _):
        index = self.dropdown_menu.curselection()[0]
        self.selected_option.set(self.options[index])
        self.dropdown_button.config(text=f"{self.selected_option.get()} ↓")
        self.command() # Call the command, in our case, it's the retoggle function
        self.toggle_dropdown()

    def remove_top_level(self):
        if self.tw.winfo_exists():  # Check if the Toplevel window exists
            if self.dropdown_menu.winfo_ismapped():
                self.tw.withdraw()