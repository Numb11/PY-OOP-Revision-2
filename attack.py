from monster import Monster
from defender import Defender
from items import items
import random
class Attacker(Monster):
    def __init__(self, monster_name):
      super().__init__(monster_name)
      self.enraged = False

        # Add the code here to create an object of the superclass
        

    # Remove the triple quotes at top and bottom to uncomment this method
    def enrage(self):
       self.enraged = True

    def attack(self, target):
      if self.enraged:
          hit_amount = random.randint(20,50)
          print(f">>> {self.name} hits {target.get_name()} enraged for {(hit_amount)} HP" )
          Monster.subtract_hp(target,hit_amount)
          self.enraged = False 
      else:
          damage = (items[self.iclass])[self.item]["damage"]
          print(">>> " + self.name + " hits " + target.get_name() + " for " + str(damage) +"HP" + " using " + self.item)
          target.subtract_hp(damage)
