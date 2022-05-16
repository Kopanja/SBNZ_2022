
import cv2
import requests

class Round:
  def __init__(self) -> None:
      pass


def crop_buy_phase(frame):
  #normal game
  #return frame[128:288,800:1126]
  #spike Rush
  return frame[203:361,712:1209]


def crop_agent_abilities(frame):
  return frame[973:1060,737:1182]
 
def detect_player_agent(frame):
  frame = crop_agent_abilities(frame)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  img1 = cv2.imread("agentAbilitiesImages/pheonix_abilities.png", cv2.IMREAD_GRAYSCALE)
  orb = cv2.ORB_create()
  bf = cv2.BFMatcher()
  kp1, bf_des = orb.detectAndCompute(img1,None)
  kp2, frame_des = orb.detectAndCompute(frame,None)
  if(frame_des is not None):
    matches = bf.knnMatch(bf_des,frame_des,k=2)
    good = []
    for i, pair in enumerate(matches):
      try:
          m, n = pair
          if m.distance < 0.5*n.distance:
              good.append(m)
      except ValueError:
          pass
    print(len(good))
    #matches = sorted(matches, key = lambda x:x.distance)
# Draw first 10 matches.
    img3 = cv2.drawMatches(img1,kp1,frame,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv2.imshow("w", img3)
    cv2.waitKey()
    if(len(good) >= 30):
      #Treba da se posalje da je buy runda pocela
      print("Pheonix")
      return False
  return True

def check_buy_phase(frame, orb, bf, bf_des):
  frame = crop_buy_phase(frame)
  frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  kp2, frame_des = orb.detectAndCompute(frame,None)

  if(frame_des is not None):
    matches = bf.knnMatch(bf_des,frame_des,k=2)
    good = []
    for i, pair in enumerate(matches):
      try:
          m, n = pair
          if m.distance < 0.7*n.distance:
              good.append(m)
      except ValueError:
          pass
    print(len(good))
    if(len(good) >= 30):
      #Treba da se posalje da je buy runda pocela
      requests.post('http://localhost:8080/api/events/buyRound', json = Round().__dict__)
      return False
  return True

def buy_phase_detection_thread(queue):
  print("Buy phase detection thread starting....")
  #normal game
  #img1 = cv2.imread("BuyPhase.png", cv2.IMREAD_GRAYSCALE)
  #spike rush
  img1 = cv2.imread("spike_rush_bf.png", cv2.IMREAD_GRAYSCALE)
  

  orb = cv2.ORB_create()
  bf = cv2.BFMatcher()
  kp1, bf_des = orb.detectAndCompute(img1,None)
  #print(bf_des)
  should_loop = True
  while(should_loop):
    frame_time = queue.get()
    if (frame_time is None):
      break
    should_loop = check_buy_phase(frame_time.frame, orb,bf, bf_des)
    #print(should_loop)
  print("Buy phase detection thread ending....")

if __name__ == '__main__':
  #frame = cv2.imread("YoruFullScreen.png")
  #frame = crop_agent_abilities(frame)
  #cv2.imwrite("yoru_abilities.png", frame)
  frame = cv2.imread("pheonix_molly_only.png")
  detect_player_agent(frame)