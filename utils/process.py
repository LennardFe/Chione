from config.setup import *
import psutil

def check_minecraft():
    minecraft_processes = get_minecraft_process_id()
    status_text = "Minecraft Process found" if minecraft_processes else "Minecraft Process not found"
    status_color = GOOD_COLOR if minecraft_processes else ERROR_COLOR
    return status_text, status_color

def get_minecraft_process_id():
    for process in psutil.process_iter(['pid', 'name', 'cmdline']):
        if process.info['name'].lower() == 'javaw.exe' and 'minecraft' in ' '.join(process.info['cmdline']).lower():
            print(f"Minecraft process found with PID {process.info['pid']}")
            return process.info['pid']
    print("No Minecraft process found.")
    return None