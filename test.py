import pyautogui
pyautogui.FAILSAFE = True
from tkinter import *
import cv2 as cv
from pynput.mouse import Listener,Button,Controller
import dlib
tk=Tk()
cv2=cv
mouse=Controller()
width = tk.winfo_screenwidth()
height = tk.winfo_screenheight()
cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
blinking_frames=0
current_value=[0,0]
def rescaleFrame(frame):
    dimension=(600,450)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
while True:
    _,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray=rescaleFrame(gray)
    frame=rescaleFrame(frame)
    faces=detector(gray)
    cv.putText(frame,"Q to exit",(230,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)


def firstpos(x,y):
    mouse.position=(x,y)

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
    
    mouse.move(movex,movey)
    print((current_value1[0]-current_value[0]),(current_value1[1]-current_value[1]))
    current_value.pop()
    current_value.pop()
    current_value.append(current_value1[0])
    current_value.append(current_value1[1])
    current_value1.pop()
    current_value1.pop()



print("choose navigation mode between 1/2/3")
print("set this according to your camera angle")
print("choose 1 if your face in camera is in upper part")
print("choose 2 if your face in camera is in middle part")
print("choose 3 if your face in camera is in lower part")
print("most of the user prefer option 3 as all are sitting in chair")
navigationrectsmall=input()
def navigation_noserectangle(value):
    
    if value=="else":
        print("As wrong input given computer automatically switched to default mode 3")
        rectangle_nav=cv.rectangle(frame,(250,225),(350,300),(255,255,255),2)
    elif value==1:
        rectangle_nav=cv.rectangle(frame,(250,125),(350,175),(255,255,255),2)
    elif value==2:
        rectangle_nav=cv.rectangle(frame,(250,175),(350,225),(255,255,255),2)
    elif value==3:
        rectangle_nav=cv.rectangle(frame,(250,225),(350,300),(255,255,255),2)
    
if(navigationrectsmall==1):
    navigation_noserectangle(1)
elif(navigationrectsmall==2):
    navigation_noserectangle(2)
elif(navigationrectsmall==3):
    navigation_noserectangle(3)
else:
    navigation_noserectangle("else")

    
if(width==1920):
    middlepoint1,middlepoint2=960,540
firstpos(middlepoint1,middlepoint2)