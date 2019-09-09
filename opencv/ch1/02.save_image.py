import cv2

gray_img = cv2.imread('./images/lena512.png', cv2.IMREAD_GRAYSCALE)

print("type(gray_img) =", type(gray_img))
print("gray_img.shape =", gray_img.shape)
print("gray_img.dtype =", gray_img.dtype)

cv2.imshow('Grayscale', gray_img)
cv2.imwrite('./images/lena512_output.png', gray_img)
cv2.waitKey(3000)
