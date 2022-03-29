import time

start1=time.time()
import numpy as np
import cv2
stop1=time.time()
print("Import: ",stop1-start1)

start2=time.time()

newcontour=[]
newcontour2=[]

path = r'F:\Projects\Caterpillar\Trail\5\Input.jpg'
img=cv2.imread(path)

#_,img = cv2.VideoCapture(1).read()

#cv2.imwrite('Input.jpg',img)

blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
#cv2.imwrite('mask.jpg',mask)
temp = np.zeros(mask.shape).astype(mask.dtype)
res = cv2.bitwise_and(img,hsv, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print("Block Area",end=' ')
for i in contour:
    Area=cv2.contourArea(i)
    if Area > 7000:
 #        newcontour.append(i)
    #     print(cv2.contourArea(i),end=' ')
          if Area > 40000:
              contour=i
    else:
       cv2.fillPoly(mask,[i],(0,0,0))

#cv2.drawContours(img, newcontour,-1,(0,0,255),0)

#cv2.imwrite('Output1.jpg',img)

print("Contour: ",cv2.contourArea(contour))

cv2.fillPoly(temp,[contour],(255,255,255))
outmask=cv2.bitwise_or(mask,~temp)

#cv2.imwrite('Outmask.jpg',outmask)
stop2=time.time()

#print("\nBlock Detection: ",stop2-start2)

#crop
(y, x) = np.where(mask==255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
img = img[topy:bottomy+1, topx:bottomx+1]
mask= ~outmask[topy:bottomy+1, topx:bottomx+1]

mask = cv2.merge((mask,mask,mask))

grey=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Pic Area:",end=' ')
for i in contour:
    if cv2.contourArea(i) > 1000:
         newcontour.append(i)
         print(cv2.contourArea(i))

#print("Number of Contours: ",len(newcontour))

#cv2.drawContours(img, newcontour,-1,(0,0,255),0)

#cv2.imwrite('Output2.jpg',img)



end2=time.time()

print("Program Execution :",end2-start2)

