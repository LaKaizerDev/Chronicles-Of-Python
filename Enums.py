from enum import Enum,auto

class Turn(Enum):
    PLAYER = auto()
    ENEMY = auto()

class PlayerBattleAction(Enum):
    ATTACK = 1
    HEAL = 2
    BLOCK = 3
