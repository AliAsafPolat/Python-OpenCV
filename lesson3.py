import cv2
import numpy as np



resim = cv2.imread("kendal.jpg")

cv2.imshow("Kendal Resmi",resim)

#for i in range (100,200):                           #bu şekilde resmin istediğim kısmına müdahele edebilirim.
#    for j in range(200,300):
#        resim[i,j]=[55,255,25]

#bolge=resim[100:200,200:300]                        #resmin belirli kısmını alıp ekranda gösterebilirim.

#print(type(bolge))                                  #bu bölgenin tipi numpy.ndarray dir.

#cv2.imshow("bolge",bolge)


#resim[0:100,100:200]=bolge                          #resimden aldığım bu kısmı resmin başka bölgesine yapıştırabilirim.

#cv2.imshow("Kendal Resmi",resim)


b,g,r=cv2.split(resim)

cv2.imshow("Orjinal olan",resim)
cv2.imshow("Blue olan",b)
cv2.imshow("Green olan",g)
cv2.imshow("Red olan",r)

birleştirilmiş=cv2.merge((b,g,r))                   #verilen değerleri birleştirip tekrardan eski halini yazabildim.
cv2.imshow("Birleştirilmiş Resim",birleştirilmiş)

#resim[:,:,1]=255                                   #burada tüm resimdeki yeşil değerlerini fullüyorum.Aynı şekilde
#cv2.imshow("Kanali Degistirilmis Resim",resim)     #0 vererek mavi değerlerini ve 2 vererek kırmızı değerlerini fulleyebilirim.

#resim[0:100,50:250,0]=255                          #burada belirli bir bölgedeki mavi değerlerini fulledim ve o kısmı
#cv2.imshow("Bolge Taranmis Resim",resim)           #mavi forforluyla taranmış gibi bir görünüm sağladım.

print(resim[130,160])                               #resmin ilgili koordinattaki BGR değerlerini göster.
print("Resim Özelliği : "+ str(resim.shape))        #resmin genişlik ve boy bilgisini ve renk kanalı bilgisini gösterir.
print("Resim Boyutu: ",resim.size)                  #resmin boyutunu gösterir = Genişlik * Yükseklik * Renk kanalı sayısı.
print("Resim Değişken Tipi : "+ str(resim.dtype))   #resmin bir pixelindeki değerlerin tipini gösterir.

cv2.waitKey(0)
cv2.destroyAllWindows()