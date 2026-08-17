import random
import Entity


class Player(Entity.Entity):
    role = ""
    blocking = False
    inventory = {}

    def __init__(self,role: str, level :int):
        self.role = role
        self.level = level
        self.behaviour = "player"

        if role == "knight":
            self.hp = 150
            self.attacker_damage = 100
        elif role == "mage":
            self.hp = 100
            self.attacker_damage = 50
        elif role == "adventurer":
            self.hp = 120
            self.attacker_damage = 70

    def toggle_block(self):
        self.blocking = True

    def inflict(self,incoming_damage):
        if self.hp-incoming_damage <= 0:
            print("You have died")
            self.is_dead = True
        elif not self.blocking:
            self.hp -= incoming_damage
        else:
            self.blocking = False

    def action_handler(self,player_input: int,enemy):
        if player_input == 1:
            odds = random.randint(0,1)
            if(odds):
                self.attack(enemy)
            else:
                print("You swung your weapon with all your might. But your strike failed to find its target")


