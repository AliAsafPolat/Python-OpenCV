import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
resim=cv2.imread("android.jpg")

while True:
    ret,goruntu=kamera.read()

    #laplacian filtresi :

    laplacian=cv2.Laplacian(resim,cv2.CV_64F)
    kam_laplacian=cv2.Laplacian(goruntu,cv2.CV_64F)

    cv2.imshow("Kamera Goruntusu Laplacian",kam_laplacian)

    #cv2.imshow("Laplacian",laplacian)

    #sobel filtresi :
    sobel_dikey_kam=cv2.Sobel(goruntu,cv2.CV_64F,1,0,ksize=5)
    sobel_yatay_kam=cv2.Sobel(goruntu,cv2.CV_64F,0,1,ksize=5)

    cv2.imshow("Sobel Yatay Kamera",sobel_yatay_kam)
    cv2.imshow("Sobel Dikey Kamera",sobel_dikey_kam)

    sobel_dikey=cv2.Sobel(goruntu,cv2.CV_64F,1,0,ksize=5)
    sobel_yatay=cv2.Sobel(goruntu,cv2.CV_64F,0,1,ksize=5)

    #cv2.imshow("Sobel Dikey",sobel_dikey)
    #cv2.imshow("Sobel Yatay",sobel_yatay)

    #Canny kenar filtreleme :

    kenarlar=cv2.Canny(goruntu,100,100)
    cv2.imshow("Canny Filtre",kenarlar)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()

