import cv2

# Görüntüyü oku
img = cv2.imread("contour.png")

# Görüntüyü gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gri tonlamalı görüntüyü eşikleme işlemine tabi tut
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Görüntü üzerindeki konturları bul
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# İlk konturu seç
cnt = contours[0]

# Konturun alanını hesapla
area = cv2.contourArea(cnt)

# Konturun momentlerini hesapla
M = cv2.moments(cnt)

# Konturun alanını ve momentlerini ekrana yazdır
print("Alan:", area)
print("Moment m00:", M["m00"])

# Konturun çevresini hesapla
perimeter = cv2.arcLength(cnt, True)

# Çevreyi ekrana yazdır
print("Çevre:", perimeter)

'''
# Açıklama: Eğer görüntüleri görmek istiyorsanız, aşağıdaki satırları açın
cv2.imshow("original", img)
cv2.imshow("gray", gray)
cv2.imshow("thresh", thresh)
'''

# Bekleme ve pencereleri kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
