import pyautogui
pyautogui.FAILSAFE = True
from tkinter import *
from pynput.mouse import Listener,Button,Controller
tk=Tk()
mouse=Controller()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
class mouseclass:
    def firstpos(self,x,y):
        mouse.position=(x,y)
    def navigateto(self,x,y):
        mouse.position=(x,y)
        print(x,y)
    def left_click(self):
        mouse.click(Button.left,1)
        print("left click")
    def right_click(self):
        print("right click")
        mouse.click(Button.right,1)
    
mouseclass=mouseclass()
middlepoint1,middlepoint2=0,0
if(width==1920):
    middlepoint1,middlepoint2=960,540
mouseclass.firstpos(middlepoint1,middlepoint2)

