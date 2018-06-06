# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:51:07 2018

@author: Toolslab6
"""

import cv2
import numpy as np

def main():
    img = np.zeros((512,512,3),np.uint8)
    windowName = 'Open CV BGR color palette'
    cv2.imshow(windowName,img)
    #cv2.waitKey(0)
    while(True):
        if cv2.waitKey(3) == 27:
          break
    
    
    
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()    