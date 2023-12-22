<<<<<<< HEAD
import cv2
import numpy as np

img = cv2.imread("helicopter.jpg",0)
col,row = img.shape

M = cv2.getRotationMatrix2D((col/2,row/2),90,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("Dst",dst)

cv2.waitKey(0)
=======
import cv2
import numpy as np

img = cv2.imread("helicopter.jpg",0)
col,row = img.shape

M = cv2.getRotationMatrix2D((col/2,row/2),90,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("Dst",dst)

cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()