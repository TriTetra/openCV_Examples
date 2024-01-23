import cv2
import numpy as np

# Beyaz bir arkaplan oluştur ve Mavi bir daire çizer
circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)

# Beyaz bir arkaplan oluştur ve Kırmızı bir dikdörtgen çizer
rectangle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(rectangle,(150,150),(350,350),(0,0,255),-1)

# İki resmi topla
added = cv2.add(circle,rectangle)
# Belirli bir pikselin değerini yazdır
print("Toplanmiş resimdeki (256, 256) piksel değeri:", added[256, 256])


cv2.imshow("Cricle",circle)
cv2.imshow("Rectangle",rectangle)
cv2.imshow("Add",added)

cv2.waitKey(0)
cv2.destroyAllWindows()


