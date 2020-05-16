import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('pothole.jpg',cv2.IMREAD_COLOR)
img = cv2.resize(img, (500, 500))

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),30)

ret,thresh = cv2.threshold(blur,125,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
_,contours,_= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# _,contours,_= cv2.findContours(thresh,1, 2)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    area = cv2.contourArea(contour)
    # print(area)

    if area > 10000:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

cv2.imshow('otsu',thresh)
cv2.imshow('img',img)
# cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Authored by Jay Rajput 