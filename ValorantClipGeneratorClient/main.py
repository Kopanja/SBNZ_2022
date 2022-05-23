import cv2
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from MTM import matchTemplates
import os
import threading
from queue import Queue
import requests
import websocket
import stomper
import json
import numpy as np
import pandas as pd
import os
import sys
import time
#import multiprocessing
from buyPhaseDetection import buy_phase_detection_thread
from killFeedDetection import kf_thread
from agent_detection.agentDetection import agent_detection_thread

class MSG(object):
    def __init__(self, msg):
        self.msg = msg
        sp = self.msg.split("\n")
        self.content = sp[0]
        self.message = ''.join(sp[7:])[0:-1] 

class Round:
  def __init__(self) -> None:
      pass

class ClipEvent:
  def __init__(self, startTime, endTime, title) -> None:
      self.startTime = startTime
      self.endTime = endTime
      self.title = title    
        
class FrameTime:
  def __init__(self, frame, frameTime) -> None:
      self.frame = frame
      self.frameTime = frameTime




          

def ff_reader(queue):
  clip = VideoFileClip("Spike-rush.mp4")
  frames = clip.iter_frames()
  for frame in frames:
    queue.put(frame)
  print("Gotov read")
  queue.put(None)
  

def video_reader(queueKF,queueBF,queueAD):
  print("Started reading the video....")
  cap = cv2.VideoCapture('C://Users//kopan//Desktop//Spike-rush_Trim_round2.mp4')
  fps = cap.get(cv2.CAP_PROP_FPS)
  requests.post('http://localhost:8080/api/events/buyRound', json =Round().__dict__)
  frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
  duration = frame_count/fps
  print(duration)
  if(cap.isOpened()== False):
    print("Error opening video stream or file")
  frame_no = 0
  while(cap.isOpened()):
    ret, frame = cap.read()
    #if frame_no %1000 == 0:
    #  print(queueKF.qsize())
    #  print(queueBF.qsize())
    #  print(queueAD.qsize())
    #  print("Radim")
    if ret == True:
      frame = FrameTime(frame,(cap.get(cv2.CAP_PROP_POS_MSEC)/1000))
      if(queueBF.full() == False):
        queueBF.put(frame)
      if(queueKF.empty()):
        queueKF.put(frame)
      #if(queueKF.empty() and queueAD.empty()):
      #  queueKF.put(frame)
        
      #  queueAD.put(frame)
    else:
      break
    frame_no +=1
  print("Finished reading the video....")
  queueKF.put(None)
  queueBF.put(None)
  queueAD.put(None)
  cap.release()

def clip_video(clipEvent):
 
  video = VideoFileClip('C://Users//kopan//Desktop//Spike-rush_Trim_round2.mp4')
  clip = video.subclip(clipEvent["startTime"],clipEvent["endTime"])
  clip.write_videofile(clipEvent["title"] + ".mp4")

def wsThreadFunction():
    uri = "ws://localhost:8080/ws"
    ws = websocket.create_connection(uri)
    ws.send("CONNECT\naccept-version:1.0,1.1,2.0\n\n\x00\n")
    sub = stomper.subscribe("/topic", 1, ack='auto')
    ws.send(sub)
    while True:
        d = ws.recv()
        print("----------------------------------")
        m = MSG(d)
        if(m.message != ""):
            obj = json.loads(m.message)
            print(obj)
            clip_video(obj)
            
            
            
if __name__ == '__main__':
  #queue = multiprocessing.Queue()
  queueKF = Queue(maxsize=600)
  
  queueBF = Queue(maxsize=600)
  
  queueAD = Queue(maxsize=600)
  #video_reader()
  #ff_reader(queue)
  videoReaderThread = threading.Thread(target = video_reader, args=(queueKF,queueBF,queueAD))
  killFeedThread = threading.Thread(target=kf_thread, args=(queueKF,))
  #agentDetectionThread = threading.Thread(target=agent_detection_thread, args=(queueAD,))
  clipVideoThread = threading.Thread(target=wsThreadFunction,args=())
  #buyPhaseThread = threading.Thread(target=buy_phase_detection_thread, args=(queueBF,))
  
  #videoReaderThread = multiprocessing.Process(target = video_reader, args=(queue,))
  #killFeedThread = multiprocessing.Process(target=kf_thread, args=(queue,))
  #clipVideoThread = multiprocessing.Process(target=wsThreadFunction,args=())
  #buyPhaseThread = multiprocessing.Process(target=buy_phase_detection_thread, args=(queue,))
  
  
  
  clipVideoThread.start()
  videoReaderThread.start()  
  killFeedThread.start()
  #buyPhaseThread.start()
  #agentDetectionThread.start()
  
  
  videoReaderThread.join()
  killFeedThread.join()
  clipVideoThread.join()
  #agentDetectionThread.join()
  #buyPhaseThread.join()
  