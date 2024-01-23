import cv2
import numpy as np

# Resmi oku
img = cv2.imread("h_line.png")

# Gri tonlamaya çevir
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Kenarları tespit et
edges = cv2.Canny(gray, 75, 150)

# Hough Transform kullanarak çizgileri tespit et
lines = cv2.HoughLines(edges, 1, np.pi / 180, 50)
lines1 = cv2.HoughLinesP(edges, 1, np.pi / 180, 50, maxLineGap=130)

# Çizgileri resmin üzerine çiz
for line in lines1:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sonuçları göster
cv2.imshow("Original Image", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
