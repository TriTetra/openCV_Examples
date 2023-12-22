<<<<<<< HEAD
import cv2
import numpy as ny

path = "test_images/engine.jpg"
img = cv2.imread(path)
print(img)

# px = img[10,10]
# print(px)

(b, g, r) = img[50,30]
=======
import cv2
import numpy as ny

path = "test_images/engine.jpg"
img = cv2.imread(path)
print(img)

# px = img[10,10]
# print(px)

(b, g, r) = img[50,30]
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
print("(0,0) - Red: {}, Green: {}, Blue: {}".format(r,g,b))