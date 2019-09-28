import cv2
import numpy as np

def main():
    resim=cv2.imread("kendal.jpg")
    android=cv2.imread("android.jpg")

    and_gri=cv2.cvtColor(android,cv2.COLOR_BGR2GRAY)               #renkli olan resmi grayscale haline getiriyor.

    #r değeri sınır değerimi gösteriyor.
    r,mask=cv2.threshold(and_gri,75,255,cv2.THRESH_BINARY)          #belli değerin altındakileri siyah değerin üstündekileri beyaz yapıyor.
    #cv2.imshow("Maskelenmis Resim",mask)

    mask_inver=cv2.bitwise_not(mask)                                #resmin tam tersini alıyoruz.Resmin tersini alınca android kısmı siyah çevre beyaz
                                                                    #kalmış oluyor.
    yukseklik,genislik=and_gri.shape                                #Android resmimin yüksekliği ve genişliği önemli çünkü bu değerlere göre alan belirlenecek

    alan=resim[0:genislik,0:yukseklik]                              #Android resmine göre alan alındı.
    cv2.imshow("ROI",alan)                                          #Alanı ayrıyeten gösterdik
    sonuc=cv2.bitwise_and(alan,alan,mask=mask_inver)                #and ile işlem yapınca resmimin üzerine siyah bir android maskesi gelmiş oluyor.


    toplam=cv2.add(sonuc,android)                                   #şimdi resmin ilgili bölgesiyle 0 olan siyah maskeyi topluyorum ve renk bilgisini de maskeye vermiş oluyorum.

    cv2.imshow("toplanmış resim",toplam)

    resim[0:genislik,0:yukseklik]=toplam                            #en son ise topladığım ve renk verdiğim alanı tekrardan ana resim ile birleştiriyorum.
    cv2.imshow("Birlestirilmis Resim",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()
