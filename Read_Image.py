# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:53:52 2018

@author: Toolslab6
"""

import cv2

def main():
    imgpath = "C:\\Users\\Toolslab6\\Desktop\\Abhishek_Kumar_JavaScript\\OpneCV\\misc\\4.1.02.tiff"
    img =cv2.imread(imgpath)
    cv2.imshow('Window_Name',img)
    cv2.waitKey(0)  # Wait for the input from the keyboard
    cv2.destroyAllWindows() # Will close all the windows opend for image display
    
if __name__ == "__main__":
    main()    