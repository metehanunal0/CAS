import cv2 
from matplotlib import pyplot as plt
img1 = cv2.imread('aa.jpeg',0)
edges = cv2.Canny(img1,150,255)
    
plt.subplot(121)
plt.imshow(img1,cmap = 'gray')
plt.title('Original Image')
plt.xticks([]) 
plt.yticks([])
plt.subplot(122)
plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image') 
plt.xticks([]) 
plt.yticks([])
plt.show()
    