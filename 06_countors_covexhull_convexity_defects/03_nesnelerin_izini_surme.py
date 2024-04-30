import cv2
import numpy as np

# Video dosyasını aç
cap = cv2.VideoCapture("dog.mp4")

while True:
    # Her bir kareyi oku
    ret, frame = cap.read()

    # Kareyi HSV renk uzayına çevir
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Beyaz renk tonlarını tespit etmek için bir renk aralığı belirle
    sensivity = 15
    lower_white = np.array([0, 0, 255 - sensivity])
    upper_white = np.array([255, sensivity, 255])

    # HSV görüntüsündeki belirli renk aralığına göre bir maske oluştur
    mask = cv2.inRange(hsv, lower_white, upper_white)

    # Orijinal kare üzerine maskeyi uygula
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Orijinal kareyi ekrana göster
    cv2.imshow("Orijinal Kare", frame)

    # Maske karesini ekrana göster (isteğe bağlı, yorum satırını açabilirsiniz)
    # cv2.imshow("Maske", mask)

    # Maske uygulanmış sonuç karesini ekrana göster
    cv2.imshow("Sonuç Kare", res)

    # Klavyeden 'ESC' tuşuna basılana kadar devam et
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

# Pencereleri kapat
cv2.destroyAllWindows()
