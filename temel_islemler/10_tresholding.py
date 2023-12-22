<<<<<<< HEAD
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("helicopter.jpg",0)

ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Image",img)
cv2.imshow("Image-th1",th1)
cv2.imshow("Image-th2",th2)

cv2.waitKey(0)
=======
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("helicopter.jpg",0)

ret,th1 = cv2.threshold(img,150,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)


cv2.imshow("Image",img)
cv2.imshow("Image-th1",th1)
cv2.imshow("Image-th2",th2)

cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()