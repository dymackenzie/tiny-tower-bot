import pyautogui
import cv2
import numpy as np

def screenshot(region):
    img = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)