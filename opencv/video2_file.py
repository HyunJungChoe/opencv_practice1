import cv2
from picamera import PiCamera

cap = cv2.VideoCapture('sample.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
            

cap.release()
cv2.destroyAllWindows()