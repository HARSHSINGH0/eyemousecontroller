import pyautogui
pyautogui.FAILSAFE = True
from tkinter import *
import cv2 as cv
from pynput.mouse import Listener,Button,Controller
import dlib
# tk=Tk()
cv2=cv
mouse=Controller()
# width = tk.winfo_screenwidth()
# height = tk.winfo_screenheight()
cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
blinking_frames=0
current_value=[0,0]
def rescaleFrame(frame):
    dimension=(600,450)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

def eyetrack(blinking_frames,navigationrectsmall):
    

  
    while True:

        _,frame=cap.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        gray=rescaleFrame(gray)
        frame=rescaleFrame(frame)
        faces=detector(gray)
        cv.putText(frame,"Q to exit",(230,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

        
        if(navigationrectsmall==1):
            rectangle_nav=cv.rectangle(frame,(300,125),(350,175),(255,255,255),2)
        elif(navigationrectsmall==2):
            rectangle_nav=cv.rectangle(frame,(300,175),(350,225),(255,255,255),2)
        elif(navigationrectsmall==3):
            rectangle_nav=cv.rectangle(frame,(300,300),(350,350),(255,255,255),2)
        else:
            rectangle_nav=cv.rectangle(frame,(300,300),(350,350),(255,255,255),2)
        
        cv.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    
    
    

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
navigationrectsmall=int(input())
eyetrack(blinking_frames,navigationrectsmall)
  
# if(width==1920):
#     middlepoint1,middlepoint2=960,540
# firstpos(middlepoint1,middlepoint2)
