import EnemiesClasses
import Player
import GameMasterMethods
from Enums import Turn, PlayerBattleAction
import BattleManager
import time

def PrintSlow(word):
    for i in word:
        print(i, flush=True,end="")
        time.sleep(.05)
    print(" ")



enemy = GameMasterMethods.random_enemy_creator()
player = Player.Player("knight",10)


PrintSlow(f"A {enemy.enemy_type} stands ahead of you. What will you do?")


BattleManager.battle(player,enemy)

