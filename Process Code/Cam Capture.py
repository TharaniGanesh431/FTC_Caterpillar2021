import cv2
_,cam = cv2.VideoCapture(2).read()
#_,frame=cam.read()
#img=cv2.imshow('Frame',cam)
#gray=cv2.cvtColor(cam,cv2.COLOR_BGR2GRAY)
#_,thresh=cv2.threshold(gray,127,255,0)
cv2.imshow('Gery',cam)
#waitKey(0)
##contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
##print("Number Of contours: ",str(len(contour)))
##print(contour[1])
##cv2.drawContours(cam, contour, -1,(0,255,0),3)
##cv2.imshow('Org_Img',cam)
