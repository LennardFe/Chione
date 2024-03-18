from utils.others import get_file_path
from utils.others import resource
import tkinter as tk

class CustomCheckbox(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Load custom images for checked and unchecked states
        self.checked_icon = tk.PhotoImage(file=resource(get_file_path("checked.png")))
        self.unchecked_icon = tk.PhotoImage(file=resource(get_file_path("unchecked.png"))) 

        # Configure the widget
        self.config(
            image=self.unchecked_icon,  # Use the unchecked image by default
            selectimage=self.checked_icon,  # Switch to checked image when selected
            indicatoron=False,  # Hide the standard checkbox indicator
            padx=0,  # Remove horizontal padding
            pady=0,  # Remove vertical padding
            borderwidth=0,  # Remove border
            highlightthickness=0,  # Remove highlight
            relief=tk.FLAT,  # Remove relief
        )