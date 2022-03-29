import time

start1=time.time()
import numpy as np
import cv2
stop1=time.time()
print("Import: ",stop1-start1)

start2=time.time()

newcontour=[]
newcontour2=[]

##path = r'F:\Projects\Caterpillar\Practical\0\IMG0.jpg'
##img=cv2.imread(path)


_,img = cv2.VideoCapture(1).read()

cv2.imwrite('Input.jpg',img)

blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
cv2.imwrite('mask.jpg',mask)
temp = np.zeros(mask.shape).astype(mask.dtype)
res = cv2.bitwise_and(img,hsv, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Block Area",end=' ')
for i in contour:
    if cv2.contourArea(i) > 7000:
         newcontour.append(i)
         print(cv2.contourArea(i),end=' ')
         contour=i
    else:
       cv2.fillPoly(mask,[i],(0,0,0))

cv2.drawContours(img, newcontour,-1,(0,0,255),0)

cv2.imwrite('Output1.jpg',img)

stop2=time.time()

print("\nProgram Execution: ",stop2-start2)
