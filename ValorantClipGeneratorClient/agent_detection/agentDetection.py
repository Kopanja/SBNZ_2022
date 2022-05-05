import cv2
import torch
import os
from PIL import Image
import shutil
import numpy as np
from mss import mss
import random
from MTM import matchTemplates
from MTM import drawBoxesOnRGB
import requests


class AgentDetectedEvent:
    def __init__(self, x_top,x_bot,y_top,y_bot, time) -> None:
        self.x_top = x_top
        self.x_bot = x_bot
        self.y_top = y_top
        self.y_bot = y_bot
        self.time = time

class BoundingBox:
    def __init__(self, x_top,x_bot,y_top,y_bot) -> None:
        self.x_top = x_top
        self.x_bot = x_bot
        self.y_top = y_top
        self.y_bot = y_bot
        
        
class FrameAgentDetectionEvent:
    def __init__(self, bboxes, time) -> None:
        self.bboxes = bboxes
        self.time= time
    
   

        
       

def agent_detection_thread(queue):
    print("Started Agent detection the video....")
    CUDA = torch.cuda.is_available()
    #print(CUDA)
    #print(torch.zeros(1).cuda())
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='agent_detection/yolov5-master/best_agent_2.pt', force_reload=True)
    if CUDA:
        model.cuda()
        model.conf = 0.8
    while True:
        frame_and_time = queue.get()
        if (frame_and_time is None):
            break
        do_detection(frame_and_time,model)
        
        
  
  
    print("Finished Agent detection the video....")

def do_detection(frame_and_time, model):
    results = model(frame_and_time.frame)
    frame = frame_and_time.frame
    if(len(results.pandas().xyxy[0]['xmin'].values)):
        bboxes = []
                #print(results.xyxy)
        for box in results.xyxy[0]:
            x_top = int(box[0])
            y_top = int(box[1])
            x_bot = int(box[2])
            y_bot = int(box[3])
            
            #agent_detection = AgentDetectedEvent(x_top, x_bot, y_top,y_bot,frame_and_time.frameTime)
            #requests.post('http://localhost:8080/api/events/agentDetected', json = agent_detection.__dict__)
            #samo za test
            
            bboxes.append(BoundingBox(x_top, x_bot, y_top, y_bot).__dict__)
            frame = cv2.rectangle(frame, (int(x_top), int(y_top)), (int(x_bot),int(y_bot)),(255, 0, 0),2)
        requests.post('http://localhost:8080/api/events/frameAgentDetection', json = FrameAgentDetectionEvent(bboxes, frame_and_time.frameTime).__dict__)
    frame = cv2.resize(frame, (640,480))
    cv2.imshow('frame', frame)
    cv2.waitKey(1)
           
#if __name__ == '__main__':
    #CUDA = torch.cuda.is_available()
    #print(CUDA)
    #print(torch.zeros(1).cuda())
    #model = torch.hub.load('ultralytics/yolov5', 'custom', path='agent_detection/yolov5-master/best_agent_2.pt',force_reload=True)
    #if CUDA:
    #    model.cuda()
    #    model.conf = 0.8
    #    print("CUDAAA")
    
    #main(model)
    #detect_on_video(model, 4)
    #f = open("agent_detection\\brojac.txt", 'r')
    #brojac = int(f.readline())
    #print(brojac)
    #f.close()
    #split_train_val()
  
 