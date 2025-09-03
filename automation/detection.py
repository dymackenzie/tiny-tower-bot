import time
import cv2
import hashlib
from automation.screen import screenshot

def hash_region(img):
    small = cv2.resize(img, (50, 20))
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    return hashlib.md5(gray.tobytes()).hexdigest()

def wait_for_coin_change(region, check_interval=0.2):
    last_hash = hash_region(screenshot(region=region))
    
    while True:
        time.sleep(check_interval)
        current_hash = hash_region(screenshot(region=region))
        
        if current_hash != last_hash:
            return True
        
        last_hash = current_hash
