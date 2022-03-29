import cv2
import numpy as np

contour_arr=[]

path = r'F:\Projects\Caterpillar\Practical\3\input.jpg'
img=cv2.imread(path)
#img=~img1
cv2.imshow('Input',img)
blur = cv2.GaussianBlur(img,(5,5),0)

#cv2.imshow('bLUR',blur)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contour:
    if cv2.contourArea(i) > 1000:
         contour_arr.append(i)
         print(cv2.contourArea(i))

print(str(len(contour_arr)))

cv2.drawContours(img, contour_arr,-1,(0,0,255),0)

cv2.imshow('output',img)
