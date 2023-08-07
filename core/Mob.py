from Init import *
from Util import *
from GlobalData import world_clients,world_mobs

MOB_ID = 0

class Mob:
  def __init__(self, X,Y,areaId):
    global MOB_ID
    self.mobInternalId = MOB_ID
    MOB_ID+=1
    self.mobId = 1
    self.X = X
    self.Y = Y
    self.areaId = areaId
    self.life = 10
    self.lifeLimit = 10
    self.exp = 1
    
    for playerInArea in world_clients[areaId]:
            msg = '{"uniqueId": "'+format(self.mobInternalId)+'","id": "'+format(self.mobId)+'", "x": "'+format(self.X)+'", "y":  "'+format(self.Y)+'","life": "'+format(self.life)+'","lifeLimit": "'+format(self.lifeLimit)+'"}'
            response = "MOB"+CALL_DELIMITER+"NEW"+CALL_DELIMITER+msg
            send_message(playerInArea.client_socket,response)

  def Damage(self, dmg):
    self.life -= dmg
    if(self.life<=0):
      del world_mobs[self.areaId][self.mobInternalId]
      for playerInArea in world_clients[self.areaId]:
              msg = '{"id": "'+format(self.mobInternalId)+'"}'
              response = "MOB"+CALL_DELIMITER+"DEAD"+CALL_DELIMITER+msg
              send_message(playerInArea.client_socket,response)
