
import cv2

def main():
    imgpath = "C:\\Users\\Toolslab6\\Desktop\\Abhishek_Kumar_JavaScript\\OpneCV\\misc\\4.1.02.tiff"
    img =cv2.imread(imgpath)
    
    cv2.namedWindow('Window_Name',cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Window_Name',img)
    cv2.waitKey(1024)  # Wait for the input from the keyboard
    cv2.destroyWindow('Window_Name') # Will close all the windows opend for image display
    
if __name__ == "__main__":
    main()    