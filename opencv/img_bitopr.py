import cv2
import numpy as np

imgFile1 ='happy_.jpg'
imgFile2 = 'sample.jpg'


img1 = cv2.imread(imgFile1)
img2 = cv2.imread(imgFile2)

bit_and = cv2.bitwise_and(img1, img2)
bit_or = cv2.bitwise_or(img2, img1)
bit_not = cv2.bitwise_not(img2)
bit_xor = cv2.bitwise_xor(img2, img1)

cv2.imshow("bit_and", bit_and)
cv2.imshow("bit_or", bit_or)
cv2.imshow("bit_not", bit_not)
cv2.imshow("bit_xor", bit_xor)

cv2.waitKey(0)
cv2.destroyAllWindows()


