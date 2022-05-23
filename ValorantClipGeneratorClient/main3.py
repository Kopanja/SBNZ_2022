import cv2
import numpy as np
import pandas as pd

from killFeedDetection import *


def test_ally_or_enemy(frame, listTemplate, killEvents):
    
    hits = check_kill_feed(frame,listTemplate)
    killEvents = create_kill_event(hits, killEvents, frameTime=0, frame=frame)




def read():
    img = cv2.imread('map_vision.png')
    print(img[253,253])
    mask1 = cv2.inRange(img, (217, 216, 217), (217, 216, 217))
    cv2.imshow("a", mask1)
    cv2.waitKey()
#read()


def readVideo():
    print("Started")
    cap = cv2.VideoCapture('C://Users//kopan//Desktop//Spike-rush_Trim_round3.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    if(cap.isOpened()== False):
        print("Error opening video stream or file")
    frame_no = 0
    listTemplate = createListTemplate()
    killEvents = []
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == True:
           
            test_ally_or_enemy(frame,listTemplate,killEvents)
            frame = cv2.resize(frame, (560,420))
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
        
    frame_no +=1    
if __name__ == '__main__':
    readVideo()
    #read()