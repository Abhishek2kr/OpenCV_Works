# -*- coding: utf-8 -*-
"""
Created on Tue May  8 12:35:12 2018

@author: Toolslab6
"""

import cv2

def main():
    imgpath = "C:\\Users\\Toolslab6\\Desktop\\Abhishek_Kumar_JavaScript\\OpneCV\\misc\\4.1.02.tiff"
    
    #img = cv2.imread(imgpath,1)
    #print(img)  # will return the n dimensional array
    #print(type(img)) # will return the output numpy.ndarray
    #print(img.dtype) # uint8
    #print(img.shape) # height,weight,channel/no of color
    #print(img.ndim)  # no of dimension 3
    #print(img.size)
 
    img = cv2.imread(imgpath,0)
    print(img)  # will return the n dimensional array
    print(type(img)) # will return the output numpy.ndarray
    print(img.dtype) # uint8
    print(img.shape) # height,weight,channel/no of color
    print(img.ndim)  # no of dimension 2
    print(img.size)

if __name__ == "__main__":
   main()    