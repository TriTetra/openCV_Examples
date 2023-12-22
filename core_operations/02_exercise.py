<<<<<<< HEAD
import cv2
import numpy as ny

import matplotlib.pyplot as ply

path = "test_images/OpenCV.jpg"
img = cv2.imread(path)
# print(img)

corner = img[0:100, 0:100]
corner_1 = img[100:300, 100:300]

img[0:100, 0:255] = (255,255,0)

cv2.namedWindow("Test",cv2.WINDOW_NORMAL)
cv2.imshow("Test",img)
cv2.imshow("Corner",corner)
cv2.imshow("Corner_1", corner_1)

cv2.waitKey(0)
=======
import cv2
import numpy as ny

import matplotlib.pyplot as ply

path = "test_images/OpenCV.jpg"
img = cv2.imread(path)
# print(img)

corner = img[0:100, 0:100]
corner_1 = img[100:300, 100:300]

img[0:100, 0:255] = (255,255,0)

cv2.namedWindow("Test",cv2.WINDOW_NORMAL)
cv2.imshow("Test",img)
cv2.imshow("Corner",corner)
cv2.imshow("Corner_1", corner_1)

cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()