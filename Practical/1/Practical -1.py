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

contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contour:
    if cv2.contourArea(i) > 20000:
         contour_check.append(i)
    else:
        cv2.fillPoly(mask,[i],(0,0,0))

cv2.drawContours(img, contour_check,-1,(255,255,255),0)
grey1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey1',grey1)
cv2.imshow('mask',mask)


#crop
(y, x) = np.where(mask==255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
img2 = img[topy:bottomy+1, topx:bottomx+1]

cv2.imshow("Output1", img2)

##blur2 = cv2.GaussianBlur(img2,(5,5),0)
##hsv2=cv2.cvtColor(blur2, cv2.COLOR_BGR2HSV)
##
##lb2= np.array([0,0,0])
##ub2= np.array([182,182,145])
##mask2 = cv2.inRange(hsv2,ub1,lb1)
##res2 = cv2.bitwise_and(img2,hsv2, mask =mask2)
##
##grey2=cv2.cvtColor(res2,cv2.COLOR_BGR2GRAY)
##
##contour2,hierarchy=cv2.findContours(grey2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
##
##for i in contour2:
##    if cv2.contourArea(i) > 1000:
##         contour_arr.append(i)
##
##print("Number Of contours: ",str(len(contour_arr)))
##print(contour_arr)
##
##cv2.drawContours(img2, contour_arr,-1,(0,255,0),2)

####cv2.imshow('HSV',hsv)
####cv2.imwrite("1.jpg",img)
####cv2.imshow('Mask',mask)
####cv2.imshow('res',res)
####cv2.imshow('Grey1',grey)
####cv2.imshow('Thresh1',thresh)
####
####cv2.imshow('hsv2',hsv2)
####cv2.imshow('grey2',grey2)
####cv2.imshow('Thresh2',thresh2)
cv2.imshow('Output2',img2)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
