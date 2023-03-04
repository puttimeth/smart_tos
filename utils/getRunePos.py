from actionEnum import ActionPos
from typing import Union
import data

x_pos = [i * 180 + 90 for i in range(6)]
y_pos = [1160] + [i * 180 + 1400 for i in range(5)]

def get_rune_pos(code: Union[ActionPos, str]):
    # check special button
    if ActionPos.has_key(code):
        return data.MOVE_POS_DICT[code]
    # check character runestone
    if any([x in code for x in ["c", "char", "character"]]):
        for i in range(1, 7):
            if str(i) in code:
                return [x_pos[i-1], y_pos[0]]
    # check normal runestone
    x, y = code.split()
    re = []
    for i in range(1, 7):
        if str(i) in x:
            re.append(x_pos[i-1])
    for j in range(1, 6):
        if str(j) in y:
            re.append(y_pos[j])
    if len(re) != 2:
        return [x_pos[0], y_pos[0]]
    return re