# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:29:28 2018

@author: Toolslab6
"""

import cv2
import matplotlib.pyplot as plt


img = cv2.imread('C:\\Users\\Toolslab6\\Desktop\\Abhishek_Kumar_JavaScript\\OpneCV\\4.1.02COPY.tiff',-1)

#plt.imshow(img)   #return image
#plt.show()
plt.imshow(img,cmap = 'gray')
plt.title('Gray color')   # to display with title
plt.xticks([])  #  To remove the number of x axis
plt.yticks([])  #  To remove the number of y axis
plt.show()

plt.imshow(img,cmap = 'Blues')
plt.title('Default color')
plt.show()

cv2.imshow('My Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()