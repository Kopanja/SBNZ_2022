import cv2
import numpy as np
import pandas as pd
import os
import sys
from math import *
import time
from MTM import matchTemplates
from MTM import drawBoxesOnRGB
import torch

def feature_match():
    img1 = cv2.imread("spike_rush_bf.png", cv2.IMREAD_GRAYSCALE)
   
    img = cv2.imread("spike_rush_bf_fs.png", cv2.IMREAD_GRAYSCALE)
    img2 = img[253:331,752:1169]
    
    
    orb = cv2.ORB_create()
    #cv2.imshow("2",img2)
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)
    
    imgKp1 = cv2.drawKeypoints(img1,kp1,None)
    imgKp2 = cv2.drawKeypoints(img2,kp2,None)
    
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    
    good = []
    
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append([m])
   
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
    print(len(good))
    cv2.imshow("kp1", imgKp1)
    cv2.imshow('kp2', imgKp2)
    cv2.imshow('kp3', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def load_templates():
    image_folder = "KFTemplates"
    listTemplate = []
    for filename in os.listdir(image_folder):
        template_img = cv2.imread(os.path.join(image_folder, filename))
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        listTemplate.append((filename.split('.')[0], template_img))
    return listTemplate

def load_map_templates():
    image_folder = "MapTemplates"
    listTemplate = []
    for filename in os.listdir(image_folder):
        template_img = cv2.imread(os.path.join(image_folder, filename))
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        listTemplate.append((filename.split('.')[0], template_img))
    return listTemplate

def check_map_template(frame,listTemplate):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    region = (56,47,424,263)
    try:
        hits = matchTemplates(listTemplate,
                        frame,
                        score_threshold=0.7,
                        searchBox=region,
                        method=cv2.TM_CCOEFF_NORMED,
                        maxOverlap=0.1)
        return hits
    except:
      pass

def doMatch(frame, templateList, timestamp):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = frame[75:190, 1479:1909]
    for template in templateList:
        res = cv2.matchTemplate(frame, template[1], cv2.TM_CCOEFF_NORMED)
        (yCoords, xCoords) = np.where( res >= 0.7)
        if (len(yCoords) >=1 and len(xCoords) >=1):
            print(template[0], "Time: " + str(timestamp))
            time.sleep(0.05)
        

def manual_match_template():
    img1 = cv2.imread("neonOrbFeature.png", cv2.IMREAD_GRAYSCALE)
    img = cv2.imread("neonKillFullscreen.png", cv2.IMREAD_GRAYSCALE)
    (tH, tW) = img1.shape[:2]
    img2 = img[90:132, 1829:1909]
    img = img[75:190, 1479:1909]
    clone = img.copy()
    
    #cv2.imshow("Before NMS", clone)
    #cv2.waitKey(0)
    res = cv2.matchTemplate(img, img1, cv2.TM_CCOEFF_NORMED)
    (yCoords, xCoords) = np.where( res >= 0.7)
    print(len(yCoords))
    print(xCoords)
    for (x, y) in zip(xCoords, yCoords):
        cv2.rectangle(clone, (x, y), (x + tW, y + tH),(255, 0, 0), 3)
    cv2.imshow("Before NMS", clone)
    cv2.waitKey(0)

def print_hits(frame,hits):
    if(hits is None):
        #print("Not found")
        return frame
    if(len(hits) == 0):
        #print("not found")
        return frame
    
    overlay = drawBoxesOnRGB(frame,
                         hits,
                         showLabel = True,
                         labelColor=(255, 0, 0),
                         boxColor = (0, 0, 255),
                         labelScale=1,
                         boxThickness = 3)
    return overlay    

def read_image(templateList, model):
    frame = cv2.imread('1.png')
    results = model(frame)
    if(len(results.pandas().xyxy[0]['xmin'].values)):
                #print(results.xyxy)
        for box in results.xyxy[0]:
            x_top = int(box[0])
            y_top = int(box[1])
            x_bot = int(box[2])
            y_bot = int(box[3])
            x_center_norm = abs((box[0] + box[2])/2.0)/1920.0
            y_center_norm = abs((box[1] + box[3])/2.0)/1080.0
            width_norm = abs(box[0] - box[2])/1920.0
            height_norm = abs(box[1] - box[3])/1080.0
            #print(x_top, x_bot)
            #print(y_top, y_bot)
            print(float(x_center_norm), float(y_center_norm), float(width_norm), float(height_norm))
            
                    #print("x_top:",type(x_top))
                    #print("y_top:",y_top)
                    #print("x_bot:",x_bot)
                    #print("y_bot:",y_bot)
            frame = cv2.rectangle(frame, (int(x_top), int(y_top)), (int(x_bot),int(y_bot)),(255, 0, 0),2)
    hits = check_map_template(frame=frame, listTemplate=templateList)       
    cv2.imshow('frame',  print_hits(frame, hits))
    cv2.waitKey()
    

def readVideo(templateList, model):
    print("Started")
    cap = cv2.VideoCapture('map_test_2_Trim2.mp4')
    fps = cap.get(cv2.CAP_PROP_FPS)
    if(cap.isOpened()== False):
        print("Error opening video stream or file")
    frame_no = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        
        if ret == True:
            #doMatch(frame=frame, templateList=templateList, timestamp=cap.get(cv2.CAP_PROP_POS_MSEC)/1000)
            #queue.put(FrameTime(frame,(cap.get(cv2.CAP_PROP_POS_MSEC)/1000)))
            results = model(frame)
            if(len(results.pandas().xyxy[0]['xmin'].values)):
                #print(results.xyxy)
                for box in results.xyxy[0]:
                    x_top = int(box[0])
                    y_top = int(box[1])
                    x_bot = int(box[2])
                    y_bot = int(box[3])
                    #print("x_top:",type(x_top))
                    #print("y_top:",y_top)
                    #print("x_bot:",x_bot)
                    #print("y_bot:",y_bot)
                    frame = cv2.rectangle(frame, (int(x_top), int(y_top)), (int(x_bot),int(y_bot)),(255, 0, 0),2)
            hits = check_map_template(frame=frame, listTemplate=templateList)
           
            cv2.imshow('frame',  print_hits(frame, hits))
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            break
        
    frame_no +=1    

if __name__ == '__main__':
    #manual_match_template()
    CUDA = torch.cuda.is_available()
    print(CUDA)
    #print(torch.zeros(1).cuda())
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='agent_detection/yolov5-master/best_agent_2.pt')
    if CUDA:
        model.cuda()
        model.conf = 0.7
        print("CUDAAA")
    templateList = load_map_templates()
    #img = cv2.imread("neonKillFullscreen.png")
    #doMatch(img, templateList=templateList)
    readVideo(templateList=templateList, model=model)
    #read_image(templateList=templateList, model=model)
    #feature_match()