import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from core.Player import *
from Util import *
from GlobalData import connected_clients
from interfaces.ComType import ComType

class CallDisconnected(ComType):
    def data(jsonData,player):
        for client in connected_clients:
            c = connected_clients[client]
           #if(c.mapId == player.mapId and c.characterId != player.characterId):
            msg = '{"id": "'+format(player.characterId)+'"}'
            response = "WORLD"+CALL_DELIMITER+"DISCONNECTED"+CALL_DELIMITER+msg
            send_message(c.client_socket,response)
