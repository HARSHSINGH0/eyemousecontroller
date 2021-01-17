import cv2 as cv
cv2=cv
import dlib
from mousecontrol_eye import *
mouseclass=mouseclass()
cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
blinking_frames=0
def rescaleFrame(frame):
    # scale=0.20
    # width=int(frame.shape[1]*scale)#frame.shape[1] is width of image
    # height=int(frame.shape[0]*scale)#frame.shape[0] is height of image
    # dimension=(width,height)
    dimension=(600,450)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)
def midlinepoint(p1,p2):
    return int((p1.x+p2.x)/2),int((p1.y+p2.y)/2)
def eyetrack(blinking_frames):
    while True:
        _,frame=cap.read()
        gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        gray=rescaleFrame(gray)
        frame=rescaleFrame(frame)
        faces=detector(gray)
        cv.putText(frame,"Q to exit",(250,50),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
        for face in faces:
            #print(face)
            x,y=face.left(),face.right()
            x1,y1=face.top(),face.bottom()
            # print("face top:",x1)
            # print("face bottom:",y1)

            facerect=cv2.rectangle(frame,(x,x1),(y,y1),(255,255,255),2)
            landmarks=predictor(gray,face)
            # left_point=(landmarks.part(36).x,landmarks.part(36).y)
            # right_point=(landmarks.part(39).x,landmarks.part(39).y)
            # hor_line=cv.line(frame,left_point,right_point,(255,255,255),2)
            up_point=(midlinepoint(landmarks.part(37),landmarks.part(38)))
            down_point=(midlinepoint(landmarks.part(41),landmarks.part(40)))
            ver_line=cv.line(frame,up_point,down_point,(255,255,255),1)

            # left_point_r=(landmarks.part(42).x,landmarks.part(42).y)
            # right_point_r=(landmarks.part(45).x,landmarks.part(45).y)
            # hor_line_r=cv.line(frame,left_point_r,right_point_r,(255,255,255),2)
            up_point_r=(midlinepoint(landmarks.part(43),landmarks.part(44)))
            down_point_r=(midlinepoint(landmarks.part(47),landmarks.part(46)))            
            ver_line_r=cv.line(frame,up_point_r,down_point_r,(255,255,255),1)
            value_of_blink=-3#this is for distance about 1 feet

            eyestonosepointx,eyestonosepointy=(landmarks.part(27).x,landmarks.part(27).y)
            #cv.rectangle(frame,(170,460),(320,202),(255,255,255),2)
            # mouseclass.navigateto(eyestonosepointx,eyestonosepointy)
            # print("blinking_frames",blinking_frames)
            print("y1-x1 (for the area of the face):",y1-x1)
            print("distance of eye tips from up to down",(up_point[1]-down_point[1]))
            print(blinking_frames)
            
            if((y1-x1)>170):
                value_of_blink=-6
            elif((y1-x1)>140):
                value_of_blink=-5
            elif((y1-x1)>130):
                value_of_blink=-5
            elif((y1-x1)>120):
                value_of_blink=-4
            elif((y1-x1)<105):
                cv.putText(frame,"come close to the camera",(80,150),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)
                value_of_blink=10
            
            if((up_point[1]-down_point[1])>=value_of_blink):
                blinking_frames+=1
                if (blinking_frames>1):
                    cv.putText(frame,"Left click",(250,150),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
                    mouseclass.left_click()
                    break
            else:
                #print((up_point[1]-down_point[1]))
                while blinking_frames!=0:
                    blinking_frames=0
            #i could have done this with elif too but this will create priority to left clicks

            if((up_point_r[1]-down_point_r[1])>=value_of_blink):
                blinking_frames+=1
                # print((up_point_r[1]-down_point_r[1]))
                if (blinking_frames>1):
                    cv.putText(frame,"Right click",(250,150),cv.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3)
                    mouseclass.right_click()
                    break
            else:
                #print((up_point[1]-down_point[1]))
                while blinking_frames!=0:
                    blinking_frames-=1
            
        cv.imshow("frame",frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
              break
eyetrack(blinking_frames)
cap.release()
cv2.destroyAllWindows()