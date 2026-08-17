import EnemiesClasses
import random

def enemy_creator(enemy_type: str,level: int,hp: int) -> EnemiesClasses.Enemy:
    if enemy_type.lower() == "orc":
        return EnemiesClasses.Orc(level, hp)
    elif enemy_type.lower() == "dark_mage":
        return EnemiesClasses.dark_mage(level,hp)
    elif enemy_type.lower() == "dragon":
        return EnemiesClasses.dragon(level,hp)
    else:
        print("An error has occurred")
        return None

def random_enemy_creator():
    enemy_types = ["orc","dark_mage"]
    selected = random.choice(enemy_types)
    level = random.randint(1,10)
    hp = random.choice([100,50,70,60,65,55])
    enemy = enemy_creator(selected,level,hp)
    return enemy
