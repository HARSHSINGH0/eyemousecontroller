from win32.win32api import GetSystemMetrics
from pynput.mouse import Listener,Button,Controller
mouse=Controller()
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
print(width,height)
def firstpos(x,y):
    mouse.position=(x,y)
def left_click():
    mouse.click(Button.left,1)
def right_click():
    mouse.click(Button.right,1)

if(width==1920):
    middlepoint1,middlepoint2=960,540
firstpos(middlepoint1,middlepoint2)