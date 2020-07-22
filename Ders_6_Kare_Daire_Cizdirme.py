import cv2
import numpy as np

def main():

    resim = np.zeros((400,400,3),dtype="uint8")             #400-400 lük 3 kanallı bir değer.

    resim.fill(255)                                         #resmi beyaz yapar tüm değerleri 255 ile doldurur.
    cv2.rectangle(resim,(150,250),(250,150),(255,0,0),2)
    cv2.line(resim,(150,250),(250,150),(0,255,0),2)
    cv2.line(resim,(150,150),(250,250),(0,255,0),2)
    cv2.circle(resim,(200,200),50,(0,0,255),2)
    cv2.putText(resim,"Ali Asaf Polat",(150,150),1,cv2.FONT_HERSHEY_PLAIN,150,1)
    #cv2.putText(resim,"Ali Asaf Polat",(75,100),1,cv2.FONT_HERSHEY_PLAIN,150,1)

    cv2.imshow("Resim", resim)
    #iki_kat_buyuk_resim=cv2.pyrUp(resim)                    #resmin boyutlarını iki kat büyütür
    #iki_kat_kucuk_resim=cv2.pyrDown(resim)                  #resmin boyutlarını iki kat küçültür


    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__=='__main__':
    main()
