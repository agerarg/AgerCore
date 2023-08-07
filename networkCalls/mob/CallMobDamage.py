import sys
import os
import json

current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from Init import *
from core.Player import *
from Util import *
from GlobalData import world_mobs
from interfaces.ComType import ComType

class CallMobDamage(ComType):
    def data(jsonData,player):

        received_data = json.loads(jsonData)

        mobId = int(received_data['mobId'])
        damage = int(received_data['damage'])
       
        mob = world_mobs[player.mapId][mobId]

        mob.Damage(damage)
