import cv2
import numpy as ny

path = "test_images/engine.jpg"
img = cv2.imread(path)
print(img)

# px = img[10,10]
# print(px)

(b, g, r) = img[50,30]
print("(0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))