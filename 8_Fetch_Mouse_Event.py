# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:01:27 2018

Program for print all mouse events
"""

import cv2

def main():
    events = [i for i in dir(cv2) if 'EVENT' in i ]
    print(events)
    
if __name__ == "__main__":
    main()    