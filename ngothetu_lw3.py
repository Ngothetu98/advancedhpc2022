# -*- coding: utf-8 -*-
"""NgoTheTu_LW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFH_t8p2Y_sWxYLNFxPWPcX6cdep4IiY
"""

import matplotlib.pyplot as plt
import matplotlib.image as img
  
# reading the image
testImage = img.imread('/content/drive/MyDrive/M21.ICT.012_NgoTheTu.jpeg')
  
# displaying the image
plt.imshow(testImage)

from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from PIL import Image
import os.path
from numba import cuda
import time

filename = ('/content/drive/MyDrive/M21.ICT.012_NgoTheTu.jpeg')

im = Image.open(filename)
width, height = im.size
im.close()

hostInput = np.zeros((height, width, 3), np.uint8)
devOutput = cuda.device_array((height, width, 3), np.uint8)
devData = cuda.to_device(hostInput)

pixelCount = width * height
blockSize = 64
gridSize  = pixelCount / blockSize

img = mpimg.imread(filename)

@cuda.jit
def grayscale(src, dst):
  tidx = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
  g = np.uint8((src[tidx, 0] + src[tidx, 1] + src[tidx, 2]) / 3)
  dst[tidx, 0] = dst[tidx, 1] = dst[tidx, 2] = g

#hostInput = np.zeros((height, width, 3),np.uint8)
#devOutput = cuda.device_array((height, width, 3),np.uint8)

flatten = img.flatten().reshape(pixelCount,3)
# imgplot = plt.imshow(devInput)
# plt.show()

t1 = time.time()

for i in flatten:
  gray = ((i[0]+i[1]+[2])/3)
  i[0], i[1], i[2] = gray, gray, gray

t2 = time.time()

print(t2-t1)

imgray1 = flatten.reshape(height, width, 3)

imgpu = Image.fromarray(imgray1)
imgpu.save("/content/drive/MyDrive/Colab Notebooks/Ngothetu_GPU.jpeg")

imgplot = plt.imshow(imgray1)
plt.show()