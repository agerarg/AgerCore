import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from interfaces.ComType import ComType


class CallMsg(ComType):
    def data(jsonData,player):
        received_data = json.loads(jsonData)
        print("Json data:"+received_data["message"])
        response = "MSG"+CALL_DELIMITER+"TXT"+CALL_DELIMITER+"Hello from the server! You send: "+received_data["message"]
        player.client_socket.sendall(response.encode())