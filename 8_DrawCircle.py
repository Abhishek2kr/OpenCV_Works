# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:07:49 2018

@author: Toolslab6
"""

import cv2
import numpy as np

windowName = "Drawing"
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

def draw_Circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
      cv2.circle(img,(x,y),40,(0,255,0),-1)
    elif event == cv2.EVENT_RBUTTONDBLCLK:  
      cv2.circle(img,(x,y),40,(0,0,255),-1)
    elif event == cv2.EVENT_MBUTTONDOWN:  
      cv2.circle(img,(x,y),40,(0,0,255),-1)
      
      
cv2.setMouseCallback(windowName,draw_Circle)

def main():
   while(True):
       cv2.imshow(windowName,img)
       if cv2.waitKey(1) == 27:
          break
      
   cv2.destroyAllWindows()

if __name__ == "__main__":
    main()     