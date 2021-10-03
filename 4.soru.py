import cv2 
from matplotlib import pyplot as plt
import numpy as np

resim = cv2.imread("everythingfine.jpeg")

cv2.line(resim,(400,400),(1460,400),(255,0,0),3)
cv2.rectangle(resim,(200,200),(600,600),(10,255,255),5)
cv2.circle(resim,(1000,500), 40, (0,0,255), -1)

cv2.imshow("resimm",resim)
v = cv2.waitKey(0)
cv2.destroyAllWindows()

if v == ord("q"):
    cv2.imwrite("fine.jpeg", resim)