import cv2

path = r'F:\Projects\Caterpillar\Images\img2.jpg'
org=cv2.imread(path)
img=cv2.resize(org,(560,340))
blur = cv2.GaussianBlur(img,(5,5),0)
hsv= cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

cv2.imshow("Blur",blur)
cv2.imshow("hsv",hsv)
