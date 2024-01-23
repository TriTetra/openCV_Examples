import cv2
import numpy as np


# Resimleri oku
img_cat = cv2.imread("cat.jpg")
img_dog = cv2.imread("dog.jpg")
img_duck = cv2.imread("duck.jpg")
img_klon = cv2.imread("klon.jpg")

# İmajların veri tiplerini ve şekillerini incele
print("img_cat - Veri Tipi:", img_cat.dtype, " Şekil:", img_cat.shape)
print("img_dog - Veri Tipi:", img_dog.dtype, " Şekil:", img_dog.shape)
print("img_duck - Veri Tipi:", img_duck.dtype, " Şekil:", img_duck.shape)
print("img_klon - Veri Tipi:", img_klon.dtype, " Şekil:", img_klon.shape)

# Resimleri farklı boyutlara boyutlandır
resized_cat = cv2.resize(img_cat, (300, 300))
resized_dog = cv2.resize(img_dog, (700, 700))
resized_duck = cv2.resize(img_duck, (900, 900))
resized_klon = cv2.resize(img_klon, (500, 500))

# Yeniden boyutlandırılmış resimlerin veri tiplerini ve şekillerini incele
print("resized_cat - Veri Tipi:", resized_cat.dtype, " Şekil:", resized_cat.shape)
print("resized_dog - Veri Tipi:", resized_dog.dtype, " Şekil:", resized_dog.shape)
print("resized_duck - Veri Tipi:", resized_duck.dtype, " Şekil:", resized_duck.shape)
print("resized_klon - Veri Tipi:", resized_klon.dtype, " Şekil:", resized_klon.shape)

# Pencerelere ad ver
cv2.namedWindow("Cat Resized", cv2.WINDOW_NORMAL)
cv2.namedWindow("Dog Resized", cv2.WINDOW_NORMAL)
cv2.namedWindow("Duck Resized", cv2.WINDOW_NORMAL)
cv2.namedWindow("Klon Resized", cv2.WINDOW_NORMAL)

# Yeniden boyutlandırılmış resimleri göster
cv2.imshow("Cat Resized", resized_cat)
cv2.imshow("Dog Resized", resized_dog)
cv2.imshow("Duck Resized", resized_duck)
cv2.imshow("Klon Resized", resized_klon)

# Bir tuşa basılmasını bekleyerek programı durdur
cv2.waitKey(0)

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
