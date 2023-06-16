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
    ActionPos.CHOOSE_REFILL_ALL_STAMINA: [570, 1460],
    ActionPos.CONFIRM_REFILL_STAMINA: [345, 1920],
    ActionPos.CHOOSE_SECOND_SKILL: [540, 1410]
}

IMAGE_RANGES = {
    ActionWaitUntilType.BATTLE_TEXT: [480, 478, 600, 512],
    ActionWaitUntilType.CHALLENGE_AGAIN_BUTTON: [745, 1160, 1001, 1269],
    ActionWaitUntilType.CONFIRM_BUTTON: [750, 2230, 1030, 2335],
    ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT: [375, 547, 697, 575],
    ActionWaitUntilType.LEVEL_UP_TEXT: [476, 1121, 681, 1154]
}

IMAGE_PATHS = {
    ActionWaitUntilType.BATTLE_TEXT: 'working_space/template_battle_text.jpg',
    ActionWaitUntilType.CHALLENGE_AGAIN_BUTTON: 'working_space/template_challenge_again_button.jpg',
    ActionWaitUntilType.CONFIRM_BUTTON: 'working_space/template_confirm_button.jpg',
    ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT: 'working_space/template_insufficient_stamina_text.jpg',
    ActionWaitUntilType.LEVEL_UP_TEXT: 'working_space/template_level_up_text.jpg'
}

# action list

refill_all_stamina_action_list = [
    ActionClick(ActionPos.CHOOSE_REFILL_ALL_STAMINA, after_delay=2000),
    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA, after_delay=4000),
    ActionClick(ActionPos.CONFIRM_REFILL_STAMINA, after_delay=4000),
]

confirm_battle_action_list = [
    ActionClick(ActionPos.CONFIRM_BATTLE, after_delay=15000)
]

initial_skill_action_list = [
    ActionClick('c6', after_delay=1500),
    ActionClick(ActionPos.CHOOSE_SECOND_SKILL, after_delay=1000),
    ActionClick(ActionPos.CONFIRM_SKILL, after_delay=2000),
]

mid_stage_skill_action_list = [
    ActionClick('c2', after_delay=10000),
    ActionClick('c2', after_delay=10000),
    ActionClick('c2', after_delay=10000),
    ActionClick('c2', after_delay=10000),
    ActionClick('c3', after_delay=2000),
    ActionMove('5 1', '6 1', duration=500, after_delay=18000),
    ActionClick('c2', after_delay=10000),
    ActionClick('c4', after_delay=2000),
    ActionMove('1 1', '2 1', duration=500, after_delay=3000),
]

# action set

default_guild_event_action_set = ActionSet(
    'default guild event', 
    'ctrl+l', 
    confirm_battle_action_list + 
    initial_skill_action_list +
    mid_stage_skill_action_list +
    [ActionWaitUntil(ActionWaitUntilType.BATTLE_TEXT_OR_LEVEL_UP_TEXT)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionWaitUntil(ActionWaitUntilType.CONFIRM_BUTTON_OR_INSUFFICIENT_STAMINA_TEXT)])

default_guild_event_action_set_multiple = ActionSet(
    'default guild event multiple', 
    'ctrl+alt+l', 
    default_guild_event_action_set.action_list * 20)

no_refill_guild_event_action_set = ActionSet(
    'default guild event', 
    'ctrl+m', 
    confirm_battle_action_list + 
    initial_skill_action_list + 
    [ActionWaitUntil(ActionWaitUntilType.BATTLE_TEXT)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionClick(ActionPos.CHALLENGE_AGAIN)] +
    [ActionWaitUntil(ActionWaitUntilType.CONFIRM_BUTTON)])

no_refill_guild_event_action_set_multiple = ActionSet(
    'default guild event', 
    'ctrl+alt+m', 
    no_refill_guild_event_action_set.action_list * 20)


action_set_list = [default_guild_event_action_set, default_guild_event_action_set_multiple, no_refill_guild_event_action_set_multiple]