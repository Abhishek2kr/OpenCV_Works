# -*- coding: utf-8 -*-
"""
Created on Wed May  9 12:46:49 2018

@author: Toolslab6

Display the name in rectangle
"""

import cv2
import numpy as np 
def main():
    #img = np.ones((512,512,3))
    img1 = np.zeros((512,512,3), np.uint8)
    #cv2.imshow('OHH',img1)
    cv2.rectangle(img,(20,20),(320,320),(0,255,0),2)
    text = "Abhishek"
    text1 = "Kumar"
    cv2.putText(img,text,(30,120),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
    cv2.putText(img,text1,(30,220),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255))
    cv2.imshow('Assignment',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()    