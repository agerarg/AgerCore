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


def check_character_exists(conn, account_name):
        try:
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM characters WHERE name ='"+account_name+"'"
            cursor.execute(query)
            result = cursor.fetchone()[0]
            cursor.close()
            return result > 0

        except mysql.connector.Error as err:
            print("Error check_account_exists:", err)
            return False

def create_character(conn, name, idClass, idUser):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO characters (name,idClass,idUser) VALUES(%s,%s,%s)"
            values = (name, idClass, idUser)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            print("characters created!")

        except mysql.connector.Error as err:
            print("Error create_account:", err)


class CallCharacterCreate(ComType):
    def data(jsonData,player):
        
        if(not player.isLogged):
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOTLOGED"
            player.client_socket.sendall(response.encode())
            return
        
        received_data = json.loads(jsonData)

        dataName =   remove_special_characters(received_data['name'])
        idClass = int(received_data['idClass'])
        connector = MySQLConnector()

        connector.connect()

        if not check_character_exists(connector.conn, dataName):
            create_character(connector.conn,dataName,idClass, player.accountId)
            response = "MSG"+CALL_DELIMITER+"CREATECHARACTEROK"+CALL_DELIMITER+"OK"
            player.client_socket.sendall(response.encode())
        else:
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"CHARACTERALREADYEXIST"
            player.client_socket.sendall(response.encode())

        connector.close()
