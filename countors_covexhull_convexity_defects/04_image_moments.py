import cv2

# Görüntüyü oku
img = cv2.imread("contour.png")

# Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü eşikleme işlemine tabi tut
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Görüntü üzerindeki konturları bul
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Eğer en az bir kontur bulunmuşsa devam et
if contours:
    # Konturun momentlerini hesapla
    M = cv2.moments(thresh)

    # Ağırlık merkezini hesapla
    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])

    # Ağırlık merkezini içeren bir daire çiz
    cv2.circle(img, (X, Y), 5, (255, 255, 0), -1)

    # Görüntüyü ekrana göster
    cv2.imshow("Image", img)

    # Bekleme ve pencereleri kapatma
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Kontur bulunamadı.")
