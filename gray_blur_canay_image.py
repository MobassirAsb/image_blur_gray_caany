
import cv2
import numpy as np
img_cb = cv2.imread('C:/Users/USER/PycharmProjects/pythonProject/pic/New_Zealand_Lake.jpg')
# Display the image
cv2.imshow("Output", img_cb)
kernel = np.ones((5,5),np.uint8)


img_gray = cv2.cvtColor(img_cb,cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(7,7),0)
img_canny = cv2.Canny(img_cb,150,200)
img_dialation = cv2.dilate(img_canny,kernel,iterations=1)
img_eroded = cv2.erode(img_dialation,kernel,iterations = 1)

cv2.imshow("Gray Image",img_gray)
cv2.imshow(" Blur Image",img_blur)
cv2.imshow("Cany image",img_canny)
cv2.imshow("Dialation image",img_dialation)
cv2.imshow('image Eroded', img_eroded)
cv2.waitKey(0)
