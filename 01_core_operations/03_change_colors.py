import cv2
import numpy as np

# Görüntüyü oku
path = "test_images/OpenCV.jpg"
img = cv2.imread(path)

# Görüntünün boyutlarını al
height, width, channels = img.shape

# Belirli bir bölgeyi seç (sol üst köşe)
corner = img[0:100, 0:100]

# Belirli bir bölgeyi seç (100-300 arasındaki bölge)
corner_1 = img[100:300, 100:300]

# Seçilen bölgelere renk atama
corner[:, :] = (255, 0, 0)  # Sol üst köşeye mavi renk ata
corner_1[:, :] = (0, 255, 0)  # Diğer bölgeye yeşil renk ata

# Görüntüyü ekranda göster
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.imshow("Original Image", img)

# Seçilen bölgeleri ekranda göster
cv2.imshow("Corner (Blue)", corner)
cv2.imshow("Corner_1 (Green)", corner_1)

# Bir tuşa basılmasını bekleyerek programı durdur
cv2.waitKey(0)

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
