from monster import Monster
from items import items
import random
import random

class Defender(Monster):
    def __init__(self, monster_name):
      super().__init__(monster_name)
      self.hp = 40
      self.defending = False
        # Add the code here to create an object of the superclass
        

    # Remove the triple quotes at top and bottom to uncomment this method
    def defend(self):
       self.defending = True

    def subtract_hp(self, hit_amount):
      if self.defending:
        if not(self.hp<20):
          defended = random.randint(0,hit_amount)
          print(f"Defended {defended} of damage!")
        self.defending = False 
        self.hp = self.hp- hit_amount
