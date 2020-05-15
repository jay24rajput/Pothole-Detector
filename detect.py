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
# print(contours)

# cnt = contours[0]
# M = cv2.moments(cnt)
# print(M)

# perimeter = cv2.arcLength(cnt,True)
# # print (perimeter)

# area = cv2.contourArea(cnt)
# print (area)

for contour in contours:
    area = cv2.contourArea(contour)
    # print(area)

    if area > 10000:
        cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

# for c in contours:
#     rect = cv2.boundingRect(c)
#     if rect[2] < 100 or rect[3] < 100: continue
#     #print cv2.contourArea(c)
#     x,y,w,h = rect
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),8)
#     cv2.putText(img,'',(x+w+40,y+h),0,2.0,(0,255,0))
    
    # plt.title("Moth Detected Pothole Image")
    # # plt.imshow(img)
    # # plt.show()

cv2.imshow('otsu',thresh)
cv2.imshow('img',img)
# cv2.imshow('res',res)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Authored by Jay Rajput 