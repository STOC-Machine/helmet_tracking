#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 11:36:06 2019

@author: kota421
"""

import cv2
from helmet_detection import test
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('example.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

def offer_XY(X,Y):
    cap = cv2.VideoCapture(0)
    _, frame = cap.read()
    try:
        x,y = test(frame)
        X.append(x)
        Y.append(y)
    except:
        pass
    return X,Y

def test_video(X,Y):
    X,Y = offer_XY(X,Y)
    #plt.axis([0,200,0,100])
# =============================================================================
#     cap = cv2.VideoCapture(0)
#     _, frame = cap.read()
#     #===== OPERATION ========#
#     try:
#         x,y = test(frame)
#         X.append(x)
#         Y.append(y)
#     except:
#         pass
#     #========================#
# =============================================================================
    ax1.clear()
    ax1.plot(X, Y)

def visualize_position():
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
        #===== OPERATION ========#

        try:
            x,y = test(frame)
            X.append(x)
            Y.append(y)
            plt.scatter(x,y)
        except IndexError or ValueError:
            pass
        #========================#
        
        plt.show()
        plt.xlim([0, 200])
        plt.ylim([0, 100])
        time.sleep(0.5)
        fig.canvas.draw()
        cv2.imshow('frame',frame) 
        k = cv2.waitKey(5) & 0xFF
        if k == 27: # Press ESC key to escape
            break   
    cv2.destroyAllWindows()

X=[]
Y=[]      
#ani = animation.FuncAnimation(fig, test_video(X,Y), interval=1000)
#plt.show()
visualize_position()