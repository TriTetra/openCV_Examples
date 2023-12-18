#ROI: region of interest --> ilgi alanı
import cv2
import numpy as ny

import matplotlib.pyplot as plt

path = "test_images/basketball.jpg"
img = cv2.imread(path)
print("Shape: {}".format(img.shape))

roiFace = img[350:500, 0:150]
img[500:650, 400:550] = roiFace

cv2.imshow("Test", img)
cv2.imshow("roi",roiFace)

cv2.waitKey(0)
cv2.destroyAllWindows()
