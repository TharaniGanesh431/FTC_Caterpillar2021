import cv2
path='F:\Projects\Caterpillar\Images\IMG6.jpg'
org=cv2.imread(path)
img=cv2.resize(org,(560,560))
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
