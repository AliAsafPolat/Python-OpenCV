import cv2
import numpy as np

kamera=cv2.VideoCapture(0)
dusuk = np.array([105,50,50])                                #en düşük HUE değeri
yuksek=np.array([127,255,255])                              #en yüksek HUE değeri

while True:
        ret,goruntu=kamera.read()

        hsv=cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)         #renk ayırt etme olayını BGR gibi birbirine bağımlı değişkenlerle yaptansa HSV uzayında yapıyoruz.

        mask=cv2.inRange(hsv,dusuk,yuksek)                  #burda verilen 90 ve 130 değerleri mavi renk aralığını ifade ediyor.
                                                            #ve eğer değerim bu aralıktaysa beyaz yap değilse siyah yap demiş oluyorum.

        son_resim=cv2.bitwise_and(goruntu,goruntu,mask=mask)        #oluşturulan maskede hsv ile and işlemi yaparsam hsv deki mavi renk görüntüsünü resme vermiş olacağım.


        #Önce yumuşatma yapacağız.

        kernel=np.ones((15,15),dtype=float)/255
        smoothed=cv2.filter2D(son_resim,-1,kernel)              #yumuşatılmış resim.

        cv2.imshow("Smoothed Pic",smoothed)

        #Gauss Blurlama
        blur=cv2.GaussianBlur(son_resim,(15,15),0)

        cv2.imshow("Blurlanmis",blur)

        #Median Blur
        medyan=cv2.medianBlur(son_resim,15)
        cv2.imshow("Medyan Blur",medyan)

        #Bilateral
        bilateral=cv2.bilateralFilter(son_resim,15,75,75)
        cv2.imshow("Bilateral",bilateral)

        #cv2.imshow("Goruntu",goruntu)
        #cv2.imshow("HSV",hsv)
        #cv2.imshow("maske",mask)
        #cv2.imshow("Renk algılama",son_resim)

        if cv2.waitKey(25)&0xFF==ord('q'):
            break;

kamera.release()
cv2.destroyAllWindows()
