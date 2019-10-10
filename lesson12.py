import cv2
import numpy as np


def main():
    resim=cv2.imread("Asaf.jpeg")

    cv2.imshow("Ben",resim)

    mask=np.zeros(resim.shape[:2],np.uint8)
    bgdModel=np.zeros((1,65),dtype=np.float64)
    fgdModel=np.zeros((1,65),dtype=np.float64)

    rect=(100,0,300,300)

    cv2.grabCut(resim,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT) #burda maske içerisinde önce 0 olan değerler arka plan ise 0 veya 2 ön plan ise 1 veya 3 değerlerini aldı.

    mask2=np.where((mask==0)|(mask==2),0,1).astype(np.uint8)                #burada maske içerisindeki değerler 0 veya 2 ise 0 değerini at dedik. Değilse 1 değerini at.

    resim=resim*mask2[:,:,np.newaxis]                                       #matrislerin çarpılması için birinin sütun sayısıyla diğerinin satır sayısı aynı olmalı.

    cv2.imshow("Son goruntu",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__=="__main__":
    main()