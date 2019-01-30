#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 12:53:56 2019

@author: kota421
"""
from region_of_interest import array2Coordinates



## SHOULD BE INCORPORATD INTO MASK4ROI

def position(islands,label_arrays,mode='biggest'):
    if mode=='top':
        x,y = array2Coordinates(label_arrays[0])
        maxX, minX =max(x),min(x)
        maxY, minY =max(y),min(y)
        return (maxX+minX)/2, (maxY+minY)/2
    if mode=='biggest':
        island_areas = [] 
        for island in islands:
            island_areas.append(len(island))
        biggest = island_areas.index(max(island_areas))
        x,y = array2Coordinates(label_arrays[biggest])
        maxX, minX =max(x),min(x)
        maxY, minY =max(y),min(y)
        return (maxX+minX)/2, (maxY+minY)/2
    
    