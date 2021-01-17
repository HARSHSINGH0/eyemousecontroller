import pyautogui
pyautogui.FAILSAFE = True
from pynput.mouse import Listener,Button,Controller
import time
mouse= Controller()
class mouseclass:

    def left_click(self):
        mouse.click(Button.left,1)
        time.sleep(1)#this small line removed multiple click
    def right_click(self):
        print("right click")
        # mouse.click(Button.right,1)
        # time.sleep(1)
    def navigateto(self,x,y):
        mouse.position=(x,y)