import cv2
import numpy as np
from imutils.video import WebcamVideoStream

def adjust_gamma(image, gamma=1.0):

   invGamma = 1.0 / gamma
   table = np.array([((i / 255.0) ** invGamma) * 255
      for i in np.arange(0, 256)]).astype("uint8")

   return cv2.LUT(image, table)

while True:
   cap=WebcamVideoStream(src=0).start()
   frame=cap.read()
   original = frame
   cv2.imshow('original',original)
   gamma = 2                                   # change the value here to get different result
   adjusted = adjust_gamma(original, gamma=gamma)
   
   cv2.imshow('gamma image 1',adjusted)
   if cv2.waitKey(1) & 0xFF == ord('q') :
       # self.cap.release()
       cv2.destroyAllWindows()
       break