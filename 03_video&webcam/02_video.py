import cv2

# Video dosyasının adını ve yolunu belirtin
video_path = 'video.mp4'

# Video dosyasını açın
cap = cv2.VideoCapture(video_path)

# Video'nun başarıyla açılıp açılmadığını kontrol edin
if not cap.isOpened():
    print("Error: Video file could not be opened.")
    exit()

# Video'nun frame'lerini okuyun ve gösterin
while True:
    ret, frame = cap.read()  # Bir frame oku
    if not ret:
        break  # Eğer frame alınamazsa döngüden çık

    # Frame üzerinde işlemler yapılabilir
    # Örneğin, frame'yi gri tonlamaya çevirmek için: frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', frame)  # Frame'i göster

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break  # 'q' tuşuna basıldığında döngüden çık

# Kullanılan kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()