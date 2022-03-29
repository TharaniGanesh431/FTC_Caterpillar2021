import cv2
import numpy as np

contour_check=[]

#path = r'F:\Projects\Caterpillar\Images\IMG0.jpg'
#org=cv2.imread(path)

_,org = cv2.VideoCapture(0).read()

img=cv2.resize(org,(560,340))
cv2.imshow('Input',img)
blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
res = cv2.bitwise_and(img,hsv, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

thresh=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print("Number Of contours: ",str(len(contour)))
#print(contour)

for i in contour:
    if cv2.contourArea(i) > 100:
         contour_check.append(i)

cv2.drawContours(img, contour_check,-1,(0,0,255),4)

