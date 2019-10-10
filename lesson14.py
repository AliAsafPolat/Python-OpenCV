import cv2
import numpy as np

#Good Features to Track işlemleri yapılacak.


resim1=cv2.imread("android.jpg")

resim_gri=cv2.cvtColor(resim1,cv2.COLOR_BGR2GRAY)

resim_gri=np.float32(resim_gri)

koseler=cv2.goodFeaturesToTrack(resim_gri,75,0.001,5)               #köşe tespiti yapıyor. 75 max köşe sayısı,0.0001 doğruluk değeri 5 ise bir köşeden sonra ne kadar baksın.

koseler=np.int0(koseler)

for kose in koseler:
    x,y=kose.ravel()
    cv2.circle(resim1,(x,y),3,(0,0,255),-1)

cv2.imshow("koseler",resim1)

cv2.waitKey(0)
cv2.destroyAllWindows()