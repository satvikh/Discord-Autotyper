import config
import pyautogui
import time


    

config.colorama_init()
interval=config.initialize()
config.countdown()

with open("messages.txt",'r') as messages:
    for line in messages:
        pyautogui.typewrite(line,interval=.01)
        time.sleep(interval)