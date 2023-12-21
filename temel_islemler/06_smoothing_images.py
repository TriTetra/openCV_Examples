import cv2
import numpy as np

# p1 = "C:\\Users\\abdul\\OneDrive\\Resimler\\Saved Pictures\\deneme.jpg"
# p2 = "C:\\Users\\abdul\\OneDrive\\Resimler\\Saved Pictures\\deneme1.jpg"
# p3 = "C:\\Users\\abdul\\OneDrive\\Resimler\\Saved Pictures\\deneme2.jpg"


'''
img_deneme = cv2.imread(p1)
if img_deneme is None:
    print(f"Hata: {p1} dosyası okunamadı.")

img_deneme1 = cv2.imread(p2)
if img_deneme1 is None:
    print(f"Hata: {p2} dosyası okunamadı.")

img_deneme2 = cv2.imread(p3)
if img_deneme2 is None:
    print(f"Hata: {p3} dosyası okunamadı.")


if img_deneme is not None and img_deneme1 is not None and img_deneme2 is not None:
    scaled_deneme = cv2.resize(img_deneme, None, fx=0.5, fy=0.5)
    scaled_deneme1 = cv2.resize(img_deneme1, None, fx=0.5, fy=0.5)
    scaled_deneme2 = cv2.resize(img_deneme2, None, fx=0.5, fy=0.5)
'''

img_deneme  = cv2.imread("median.png")
img_deneme1 = cv2.imread("filter.png")
img_deneme2 = cv2.imread("bilateral.png")


blur  = cv2.blur(img_deneme,(5,5))
blur1 = cv2.medianBlur(img_deneme,5)
blur2 = cv2.GaussianBlur(img_deneme,(5,5),cv2.BORDER_DEFAULT)
blur3 = cv2.bilateralFilter(img_deneme,9,75,75)


cv2.imshow("Original",img_deneme)
cv2.imshow("Blur",blur)
cv2.imshow("Blur1",blur1)
cv2.imshow("Blur2",blur2)

cv2.waitKey(0)
cv2.detryoAllWindows()
