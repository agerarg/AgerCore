import sys
import os
import json
import pprint
current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from MySQLConnector import *
from core.Player import *
from Util import *
from GlobalData import connected_clients,world_mobs
from interfaces.ComType import ComType

def get_area_data(conn,areaId):
        query = "SELECT id, name, level, areaType FROM area WHERE id   ='"+format(areaId)+"'"
        results = conn.execute_query(query)
        response=""
        if results:
            for row in results:
                data = '{"id": "'+format(row[0])+'","name": "'+format(row[1])+'", "level": "'+format(row[2])+'", "areaType":  "'+format(row[3])+'"}'
                response += "WORLD"+CALL_DELIMITER+"DATA"+CALL_DELIMITER+""+data+CALL_MULTYLINE
            return response
        return ""

def get_all_players(areaId):
        response=""
        for socketId in connected_clients:
            if(connected_clients[socketId].mapId == areaId):
                playerMsg = '{"id": "'+format(connected_clients[socketId].characterId)+'", "name": "'+connected_clients[socketId].name+'", "idClass":  "'+format(connected_clients[socketId].idClass)+'", "positionX":  "'+format(connected_clients[socketId].mapPositionX)+'", "positionY":  "'+format(connected_clients[socketId].mapPositionY)+'"}'
                response += "WORLD"+CALL_DELIMITER+"PLAYER"+CALL_DELIMITER+""+playerMsg+CALL_MULTYLINE
        return response

def hey_im_here_to_players(player,areaId):
        response=""
        for socketId in connected_clients:
            if(connected_clients[socketId].mapId == areaId):
                newPlayerMsg = '{"id": "'+format(player.characterId)+'", "name": "'+player.name+'", "idClass":  "'+format(player.idClass)+'", "positionX":  "'+format(player.mapPositionX)+'", "positionY":  "'+format(player.mapPositionY)+'"}'
                response = "WORLD"+CALL_DELIMITER+"PLAYER"+CALL_DELIMITER+""+newPlayerMsg+CALL_MULTYLINE
                connected_clients[socketId].client_socket.sendall(response.encode())

def get_all_mobs(player,areaId):
         for mobId in world_mobs[areaId]:
            mob = world_mobs[areaId][mobId]
            msg = '{"uniqueId": "'+format(mob.mobInternalId)+'","id": "'+format(mob.mobId)+'", "x": "'+format(mob.X)+'", "y":  "'+format(mob.Y)+'","life": "'+format(mob.life)+'","lifeLimit": "'+format(mob.lifeLimit)+'"}'
            response = "MOB"+CALL_DELIMITER+"NEW"+CALL_DELIMITER+msg
            send_message(player.client_socket,response)

class CallEnterArea(ComType):
    def data(jsonData,player):
        
        if(not player.isLogged):
            response = "ERROR"+CALL_DELIMITER+"CHARACTER"+CALL_DELIMITER+"NOTLOGED"
            player.client_socket.sendall(response.encode())
            return
        
        received_data = json.loads(jsonData)
        areaId = int(received_data['area'])

        player.mapId = areaId
        player.MovePlayerToArea(player.mapId)

        connector = MySQLConnector()
        connector.connect()

        response = get_area_data(connector,areaId)
        if(areaId>0):
            #Load all mobs in this location
             get_all_mobs(player,areaId)
            #Load all players in this location
             response += get_all_players(areaId)
            #Tell all players in this area that you join in
             hey_im_here_to_players(player,areaId)
             player.client_socket.sendall(response.encode())

        

