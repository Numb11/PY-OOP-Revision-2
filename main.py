from monster import Monster
from defender import Defender
from attack import Attacker
from items import items
import random
#Choosing Item

# Create monsters
player_name = input("What is your Player called?")
you = Defender(player_name)
bad_guy = Attacker("Doombeast")

# Describe the HP of both players
you.describe()
bad_guy.describe()

# Continue while both players are alive
while you.is_alive() and bad_guy.is_alive():
    if you.item == "Health Potion":
      you.hp += 40
      you.iclass = "weapon"
      you.item = "Rusty Sword"
    elif you.item == "Enrage Potion":
     you.defender.enrage()
    elif bad_guy.item == "Health Potion":
     bad_guy.hp += 40
     bad_guy.iclass = "weapon"
     bad_guy.item = "Rusty Sword"
    elif bad_guy.item == "Enrage Potion":
     bad_guy.enrage()
    attack = input("Attack or Defend?").lower()
    if attack.count("a") == 2:
        if not you.is_alive():
            print("You lost :(")
            break
        else:
            you.attack(bad_guy)
    elif attack[0] == "d":
      if not you.is_alive():
            print("You lost :(")
            break
      else:
        you.defend()
    else:
        pass

    if attack.count("a") == 2 or attack[0] == "d":
        # Monster's turn
        if bad_guy.is_alive():
            if random.randint(1,3) == 1:
                bad_guy.enrage()
            bad_guy.attack(you)
            you.describe()

            # Is the player now dead?

            # Describe the outcome
            bad_guy.describe()
if not you.is_alive():
     print("You lost :(")
if not bad_guy.is_alive():
            print("You win!")
