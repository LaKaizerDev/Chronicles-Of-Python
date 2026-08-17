import Entity

class Enemy(Entity.Entity):
    enemy_type = ""
    attacker_damage = 20

    def __init__(self,level: int,hp: int):
        super().__init__(level,hp)
        self.class_name = "enemy"
        self.behaviour = "hostile"

    def damage_calculator(self,incoming_damage: int) -> float:
        damage_modifier = self.level/10
        final_damage = damage_modifier * incoming_damage
        return final_damage

    def inflict(self,incoming_damage):
        final_damage = self.damage_calculator(incoming_damage)
        if self.hp-final_damage <= 0:
            self.is_dead = True
        else:
            self.hp -= final_damage

    def attack(self,defender):
        effective_attack_damage = 20
        defender.inflict(effective_attack_damage) #hardcoded for now



class Orc(Enemy):

    def __init__(self, level: int,hp: int):
        super().__init__(level,hp)
        self.enemy_type = "Orc"

    def attack(self,defender):
        super().attack(defender)
        print("The Orc uses all his strength to swing his axe with pure fury")

class dark_mage(Enemy):

    def __init__(self, level: int,hp: int):
        super().__init__(level,hp)
        self.enemy_type = "Dark Mage"

    def attack(self,defender):
        super().attack(defender)
        print("The dark mage casts a blazing fireball at you, inflicting heavy magical fire damage.")

class dragon(Enemy):

    def __init__(self, level: int,hp: int):
        super().__init__(level,hp)
        self.behaviour = "boss"
        self.enemy_type = "Dragon"
        self.attacker_damage = 100

    def attack(self,defender):
        super().attack(defender)
        print("A blinding wave of fire sweeps across the battlefield.")


