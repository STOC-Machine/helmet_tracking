#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:01:35 2018

@author: kota421, David Chae
"""
import cv2
import numpy as np

### A function to apply a color filter to a video
### Good point: Can detect red!
### Not so good point: Full of noise!

def colorfilter(color=None,showFrame=True,showRes=True):
    """
    Displays a video filtered for a user input color. Default color is red.
    Assumes: color(int) is the Hue value of the target color; 0 <= color <= 180
    Returns: None
    """
    cap = cv2.VideoCapture(0)
    while(1):
        ### Getting the frame as input
        
        # read a frame
        _, frame = cap.read()
        frame = cv2.resize(frame,(960,540))
        # Convert the frame enconding from BGR to HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
        ### Define the range for the target color in HSV
        
        # Default target color is red. We may need to tune the HSV value.
        if not color:
            lower_color1 = np.array([0,100,100])
            upper_color1= np.array([10,255,255])
            lower_color2 = np.array([160,100,130])
            upper_color2 = np.array([180,255,200])
        # User color
        else:
            lower_color1 = np.array([color-10,100,100])
            upper_color1= np.array([color+10,255,255]) 
            # this range is a dummy
            lower_color2 = np.array([0,0,0])
            upper_color2 = np.array([0,0,0])


        ### Apply a color filter to the input
        
        # Create a mask i.e. an array of 0 or 1(uint8); 
        #   1 means that a pixel is in the range, 0 means it is not
        mask1 = cv2.inRange(hsv, lower_color1, upper_color1)
        mask2 = cv2.inRange(hsv,lower_color2,upper_color2)
        # combination of two masks
        comb_mask = np.logical_or(mask1,mask2) # np.logical_or converts uint8 to bool
        comb_mask = comb_mask.astype(np.uint8) # converting back to uint8
        # Apply the color filter to the input
        res= cv2.bitwise_and(frame,frame,mask = comb_mask)
        
        
        ### Display
        
        # Show input
        if showFrame:
            cv2.imshow('frame',frame) 
        # Show color-filtered input
        if showRes:
            cv2.imshow('color-filtered',res)
        
        k = cv2.waitKey(5) & 0xFF
        if k == 27: # Press ESC key to escape
            break
        
    cv2.destroyAllWindows()
        
colorfilter()

### Color filter for blue
#colorfilter(120)

##### Why do you need two ranges for red?
### That's because cv2.inRange will interpret a negative value as 0 
### i.e. You cannot specify red as [-20, 100, 100] to [10, 255, 255]
### Try this code.
### You will get two identical results.
# =============================================================================
# lower1 = np.array([0,100,100])
# lower2 = np.array([-20,100,100])
# upper = np.array([10,255,250])
# img = cv2.imread('YOUR_FILE_NAME.png',1) # Pick an image with red color
# cv2.imshow('img',img)
# 
# img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# mask1 = cv2.inRange(img, lower1, upper)
# mask2 = cv2.inRange(img, lower2, upper)
# res1 = cv2.bitwise_and(img, img, mask = mask1)
# res2 = cv2.bitwise_and(img, img, mask = mask2)
# cv2.imshow('zero as limit', res1)
# cv2.imshow('negative as limit', res2)
# cv2.waitKey(0)
# =============================================================================

### How to find a range for a color
# ============================f=================================================
# # red color in hsv
# red = np.uint8([[[0,0,255]]])
# hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
# # [[[0,255,255]]]
# =============================================================================

# helmet_tracking
