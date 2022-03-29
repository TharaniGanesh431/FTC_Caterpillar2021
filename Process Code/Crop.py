import numpy as np
import cv2

crop_array=[]

path = r'F:\Projects\Caterpillar\Images\IMG0.jpg'
org=cv2.imread(path)
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

#for i in contour:
#    if cv2.contourArea(i) > 100:
#       crop_array.append(i)

cv2.drawContours(img,contour,-1,(0,0,255),2)
#out = np.zeros_like(img) # Extract out the object and place into output image
#out[mask == 255] = img[mask == 255]

#Now crop
(y, x) = np.where(mask == 255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
img = img[topy:bottomy+1, topx:bottomx+1]

# Show the output image
#cv2.imwrite("Output.jpg", out)
cv2.imshow("Output", img)

#crop = image[y:y+h, x:x+w]
#cv2.imshow('Crop', img)
cv2.waitKey(0) 
