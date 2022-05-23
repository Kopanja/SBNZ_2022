import cv2
import os
import requests
from MTM import matchTemplates
import numpy as np


class KillEvent:
  def __init__(self, killer, isKillAlly, defeated, isDefeatAlly, time) -> None:
      self.killer = killer
      self.isKillAlly = isKillAlly
      self.defeated = defeated
      self.isDefeatAlly = isDefeatAlly
      self.time = time
class EndRound:
  def __init__(self) -> None:
      pass

def check_kill_feed(frame,listTemplate):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #region = (1479,75,440,110)
    region = (1400,75,520,110)
    try:
        hits = matchTemplates(listTemplate,
                        frame,
                        score_threshold=0.75,
                        searchBox=region,
                        method=cv2.TM_CCOEFF_NORMED,
                        maxOverlap=0.1)
        return hits
    except:
      pass

def createListTemplate():
    image_folder = "SRKFTemplate"
    listTemplate = []
    for filename in os.listdir(image_folder):
        template_img = cv2.imread(os.path.join(image_folder, filename))
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        listTemplate.append((filename.split('.')[0], template_img))
    return listTemplate
   


def kf_thread(queue):
  print("Started KF detection the video....")
  killEvents = []
  listTemplate = createListTemplate()
  while True:
    frame_and_time = queue.get()
    #print("ovde")
    if (frame_and_time is None):
      requests.post('http://localhost:8080/api/events/endRound', json = EndRound().__dict__)
      break
    #print("ovde")
    hits = check_kill_feed(frame_and_time.frame,listTemplate)
    #print("sad ovde")
    killEvents = create_kill_event(hits, killEvents, frameTime=frame_and_time.frameTime, frame=frame_and_time.frame)
    #print("ovdeeeeee")
  print("Finished KF detection the video....")

  
def ally_or_enemy(bbox,frame):
  
 # print("----------------------------------------------------")
 # print(bbox[0],bbox[1], bbox[2],bbox[3])
 # print("----------------------------------------------------")
  if(bbox[0] < 1700):
    frame = frame[bbox[1]:(bbox[1] + bbox[3]), bbox[0] + bbox[2]:(bbox[0] + bbox[2]) + 30]
  else:
    frame = frame[bbox[1]:(bbox[1] + bbox[3]), bbox[0] - 30:bbox[0]]
  
  image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  mask1 = cv2.inRange(image, (0,50,20), (5,255,255))
  mask2 = cv2.inRange(image, (175,50,20), (180,255,255))
  #mask = cv2.inRange(image, lower_red, upper_red)
  mask = cv2.bitwise_or(mask1, mask2 )
  n_white_pix = np.sum(mask == 255)
  if(n_white_pix > 15):
    return False
  else:
    return True
  
def create_kill_event(hits, killEvents, frameTime, frame):
  if(hits is None):
    return killEvents
  if(len(hits) == 0):
    return killEvents
  for _,hit in hits.iterrows():
    for _,hit2 in hits.iterrows():
      if(hit["TemplateName"] != hit2["TemplateName"] and abs(hit["BBox"][1] - hit2["BBox"][1]) <= 15):
        killer = ""
        defeated = ""
        isKillAlly = False
        isDefeatAlly = False
        hitInfo = hit["TemplateName"].split("_")
        hitInfo2 = hit2["TemplateName"].split("_")
        if(hitInfo[-1] == 'kill'):
          killer = hitInfo[0]
          isKillAlly = ally_or_enemy(hit["BBox"], frame)
          defeated = hitInfo2[0]
          isDefeatAlly = ally_or_enemy(hit2["BBox"], frame)
        else :
          killer = hitInfo2[0]
          isKillAlly = ally_or_enemy(hit2["BBox"], frame)
          defeated = hitInfo[0]
          isDefeatAlly = ally_or_enemy(hit["BBox"], frame)
        killEvent = killer + " Killed: " + defeated
        if killEvent not in killEvents:
          ally_or_enemy(hit["BBox"], frame)
          ally_or_enemy(hit2["BBox"], frame)
          killEvents.append(killEvent)
          ke = KillEvent(killer=killer, isKillAlly=isKillAlly,defeated=defeated, isDefeatAlly=isDefeatAlly,time=frameTime)
          print(ke.__dict__)
          requests.post('http://localhost:8080/api/events/postKill', json = ke.__dict__)
  return killEvents