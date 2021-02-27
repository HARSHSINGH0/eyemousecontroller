import cv2 as cv
cv2=cv
import dlib
import mousecontrol_eye
from win32.win32api import GetSystemMetrics
import time
from pynput.mouse import Listener,Button,Controller
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from imutils.video import WebcamVideoStream
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
        #dimension=(600,450)#this is 4:3
        dimension=(600,380)
        return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
    def midlinepoint(self,p1,p2):
        return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
    def aspectratiochanger(self,ratio):

        if ratio=="4by3":
            print("if statement ran")
            src = self.frame
            new_width = 450
            dsize = (new_width, src.shape[0])
            self.frame= cv2.resize(src, dsize, interpolation = cv2.INTER_AREA)
        

    def eyetrack(self):
        blinking_frames=self.blinking_frames
        #self.cap=cv.VideoCapture("videos/testvideo.mp4")#using this to lower the fps because video is 30 fps and it is taking it in 60 fps
    
        self.cap=WebcamVideoStream(src="videos/testvideo.mp4").start()
        #self.cap=cv.VideoCapture(self.camerainput-1,cv.CAP_DSHOW)
        cameracheck=self.cameracheck
        self.detector=dlib.get_frontal_face_detector()
        self.predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        mouse=Controller()
        # self.interfaceclass.changestatus(self.interfaceclass,"good")
        while True:
            try:
                errornumber=0
                if cameracheck==False:
                    #_,frame=self.cap.read()
                    frame=self.cap.read()
                    self.frame=frame
                    print("This  is running before function")
                    self.aspectratiochanger("4by3")
                    frame=self.frame
                    print("This  is running after function")
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    gray=self.rescaleFrame(gray)
                    frame=self.rescaleFrame(frame)
                    faces=self.detector(gray)
                else:#this will flip the camera if checkbox is clicked
                    frame=self.cap.read()
                    #_,frame=self.cap.read()
                    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
                    gray=cv.flip(self.rescaleFrame(gray),1)
                    frame=cv.flip(self.rescaleFrame(frame),1)
                    faces=self.detector(gray)
                
                cv.putText(frame,"Q to exit",(230,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
                
                cv.imshow("frame",frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    # self.cap.release()
                    cv2.destroyAllWindows()
                    
                    break
            except :
                cv2.destroyAllWindows()
                
                break
camerainput=1
cameracheck=False
eyemouse=eye_mouse(camerainput,cameracheck)
eyemouse.eyetrack()
cv2.destroyAllWindows()