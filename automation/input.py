import pyautogui
import time
from config import CLICK_DELAY

def click(x, y):
    pyautogui.click(x, y)
    time.sleep(CLICK_DELAY)
