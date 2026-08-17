
import EnemiesClasses
import Player
import GameMasterMethods
from Enums import Turn, PlayerBattleAction

def battle(player,enemy):

    battle_ongoing = True
    current_turn = Turn.PLAYER
    while (battle_ongoing):
        print(f" {enemy.enemy_type.title()} HP: {enemy.hp} | Player HP: {player.hp}")

        if enemy.is_dead or player.is_dead:
            battle_ongoing = False
            battle_victor = player if enemy.is_dead else enemy
            break

        if current_turn is Turn.PLAYER:
            print("Action list:")
            print("1) Attack enemy \n2) Heal \n3) Block")
            player_action = int(input("Please select your action:"))
            if player_action == 1:
                player.attack(enemy)
            elif player_action == 2:
                pass  # Need to finish coding the healing function for the player
            elif player_action == 3:
                player.toggle_block()
            current_turn = Turn.ENEMY

        elif current_turn is Turn.ENEMY:
            enemy.attack(player)
            current_turn = Turn.PLAYER

    if battle_victor == player:
        print("Congrats you won")
    elif battle_victor == enemy:
        print("Shame you lost")
    else:
        print("Something went wrong")
