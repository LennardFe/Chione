from config.categories import ModuleCategory as MC
from modules.autoclicker import (
    thread_lclick, 
    thread_rclick
    )
from modules.movement import (
    thread_autosprint,
    thread_sprintreset,
    thread_strafing
)
from modules.misc import (
    thread_antiafk,
    selfdestruct
)
from modules.configs import (
    save_config,
    load_config
)
from modules.settings import (
    thread_window,
    thread_menu,
    hide_taskbar,
    dis_tooltips,
    on_top,
    reset_settings,
    set_controls
)

modules = {
    "LeftClicker": {
        "name": "LeftClicker",
        "category": MC.COMBAT,
        "hotkey": "None",
        "toggle": True,
        "slider": 4,
        "slider_min1": 1,
        "slider_max1": 40,
        "slider_text1": "CPS:",
        "slider_step1": 1,
        "slider_default1": 20,
        "slider_tooltip1": "Leftclicks per second.",
        "slider_min2": 0,
        "slider_max2": 10,
        "slider_text2": "Randomize:",
        "slider_step2": 1,
        "slider_default2": 2,
        "slider_tooltip2": "Randomize the clicks.",
        "slider_min3": 0,
        "slider_max3": 10,
        "slider_text3": "Shake:",
        "slider_step3": 1,
        "slider_default3": 2,
        "slider_tooltip3": "Shake the mouse while leftclicking.",
        "slider_min4": 0,
        "slider_max4": 100,
        "slider_text4": "Blockhit (%):",
        "slider_step4": 1,
        "slider_default4": 10,
        "slider_tooltip4": "Chance to blockhit.",
        "dropdown": 1,
        "dropdown_label1": "Pattern",
        "dropdown_tooltip1": "Specify the click pattern to use.",
        "dropdown_values1": ["Basic", "Butterfly", "Jitter"],
        "checkbox": 2,
        "checkbox_text1": "Hold Leftclick",
        "checkbox_tooltip1": "Click while holding leftclick.",
        "checkbox_text2": "Break Blocks ⚠",
        "checkbox_tooltip2": "Allow for breaking blocks while clicking.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_slider_value", "get_checkbox_value", "get_checkbox_value"], 
        "command": thread_lclick
    },
    "RightClicker": {
        "name": "RightClicker",
        "category": MC.COMBAT,
        "hotkey": "None",
        "toggle": True,
        "slider": 3,
        "slider_min1": 1,
        "slider_max1": 40,
        "slider_text1": "CPS:",
        "slider_step1": 1,
        "slider_default1": 15,
        "slider_tooltip1": "Rightclicks per second.",
        "slider_min2": 0,
        "slider_max2": 10,
        "slider_text2": "Randomize:",
        "slider_step2": 1,
        "slider_default2": 2,
        "slider_tooltip2": "Randomize the clicks.",
        "slider_min3": 0,
        "slider_max3": 10,
        "slider_text3": "Shake:",
        "slider_step3": 1,
        "slider_default3": 2,
        "slider_tooltip3": "Shake the mouse while rightclicking.",
        "checkbox": 2,
        "checkbox_text1": "Hold Rightclick",
        "checkbox_tooltip1": "Click while holding rightclick.",
        "checkbox_text2": "Allow Eating ⚠",
        "checkbox_tooltip2": "Allow for eating while clicking.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_checkbox_value", "get_checkbox_value"], 
        "command": thread_rclick
    },
    "AutoSprint": {
        "name": "AutoSprint",
        "category": MC.MOTION,
        "hotkey": "None",
        "toggle": True,
        "params": [],
        "command": thread_autosprint
    },
    "SprintReset": {
        "name": "SprintReset",
        "category": MC.MOTION,
        "hotkey": "None",
        "toggle": True,
        "slider": 3,
        "slider_min1": 0.01,
        "slider_max1": 1,
        "slider_text1": "Delay:",
        "slider_step1": 0.01,
        "slider_default1": 0.25,
        "slider_tooltip1": "The delay between each Reset.",
        "slider_min2": 0.00,
        "slider_max2": 0.20,
        "slider_text2": "Randomize:",
        "slider_step2": 0.01,
        "slider_default2": 0.10,
        "slider_tooltip2": "Randomize the delay.",
        "slider_min3": 0.00,
        "slider_max3": 0.50,
        "slider_text3": "Hold:",
        "slider_step3": 0.01,
        "slider_default3": 0.15,
        "slider_tooltip3": "The time the Key will be held.",
        "dropdown": 1,
        "dropdown_label1": "Mode",
        "dropdown_tooltip1": "The mode of the Sprint Reset.",
        "dropdown_values1": ["W-Tap", "S-Tap", "Crouch"],
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_dropdown_value"], 
        "command": thread_sprintreset
    },
    "Strafing": {
        "name": "Strafing",
        "category": MC.MOTION,
        "hotkey": "None",
        "toggle": True,
        "slider": 3,
        "slider_min1": 0.01,
        "slider_max1": 1,
        "slider_text1": "Delay:",
        "slider_step1": 0.01,
        "slider_default1": 0.25,
        "slider_tooltip1": "The delay between each strafe.",
        "slider_min2": 0.00,
        "slider_max2": 0.20,
        "slider_text2": "Randomize:",
        "slider_step2": 0.01,
        "slider_default2": 0.10,
        "slider_tooltip2": "Randomize the delay.",
        "slider_min3": 0.00,
        "slider_max3": 0.50,
        "slider_text3": "Hold:",
        "slider_step3": 0.01,
        "slider_default3": 0.15,
        "slider_tooltip3": "The time the strafe will be held.",
        "checkbox": 1,
        "checkbox_text1": "Random Direction",
        "checkbox_tooltip1": "Randomize the strafe direction.",
        "params": ["get_slider_value", "get_slider_value", "get_slider_value", "get_checkbox_value"], 
        "command": thread_strafing
    },
    "AntiAFK": {
        "name": "AntiAFK",
        "category": MC.MISC,
        "hotkey": "None",
        "toggle": True,
        "slider": 2,
        "slider_min1": 1,
        "slider_max1": 120,
        "slider_text1": "Timer:",
        "slider_default1": 60,
        "slider_tooltip1": "The time in seconds before the player will be moved.",
        "slider_min2": 1,
        "slider_max2": 20,
        "slider_text2": "Randomize:",
        "slider_default2": 10,
        "slider_tooltip2": "Randomize the timer.",
        "params": ["get_slider_value", "get_slider_value"],
        "command": thread_antiafk
    },
    "SelfDestruct": {
        "name": "SelfDestruct",
        "category": MC.MISC,
        "hotkey": "None",
        "toggle": True,
        "params": [],
        "command": selfdestruct
    },
    "LoadConfig": {
        "name": "Load Config",
        "category": MC.CONFIG,
        "toggle": False,
        "label": 1,
        "label_text1": "Load the settings from one of your saved config-files.",
        "button": 1,
        "button_img1": "Load",
        "button_params1": [],
        "button_command1": load_config
    },
    "SaveConfig": {
        "name": "Save Config",
        "category": MC.CONFIG,
        "toggle": False,
        "label": 1,
        "label_text1": "Save your current settings to a config-file.",
        "button": 1,
        "button_img1": "Save",
        "button_params1": [],
        "button_command1": save_config
    },
    "General": {
        "name": "General",
        "category": MC.SETTINGS,
        "toggle": False,
        "checkbox": 5,
        "checkbox_text1": "Hide from Taskbar",
        "checkbox_tooltip1": "Hide Chione from the taskbar.",
        "checkbox_command1": hide_taskbar,
        "checkbox_text2": "Disable Tooltips",
        "checkbox_tooltip2": "Disable all tooltips.",
        "checkbox_command2": dis_tooltips,
        "checkbox_text3": "Pause in Menu",
        "checkbox_tooltip3": "Pause all modules when game menues are open.",
        "checkbox_command3": thread_menu,
        "checkbox_text4": "Only in Focus",
        "checkbox_tooltip4": "Pause all modules when the focussed window is not Minecraft.",
        "checkbox_command4": thread_window,
        "checkbox_text5": "Always on Top",
        "checkbox_tooltip5": "Keep Chione always on top.",
        "checkbox_command5": on_top,
        "button": 1,
        "button_text1": "Reset Chione",
        "button_tooltip1": "Reset and closes Chione. Helps with fixing bugs.",
        "button_command1": reset_settings
    },
    "Controls": {
        "name": "Controls",
        "category": MC.SETTINGS,
        "toggle": False,
        "label": 1,
        "label_text1": "Change to your keys in Minecraft, so Chione will work.",
        "button": 6,
        "button_text1": "[CTRL]",
        "button_label1": "Sprint-Key:",
        "button_command1": set_controls,
        "button_text2": "[SHIFT]",
        "button_label2": "Crouch-Key:",
        "button_command2": set_controls,
        "button_text3": "[W]",
        "button_label3": "Forward-Key:",
        "button_command3": set_controls,
        "button_text4": "[A]",
        "button_label4": "Left-Key:",
        "button_command4": set_controls,
        "button_text5": "[S]",
        "button_label5": "Backward-Key:",
        "button_command5": set_controls,
        "button_text6": "[D]",
        "button_label6": "Right-Key:",
        "button_command6": set_controls
    },
    "Others": {
        "name": "Others",
        "category": MC.SETTINGS,
        "toggle": False,
        "label": 3,
        "label_text1": "If you find any bugs or have suggestions, please report them on the GitHub page or Discord server.",
        "label_text2": "Discord:\n'marshall.com'",
        "label_link2": "https://discord.gg/HpA7JdP3uq",
        "label_text3": "GitHub:\n'vs-marshall'",
        "label_link3": "https://github.com/vs-marshall/Chione"
    }
}