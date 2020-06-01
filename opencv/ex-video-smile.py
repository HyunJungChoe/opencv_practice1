import numpy as np 
import cv2

faceCascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')
smileCascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while (True):
    # ret : frame capture (boolean)
    # img : Capture frame
    ret, img = cap.read()


    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("video", img)
    #detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20),  
    )
    
   
    for(x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor =1.5,
            minNeighbors = 15,
            minSize =(25, 25),
        )
        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy+ hh), (0, 255, 0), 2)


        cv2.imshow("video", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'): # ESC
        break

cap.release()
cv2.destroyAllWindows()