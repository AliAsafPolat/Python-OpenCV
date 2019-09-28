import cv2
import numpy as np

resim=cv2.imread("kendal.jpg")

cv2.imshow("Kendall Mickal",resim)

#resmin kenar pixellerini kopyalıyor ve yüzer yüzer artırıyor.
uzatilan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

#resmi 100 pixel boyunca en ve boy olarak aynalıyor.
aynalanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

#resmi 100 pixel boyunca tekrarlıyor.Duvar kağıdı gibi
tekrarlanan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

#resmi çevreliyen bir kare oluşturuyor. siyah
sarılan_resim=cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_CONSTANT)


#cv2.imshow("Uzatılan Resim",uzatilan_resim)
#cv2.imshow("Aynalanan Resim",aynalanan_resim)
#cv2.imshow("Tekrarlanan Resim",tekrarlanan_resim)
#cv2.imshow("Sarılan Resim",sarılan_resim)

cv2.rectangle(resim,(50,240),(275,50),[0,0,255],2)  #ilk koordinat sol alt köşenin ikinci koordinat ise sağ üst köşenindir.
                                                    #burada kırmızı rengi tercih ettim ve kalınlığı da 2 seçtim.
cv2.imshow("kendall",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
