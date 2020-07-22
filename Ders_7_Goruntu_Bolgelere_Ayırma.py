import cv2
import numpy as np

#0 değerini girersem bilgisayarda tanımlı olan kamerayı kullanacak.
#1 değerini girersem usb ile bağlı olan kamera değerini kullanacak.
#Video değerini girersem kayıtlı olan videoyu alacak.

kamera=cv2.VideoCapture(0)

#kamera.set(3,300)       #genişlik belirtir.
#kamera.set(4,300)       #yükseklik belirtir.

def ayarlama(kare ,yüzde=75):
    genişlik=int(kare.shape[1]*yüzde/100)
    yukseklik=int(kare.shape[0]*yüzde/100)
    boyut=(genişlik,yukseklik)
    return cv2.resize(kare,boyut,interpolation= cv2.INTER_AREA)


while True:
    ret,kare=kamera.read()                  #ret değeri kameranın aktif olup olmadığı bilgisini bana döndürüyor. kare ise fotoğrafı.
    #cv2.rectangle(kare, (875, 700), (1100, 500), (0, 0, 2550, 2))
    #bolge=kare[200:500,100:400]             #belirli bir bölgeyi alıp buradan yayınlama yapabiliriz.
    #cv2.imshow("Bolge",bolge)               #bolge yayınlandı.

    kare2=ayarlama(kare)

    gri_ton=cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)

    cv2.imshow("Video",kare)
    cv2.imshow("Video2",kare2)
    cv2.imshow("Gri Ton",gri_ton)

    if cv2.waitKey(25)& 0xFF==ord('q'):     #her 25 milisaniyede bir kare al ve göster anlamına geliyor. klavyede q ya basıldığında
        break

kamera.release()
cv2.destroyAllWindows()
