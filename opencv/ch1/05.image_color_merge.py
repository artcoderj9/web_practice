import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/lena512.png", cv2.IMREAD_COLOR)

b, g, r = cv2.split(img) # order is B,G,R

bgr_img = cv2.merge((b,g,r))
rgb_img = cv2.merge((r,g,b))

#plt.imshow(rgb_img, interpolation='bicubic') # plt show rgb order
#plt.show()

cv2.imshow("Original", img)
cv2.imshow("BGR", bgr_img)
cv2.imshow("RGB", rgb_img)

cv2.waitKey()
