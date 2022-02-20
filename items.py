from monster import Monster

items = {
  "weapons":{
   "Rusty Sword":{
   "damage":15,
   "durability":2,
   },
   "Glass Shard":{
   "damage":25,
   "durability":1,
   },
   "Iron Axe":{
   "damage":20,
   "durability":3,
   }
   },
  "potions":{
   "Enrage Potion":{
     "damage":40,
     "durability":1
   },
   "Health Potion":{
     "damage":-40,
     "durability":1
   }
  }
}
class Item(Monster):
  def __init__ (self,item):
    self.item = item
    self.damage 
    self.durability
  def giveitem(self):
    
