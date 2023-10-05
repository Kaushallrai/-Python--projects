import cv2
import random

img = cv2.imread('assets/retro marlboro.jpg', -1)

# for i in range(700):
#     for j in range(img.shape[1]):
#         img[i][j] = [random.randint(0, 255), random.randint(
#             0, 255), random.randint(0, 255)]

tag = img[400:600, 300:500]
img[100:300, 450:650] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
