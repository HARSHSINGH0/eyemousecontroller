import cv2 as cv
cv2=cv
import dlib

cap=cv.VideoCapture(0)
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
while True:
    _,frame=cap.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    faces=detector(gray)
    for face in faces:
        #print(face)
        x,y=face.left(),face.right()
        x1,y1=face.top(),face.bottom()

        cv2.rectangle(frame,(x,x1),(y,y1),(0,255,0),2)
        landmarks=predictor(gray,face)
        x=landmarks.part(37).x
        y=landmarks.part(37).y
        
        cv.circle(frame,(x+5,y+5),3,(0,255,0),1)
    cv.imshow("frame",frame)
    
    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()