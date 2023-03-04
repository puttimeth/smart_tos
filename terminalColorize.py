# reference https://learn.microsoft.com/en-us/windows/terminal/customize-settings/color-schemes

from enum import Enum

class Color(Enum):
    RED=31
    GREEN=32
    YELLOW=33
    BLUE=34
    PURPLE=35

def colorize(text: str, color: Color):
    return f'\x1b[{color.value};40m{text}\x1b[0m'