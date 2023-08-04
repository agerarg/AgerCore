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



class CallCharactersList(ComType):
    def data(jsonData,player):
        
        if(not player.isLogged):
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOTLOGED"
            player.client_socket.sendall(response.encode())
            return
        
        connector = MySQLConnector()

        connector.connect()

        query = "SELECT id,name,level,class_id FROM characters WHERE account_id  ='"+format(player.accountId)+"'"
        results = connector.execute_query(query)
        response=""
        if results:
            for row in results:
                character = '{"id": "'+format(row[0])+'", "name": "'+format(row[1])+'", "level":  "'+format(row[2])+'", "class_id": "'+format(row[3])+'"}'
                response += "MSG"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"LIST"+CALL_DELIMITER+""+character+CALL_MULTYLINE
                
            response += "MSG#CHARACTER"+CALL_DELIMITER+"SELECTED"+CALL_DELIMITER+format(player.selectedCharacterId)+CALL_MULTYLINE
            player.client_socket.sendall(response.encode())
            connector.close()
            return
        else:
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOCHARACTERS"
            player.client_socket.sendall(response.encode())

        connector.close()
