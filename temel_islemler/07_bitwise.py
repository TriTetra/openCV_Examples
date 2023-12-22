<<<<<<< HEAD
import cv2
import numpy as ny

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")
# Beyaz yerler 1 Siyah yerler 0 olarak düşünürsek
bit_and = cv2.bitwise_and(img2,img1) # burada 0 and 1 olduğundan hep siyah yani 0 sonuçyur
bit_or = cv2.bitwise_or(img2,img1) # burada 0 or 1 olduğu için sonuç 1 dir yani beyaz
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not = cv2.bitwise_not(img2)
bit_not1 = cv2.bitwise_not(img1)


cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("Bit_And",bit_and)
cv2.imshow("Bit_Or",bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows()
=======
import cv2
import numpy as ny

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")
# Beyaz yerler 1 Siyah yerler 0 olarak düşünürsek
bit_and = cv2.bitwise_and(img2,img1) # burada 0 and 1 olduğundan hep siyah yani 0 sonuçyur
bit_or = cv2.bitwise_or(img2,img1) # burada 0 or 1 olduğu için sonuç 1 dir yani beyaz
bit_xor = cv2.bitwise_xor(img2,img1)
bit_not = cv2.bitwise_not(img2)
bit_not1 = cv2.bitwise_not(img1)


cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("Bit_And",bit_and)
cv2.imshow("Bit_Or",bit_or)

cv2.waitKey(0)
cv2.destroyAllWindows()
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
