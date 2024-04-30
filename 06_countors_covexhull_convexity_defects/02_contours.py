import cv2

image_path = "C:\\Users\\Dimoontri\\Desktop\\opencv_udemy\\countors_covexhull_convexity_defects\\contour1.png"

# Resmi oku
img = cv2.imread(image_path)

# Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Kontur tespiti yap
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları ekrana yazdır
print("Konturlar:", len(contours))

# Tüm konturları çiz
# -1 değeri, tüm konturları çizmek için kullanılır
# Mavi renkte çizilecek ve çizgi kalınlığı 3 olacak
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)

# Sonuçları ekrana göster
cv2.imshow("Contour", img)

# Bekleme ve pencereleri kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
