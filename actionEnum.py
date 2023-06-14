from enum import Enum

class ActionWaitUntilType(Enum):
    BATTLE_TEXT = 0
    CHALLENGE_AGAIN_BUTTON = 1
    CONFIRM_BUTTON_OR_INSUFFICIENT_STAMINA_TEXT = 2
    CONFIRM_BUTTON = 3
    INSUFFICIENT_STAMINA_TEXT = 4
    LEVEL_UP_TEXT = 5
    BATTLE_TEXT_OR_LEVEL_UP_TEXT = 6

class ActionType(Enum):
    MOVE = 0
    WAIT_UNTIL = 1
    CLICK = 2

class ActionPos(Enum):
    CHALLENGE_AGAIN = 0
    CONFIRM_BATTLE = 1
    CONFIRM_SKILL = 2
    CHOOSE_REFILL_ALL_STAMINA = 3
    CONFIRM_REFILL_STAMINA = 4

    @classmethod
    def has_key(self, value):
        return isinstance(value, self) and value._name_ in self._member_map_