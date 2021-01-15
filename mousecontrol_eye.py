import pyautogui
pyautogui.FAILSAFE = True
from pynput.mouse import Listener,Button,Controller
import time
mouse= Controller()
class mouseclass:

    def left_click(self):
        mouse.click(Button.left,1)
    def right_click(self):
        
        mouse.click(Button.right,1)

    def navigateto(self,x,y):
        mouse.position=(x,y)