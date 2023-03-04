from utils.getRunePos import get_rune_pos
from structure import ActionSet, ActionMove, ActionClick, ActionWaitUntil
from actionEnum import ActionPos, ActionWaitUntilType

# global variable

PROGRAM_LISTEN = None
device = None

MOVE_POS_DICT = {
    ActionPos.CHALLENGE_AGAIN: [870, 1190],
    ActionPos.CONFIRM_BATTLE: [880, 2280],
    ActionPos.CONFIRM_SKILL: [330, 1780],
    ActionPos.CHOOSE_REFILL_ALL_STAMINA: [570, 1590],
    ActionPos.CONFIRM_REFILL_STAMINA: [345, 1800]
}

IMAGE_RANGES = {
    ActionWaitUntilType.BATTLE_TEXT: [480, 448, 600, 483],
    ActionWaitUntilType.CHALLENGE_AGAIN_BUTTON: [745, 1131, 1001, 1239],
    ActionWaitUntilType.CONFIRM_BUTTON: [750, 2230, 1030, 2335],
    ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT: [376, 679, 697, 706]
}

IMAGE_PATHS = {
    ActionWaitUntilType.BATTLE_TEXT: 'working_space/template_battle_text.jpg',
    ActionWaitUntilType.CHALLENGE_AGAIN_BUTTON: 'working_space/template_challenge_again_button.jpg',
    ActionWaitUntilType.CONFIRM_BUTTON: 'working_space/template_confirm_button.jpg',
    ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT: 'working_space/template_insufficient_stamina_text.jpg'
}

# action list

refill_all_stamina_action_list = [
    ActionClick(ActionPos.CHOOSE_REFILL_ALL_STAMINA, after_delay=2000),
    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA, after_delay=4000),
    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA, after_delay=4000),
]

confirm_battle_action_list = [
    ActionClick(ActionPos.CONFIRM_BATTLE, after_delay=12000)
]

initial_skill_action_list = [
    ActionClick('c2'),
    ActionClick('c3'),
    ActionClick('c4'),
    ActionClick(ActionPos.CONFIRM_SKILL),
    ActionClick('c5')
]

# action set

default_guild_event_action_set = ActionSet(
    'default guild event', 
    'ctrl+l', 
    confirm_battle_action_list + 
    initial_skill_action_list + 
    [ActionWaitUntil(ActionWaitUntilType.BATTLE_TEXT)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionWaitUntil(ActionWaitUntilType.CONFIRM_BUTTON_OR_INSUFFICIENT_STAMINA_TEXT)])

default_guild_event_action_set_multiple = ActionSet(
    'default guild event multiple', 
    'ctrl+alt+l', 
    default_guild_event_action_set.action_list * 20)

action_set_list = [default_guild_event_action_set, default_guild_event_action_set_multiple]
