import cv2 as cv
cv2=cv
import dlib
from mousecontrol_eye import *

cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

class lefteyeblink:
    def __init__(self,blinking_frames,value_of_blink,landmarks):
        self.value_of_blink=value_of_blink
        self.blinking_frames=blinking_frames
        self.landmarks=landmarks
    def rescaleFrame(self,frame):
        dimension=(600,450)
        return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    def midlinepoint(self,p1,p2):
        return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
    def lefteye(self):
        up_point=(midlinepoint(landmarks.part(37),landmarks.part(38)))
        down_point=(midlinepoint(landmarks.part(41),landmarks.part(40)))
        if((up_point[1]-down_point[1])>=value_of_blink):
                blinking_frames+=1
                if (blinking_frames>2):
                    mouseclass.left_click()
                
        else:
            while blinking_frames!=0:
                blinking_frames-=1
