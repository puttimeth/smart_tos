import os
import numpy as np
import data
import cv2
from terminalColorize import colorize, Color
from actionEnum import ActionWaitUntilType

def save_screenshot(filename='screenshot.jpg'):    
    if data.device:
        result = data.device.screencap()
        with open(os.path.join('working_space', filename), 'wb') as f:
            f.write(result)
    else:
        print(colorize('Device not found.', Color.RED))

def is_template_appear_in_screenshot(template: ActionWaitUntilType, screenshot_path='working_space/screenshot.jpg', confidence=0.95):
    # get template_path and image_range from template
    template_path = data.IMAGE_PATHS[template]
    image_range = data.IMAGE_RANGES[template]

    # load image
    screenshot_image = cv2.imread(screenshot_path)
    template_image = cv2.imread(template_path)

    # crop
    screenshot_image = screenshot_image[image_range[1]
        : image_range[3], image_range[0]: image_range[2]]
    template_image = template_image[image_range[1]
        : image_range[3], image_range[0]: image_range[2]]

    # to black white by thresholding
    (_, screenshot_image) = cv2.threshold(cv2.cvtColor(
        screenshot_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    (_, template_image) = cv2.threshold(cv2.cvtColor(
        template_image, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)

    # direct compare
    compare = screenshot_image == template_image

    # calculate confidence
    conf = np.count_nonzero(compare == 1) / (compare.shape[0] * compare.shape[1])

    return conf >= confidence