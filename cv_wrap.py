#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import math


img = cv2.imread('path_to_origin_image.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

#####################
# Vertical wave

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x = int(20.0 * math.sin(2 * 3.14 * i / 180))
        offset_y = 0
        if j+offset_x < rows:
            img_output[i,j] = img[i,(j+offset_x)%cols]
        else:
            img_output[i,j] = 255

cv2.imshow('Input', img)
cv2.imshow('Vertical wave', img_output)
cv2.imwrite('path_to_ouput_image.jpg', img_output)

#####################
