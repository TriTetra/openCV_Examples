<<<<<<< HEAD
import  cv2
import numpy as ny

canvas = ny.zeros((512,512,3), dtype=ny.uint8) + 255

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


cv2.putText(canvas, "OpenCV", (10,150), font, 4, (0,0,0),cv2.LINE_AA)
cv2.putText(canvas, "Machine", (20,300), font1, 2, (0,0,0),cv2.LINE_4)
cv2.putText(canvas, "Rolex", (30,400), font2, 3, (0,0,0),cv2.LINE_8)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
=======
import  cv2
import numpy as ny

canvas = ny.zeros((512,512,3), dtype=ny.uint8) + 255

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX
font2 = cv2.FONT_HERSHEY_SCRIPT_COMPLEX


cv2.putText(canvas, "OpenCV", (10,150), font, 4, (0,0,0),cv2.LINE_AA)
cv2.putText(canvas, "Machine", (20,300), font1, 2, (0,0,0),cv2.LINE_4)
cv2.putText(canvas, "Rolex", (30,400), font2, 3, (0,0,0),cv2.LINE_8)

cv2.imshow("Canvas",canvas)
cv2.waitKey(0)
>>>>>>> 862eac3a172ae5897f0b06821cfe8a6f33164a35
cv2.destroyAllWindows()