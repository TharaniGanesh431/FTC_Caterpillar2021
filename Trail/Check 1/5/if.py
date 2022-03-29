import time

start1=time.time()
import sys
import numpy as np
import cv2
stop1=time.time()
print("Import: ",stop1-start1)

start2=time.time()

count=0
newcontour=[]

##path = r'F:\Projects\Caterpillar\Trail\5\If case\IMG0.jpg'
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
         count+=1
         print(cv2.contourArea(i),end=' ')

cv2.drawContours(img, newcontour,1,(0,0,255),0)

cv2.imwrite('Output1.jpg',img)

stop2=time.time()

if (count==2) and (cv2.contourArea(newcontour[1]) > 10000):

    print("\nProgram Execution: ",stop2-start2)
    print('Contour....\n',newcontour[1])
    sys.exit()
    
else:

    print("\n\nExecuting Else...")

    newcontour2=[]
    contour=np.array(contour).dtype as 

    for i in contour:
        if cv2.contourArea(i) < 20000:
             cv2.fillPoly(mask,[i],(0,0,0))

    cv2.fillPoly(temp,[contour],(255,255,255))
    outmask=cv2.bitwise_or(mask,~temp)
    cv2.imwrite('Outmask.jpg',outmask)

    #crop
    (y, x) = np.where(mask==255)
    (topy, topx) = (np.min(y), np.min(x))
    (bottomy, bottomx) = (np.max(y), np.max(x))
    img2 = img[topy:bottomy+1, topx:bottomx+1]
    mask2= ~outmask[topy:bottomy+1, topx:bottomx+1]

    mask2=cv2.merge((mask2,mask2,mask2))
    img2=cv2.merge((img2,img2,img2))

    grey=cv2.cvtColor(mask2,cv2.COLOR_BGR2GRAY)
    contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print("Pic Area:",end=' ')
    for i in contour:
        if cv2.contourArea(i) > 5000:
             newcontour2.append(i)
             print(cv2.contourArea(i))

    cv2.drawContours(img2, newcontour2,-1,(0,0,255),0)

    cv2.imwrite('Output2.jpg',img2)

    end2=time.time()

    print("Program Execution :",end2-start2)
    
    
    
