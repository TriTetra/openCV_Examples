<<<<<<< HEAD
import cv2
import numpy as np

img = cv2.imread("helicopter.jpg", 0)
row, col = img.shape

M = np.float32([[1, 0, 10], [0, 1, 70]])

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
=======
import cv2
import numpy as np

img = cv2.imread("helicopter.jpg", 0)
row, col = img.shape

M = np.float32([[1, 0, 10], [0, 1, 70]])

dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
