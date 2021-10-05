import cv2
from matplotlib import pyplot as plt

img2 = cv2.imread("bb.jpeg") 
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB) 

Gaussian = cv2.GaussianBlur(img2, (5,5), 0)
Mean = cv2.blur(img2,(5,5))
Median = cv2.medianBlur(img2, 5)

filters = [img2, Gaussian, Mean, Median]
titles = ['Original pic', 'Gaussian', 'Mean', 'Median']

for i in range(4):
    plt.subplot(1, 4, i+1)
    plt.imshow(filters[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

    