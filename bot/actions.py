from automation.input import click
from config import KMSF_BUTTON, ZACH_BUTTON, CONTINUE_BUTTON, EXIT_BUTTON
import time

def visit_kmsf():
    click(KMSF_BUTTON[0], KMSF_BUTTON[1])
    time.sleep(4)

def exit():
    click(EXIT_BUTTON[0], EXIT_BUTTON[1])

def visit_zach():
    click(ZACH_BUTTON[0], ZACH_BUTTON[1])
    time.sleep(4)

def continue_button():
    click(CONTINUE_BUTTON[0], CONTINUE_BUTTON[1])
