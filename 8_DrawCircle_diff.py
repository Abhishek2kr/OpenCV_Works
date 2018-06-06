# -*- coding: utf-8 -*-
"""
Created on Thu May 10 12:04:44 2018

@author: Toolslab6
"""

import numpy as np
import cv2

drawing = False

img = np.zeros((512,512,3),np.uint8)
windowName = "draw Circle"
cv2.namedWindow(windowName)


def draw_Circle(event,x,y,flag,param):
    global drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    #if event == cv2.EVENT_MOUSEMOVE and drawing:
     #cv2.circle(img,(x,y),5,(51,153,255),-1)
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
          cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)


cv2.setMouseCallback(windowName,draw_Circle)
                    
def main():
   while(True):
       cv2.imshow(windowName,img)
       if cv2.waitKey(1) ==  27:
           break
       elif cv2.waitKey(1) == 'b':
          img.dump                 
   cv2.destroyAllWindows()       
        
if __name__ == "__main__":
   main()        