<<<<<<< HEAD
import cv2
import numpy as np
import numpy as ny

canvas = ny.zeros((512,512,3),dtype=ny.uint8) + 255
# print(canvas)

# Çizgi çizmek için cv2.line
cv2.line(canvas,(50,50),(250,250),(255,0,0),thickness=5)
cv2.line(canvas,(50,20),(170,200),(0,0,255),thickness=4)


# Kare için cv2.rectangle
cv2.rectangle(canvas,(80,80),(120,120),(0,255,0),thickness=2)
cv2.rectangle(canvas,(300,300),(500,500),(50,100,140),thickness=-1)

# Daire için cv2.circle
cv2.circle(canvas,(100,150),80,(150,150,150),4)

# Üçgen için 3 adet konumu yani çizgiyi birleştirerek oluşturuyoruz
p1 = (100,100)
p2 = (50,50)
p3 = (300,100)

cv2.line(canvas,p1,p2,(0,0,0),thickness=3)
cv2.line(canvas,p2,p3,(0,0,0),thickness=3)
cv2.line(canvas,p1,p3,(0,0,0),thickness=3)


# Çokgen için noktaları bir değişkene veriyoruz noktalarını
points = np.array([[[110,200],[330,200],[290,220],[350,250]]], np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),thickness=5)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

=======
import cv2
import numpy as np
import numpy as ny

canvas = ny.zeros((512,512,3),dtype=ny.uint8) + 255
# print(canvas)

# Çizgi çizmek için cv2.line
cv2.line(canvas,(50,50),(250,250),(255,0,0),thickness=5)
cv2.line(canvas,(50,20),(170,200),(0,0,255),thickness=4)


# Kare için cv2.rectangle
cv2.rectangle(canvas,(80,80),(120,120),(0,255,0),thickness=2)
cv2.rectangle(canvas,(300,300),(500,500),(50,100,140),thickness=-1)

# Daire için cv2.circle
cv2.circle(canvas,(100,150),80,(150,150,150),4)

# Üçgen için 3 adet konumu yani çizgiyi birleştirerek oluşturuyoruz
p1 = (100,100)
p2 = (50,50)
p3 = (300,100)

cv2.line(canvas,p1,p2,(0,0,0),thickness=3)
cv2.line(canvas,p2,p3,(0,0,0),thickness=3)
cv2.line(canvas,p1,p3,(0,0,0),thickness=3)


# Çokgen için noktaları bir değişkene veriyoruz noktalarını
points = np.array([[[110,200],[330,200],[290,220],[350,250]]], np.int32)
cv2.polylines(canvas,[points],True,(0,0,100),thickness=5)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()

>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
