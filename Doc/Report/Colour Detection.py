import time

start1=time.time()
import numpy as np
import cv2
#from scipy.spatial import distance
stop1=time.time()

print("Import: ",stop1-start1)

start2=time.time()


path = r'F:\Projects\Caterpillar\Trail\Check 2\Input2.jpg'
img=cv2.imread(path)

##capture_start=time.time()
##
##_,img = cv2.VideoCapture(1).read()
##
##capture_end=time.time()
##
##cv2.imwrite('Input_check.jpg',img)

blur = cv2.blur(img,(9,9))

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
cv2.imwrite('blur.jpg',blur)
cv2.imwrite('mask.jpg',mask)

