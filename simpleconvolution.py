import cv2
import numpy as np

image = cv2.imread("mandrill.jpg", cv2.IMREAD_UNCHANGED)
namedWindow = 'Display window'

x = [1,1,1,1,1,1,1,1,1]  #softens image
kernel = (np.asarray(x)).reshape(3,3)
print(kernel)


for y in range(1, image.shape[0]-1):  # go through all rows (or scanlines)
  for x in range(1, image.shape[1]-1):  # go through all columns  
    a1 = image[y - (-1), x - (-1)] * kernel[0,0]  # h(-1,-1)
    a2 = image[y - (-1), x - (0)] * kernel[0,1]  # h(-1,0)
    a3 = image[y - (-1), x - (1)] * kernel[0,2] # h(-1,1)
    a4 = image[y - (0), x - (-1)] * kernel[1,0] # h(0,-1)
    a5 = image[y - (0), x - (0)] * kernel[1,1] # h(0,0)
    a6 = image[y - (0), x - (1)] * kernel[1,2] # h(0,1)
    a7 = image[y - (1), x - (-1)] * kernel[2,0] # h(1,-1)
    a8 = image[y - (1), x - (0)] * kernel[2,1] # h(1,0)
    a9 = image[y - (1), x - (1)] * kernel[2,2] # h(1,1)
    summation = a1+a2+a3+a4+a5+a6+a7+a8+a9
    image[y,x] = summation * (1/9)




cv2.imshow(namedWindow, image)
cv2.waitKey(0)
cv2.destroyAllWindows()