import cv2
import numpy as np

kamera=cv2.VideoCapture(0)

yuz_tanıma=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,goruntu=kamera.read()

    goruntu_gri=cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)


    #resim=cv2.imread("bilim_insanlari.jpg")
    #print(resim)
    #resim_gri=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)

    yuzler = yuz_tanıma.detectMultiScale(goruntu_gri, 1.1, 2)

    for (x,y,w,h) in yuzler:                                #x ve y sol üstteki köşenin koordinatları w bu resmin genişliği h ise boyu
        cv2.rectangle(goruntu,(x,y),(x+w,y+h),(0,0,255),2)


    cv2.imshow("yuzler", goruntu)

    if cv2.waitKey(10)& 0xFF==ord('q'):
        break
kamera.release()
cv2.destroyAllWindows()
