import cv2 
from matplotlib import pyplot as plt

resim1 = cv2.imread("aa.jpeg")

formats = ["jpeg", "png", "bmp"] #tablo haline getireceğim fotoğrafların başlıklarını hazırladım.

cv2.imwrite("girlA.jpeg", resim1) #farklı formatlarda kayıt işlemleri gerçekleşir.
cv2.imwrite("girlB.png", resim1)
cv2.imwrite("girlC.bmp", resim1)

img1= cv2.imread("girlA.jpeg")    # kaydedilen görüntüler değişkene atılır ve renk dönüşümleri yapılır.
img1 = cv2.cvtColor(resim1, cv2.COLOR_BGR2RGB)
img2= cv2.imread("girlB.png")
img2 = cv2.cvtColor(resim1, cv2.COLOR_BGR2RGB)
img3= cv2.imread("girlC.bmp")
img3 = cv2.cvtColor(resim1, cv2.COLOR_BGR2RGB)
images = [img1,img2,img3]

for i in range(3):  # tablolama işlemi gerçekleşir.
    plt.subplot(1,3,i+1) 
    plt.imshow(images[i])
    plt.title(formats[i])
    plt.xticks([])
    plt.yticks([])
plt.show()



    