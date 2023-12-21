import cv2

# webcam veya kendi görüntümüz verebiliriz, VideoCapture ile ne kullanacağımızı
# belirtmiş oluruz 0 verirsek webcam, görüntü ise doya yolu vermeliyiz.
cap = cv2.VideoCapture(0)

# while ile sürekli olarak kayıt alacağı için süreklilik adına açıyoruz
while True:

    # read ile kareleri yakalar frame değerleri doğru okuduysa ret true olur
    # yanlış okuduysa false olacaktır (ilerleyen dönemlerde ret kullanılır)
    ret, frame = cap.read()

    # webcam den alınan video direkt olarak gösterirsek ters olarak görünüz
    # bunun önüne geçmek için flip kullanıyoruz ve hangi kare olduğunu belirtiyoruz.
    frame = cv2.flip(frame, 1,)

    # Pencereye adını veriyoruz ve kareleri imshow ile gösteriyoruz frame ile
    cv2.imshow("Webcam",frame)

    # if ile q ya tıklandığında webcami kapatacak kod satırı
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

# release() video işlemlerinde faklı işlemler de yapılacaksa işlemi bir nevi durdurur.
cap.release()
cv2.destroyAllWindows()