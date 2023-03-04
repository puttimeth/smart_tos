from utils.getRunePos import get_rune_pos
from typing import List, Union
import data
from terminalColorize import colorize, Color
import time
from actionEnum import ActionType, ActionWaitUntilType, ActionPos
from utils.imageComparison import save_screenshot, is_template_appear_in_screenshot

class Action:
    def __init__(self, t: ActionType):
        self.action_type = t

    def resolve(self):
        pass

class ActionClick(Action):
    def __init__(self, pos: Union[ActionPos, str], duration = 25, after_delay = 3000):
        super().__init__(ActionType.CLICK)
        self.pos = get_rune_pos(pos)
        self.duration = duration
        self.after_delay = after_delay

    def resolve(self):
        if data.device:
            data.device.shell(f'input touchscreen swipe {self.pos[0]} {self.pos[1]} {self.pos[0]} {self.pos[1]} {self.duration}')
            time.sleep(self.after_delay / 1000)
        else:
            print(colorize('Device not found.', Color.RED))

class ActionMove(Action):
    def __init__(self, start_pos: Union[ActionPos, str], end_pos: Union[ActionPos, str], duration, after_delay):
        super().__init__(ActionType.MOVE)
        self.start_pos = get_rune_pos(start_pos)
        self.end_pos = get_rune_pos(end_pos)
        self.duration = duration
        self.after_delay = after_delay

    def resolve(self):
        if data.device:
            data.device.shell(f'input touchscreen swipe {self.start_pos[0]} {self.start_pos[1]} {self.end_pos[0]} {self.end_pos[1]} {self.duration}')
            time.sleep(self.after_delay / 1000)
        else:
            print(colorize('Device not found.', Color.RED))

class ActionWaitUntil(Action):
    def __init__(self, t: ActionWaitUntilType, check_interval=1000):
        super().__init__(ActionType.WAIT_UNTIL)
        self.wait_until_type = t
        self.check_interval = check_interval

    def resolve(self):
        while True:
            save_screenshot()
            if self.wait_until_type == ActionWaitUntilType.CONFIRM_BUTTON_OR_INSUFFICIENT_STAMINA_TEXT:
                if is_template_appear_in_screenshot(ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT):
                    # auto refill stamina
                    # 1. choose refill all stamina
                    ActionClick(ActionPos.CHOOSE_REFILL_ALL_STAMINA)
                    # 2. confirm refill stamina
                    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA)
                    # 3. close refill stamina window
                    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA)
                elif is_template_appear_in_screenshot(ActionWaitUntilType.CONFIRM_BUTTON):
                    break
            else:
                if is_template_appear_in_screenshot(self.wait_until_type):
                    break
            time.sleep(self.check_interval / 1000)

class ActionSet:
    def __init__(self, name, hotkey_code, action_list: List[Action]):
        self.name = name
        self.hotkey_code = hotkey_code
        self.action_list = action_list

    def resolve(self):
        print(colorize(f'Start {self.name}', Color.GREEN))
        for idx, action in enumerate(self.action_list):
            print(colorize(f'In progress {idx+1}/{len(self.action_list)}: {action.action_type}', Color.YELLOW))
            action.resolve()
        print(colorize(f'Finish {self.name}\n', Color.GREEN))