import numpy as np
import cv2

path = r'F:\Projects\Caterpillar\Images\IMG0.jpg'
org=cv2.imread(path)
img=cv2.resize(org,(560,340))
blur = cv2.GaussianBlur(img,(5,5),0)

#med=cv2.medianBlur(img,3)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
res = cv2.bitwise_and(img,hsv, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

cv2.imwrite("Masked.jpg",res)
    
#ret,thresh=cv2.threshold(grey,215,255,1)
thresh=cv2.adaptiveThreshold(grey,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,5,2)
#thresh=cv2.Canny(grey,80,96)
contour,hierarchy=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#for cnt in contours:
#            approx = approxPolyDP(cnt, 0.01*arcLength(cnt, True), True)
#            drawContours(mask, [approx], 0, (0), 5)

print("Number Of contours: ",str(len(contour)))
print(contour[0])
cv2.drawContours(res, contour,-1,(0,0,255),2)
#cv2.imshow('HSV',hsv)
#cv2.imwrite("abc.jpg",img)
cv2.imshow('Mask',mask)
cv2.imshow('res',res)
cv2.imshow('Contour',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
