<<<<<<< HEAD
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((500,500),np.uint8)
cv2.rectangle(img,(0,60),(200,100),(255,255,255),-1)
cv2.rectangle(img,(250,100),(350,200),(255,255,255),-1)

simle_img = cv2.imread("smile.jpg")

cv2.imshow("Simle",simle_img)

b,g,r = cv2.split(simle_img)

# plt.hist() ile histogram da verilen resmi inceleyebiliriz.
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])


#plt.hist(simle_img.ravel(),256,[0,256])
# cv2.imshow("Image",img)
# plt.hist(img.ravel(),256,[0,256])

# plt.show() ile de histogram çıktı olarak görmemizi sağlıyor
plt.show()

cv2.waitKey(0)
=======
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = np.zeros((500,500),np.uint8)
cv2.rectangle(img,(0,60),(200,100),(255,255,255),-1)
cv2.rectangle(img,(250,100),(350,200),(255,255,255),-1)

simle_img = cv2.imread("smile.jpg")

cv2.imshow("Simle",simle_img)

b,g,r = cv2.split(simle_img)

# plt.hist() ile histogram da verilen resmi inceleyebiliriz.
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])


#plt.hist(simle_img.ravel(),256,[0,256])
# cv2.imshow("Image",img)
# plt.hist(img.ravel(),256,[0,256])

# plt.show() ile de histogram çıktı olarak görmemizi sağlıyor
plt.show()

cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()