import pyautogui
pyautogui.FAILSAFE = True
from tkinter import *
from pynput.mouse import Listener,Button,Controller
tk=Tk()
mouse=Controller()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()

def firstpos(x,y):
    mouse.position=(x,y)
# def navigateto(x,y):
#     currentvalue1=x,y
#     currentvalue=currentvalue1-currentvalue
#     mouse.move(currentvalue)
#     currentvalue=currentvalue1
#     print(x,y)
def left_click():
    # mouse.click(Button.left,1)
    print("left click")
def right_click():
    print("right click")
    # mouse.click(Button.right,1)
    

middlepoint1,middlepoint2=0,0
if(width==1920):
    middlepoint1,middlepoint2=960,540
firstpos(middlepoint1,middlepoint2)