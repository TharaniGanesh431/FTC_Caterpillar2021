#import numpy as np
import cv2
path = r'F:\Python Programs\Opencv check\IMG6.jpg'
org=cv2.imread(path)
img=cv2.resize(org,(560,340))
grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(grey,158,255,1)
#ret,thresh=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
#thresh=cv2.Canny(grey,80,96)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number Of contours: ",str(len(contour)))
print(contour[0])
cv2.drawContours(img, contour, -1,(255,0,0),2)
cv2.imshow('Threshold',thresh)
cv2.imshow('Grey',grey)
cv2.imshow('Contour6',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
