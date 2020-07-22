import cv2
import numpy as np


def main():

    kamera=cv2.VideoCapture(0)

    fourcc=cv2.VideoWriter_fourcc(*"XVID")#Format belirleme işlemi. Farklı formatlarda olabilir.

    kayit =cv2.VideoWriter("kayit.avi",fourcc,30,(640,480)) #30 FPS
    while True:
        ret,kare=kamera.read()

        if ret==True:
            kayit.write(kare)               #Video Writer'a yazdırma işlemi yaptırılıyor.


        cv2.imshow("Video",kare)

        if cv2.waitKey(25)& 0xFF==ord('q'):
            break

    kamera.release()
    cv2.destroyAllWindows()


if __name__=='__main__':
    main()
