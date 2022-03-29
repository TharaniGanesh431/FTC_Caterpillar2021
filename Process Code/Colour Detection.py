import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow('Tracking')
cv2.createTrackbar("LH","Tracking", 0,255,nothing)
cv2.createTrackbar("LS","Tracking", 0,255,nothing)
cv2.createTrackbar("LV","Tracking", 0,255,nothing)
cv2.createTrackbar("UH","Tracking", 255,255,nothing)
cv2.createTrackbar("US","Tracking", 255,255,nothing)
cv2.createTrackbar("UV","Tracking", 255,255,nothing)

while True:
    

    path = r'/media/tharani/DISK/Projects/Box Dimension Capture/Image/1/lb.jpg'
    org=cv2.imread(path)
    img=cv2.resize(org,(560,340))
    blur = cv2.GaussianBlur(img,(5,5),0)
    hsv= cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("LH", "Tracking")
    ls = cv2.getTrackbarPos("LS", "Tracking")
    lv = cv2.getTrackbarPos("LV", "Tracking")

    uh = cv2.getTrackbarPos("UH", "Tracking")
    us = cv2.getTrackbarPos("US", "Tracking")
    uv = cv2.getTrackbarPos("UV", "Tracking")

    lb= np.array([0,0,0])
    ub= np.array([182,184,145])

    mask = cv2.inRange(hsv, lb, ub)

    res = cv2.bitwise_and(hsv,hsv, mask =mask)

    #cv2.imwrite("Masked.jpg",res)

    cv2.imshow("Org",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    #cv2.imshow("Masked",masked)

    key= cv2.waitKey(1)

    if key == 27 :
        break

cv2.destroyAllWindow()
