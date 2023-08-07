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

def check_account_exists(conn, account_name):
        try:
            cursor = conn.cursor()
            query = "SELECT COUNT(*) FROM users WHERE username ='"+account_name+"'"
            cursor.execute(query)
            result = cursor.fetchone()[0]
            cursor.close()
            return result > 0

        except mysql.connector.Error as err:
            print("Error check_account_exists:", err)
            return False

def create_account(conn, username, password, email):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO users (username,password,email) VALUES(%s,%s,%s)"
            values = (username, password, email)
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            print("account created!")

        except mysql.connector.Error as err:
            print("Error create_account:", err)


class CallRegister(ComType):
    def data(jsonData,player):
        received_data = json.loads(jsonData)

        connector = MySQLConnector()

        connector.connect()
        
        user = remove_special_characters(received_data["username"]).lower()
        password = remove_special_characters(received_data["password"])

        if(is_valid_email(received_data["mail"])):
            mail = received_data["mail"]
        else:
            response = "ERROR"+CALL_DELIMITER+"REGISTER"+CALL_DELIMITER+"INVALIDMAIL"
            player.client_socket.sendall(response.encode())
            connector.close()
            return

        if not check_account_exists(connector.conn, user):
            create_account(connector.conn,user,password,mail)
            response = "MSG"+CALL_DELIMITER+"REGISTEROK"+CALL_DELIMITER+"OK"
            player.client_socket.sendall(response.encode())
        else:
            response = "ERROR"+CALL_DELIMITER+"REGISTER"+CALL_DELIMITER+"USERNAMEALREADYEXIST"
            player.client_socket.sendall(response.encode())

        connector.close()

    