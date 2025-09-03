from automation.detection import wait_for_coin_change
from config import COIN_REGION

def wait_for_stop():
    return wait_for_coin_change(COIN_REGION)
