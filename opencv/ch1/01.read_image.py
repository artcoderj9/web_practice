import cv2

img = cv2.imread('images/cat.jpg', cv2.IMREAD_UNCHANGED)

print("type(img) =", type(img))
print("img.shape =", img.shape)
print("img.dtype =", img.dtype)

cv2.imshow('Image', img)

print("To close window, press esc key")
key = 0
while key != 27:
    key = cv2.waitKey(10)
    
print("key =", key) 
# key = 27 (<= esc)
# key = 49 (<= number 1)
