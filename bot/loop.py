from .elevator import wait_for_stop
from .actions import visit_zach, exit, visit_kmsf, continue_button
import time

def run():
    runs = 0
    while True:
        try:
            visit_kmsf()
            wait_for_stop()
            exit()
            visit_zach()
            continue_button()
            exit()

            runs += 1
            print(f"Completed {runs} elevator runs.")
        except OSError as e:
            print(f"Elevator run failed: {e}, retrying in 2s...")
            time.sleep(2)
            continue
