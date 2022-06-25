from random import randint, getrandbits
import time
import requests
import json
class Game:
  def __init__(self, myAgent, myTeam , enemyTeam) -> None:
      self.myAgent = myAgent
      self.myTeam = myTeam 
      self.enemyTeam = enemyTeam


class KillEvent:
  def __init__(self, killer, isKillAlly, defeated, isDefeatAlly, weapon, isHeadshot, time) -> None:
      self.killer = killer
      self.isKillAlly = isKillAlly
      self.defeated = defeated
      self.isDefeatAlly = isDefeatAlly
      self.weapon = weapon
      self.isHeadshot = isHeadshot
      self.time = time


class EndRound:
  def __init__(self) -> None:
      pass


class Round:
  def __init__(self) -> None:
      pass
  
  

def create_team(all_agents):
    selectedAgents = []
    team = []
    i = 0
    while i < 5:
        index = randint(0,len(all_agents)-1)
        if index not in selectedAgents:
            team.append(all_agents[index])
            selectedAgents.append(index)
            i = i + 1
    return team

def create_my_agent(my_team):
     index = randint(0,4)
     return my_team[index]

def create_kill_event(my_team, enemy_team, all_weapons, time):
    #print("a")
    teams = [my_team, enemy_team]
    t = []
    killer_team_index = randint(0,1)
    
    if(killer_team_index == 0):
        
        killer = my_team[randint(0, len(my_team)-1)]
        defeated = enemy_team[randint(0, len(enemy_team)-1)]
        weapon = all_weapons[randint(0,len(all_weapons) - 1)]
        isHeadshot = bool(getrandbits(1))
        
        enemy_team.remove(defeated)
        
        kill_event = KillEvent(killer=killer, isKillAlly=True,defeated=defeated,isDefeatAlly=False, weapon=weapon, isHeadshot=isHeadshot, time=time)
        
        return my_team, enemy_team, kill_event
    
    
    else:  
        killer = enemy_team[randint(0, len(enemy_team)-1)]
        defeated = my_team[randint(0, len(my_team)-1)]
        weapon = all_weapons[randint(0,len(all_weapons) - 1)]
        isHeadshot = bool(getrandbits(1))        
        kill_event = KillEvent(killer=killer, isKillAlly=False,defeated=defeated,isDefeatAlly=True, weapon=weapon, isHeadshot=isHeadshot, time=time)
        my_team.remove(defeated)

        return my_team, enemy_team, kill_event
    

def simulate_game_from_script(fileName):
    f = open("client_siulator/simulations/" + fileName)
    data = json.load(f)
    i = True
    for d in data:
        time.sleep(0.5)
        if(i):
            requests.post('http://localhost:8080/api/events/game', json =d)
            time.sleep(1)
            requests.post('http://localhost:8080/api/events/buyRound', json =Round().__dict__)
            time.sleep(1)
            i = False
        else:
            requests.post('http://localhost:8080/api/events/postKill', json = d)
            
        


    
    

def simulate_game():
    
    all_agents = ["brimstone", "viper", "omen", "killjoy", "cypher", "sova", "sage", "pheonix", "jett",
              "reyna", "raze", "breach", "skye", "yoru", "astra", "kay/o", "chamber", "neon", "fade"]

    all_weapons = ["classic", "shorty", "frenzy", "ghost", "sheriff", "stinger", "spectre", "bucky", "judge", 
               "bulldog", "guardian", "phantom", "vandal", "marshal", "operator", "ares", "odin", "knife"]
    
    start_time = time.time()
    my_team = create_team(all_agents=all_agents)    
    my_agent = create_my_agent(my_team=my_team)
    enemy_team = create_team(all_agents=all_agents)   
    game = Game(myAgent=my_agent, myTeam=my_team.copy(), enemyTeam=enemy_team.copy())
    #send Game object - ima teams i my agent
    requests.post('http://localhost:8080/api/events/game', json =game.__dict__)
    print(game.__dict__)
    while True:
    
        requests.post('http://localhost:8080/api/events/buyRound', json =Round().__dict__)
        #print("Round started")
        #print("My agent " + my_agent)
        #print("My Team ",my_team)
        #print("Enemy Team ",enemy_team)
        #print(enemy_team)
        time.sleep(2)
        while True:
            
            #send round
            #wait 2 second
            
            
            my_team, enemy_team, kill_event = create_kill_event(my_team, enemy_team, all_weapons, time.time() - start_time)
           # print()
            print(kill_event.__dict__)
            requests.post('http://localhost:8080/api/events/postKill', json = kill_event.__dict__)
           # print("My Team ",my_team)
           # print("Enemy Team ",enemy_team)
            if(len(my_team) == 0 or len(enemy_team) == 0):
                break
            #send a kill every 0.5 seconds
            time.sleep(0.5)
        print("Round over")
            #if one team is empty
            #end round - mozda u droolsu mozda ovako
        
        enemy_team = game.enemyTeam
        my_team = game.myTeam
        print(enemy_team)
        print(my_team)
        break
#simulate_game()
simulate_game_from_script("sim1.json")



        


