import cv2 as cv
cv2=cv
import dlib

cap=cv.VideoCapture(0)
while True:
    frame=cap.read()
    cv.imshow("Frame",frame)
    
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()