#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:54:30 2019

@author: kota421
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
from color_filter import redColorFilter_simple as color_filter
from noise_cancel import noise_cancel
from region_of_interest import region_of_interest, mask4ROI

###---------RUN TEST---------###
# =============================================================================
# ## test image
# img = cv2.imread("test_5.png",1)
# img_small = cv2.resize(img,(200,100))
# #color filtering
# _,img_red = color_filter("test_5.png")
# # noise canceling
# img_noiseless = noise_cancel(img_red)
# # resize
# img_noiseless_small = cv2.resize(img_noiseless,(200,100))
# # region of interest
# 
# print("img shape",img_small.shape)
# print("img datatype:",img_small.dtype)
# mask = mask4ROI(img_noiseless_small) 
# print("mask shape:",mask.shape)
# print("mask datatype:", mask.dtype)
# img_ROI = region_of_interest(img_small,mask)
# 
# =============================================================================
# =============================================================================
# #show
# cv2.imshow('original',img)
# cv2.waitKey(0)
# cv2.imshow('red',img_red)
# cv2.waitKey(0)
# cv2.imshow('noiseless',img_noiseless)
# cv2.waitKey(0)
# cv2.imshow('ROI',img_ROI)
# cv2.waitKey(0)
# 
# =============================================================================
def testROI(n):
    for i in range(1,12):
        try:
            name = "test_"+str(i)+".png"
        except:
            name = "test_"+str(i)+".jpg"
        img = cv2.imread(name,1)
        img_small = cv2.resize(img,(200,100))
        #color filtering
        _,img_red = color_filter(name)
        # noise canceling
        img_noiseless = noise_cancel(img_red)
        # resize
        img_noiseless_small = cv2.resize(img_noiseless,(200,100))
        # region of interest
        mask = mask4ROI(img_noiseless_small) 
        img_ROI = region_of_interest(img_small,mask)
        cv2.imshow('ROI',img_ROI)
        cv2.waitKey(0)
testROI(11)