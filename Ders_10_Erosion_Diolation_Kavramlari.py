import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

dusuk=np.array([88,50,50])
yuksek=np.array([130,255,255])
while True:

    ret,goruntu=kamera.read()

    hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)

    mask=cv2.inRange(hsv,dusuk,yuksek)

    son_resim=cv2.bitwise_and(goruntu,goruntu,mask=mask)

    cv2.imshow("Goruntu",son_resim)

    #Morfolojik Filtreleme uygulanacak.

    kernel=np.ones((5,5),np.uint8)

    erosion=cv2.erode(mask,kernel,iterations=1)             #spesifik yapmaya çalışıyor.

    diolation=cv2.dilate(mask,kernel,iterations=1)          #Bütünsel yapmaya çalışıyor.


    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)    #yazıyı iyice göstermeye çalışıyor. renk farklılığını ayırmaya çalışıyor.

    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)   #kernelde verdiğim değerlerle kapatma işlemi yapmaya çalışıyor.
                                                            #kadınların suratındaki kusurları kapatması gibi.

    cv2.imshow("Opening",opening)
    cv2.imshow("Closing",closing)

    cv2.imshow("Diolation",diolation)
    cv2.imshow("Erosion",erosion)

    if cv2.waitKey(25)&0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
