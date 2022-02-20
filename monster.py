import random
from items import items
import random
from time import sleep

class Monster():

    # Constructor
    def __init__(self, monster_name):
        self.name = monster_name
        self.hp = 30
        self.iclass = random.choice(list(items))
        self.item = random.choice(list(items[self.iclass]))
    # Getters and setters
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def describe(self):
        print("[" + self.name +"] has " + str(self.hp) + "HP" + " holding " + "["+self.item+"]")
        sleep(1)

    def is_alive(self):
        return self.hp > 0

    def subtract_hp(self,hit_amount):
        self.hp = self.hp - hit_amount

    def attack(self, target):
        damage = random.choice([30, 20, 20, 10, 10, 10, 10, 10, 10, 10, 10])
        print(">>> " + self.name + " hits " + target.get_name() + " for " + str(damage) +"HP" + " using " + self.item)
        target.subtract_hp(damage)
    
