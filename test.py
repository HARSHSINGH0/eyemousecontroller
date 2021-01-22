import pyautogui
pyautogui.FAILSAFE = True
from tkinter import *
from pynput.mouse import Listener,Button,Controller
tk=Tk()
import time
mouse=Controller()
movex=50
movey=50
mouse.position=(960,540)
while True:
    time.sleep(0.5)
    mouse.move(movex,movey)