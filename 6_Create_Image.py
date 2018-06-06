# -*- coding: utf-8 -*-
"""
Created on Tue May  8 14:32:29 2018

@author: Toolslab6
"""

import numpy as np
import cv2

def main():
    img = np.zeros((256,256,3),np.uint8)
    #cv2.line(img,(0,99),(99,0),(255,0,0),2) #will draw line
    cv2.rectangle(img,(40,50),(80,90),(0,255,0),2)
    #cv2.circle(img,(50,50),20,(0,0,255),2)
    #cv2.circle(img,(50,50),20,(0,0,255),-1)
    #cv2.ellipse(img,(160,260),(50,30),0,0,360,(127,127,127),-1)

    #points = np.array([[80,2],[125,40],[179,19],[230,5],[30,50]],np.int32)
    #points = points.reshape(-1,1,2)
    #cv2.polylines(img,[points],True,(0,255,255))
    #cv2.imshow('MyImage',img)
    #cv2.waitKey(0)
    #cv2.destroyWindow('MyImage')
    
if __name__ == "__main__":
    main()
    