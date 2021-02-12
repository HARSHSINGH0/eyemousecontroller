import cv2 as cv
cv2=cv
import dlib
import mousecontrol_eye
from win32.win32api import GetSystemMetrics
import time
from pynput.mouse import Listener,Button,Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class eye_mouse:
    def __init__(self,camerainput,cameracheck):
            self.camerainput=int(camerainput)
            self.blinking_frames=0
            self.mousecontrol=mousecontrol_eye.mousecontrol()
            self.cameracheck=cameracheck
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
            middlepoint1=width/2
            middlepoint2=height/2
            self.mousecontrol.firstpos(middlepoint1,middlepoint2)
    def rescaleFrame(self,frame):
        dimension=(600,450)
        return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    def midlinepoint(self,p1,p2):
        return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
    def eyetrack(self):
        blinking_frames=self.blinking_frames
        self.cap=cv.VideoCapture(self.camerainput-1,cv.CAP_DSHOW)
        cameracheck=self.cameracheck
        self.detector=dlib.get_frontal_face_detector()
        self.predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        mouse=Controller()
        # self.interfaceclass.changestatus(self.interfaceclass,"good")
        while True:
            try:
                errornumber=0
                if cameracheck==False:
                    _,frame=self.cap.read()
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    gray=self.rescaleFrame(gray)
                    frame=self.rescaleFrame(frame)
                    faces=self.detector(gray)
                else:#this will flip the camera if checkbox is clicked
                    _,frame=self.cap.read()
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    gray=cv.flip(self.rescaleFrame(gray),1)
                    frame=cv.flip(self.rescaleFrame(frame),1)
                    faces=self.detector(gray)
                
                cv.putText(frame,"Q to exit",(230,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                for face in faces:
                    x,y=face.left(),face.right()
                    x1,y1=face.top(),face.bottom()
                    facerect=cv2.rectangle(frame,(x,x1),(y,y1),(255,255,255),2)
                    landmarks=self.predictor(gray,face)
                    noselandmark=(landmarks.part(30).x,landmarks.part(30).y)
                    xvaluerectsmall=275
                    yvaluerectsmall=300
                    xvaluerectsmall_r=325
                    yvaluerectsmall_r=350
                    eyestonosepointx,eyestonosepointy=landmarks.part(30).x,landmarks.part(30).y
                    nose_to_cursorx=325
                    nose_to_cursory=290
                    cv.rectangle(frame,(eyestonosepointx,eyestonosepointy),(eyestonosepointx,eyestonosepointy),(255,255,255),thickness=4)
                    cv.rectangle(frame,(nose_to_cursorx,nose_to_cursory),(nose_to_cursorx,nose_to_cursory),(0,0,0),thickness=5)
                    cv.line(frame,(eyestonosepointx,eyestonosepointy),(nose_to_cursorx,nose_to_cursory),(255,255,255),thickness=2)
                    positivecursorvalue=15
                    negativesursorvalue=-15
                    if((eyestonosepointx-nose_to_cursorx)>positivecursorvalue):
                        if((eyestonosepointx-nose_to_cursorx)>40):
                            mouse.move(8,0) #this is for gradually increasing the speed
                        elif((eyestonosepointx-nose_to_cursorx)>15):
                            mouse.move(2,0)#this is moving right
                    if((eyestonosepointx-nose_to_cursorx)<negativesursorvalue):
                        if((eyestonosepointx-nose_to_cursorx)<-40):
                            mouse.move(-8,0) #this is for gradually increasing the speed
                        elif((eyestonosepointx-nose_to_cursorx)<-15):
                            mouse.move(-2,0)#this is moving left
                    if(eyestonosepointy-nose_to_cursory)<positivecursorvalue:
                        if(eyestonosepointy-nose_to_cursory)<15:
                            mouse.move(0,-3)#this is moving up
                    if(eyestonosepointy-nose_to_cursory)>negativesursorvalue:
                        if(eyestonosepointy-nose_to_cursory)>-15:
                            mouse.move(0,3)# this is moving down
                    left_point=(landmarks.part(36).x,landmarks.part(36).y)
                    right_point=(landmarks.part(39).x,landmarks.part(39).y)
                    hor_line=cv.line(frame,left_point,right_point,(255,255,255),2)
                    up_point=(self.midlinepoint(landmarks.part(37),landmarks.part(38)))
                    down_point=(self.midlinepoint(landmarks.part(41),landmarks.part(40)))
                    ver_line=cv.line(frame,up_point,down_point,(255,255,255),2)
                    left_point_r=(landmarks.part(42).x,landmarks.part(42).y)
                    right_point_r=(landmarks.part(45).x,landmarks.part(45).y)
                    hor_line_r=cv.line(frame,left_point_r,right_point_r,(255,255,255),2)
                    up_point_r=(self.midlinepoint(landmarks.part(43),landmarks.part(44)))
                    down_point_r=(self.midlinepoint(landmarks.part(47),landmarks.part(46)))            
                    ver_line_r=cv.line(frame,up_point_r,down_point_r,(255,255,255),2)
                    value_of_blink=-3#this is for distance about 1 feet
                    if((y1-x1)>170):
                        value_of_blink=-7
                    elif((y1-x1)>140):
                        value_of_blink=-6
                    elif((y1-x1)>130):
                        value_of_blink=-5
                    elif((y1-x1)>120):
                        value_of_blink=-4
                    elif((y1-x1)<105):
                        cv.putText(frame,"come close to the camera",(80,150),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
                        value_of_blink=10
                    if((up_point[1]-down_point[1])>=value_of_blink):
                        blinking_frames+=1
                        
                        if (blinking_frames>2):
                            blinking_frames=0#this will reduce multiple clicks
                            cv.putText(frame,"Left click",(250,150),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
                            self.mousecontrol.left_click()
                    elif((up_point_r[1]-down_point_r[1])>=value_of_blink):
                        blinking_frames+=1
                        if (blinking_frames>1):
                            blinking_frames=0#this will reduce multiple clicks
                            cv.putText(frame,"Right click",(250,150),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
                            self.mousecontrol.right_click()
                    else:
                        while blinking_frames!=0:
                            blinking_frames-=1
                
                cv.imshow("frame",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # self.cap.release()
                    cv2.destroyAllWindows()
                    break
            except :
                cv2.destroyAllWindows()
                break

cv2.destroyAllWindows()