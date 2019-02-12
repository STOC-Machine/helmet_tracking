#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:54:30 2019

@author: kota421
"""
## BUG with an image that does not have a red pixel

import cv2
from color_filter import redColorFilter_simple as color_filter
from noise_cancel import noise_cancel
from region_of_interest import region_of_interest, mask4ROI

def isColoredPixel(x,y,image):
    try:
        return image[x][y] > 0
    except IndexError:
        return False

def test(img):
    """
    ASSUMES:
        -img: numpy.array, cv2 image in BGR,
    RETURNS:
        -img_ROI: numpy.array, cv2 image in BGR, image that shows ONLY around
            the biggest red region in img
        -centerX: int, x coordinate of the center of the ROI in img_ROI
        -centerY: int, y coordinate of the center of the ROI in img_ROI
    """
    #color filtering
    _,img_red = color_filter(img)
    # noise canceling
    img_noiseless = noise_cancel(img_red)
    # resize
    img_noiseless_small = cv2.resize(img_noiseless,(200,100))
    img_small = cv2.resize(img,(200,100))
    # region of interest
    mask,centerX,centerY = mask4ROI(img_noiseless_small,isColoredPixel) 
    img_ROI = region_of_interest(img_small,mask)
    return img_ROI,centerX,centerY


###---------RUN TEST with a single image---------###
# =============================================================================
# ## Test image
# img = cv2.imread("test_images/test_8.png",1)
# img_small = cv2.resize(img,(200,100))
# img_ROI,centerX,centerY = test(img)
# #  position
# if centerX:
#     print('helmetX =',centerX, 'helmetY=',centerY)
#     print('The helmet is off from the center of the image by')
#     print('x =',(centerX-(0.5*img_small.shape[1]))*100/img_small.shape[1],'%,',
#           'y =',(centerY-(0.5*img_small.shape[0]))*100/img_small.shape[0],'%')
# else:
#     print('No helmet found in the image.')
# ## Show
# cv2.imshow('original',img_small)
# cv2.waitKey(0)
# cv2.imshow('ROI',img_ROI)
# cv2.waitKey(0)
# 
# =============================================================================

###---------RUN TEST with many images---------###
def test_pics(n):
    for i in range(1,12):
        try:
            name = "test_images/test_"+str(i)+".png"
            img = cv2.imread(name,1)
            img_small = cv2.resize(img,(200,100))
        except:
            name = "test_images/test_"+str(i)+".jpg"
            img = cv2.imread(name,1)
            img_small = cv2.resize(img,(200,100))
        ## Test image
        img_ROI,centerX,centerY = test(img_small)
        #  position
        if centerX:
            print('helmetX =',centerX, 'helmetY=',centerY)
            print('The helmet is off from the center of the image by')
            print('x =',(centerX-(0.5*img_small.shape[1]))*100/img_small.shape[1],'%,',
                  'y =',(centerY-(0.5*img_small.shape[0]))*100/img_small.shape[0],'%')
        else:
            print('No helmet found in the image.')
        ## Show
        cv2.imshow('original',img_small)
        cv2.waitKey(0)
        cv2.imshow('ROI',img_ROI)
        cv2.waitKey(0)
## Uncomment line below to test many images
# test_pics(11)


###---------RUN TEST with a video---------###
def test_video():
    cap = cv2.VideoCapture(0)
    while True:
        # read a frame
        _, frame = cap.read()
        #===== OPERATION ========#
        result,_,_ = test(frame)  
        cv2.imshow('result',result) 
        # Press ESC key to escape
        k = cv2.waitKey(5) & 0xFF
        if k == 27: 
            break   
    cv2.destroyAllWindows()

## Uncomment line below to test a video
test_video()