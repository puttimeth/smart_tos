import keyboard
import threading
import time
from utils.getRunePos import get_rune_pos
from data import action_set_list
import data
from terminalColorize import colorize, Color

def call_action_set_thread(action_set):
    if data.PROGRAM_LISTEN:
        thread = threading.Thread(
            target=lambda action_set=action_set: action_set.resolve())
        thread.start()

def hotkey():
    for action_set in action_set_list:
        keyboard.add_hotkey(action_set.hotkey_code, lambda action_set=action_set: call_action_set_thread(action_set))
        print(colorize(f'Finished loading action: {action_set.name} ({action_set.hotkey_code})', Color.BLUE))
