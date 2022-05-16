import cv2
import os
import requests
from MTM import matchTemplates
import numpy as np


def createListTemplate():
    image_folder = "agentAbilityTemplate"
    listTemplate = []
    for filename in os.listdir(image_folder):
        template_img = cv2.imread(os.path.join(image_folder, filename))
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        listTemplate.append((filename.split('.')[0], template_img))
    return listTemplate


def check_player(frame,listTemplate):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    region = (932,918,172,169)
    try:
        hits = matchTemplates(listTemplate,
                        frame,
                        score_threshold=0.9,
                        searchBox=region,
                        method=cv2.TM_CCOEFF_NORMED,
                        maxOverlap=0.1)
        return hits
    except:
      pass
  
if __name__ == '__main__':
    frame = cv2.imread("FullScreen.png")
    listTemplate = createListTemplate()
    print(check_player(frame, listTemplate))