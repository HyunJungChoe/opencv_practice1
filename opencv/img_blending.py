import cv2
import numpy as np

img1 = cv2.imread('flower1.jpg')
img2 = cv2.imread('flower2.jpg')

while True:
    dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
    cv2.imshow('dst', dst)

    if cv2.waitKey(1) & 0xFF ==27:
        break

cv2.destroyAllWindows()

