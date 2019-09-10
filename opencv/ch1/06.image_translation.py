import cv2
import numpy as np

img = cv2.imread("./images/lena512.png")
num_rows, num_cols = img.shape[:2]

print("num_rows =", num_rows)
print("num_cols =", num_cols)

# translation 0
trans0 = [70, 110]
translation_matrix = np.float32([[1, 0, trans0[0]], [0, 1, trans0[1]]])
img_translation = cv2.warpAffine(img, translation_matrix, \
    (num_cols + trans0[0], num_rows + trans0[1])) # result image size

# translation 1
trans1 = [-30, -50]
translation_matrix = np.float32([[1, 0, trans1[0]], [0, 1, trans1[1]]])
img_translation = cv2.warpAffine(img, translation_matrix, \
    (num_cols + abs(trans0[0]) + abs(trans1[0]), num_rows + abs(trans0[1]) + abs(trans1[1]))) # result image size

cv2.imshow('Translation', img_translation)
cv2.waitKey()