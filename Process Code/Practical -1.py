import time
start=time.time()
import numpy as np
import cv2
stop=time.time()
print(stop-start)

contour_arr=[]

#path = r'F:\Projects\Caterpillar\Images\IMG0.jpg'
#org=cv2.imread(path)

_,org = cv2.VideoCapture(0).read()

img=cv2.resize(org,(560,340))
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

#cv2.drawContours(img, contour,-1,(0,0,255),2)

#crop
(y, x) = np.where(mask == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
img2 = img[topy:bottomy+1, topx:bottomx+1]

cv2.imshow("Output1", img2)

blur2 = cv2.GaussianBlur(img2,(5,5),0)
hsv2=cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)

lb2= np.array([0,0,0])
ub2= np.array([182,182,145])
mask2 = cv2.inRange(hsv2, lb2, ub2)
res2 = cv2.bitwise_and(img2,hsv2, mask =mask2)

grey2=cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)

thresh=cv2.adaptiveThreshold(grey2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
contour2,hierarchy=cv2.findContours(grey2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contour2:
    if cv2.contourArea(i) > 100:
         contour_arr.append(i)

print("Number Of contours: ",str(len(contour_arr)))
print(contour_arr)

cv2.drawContours(img2, contour_arr,-1,(0,255,0),2)

#cv2.imshow('HSV',hsv)
#cv2.imwrite("abc.jpg",img)
#cv2.imshow('Mask',mask)
#cv2.imshow('res',res)
cv2.imshow('Output2',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
