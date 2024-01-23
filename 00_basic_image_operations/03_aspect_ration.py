import cv2

def resizewithAspectRaito(img, width=None, height=None, inter=cv2.INTER_AREA):

    """
    Orijinal resmi koruyarak ve oranlari koruyarak belirli bir genişlik veya yüksekliğe yeniden boyutlandirma fonksiyonu.

    Parameters:
        img (numpy.ndarray): Boyutlandirilacak resim.
        width (int): Belirli bir genişlik değeri (piksel cinsinden).
        height (int): Belirli bir yükseklik değeri (piksel cinsinden).
        inter: Yeniden boyutlandirma sirasinda kullanilacak interpolasyon yöntemi (varsayilan: cv2.INTER_AREA).

    Returns:
        numpy.ndarray: Boyutlandirilmiş resim.
    """

    dimension = None
    (h, w) = img.shape[:2]

    # Genişlik ve yükseklik belirtilmemişse, orijinal resmi geri döndür
    if width is None and height is None:
        return img

    # Yükseklik belirtilmişse, genişliği oranı koruyarak ayarla
    if width is None:
        r = height / float(h)
        dimension = (int(w * r), height)

    # Genişlik belirtilmişse, yüksekliği oranı koruyarak ayarla
    else:
        r = width / float(w)
        dimension = (width, int(h * r))

    # Boyutları kullanarak resmi yeniden boyutlandır
    resized_img = cv2.resize(img, dimension, interpolation=inter)

    return resized_img

# Örnek kullanım
img = cv2.imread("klon.jpg")
img1 = resizewithAspectRaito(img, width=None, height=600, inter=cv2.INTER_AREA)

# Orijinal ve boyutlandırılmış resimleri göster
cv2.imshow("Original", img)
cv2.imshow("Resized", img1)

# Bir tuşa basılmasını bekleyerek programı durdur
cv2.waitKey(0)

# Tüm açık pencereleri kapat
cv2.destroyAllWindows()
