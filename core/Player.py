import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from GlobalData import world_clients
PLAYER_ID = 0
class Player:
  def __init__(self, socket, address):
    global PLAYER_ID
    PLAYER_ID+=1
    self.internalPlayerId = PLAYER_ID
    self.isLogged = False
    self.accountId = 0
    self.isCharacterSelected=False
    self.selectedCharacterId = 0

    self.isCharacterEntered=False
    self.characterId=0
    self.name=""
    self.level = 0
    self.exp = 0
    self.expLimit = 0
    self.idClass = 0

    self.mapId = 0
    self.mapPositionX = 0
    self.mapPositionY = 0

    self.client_socket = socket
    self.client_address = address

  def Loged(self,acccountId,selectedCharacterId):
   self.isLogged = True
   self.accountId = acccountId
   self.selectedCharacterId = selectedCharacterId
  # print("loged! ".format(acccountId))

  def SetMapLocation(self,mapId,X,Y):
     self.mapId = mapId
     self.mapPositionX = X
     self.mapPositionY = Y

  def MovePlayerToArea(self,mapId):
     self.RemovePlayerFromAreas()
     #add player to area for easy search
     world_clients[mapId][self]=self

  def CharacterEnter(self,characterId,name,level,exp,expLimit,idClass):
    self.characterId = characterId
    self.name = name
    self.level = level
    self.exp = exp
    self.expLimit = expLimit
    self.idClass = idClass
    self.isCharacterEntered=True
    #print( f"{self.characterId} {self.name} {self.level} {self.exp} {self.expLimit} {self.idClass}"  )

  def RemovePlayerFromAreas(self):
    #remove player from all posible areas
    for area in world_clients:
       try:
            if self in area:
             del area[self]
       finally:
        pass
    
  def OnDelete(self):
    self.RemovePlayerFromAreas()
      
