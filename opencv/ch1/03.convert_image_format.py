import cv2

img = cv2.imread("./images/cat.jpg")
cv2.imwrite("./images/cat_output.png", img, [cv2.IMWRITE_PNG_COMPRESSION])