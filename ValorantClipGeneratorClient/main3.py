import cv2
import numpy as np
import pandas as pd





def read():
    img = cv2.imread('map_vision.png')
    print(img[253,253])
    mask1 = cv2.inRange(img, (217, 216, 217), (217, 216, 217))
    cv2.imshow("a", mask1)
    cv2.waitKey()
#read()


def readVideo():
    print("Started")
    cap = cv2.VideoCapture('map_test_trim.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    if(cap.isOpened()== False):
        print("Error opening video stream or file")
    frame_no = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == True:
            frame = cv2.resize(frame, (480,270))
            #hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
            #lower_gray = np.array([50, 0, 50])
            #upper_gray = np.array([255, 10, 255])
            #resized = cv2.resize(frame, (480,270))
            #mask1 = cv2.inRange(hsv, lower_gray, upper_gray)
            #mask1 = cv2.inRange(frame, (217, 216, 217), (217, 216, 217))
            mask1 = cv2.inRange(frame, (200, 200, 200), (217, 216, 217))
            cv2.imshow("a", mask1)
            cv2.imshow("b", frame)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
        
    frame_no +=1    
if __name__ == '__main__':
    readVideo()
    #read()