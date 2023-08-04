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
from interfaces.ComType import ComType
from GlobalData import connected_clients


class CallCharacterEnter(ComType):
    def data(jsonData,player):
        
        if(not player.isLogged):
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOTLOGED"
            player.client_socket.sendall(response.encode())
            return
        
        connector = MySQLConnector()

        connector.connect()
        
        received_data = json.loads(jsonData)

        characterId = int(received_data['characterId'])

        query = "SELECT id,name,level,exp,expLimit, class_id, mapLocation, mapPositionX, mapPositionY FROM characters WHERE account_id  ='"+format(player.accountId)+"' AND id="+format(characterId)+" LIMIT 0,1"
        results = connector.execute_query(query)
        response=""
        if results:
            for row in results:
                character = '{"id": "'+format(row[0])+'", "name": "'+format(row[1])+'", "level":  "'+format(row[2])+'","exp":  "'+format(row[3])+'","expLimit":  "'+format(row[4])+'", "class_id": "'+format(row[5])+'", "mapLocation": "'+format(row[6])+'", "mapPositionX": "'+format(row[7])+'", "mapPositionY": "'+format(row[8])+'"}'
                response += "MSG"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"ENTER"+CALL_DELIMITER+""+character+CALL_MULTYLINE
                #check if you have already a character loged
                for client in connected_clients:
                    c = connected_clients[client]
                    if(c.accountId == player.accountId and c.client_socket != player.client_socket):
                         msg = "ERROR"+CALL_DELIMITER+"DISCONNECTED"
                         c.client_socket.sendall(msg.encode())

                player.CharacterEnter(row[0],row[1],row[2],row[3],row[4],row[5])
                player.SetMapLocation(row[6],row[7],row[8])
                
            player.client_socket.sendall(response.encode())
            connector.close()
            return
        else:
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOCHARACTERS"
            player.client_socket.sendall(response.encode())

        connector.close()