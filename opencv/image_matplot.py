#-*- coding:utf-8 -*-
import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

b,g,r= cv2.split(img)
img=cv2.merge([r, g, b])

plt.imshow(img)
plt.xticks([]), plt.yticks([])
plt.show()

