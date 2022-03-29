import time

start1=time.time()
import numpy as np
import cv2
#from scipy.spatial import distance
stop1=time.time()

print("Import: ",stop1-start1)

start2=time.time()

length=0
Area=[]
newcontour=[]
newcontour2=[]

path = r'F:\Projects\Caterpillar\Trail\Check 2\Input2.jpg'
img=cv2.imread(path)

##capture_start=time.time()
##
##_,img = cv2.VideoCapture(1).read()
##
##capture_end=time.time()
##
##cv2.imwrite('Input_check.jpg',img)

blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
cv2.imwrite('mask.jpg',mask)
cv2.imshow('mask1',mask)

contour,hierarchy=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in contour:
    if cv2.contourArea(i) > 15000:
         length+=1
         Area.append(cv2.contourArea(i))
         newcontour.append(i)
         contour=i
    else:
       cv2.fillPoly(mask,[i],(0,0,255))

cv2.imwrite("Mask2.jpg",mask)

       
##length=len(newcontour)
##
##cv2.drawContours(img, newcontour,-1,(0,0,255),0)
##
##cv2.imshow('Contour',img)
##
##start_pic=time.time()
##
##(y1, x1) = np.where(mask==0)
###(topy1, topx1) = (np.min(y1), np.min(x1))
##(bottomy1, bottomx1) = (np.max(y1), np.max(x1))
##
##end_pic=time.time()
##
##print("\nPic Co-ordinate Execution: ",end_pic-start_pic)
##
##(y, x) = np.where(mask==255)
##(topy, topx) = (np.min(y), np.min(x))
##(bottomy, bottomx) = (np.max(y), np.max(x))
##
##print("No. of contours",length)
##print("pic x: ",bottomx1)
##print("block x: ",topx,bottomx)
##
###if length==2 and (Area[0]<30000 and Area[1]<30000):
##if length ==2:
##    print("Area: ",Area[0],Area[1])
##    print("\n\nBlock: 0")
###elif length==1 and Area > 30000:
##elif length == 1:
##    print("Area: ",Area[0])
##    if topx > 100 and (bottomx1-bottomx)<100:
##        print("\n\nBlock: -1")
##    else: #topx < 100 and (bottomx1-bottomx)>100:
##        print("\n\nBlock: 1")
####    else:
####        print("*\n\n***************Condition Not Satisfied**************")
##    
##
##end2=time.time()
##
##print("\n\nProgram Execution :",end2-start2)
