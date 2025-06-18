# utils/rain.py
import random
import time
import os
import shutil

def matrix_rain(duration=3):
    chars = "01☯∆¥§"
    columns = shutil.get_terminal_size().columns
    end_time = time.time() + duration

    while time.time() < end_time:
        line = "".join(random.choice(chars) for _ in range(columns))
        print
