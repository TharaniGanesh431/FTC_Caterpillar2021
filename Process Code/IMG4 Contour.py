#import numpy as np
import cv2
path = r'F:\Projects\Caterpillar\Images\IMG 01.jpg'
org=cv2.imread(path)
img=cv2.resize(org,(560,340))
med=cv2.medianBlur(img,3)
hsv=cv2.cvtColor(med, cv2.COLOR_BGR2HSV)
grey=cv2.cvtColor(med, cv2.COLOR_BGR2GRAY)

#ret,thresh=cv2.threshold(grey,215,255,1)
thresh=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
#thresh=cv2.Canny(grey,80,96)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number Of contours: ",str(len(contour)))
print(contour[0])
cv2.drawContours(img, contour, -1,(255,0,0),2)
cv2.imshow('HSV',hsv)
cv2.imwrite("abc.jpg",img)
cv2.imshow('Threshold',thresh)
cv2.imshow('Grey',grey)
cv2.imshow('Contour',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
