import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

while True:

    ret,goruntu=kamera.read()



    gri_goruntu=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)

    silgi=cv2.imread("powerbank.jpg",0)

    w,h=silgi.shape #(weight,height)

    res=cv2.matchTemplate(gri_goruntu,silgi,cv2.TM_CCOEFF_NORMED)

    esik=0.8

    local=np.where(res>esik)

    for n in zip(*local[::-1]):
        cv2.rectangle(goruntu,n,(n[0]+h,n[1]+w),(0,255,0),2)  # resimde bulduğu yerleri kare içine alıyor.

    cv2.imshow("Goruntu", goruntu)
    if cv2.waitKey(25)&0xFF==ord('q'):
        break

kamera.release()
cv2.destroyAllWindows()
