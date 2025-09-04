import pyautogui
import cv2
import numpy as np

import pyautogui
import time

def capture_screen(region=None, retries=3, delay=0.2):
    attempt = 0
    while attempt < retries:
        try:
            return pyautogui.screenshot(region=region)
        except OSError:
            attempt += 1
            time.sleep(delay)
    raise OSError("Screen grab failed after {0} retries".format(retries))

def screenshot(region):
    img = capture_screen(region=region)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)