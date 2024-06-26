import cv2

image_path = "C:\\Users\\Dimoontri\\Desktop\\opencv_udemy\\countors_covexhull_convexity_defects\\contour.png"

# Resmi oku
img = cv2.imread(image_path)

# Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Kontur tespiti yap
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Konturları ekrana yazdır
print(contours)

'''
# Her bir konturu çiz
for i, contour in enumerate(contours):
    cv2.drawContours(img, [contour], 0, (0, 255, 0), 2)
    # Kontur bilgilerini ekrana yazdir
    print(f"Kontur {i + 1}, Nokta Sayisi: {len(contour)}")

'''

# Sonuçları ekrana göster
cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
