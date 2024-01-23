import cv2
import numpy as np

# İlk resmi oku
img1 = cv2.imread("balls.jpg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_blur1 = cv2.medianBlur(gray1, 5)
circles1 = cv2.HoughCircles(img_blur1, cv2.HOUGH_GRADIENT, 1, img1.shape[0] / 7, param1=200, param2=10, minRadius=30, maxRadius=90)

# İkinci resmi oku
img2 = cv2.imread("coins.jpg")
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
img_blur2 = cv2.medianBlur(gray2, 5)
circles2 = cv2.HoughCircles(img_blur2, cv2.HOUGH_GRADIENT, 1, img2.shape[0] / 4, param1=200, param2=10, minRadius=40, maxRadius=80)

# İlk resimdeki daireleri çiz
if circles1 is not None:
    circles1 = np.uint16(np.around(circles1))
    for i in circles1[0, :]:
        cv2.circle(img1, (i[0], i[1]), i[2], (0, 0, 255), 2)

# İkinci resimdeki daireleri çiz
if circles2 is not None:
    circles2 = np.uint16(np.around(circles2))
    for i in circles2[0, :]:
        cv2.circle(img2, (i[0], i[1]), i[2], (0, 0, 255), 2)

# İki resmi yan yana göster
# result = np.hstack((img1, img2))
cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
