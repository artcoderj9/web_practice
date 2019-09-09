import cv2

img = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

y, u, v = cv2.split(yuv_img)

cv2.imshow("Grayscale Image", gray_img)
cv2.imshow("Y Channel", y)
cv2.imshow("U Channel", u)
cv2.imshow("V Channel", v)

cv2.waitKey()