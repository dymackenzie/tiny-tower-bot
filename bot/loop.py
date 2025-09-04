from .elevator import wait_for_stop
from .actions import visit_zach, exit, visit_kmsf, continue_button

def run():
    runs = 0
    while True:
        visit_kmsf()
        wait_for_stop()
        exit()
        visit_zach()
        continue_button()
        exit()

        runs += 1
        print(f"Completed {runs} elevator runs.")
