import time
start=time.time()
import numpy as np
import cv2
stop=time.time()
print(stop-start)

contour_arr=[]
contour_check=[]

#path = r'F:\Projects\Caterpillar\Images\IMG0.jpg'
#org=cv2.imread(path)

_,org = cv2.VideoCapture(1).read()

img=cv2.resize(org,(560,340))
cv2.imshow('Input',img)
blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
res = cv2.bitwise_and(img,hsv, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

#thresh=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print("Number Of contours: ",str(len(contour)))
#print(contour)

cv2.imshow('mask1',mask)
for i in contour:
    if cv2.contourArea(i) > 20000:
         contour_check.append(i)
         print("Area:",cv2.contourArea(i))
    else:
        cv2.fillPoly(mask,pts=[i],color=(0,0,0))

cv2.drawContours(img, contour_check,-1,(255,255,255),3)
grey1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('mask2',mask)
cv2.imshow('grey1',grey1)
cv2.imshow('img',img)
