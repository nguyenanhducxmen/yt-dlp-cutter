import os
import time
import tkinter as tk
from tkinter import filedialog

def convert_time(time_str):
    time_str = time_str.replace(",", ".")
    parts = time_str.split(':')
    if len(parts) == 1:
        return float(parts[0])
    elif len(parts) == 2:
        minutes = int(parts[0])
        seconds = float(parts[1])
        return minutes * 60 + seconds
    else:
        hours = int(parts[0])
        minutes = int(parts[1])
        seconds = float(parts[2])
        return hours * 3600 + minutes * 60 + seconds

def select_path(title):
    root = tk.Tk()
    root.withdraw()
    path = filedialog.askdirectory(title=title)
    return path + '/' if path else os.getcwd() + '/'
