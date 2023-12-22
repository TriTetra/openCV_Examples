import cv2
import numpy as np

# Görüntüyü oku
img = cv2.imread("star.png")

# Gri tonlamalı görüntüyü elde et
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme işlemi uygula
_, thresh = cv2.threshold(gray, 127, 255, 0)

# Konturları bul
contours, _ = cv2.findContours(thresh, 2, 1)

# İlk konturu seç
cnt = contours[0]

# Konturun konveks kabukunu bul
hull = cv2.convexHull(cnt, returnPoints=False)

# Konveks kabuktaki çıkıntıları bul
defects = cv2.convexityDefects(cnt, hull)

# Çıkıntıları yeşil çizgiler ve dairelerle işaretle
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])

    # Çıkıntıları yeşil çizgilerle işaretle
    cv2.line(img, start, end, [0, 255, 0], 2)

    # Çıkıntı noktalarını yeşil dairelerle işaretle
    cv2.circle(img, far, 5, [0, 255, 0], -1)

# Sonuç görüntüyü ekrana göster
cv2.imshow("Image", img)

# Bekleme ve pencereyi kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
