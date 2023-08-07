class Player:
  def __init__(self, socket, address):
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
    self.class_id = 0

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

  def CharacterEnter(self,characterId,name,level,exp,expLimit,class_id):
    self.characterId = characterId
    self.name = name
    self.level = level
    self.exp = exp
    self.expLimit = expLimit
    self.class_id = class_id
    self.isCharacterEntered=True
    #print( f"{self.characterId} {self.name} {self.level} {self.exp} {self.expLimit} {self.class_id}"  )

    

