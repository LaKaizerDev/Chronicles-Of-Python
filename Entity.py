class Entity:
    hp = 0
    class_name = ""
    behaviour = ""
    is_dead = False
    level = 0
    attacker_damage = 0

    def __init__(self,level: int,hp :int):
        self.level = level
        self.hp = hp

    def printEverything(self): #For debugging
        print(self.class_name)
        print(self.level)
        print(self.hp)
        print(self.behaviour)
        print(self.is_dead)

    def attack(self,defender):
        defender.inflict(self.attacker_damage)#Temp hardcoding, will change this later
