import cv2
import numpy as np

img = cv2.imread("./images/lena512.png")
num_rows, num_cols = img.shape[:2]

print("num_rows =", num_rows)
print("num_cols =", num_cols)

