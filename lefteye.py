import cv2 as cv
cv2=cv
import dlib
from mousecontrol_eye import *
mouseclass=mouseclass()
cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
blinking_frames=0
def __init__(self,blinking_frames,value_of_blink):
    lefteye(value_of_blink,blinking_frames)
def rescaleFrame(frame):
    dimension=(600,450)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
def midlinepoint(p1,p2):
    return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
def lefteye(value_of_blink):
    _,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    gray=rescaleFrame(gray)
    frame=rescaleFrame(frame)
    faces=detector(gray)
    for face in faces:
        landmarks=predictor(gray,face)
        up_point=(midlinepoint(landmarks.part(37),landmarks.part(38)))
        down_point=(midlinepoint(landmarks.part(41),landmarks.part(40)))
        if((up_point[1]-down_point[1])>=value_of_blink):
                blinking_frames+=1
                if (blinking_frames>2):
                    cv.putText(frame,"Left click",(250,150),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
                    mouseclass.left_click()
                    break
            
        else:
            while blinking_frames!=0:
                blinking_frames-=1