import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from core.Player import *
from Util import *
from GlobalData import world_clients
from interfaces.ComType import ComType

class CallSkill(ComType):
    def data(jsonData,player):

        received_data = json.loads(jsonData)

        targetId = int(received_data['mobTarget'])
        skillId = int(received_data['skillId'])
        damage = 5
        for playerInArea in world_clients[player.mapId]:
               msg = '{"fromId": "'+format(player.characterId)+'", "toMob": "'+format(targetId)+'", "skillId":  "'+format(skillId)+'", "damage":  "'+format(damage)+'"}'
               response = "SKILL"+CALL_DELIMITER+"USE"+CALL_DELIMITER+msg
               send_message(playerInArea.client_socket,response)