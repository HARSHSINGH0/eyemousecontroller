import pyautogui
pyautogui.FAILSAFE = True
from pynput.mouse import Listener,Button,Controller
import time
mouse= Controller()
class mouseclass:

    def left_click(self):
        print("left click")
        mouse.click(Button.left,1)
    def right_click(self):
        print("right click")

    def navigateto(self,x,y):
        print("navigate to")