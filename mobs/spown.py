import random
import sys
import os
current_path = os.path.dirname(os.path.abspath(__file__))
carpeta_paralela_path = os.path.join(current_path, '../')
sys.path.append(carpeta_paralela_path)

from core.Mob import Mob;
from GlobalData import world_mobs


def generate_random_location(point,size):
    
    start = point - size
    end = point + size

    x = random.uniform(start, end)
    y = random.uniform(start, end)
    return x, y

def generate_mob_in_area(areaId,quantity):
       for _ in range(quantity):
                x, y = generate_random_location(0,20)
                newMob = Mob(x, y, areaId)
                world_mobs[2][newMob.mobInternalId]=newMob

def check_world_quantityes(areaId,quantity):
       if( len(world_mobs[areaId]) < quantity ):
               generate_mob_in_area(areaId, quantity-len(world_mobs[areaId]))
               #print("now we have " + str(len(world_mobs[areaId])) + " mobs")


def StartSpowning():
        quantity = 5
        check_world_quantityes(2,quantity)

