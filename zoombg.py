import os
import shutil
from pynput import keyboard
from pynput.keyboard import Key, Listener

background_path = "User/tk/zoom/bgpictures/friday.mov"
zoom_virtual_background_folder = os.path.expanduser("~/Library/Application Support/zoom.us/data/VirtualBkgs_custom/")
backup_path = os.path.join(zoom_virtual_background_folder, "backup_original.mov")

def change_background():
    # If a backup doesn't exist, create one
    if not os.path.exists(backup_path):
        original_files = [f for f in os.listdir(zoom_virtual_background_folder) if f.endswith(".mov")]
        if original_files:
            original_file_path = os.path.join(zoom_virtual_background_folder, original_files[0])
            shutil.copyfile(original_file_path, backup_path)

    # Replace the current virtual background with the specified .mov file
    shutil.copyfile(background_path, os.path.join(zoom_virtual_background_folder, "friday.mov"))

def restore_background():
    if os.path.exists(backup_path):
        # Delete the friday.mov
        friday_path = os.path.join(zoom_virtual_background_folder, "friday.mov")
        if os.path.exists(friday_path):
            os.remove(friday_path)

        # Restore the original virtual background
        original_files = [f for f in os.listdir(zoom_virtual_background_folder) if f.endswith(".mov")]
        if original_files:
            original_file_path = os.path.join(zoom_virtual_background_folder, original_files[0])
            shutil.copyfile(backup_path, original_file_path)

def on_press(key):
    try:
        if key == Key.shift_l and key == Key.alt_l and key == Key.ctrl_l and key.char == "x":
            change_background()
        elif key == Key.shift_l and key == Key.alt_l and key == Key.ctrl_l and key.char == "c":
            restore_background()
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        # Stop the listener
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
