import numpy as np
import cv2

image = cv2.imread("mandrill.jpg", 0)

arr = [1] * 9
kernel = np.array(arr)
kernel = kernel.reshape((3, 3))

def convolution2d(image, kernel):
    m, n = kernel.shape
    if (m == n):
        y, x = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = np.zeros((y,x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i:i+m, j:j+m]*kernel)
    return new_image

new_image = convolution2d(image, float(1/9) * kernel)
cv2.imwrite( "mandrillblur.jpg", new_image)

