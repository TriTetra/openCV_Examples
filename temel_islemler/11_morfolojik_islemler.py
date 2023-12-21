import cv2
import numpy as np

img = cv2.imread("helicopter.jpg",0)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=2) # iteration arttıkça bozulma çoklaşır
dilation = cv2.dilate(img,kernel,iterations=2)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

cv2.imshow("Image",img)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Opening",opening)

cv2.waitKey(0)
cv2.destroyAllWindows()
