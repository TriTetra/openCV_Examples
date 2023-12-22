<<<<<<< HEAD
import cv2
import numpy as ny

import matplotlib.pyplot as plt

path = "test_images/forest.jpg"
img = cv2.imread(path)

print(img.shape)
# width, height, channel
# channel:3 --> color
# channel:1 --> grayscale

print("height: {} pixels".format(img.shape[0]))
print("width: {} pixels".format(img.shape[1]))
print("channel: {} pixels".format(img.shape[2]))


print("Image Size: {}".format(img.size))

cv2.imshow("Forest",img)

cv2.waitKey(0)
=======
import cv2
import numpy as ny

import matplotlib.pyplot as plt

path = "test_images/forest.jpg"
img = cv2.imread(path)

print(img.shape)
# width, height, channel
# channel:3 --> color
# channel:1 --> grayscale

print("height: {} pixels".format(img.shape[0]))
print("width: {} pixels".format(img.shape[1]))
print("channel: {} pixels".format(img.shape[2]))


print("Image Size: {}".format(img.size))

cv2.imshow("Forest",img)

cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()