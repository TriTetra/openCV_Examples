import cv2
import numpy as ny

# ny.zeros kodu ile istediğimiz piksel oranında bir görsel oluşturuyoruz mod 3 tarzında
img = ny.zeros((10,10,3), ny.uint8)

# ve görselin belirli yerlerindeki pikselleri BGR ye göre renklendiriyoruz
img[0,0] = (255,255,255)
img[0,1] = (255,255,200)
img[0,2] = (255,255,170)
img[0,3] = (255,255,100)

# burada görseli büyürüyoruz yani yeniden boyutlanıdırıyoruz
img = cv2.resize(img, (500,500), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()