# opencv kütüphanesini kodumuza ekliyoruz
import cv2

# kodumuzun bulunduğu directory e resmi atıyoruz ve imread ile
# resmi okuması için resmi içine atıyoruz ve print ediyoruz

img = cv2.imread("klon.jpg")
# print(img)

# Çıktı matris çeklinde gelecektir çünkü resimler matrislerden oluşurlar.


# Burada resmi gösterme kodu namesWindows ile açılan penceredeki ekrana
# işlevler verilebilir atanan ilk Image pencere adı ikinci ise
# pencerenin özelliğidir burada ayarlanabilir ekran yaptık.
cv2.namedWindow("Image",cv2.WINDOW_NORMAL)

# imshow ile pencerede hangi resmin görünceğini atıyoruz ilki hangi pencere
# ikinci hangi resim şeklinde işlem ilerler.
cv2.imshow("Image",img)

# imwrite ile işleme sokulan resmin son halini kaydetmemizi sağlar
# ilk istediğimiz dosya ismi ikinci ise hangi resim onu seçeriz.
cv2.imwrite("klon1.jpg",img)

# waitkey ile açılan pencerenin hemen gitmemesini ve biz kapatana
# kadar açık kalmasını sağlarız.
cv2.waitKey(0)
cv2.destroyAllWindows()