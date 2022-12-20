# -*- coding: utf-8 -*-
"""NgoTheTu_LW3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tFH_t8p2Y_sWxYLNFxPWPcX6cdep4IiY
"""

import numba
from numba import cuda

import matplotlib.pyplot as plt
import matplotlib.image as img
  
# reading the image
testImage = img.imread('/content/drive/MyDrive/M21.ICT.012_NgoTheTu.jpeg')
  
# displaying the image
plt.imshow(testImage)

from PIL import Image
import os.path

filename = ('/content/drive/MyDrive/M21.ICT.012_NgoTheTu.jpeg')

img = Image.open(filename)
width, height = img.size
print(img.size, "Pixel Count:", width * height)

import numba
from numba import cuda
import numpy as np

@cuda.jit
def grayscale(src, dst):
  tidx = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
  g = np.uint8((src[tidx, 0] + src[tidx, 1] + src[tidx, 2]) / 3)
  dst[tidx, 0] = dst[tidx, 1] = dst[tidx, 2] = g

hostInput = np.zeros((height, width, 3),np.uint8)

#devOutput = cuda.device_array((height, width, 3),np.uint8)