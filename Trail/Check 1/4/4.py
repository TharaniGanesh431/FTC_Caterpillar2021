import time

start1=time.time()
##from io import BytesIO
##from PIL import Image
import numpy as np
import cv2

stop1=time.time()
print("Import: ",stop1-start1)

##def convertToJpeg(im):
##    with BytesIO() as f:
##        im.save(f,format='JPEG')
##        f.seek(0)
##        return Image.open(f)

start2=time.time()

newcontour=[]
newcontour2=[]

#path = r'F:\Projects\Caterpillar\Practical\0\IMG0.jpg'
#img=cv2.imread(path)


_,img = cv2.VideoCapture(1).read()

cv2.imwrite('Input.jpg',img)

blur = cv2.GaussianBlur(img,(5,5),0)

hsv=cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

lb= np.array([15,80,50])
ub= np.array([39,255,255])
mask = cv2.inRange(hsv, lb, ub)
cv2.imwrite('mask.jpg',mask)
temp = np.zeros(mask.shape).astype(mask.dtype)
res = cv2.bitwise_and(img,blur, mask =mask)

grey=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

cv2.imwrite('Grey.jpg',res)

contour,hierarchy=cv2.findContours(mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#print("Contour Dtype: ",np.dtype(contour))
print("Block Area",end=' ')
for i in contour:
    if cv2.contourArea(i) > 100:
         newcontour.append(i)
         print(cv2.contourArea(i),end=' ')
         contour=i
    else:
       cv2.fillPoly(mask,[i],(0,0,0))

cv2.drawContours(img, newcontour,-1,(0,0,255),0)

cv2.imwrite('Output1.jpg',img)

cv2.fillPoly(temp,[contour],(255,255,255))
outmask=cv2.bitwise_or(mask,~temp)

cv2.imwrite('Outmask.jpg',outmask)
stop2=time.time()

print("\nBlock Detection: ",stop2-start2)



#crop
(y, x) = np.where(mask==255)
(topy, topx) = (np.min(y), np.min(x))
(bottomy, bottomx) = (np.max(y), np.max(x))
img2 = img[topy:bottomy+1, topx:bottomx+1]
mask2= ~outmask[topy:bottomy+1, topx:bottomx+1]

print("Channel: ",len(mask2.shape))

ms=time.time()
mask21 = cv2.merge((mask2,mask2,mask2))
mf=time.time()
print("Merging: ",mf,ms)

#mask21 = np.array(mask2, dtype=np.uint8)

##mask2= Image.fromarray(mask2)
##with BytesIO() as f:
##    mask2.save(f,format='JPEG')
###mask2=convertToJpeg(mask2)


##write=time.time()
##cv2.imwrite('crop.jpg',mask2)
##cv2.imwrite('img2.jpg',img2)
##path = r'F:\Projects\Caterpillar\Trail\4\crop.jpg'
##mask2=cv2.imread(path)
##path = r'F:\Projects\Caterpillar\Trail\4\img2.jpg'
##img2=cv2.imread(path)
##read=time.time()
##print("Write Read: ",read-write)



grey=cv2.cvtColor(mask21,cv2.COLOR_BGR2GRAY)
contour,hierarchy=cv2.findContours(grey,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Pic Area:",end=' ')
for i in contour:
    if cv2.contourArea(i) > 1000:
         newcontour2.append(i)
         print(cv2.contourArea(i))
print("Number of Contours: ",len(newcontour2))

cv2.drawContours(img2, newcontour2,-1,(0,0,255),0)

cv2.imwrite('Output2.jpg',img2)

end2=time.time()

print("Program Execution :",end2-start2)
