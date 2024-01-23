import cv2

# Görüntüyü oku
path = "test_images/basketball.jpg"
img = cv2.imread(path)

# Görüntünün boyutlarını ekrana yazdır
print("Shape: {}".format(img.shape))

# İlgilenilen yüz bölgesini seç (ROI)
roiFace = img[350:500, 0:150]

# Görüntüde farklı bir bölgeye ilgi alanını (ROI) yerleştirme
img[500:650, 400:550] = roiFace

# Görüntüyü ekranda göster
cv2.imshow("Original Image", img)
cv2.imshow("ROI Face", roiFace)

# Bir tuşa basılmasını bekleyerek programı durdurma
cv2.waitKey(0)

# Tüm açık pencereleri kapatma
cv2.destroyAllWindows()
