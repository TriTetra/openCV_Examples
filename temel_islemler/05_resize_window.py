<<<<<<< HEAD
import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    global img, scale_percent

    if event == cv2.EVENT_MOUSEWHEEL:
        delta = flags >> 16  # Mousewheel scroll direction
        if delta > 0:
            # Fare yukarı doğru kaydırıldığında (zoom in)
            scale_percent += 10
        else:
            # Fare aşağı doğru kaydırıldığında (zoom out)
            scale_percent = max(10, scale_percent - 10)

        # Yeni ölçekleme yüzdesini hesapla
        new_width = int(img.shape[1] * scale_percent / 100)
        new_height = int(img.shape[0] * scale_percent / 100)

        # Yeni boyutlarda resmi yeniden boyutlandır
        resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        # Yeni boyutlarda pencereyi oluştur
        cv2.namedWindow('Resizable Window', cv2.WINDOW_NORMAL)
        cv2.imshow('Resizable Window', resized_img)

img_path = "C:\\Users\\abdul\\OneDrive\\Resimler\\Saved Pictures\\deneme.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"Hata: {img_path} dosyası okunamadı.")
else:
    scale_percent = 100  # Başlangıçta orijinal boyutta başlat

    cv2.namedWindow('Resizable Window', cv2.WINDOW_NORMAL)
    cv2.imshow('Resizable Window', img)
    cv2.setMouseCallback('Resizable Window', on_mouse)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
=======
import cv2
import numpy as np

def on_mouse(event, x, y, flags, param):
    global img, scale_percent

    if event == cv2.EVENT_MOUSEWHEEL:
        delta = flags >> 16  # Mousewheel scroll direction
        if delta > 0:
            # Fare yukarı doğru kaydırıldığında (zoom in)
            scale_percent += 10
        else:
            # Fare aşağı doğru kaydırıldığında (zoom out)
            scale_percent = max(10, scale_percent - 10)

        # Yeni ölçekleme yüzdesini hesapla
        new_width = int(img.shape[1] * scale_percent / 100)
        new_height = int(img.shape[0] * scale_percent / 100)

        # Yeni boyutlarda resmi yeniden boyutlandır
        resized_img = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

        # Yeni boyutlarda pencereyi oluştur
        cv2.namedWindow('Resizable Window', cv2.WINDOW_NORMAL)
        cv2.imshow('Resizable Window', resized_img)

img_path = "C:\\Users\\abdul\\OneDrive\\Resimler\\Saved Pictures\\deneme.jpg"
img = cv2.imread(img_path)

if img is None:
    print(f"Hata: {img_path} dosyası okunamadı.")
else:
    scale_percent = 100  # Başlangıçta orijinal boyutta başlat

    cv2.namedWindow('Resizable Window', cv2.WINDOW_NORMAL)
    cv2.imshow('Resizable Window', img)
    cv2.setMouseCallback('Resizable Window', on_mouse)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
