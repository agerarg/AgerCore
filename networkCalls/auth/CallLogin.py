import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from MySQLConnector import *
from core.Player import *
from interfaces.ComType import ComType
from Util import *

class CallLogin(ComType):
    def data(jsonData,player):
        received_data = json.loads(jsonData)

        connector = MySQLConnector()

        connector.connect()
        
        user = remove_special_characters(received_data["username"]).lower()
        userpass = remove_special_characters(received_data["userpass"])

        query = "SELECT * FROM login WHERE username ='"+user+"' AND userpass='"+userpass+"' LIMIT 0,1"
        results = connector.execute_query(query)
        if results:
            for row in results:
                playerId = row[0]
                playerAccount = row[1]
                playerSelectedCharacter = row[4]
                #print("account "+playerAccount+" ("+format(playerSelectedCharacter)+") logged!")
                player.Loged(playerId,playerSelectedCharacter)
                response = "MSG"+CALL_DELIMITER+"LOGINOK"+CALL_DELIMITER+"OK"
                player.client_socket.sendall(response.encode())
        else:
            #print("wroing user or userpass")
            response = "ERROR"+CALL_DELIMITER+"LOGIN"+CALL_DELIMITER+"ERR"
            player.client_socket.sendall(response.encode())

        connector.close()

