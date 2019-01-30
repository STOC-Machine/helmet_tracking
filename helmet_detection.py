#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:54:30 2019

@author: kota421
"""
import time
import cv2
import matplotlib.pyplot as plt
import numpy as np
from color_filter import redColorFilter_simple as color_filter
from noise_cancel import noise_cancel
from region_of_interest import region_of_interest, mask4ROI

###---------RUN TEST---------###
# =============================================================================
# ## test image
# img = cv2.imread("test_images/test_8.png",1)
# img_small = cv2.resize(img,(200,100))
# #color filtering
# _,img_red = color_filter(img)
# # noise canceling
# img_noiseless = noise_cancel(img_red)
# # resize
# img_noiseless_small = cv2.resize(img_noiseless,(200,100))
# # region of interest
# mask,islands,label_arrays = mask4ROI(img_noiseless_small) 
# img_ROI = region_of_interest(img_small,mask)
# #  position
# centerX,centerY = position(islands,label_arrays)
# print('helmetX =',centerX, 'helmetY=',centerY)
# print('The helmet is off from the center of the image by')
# print('x =',((0.5*img_small.shape[1])-centerX)*100/img_small.shape[1],'%,',
#       'y =',((0.5*img_small.shape[0])-centerY)*100/img_small.shape[0],'%')
# =============================================================================
#show
#cv2.imshow('original',img)
#cv2.waitKey(0)
#cv2.imshow('red',img_red)
#cv2.waitKey(0)
#cv2.imshow('noiseless',img_noiseless)
#cv2.waitKey(0)
# =============================================================================
# cv2.imshow('ROI',img_ROI)
# cv2.waitKey(0)
# 
# =============================================================================
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
        #color filtering
        _,img_red = color_filter(img)
        # noise canceling
        img_noiseless = noise_cancel(img_red)
        # resize
        img_noiseless_small = cv2.resize(img_noiseless,(200,100))
        # region of interest
        mask,centerX,centerY = mask4ROI(img_noiseless_small) 
        img_ROI = region_of_interest(img_small,mask)
        # Position
        print('The helmet is off from the center of the image by')
        print('x =',((-0.5*img_small.shape[1])+centerX)*100/img_small.shape[1],'%,',
              'y =',((-0.5*img_small.shape[0])+centerY)*100/img_small.shape[0],'%')
        # Show images
        #cv2.imshow('noiseless',img_noiseless)
        #cv2.waitKey(0)
        cv2.imshow('ROI',img_ROI)
        cv2.waitKey(0)
#test_pics(11)

def test(img):
    img_small = cv2.resize(img,(200,100))
    #color filtering
    _,img_red = color_filter(img)
    # noise canceling
    img_noiseless = noise_cancel(img_red)
    # resize
    img_noiseless_small = cv2.resize(img_noiseless,(200,100))
    # region of interest
    mask,centerX,centerY = mask4ROI(img_noiseless_small) 
    #img_ROI = region_of_interest(img_small,mask)
    # Position
# =============================================================================
#     print('The helmet is off from the center of the image by')
#     print('x =',((-0.5*img_small.shape[1])+centerX)*100/img_small.shape[1],'%,',
#           'y =',((-0.5*img_small.shape[0])+centerY)*100/img_small.shape[0],'%')
# =============================================================================
    # Show images
    #cv2.imshow('noiseless',img_noiseless)
    #cv2.waitKey(0)
    #cv2.imshow('ROI',img_ROI)
    #cv2.waitKey(0)
    return centerX,centerY   

def test_video():
    plt.axis([0,200,0,100])
    X=[]
    Y=[]
    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()
    cap = cv2.VideoCapture(0)
    while True:
        ### Getting the frame as input
        # read a frame
        _, frame = cap.read()
        frame = cv2.resize(frame,(960,540))
        #===== OPERATION ========#
        try:
            x,y = test(frame)
            X.append(x)
            Y.append(y)
            plt.scatter(x,y)
        except IndexError:
            pass
        #========================#
        
        plt.show()
        plt.xlim([0, 200])
        plt.ylim([0, 100])
        time.sleep(1)
        fig.canvas.draw()
    
        k = cv2.waitKey(5) & 0xFF
        if k == 27: # Press ESC key to escape
            break   
    cv2.destroyAllWindows()

test_video()