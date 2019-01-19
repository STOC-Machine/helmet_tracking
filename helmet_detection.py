#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:54:30 2019

@author: kota421
"""
import cv2
from color_filter import redColorFilter_simple as color_filter
from noise_cancel import noise_cancel

###---------RUN TEST---------###
## test image
img = cv2.imread("test_10.png",1)
#color filtering
_,img_red = color_filter("test_10.png")
# noise canceling
img_noiseless = noise_cancel(img_red)

#show
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.imshow('red',img_red)
cv2.waitKey(0)
cv2.imshow('result',img_noiseless)
cv2.waitKey(0)