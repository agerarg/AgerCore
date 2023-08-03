import sys
import os

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from networkCalls.CallMsg import CallMsg

from networkCalls.auth.CallLogin import CallLogin
from networkCalls.auth.CallRegister import CallRegister

from networkCalls.character.CallCharactersList import CallCharactersList
from networkCalls.character.CallCharacterCreate import CallCharacterCreate
from networkCalls.character.CallCharacterEnter import CallCharacterEnter


from networkCalls.world.CallMovement import CallMovement
from networkCalls.world.CallEnterArea  import CallEnterArea
from networkCalls.world.CallDisconnected import CallDisconnected
callList={}

callList['CallMsg'] = CallMsg
callList['CallLogin']= CallLogin
callList['CallRegister']=CallRegister

callList['CallCharactersList']=CallCharactersList
callList['CallCharacterCreate']=CallCharacterCreate
callList['CallCharacterEnter']=CallCharacterEnter


callList['CallMovement']=CallMovement
callList['CallEnterArea']=CallEnterArea

callList['CallDisconnected']=CallDisconnected



