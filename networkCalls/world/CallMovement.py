import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from MySQLConnector import *
from core.Player import *
from Util import *
from GlobalData import connected_clients
from interfaces.ComType import ComType

class CallMovement(ComType):
    def data(jsonData,player):
        
        if(not player.isLogged):
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOTLOGED"
            player.client_socket.sendall(response.encode())
            return
        
        received_data = json.loads(jsonData)

        player.mapPositionX = float(received_data['X'])
        player.mapPositionY = float(received_data['Y'])

        for client in connected_clients:
            c = connected_clients[client]
            if(c.mapId == player.mapId):
               msg = '{"id": "'+format(player.characterId)+'", "x": "'+format(player.mapPositionX)+'", "y":  "'+format(player.mapPositionY)+'"}'
               response = "WORLD"+CALL_DELIMITER+"MOVE"+CALL_DELIMITER+msg
               send_message(c.client_socket,response)
