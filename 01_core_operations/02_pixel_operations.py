import cv2
import numpy as np

# Görüntüyü oku
img = cv2.imread("test_images/OpenCV.jpg")

# Görüntünün boyutlarını al
height, width, channels = img.shape

# Belirli bir bölgeyi seç
roi = img[100:300, 100:300]

# Seçilen bölgeye renk atama
roi[:, :] = (0, 255, 0)  # Tüm piksellere yeşil renk ata

# Görüntüyü aynalama
mirrored_img = cv2.flip(img, 1)  # 1: Yatay aynalama

# Görüntüyü gri tonlamaya çevir
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Görüntüyü 2 kat büyütme
resized_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Görüntüyü ekranda göster
cv2.imshow("Original Image", img)
cv2.imshow("Region of Interest", roi)
cv2.imshow("Mirrored Image", mirrored_img)
cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("Resized Image", resized_img)

# Bir tuşa basılmasını bekleyerek programı durdur
cv2.waitKey(0)

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
