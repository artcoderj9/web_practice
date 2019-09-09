import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./images/cat.jpg", cv2.IMREAD_COLOR)

# plt.imshow(img[...,::-1], interpolation='bicubic') # also working
plt.imshow(img[:,:,::-1], interpolation='bicubic')
#plt.xticks([])
#plt.yticks([])
plt.show()
