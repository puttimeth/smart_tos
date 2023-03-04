import cv2
import numpy as np
import os
import data
# from tos_android_control import get_device
from actionEnum import ActionPos, ActionWaitUntilType

# Read the images from the file
# large_image = np.array([[ [0,0,0],  [1,1,1],  [2,2,2],  [3,3,3]],
#               [[10,10,10], [11,11,11], [12,12,12], [13,13,13]],
#               [[20,20,20], [21,21,21], [22,22,22], [23,23,23]]])
# small_image = np.array([[ [0,0,0], [1,1,1]],
#               [ [2,2,2], [3,3,3]]])

# x1, y1, x2, y2
# 465, 440, 605, 490


def save_screenshot(filename='screenshot.jpg'):
    result = device.screencap()
    with open(os.path.join('working_space', filename), 'wb') as f:
        f.write(result)


def mark_image(target, image_range):
    target_image = cv2.imread(target)
    mark_target_image = cv2.rectangle(target_image, (image_range[0], image_range[1]), (image_range[2], image_range[3]), (0,0,255), 1)
    filename, ext = os.path.splitext(target)
    cv2.imwrite(filename + '_mark' + ext, mark_target_image)


def is_similar(template, target, image_range, confidence=0.95):
    target_image = cv2.imread(target)
    template_image = cv2.imread(template)

    # to black white
    (_, target_image) = cv2.threshold(cv2.cvtColor(
        target_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    (_, template_image) = cv2.threshold(cv2.cvtColor(
        template_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

    # crop
    target_image = target_image[image_range[1]
        : image_range[3], image_range[0]: image_range[2]]
    template_image = template_image[image_range[1]
        : image_range[3], image_range[0]: image_range[2]]

    cv2.imshow('a', target_image)

    # direct compare
    compare = target_image == template_image

    # calculate confidence
    conf = np.count_nonzero(compare == 1) / \
        (compare.shape[0] * compare.shape[1])
    print(conf)

    return conf >= confidence


# device = get_device()
# save_screenshot()

# print(is_similar('working_space/screenshot.jpg',
#                  'working_space/full-after-battle-unreveal.jpg', IMAGE_RANGES['battle_text']))

# print(is_similar('working_space/screenshot.jpg',
#                  'working_space/full-after-battle-reveal.jpg', IMAGE_RANGES['battle_text']))

# print(is_similar('working_space/screenshot.jpg',
#                  'working_space/VideoCapture_20220906-153701.jpg', IMAGE_RANGES['battle_text']))
# print(is_similar('working_space/template_battle_text.jpg',
#                  'working_space/template_insufficient_stamina_text.jpg', data.IMAGE_RANGES[ActionWaitUntilType.INSUFFICIENT_STAMINA_TEXT]))

# a = ActionPos.CHOOSE_REFILL_ALL_STAMINA

# target_image = cv2.imread('working_space/screenshot.jpg')
# image_range = IMAGE_RANGES['battle_text']
# (_, target_image) = cv2.threshold(cv2.cvtColor(
#     target_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
# target_image = target_image[image_range[1]
#         : image_range[3], image_range[0]: image_range[2]]
# cv2.imshow('a', target_image)
# cv2.waitKey(0)


# mark_image('working_space/screenshot.jpg', IMAGE_RANGES['battle_text'])
a = ['a','b','c']
print(a * 5)