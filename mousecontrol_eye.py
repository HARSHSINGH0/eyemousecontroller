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
def navigateto(x,y,current_value):
    current_value1=[]
    current_value1.append(x)
    current_value1.append(y)
    movex=0
    movey=0
    if((current_value1[0]-current_value[0])<0):
        movex=(current_value1[0]-current_value[0])+(-5)
    elif((current_value1[0]-current_value[0])>0):
        movey=(current_value1[0]-current_value[0])+5
    if((current_value1[1]-current_value[1])<0):
        movey=(current_value1[1]-current_value[1])+(-5)
    elif((current_value1[1]-current_value[1])>0):
        movey=((current_value1[1]-current_value[1])+5)
    mouse.move(movex,movey)
    print((current_value1[0]-current_value[0]),(current_value1[1]-current_value[1]))
    current_value.pop()
    current_value.pop()
    current_value.append(current_value1[0])
    current_value.append(current_value1[1])
    current_value1.pop()
    current_value1.pop()

if(width==1920):
    middlepoint1,middlepoint2=960,540
firstpos(middlepoint1,middlepoint2)