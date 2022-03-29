import cv2

def nothing(x):
    pass


cv2.namedWindow('Tracking')
cv2.createTrackbar("LH","Tracking", 0,255,nothing)
cv2.createTrackbar("LS","Tracking", 0,255,nothing)
cv2.createTrackbar("LV","Tracking", 0,255,nothing)
cv2.createTrackbar("HH","Tracking", 255,255,nothing)
cv2.createTrackbar("HS","Tracking", 255,255,nothing)
cv2.createTrackbar("HV","Tracking", 255,255,nothing)
