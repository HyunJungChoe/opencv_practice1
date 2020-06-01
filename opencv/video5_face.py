import cv2
import numpy as np 


# cascPath = sys.argv[1]
# faceCascade = cv2.CascadeClassifier(cascPath)
faceCascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)
#print('width: {0}, height: {1}'.format(video_capture.get(3), video_capture.get(4)))

# cap.get(prodId)/cap.set(propId, value) can change video properties

video_capture.set(3,640) # set Width
video_capture.set(4,480) # set Height



while (True):
    # ret : frame capture (boolean)
    # frame : Capture frame
    ret, frame = video_capture.read()

    if (ret):

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Faces Found", frame)
        

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags = cv2.CASCADE_SCALE_IMAGE #python2: flags = cv2.cv.CV_HAAR_SCALE_IMAGE
        )

        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.imshow("Faces Found", frame)
        
        
    if cv2.waitKey(1) & 0xFF == ord('q'): # ESC
        break

video_capture.release()
cv2.destroyAllWindows()