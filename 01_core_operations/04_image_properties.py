import cv2

# Görüntüyü oku
path = "test_images/forest.jpg"
img = cv2.imread(path)

# Görüntünün boyutlarını, kanal sayısını ve toplam piksel sayısını al
height, width, channels = img.shape
image_size = img.size

# Görüntü bilgilerini ekrana yazdır
print("Image Shape: {}".format(img.shape))
print("Height: {} pixels".format(height))
print("Width: {} pixels".format(width))
print("Channels: {}".format(channels))
print("Image Size: {} pixels".format(image_size))

# Görüntüyü ekranda göster
cv2.imshow("Forest", img)

# Bir tuşa basılmasını bekleyerek programı durdur
cv2.waitKey(0)

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
