"""Trial for top level programing"""

import munch_v3 as mv3

"""this will not run till it works through the script"""
print(mv3.__doc__)
print(dir(mv3))

from sys import exit
import random

dice_roll = [1, 2, 3, 4, 5, 6]

random.choice(dice_roll)
#print(random.choice(dice_roll))


class Weapons:
    """ A class detailing all weapons"""


    def __init__(self, level, effects):
        self.level = level
        self.effects = effects

    #def axe(self):




class Player:

    """The attributes for any given player"""

    def __init__(self, level, race, sex, classes, head, armour, knees, feet, hands):
        self.level = level
        self.race = race
        self.sex = sex
        self.classes = classes
        self.head = head
        self.armour = armour
        self.knees = knees
        self.feet = feet
        self.hands = hands
        self.weapons = None
        self.item = None
        self.curses = None
        self.effect = None
        self.run = True

    def my_stats(self):
        print(f"\nYou are a level {self.level}, {self.race}, {self.sex} and have {self.classes}.")
        print(f"\nYou are wearing:\nHead: {self.head} \nArmour: {self.armour} \nKnees: {self.knees}"
              f"\nFeet: {self.feet}\nHands: {self.hands}")
        print(f"Weapons: {self.weapons} \nItems: {self.item}.")
        print(f"Curses {self.curses}.")

    def death(self):
        if self.level <= 1:
            reborn = input("You have been killed. Do you want to be reborn? Y or N: ")
            if reborn == "y" or reborn == "yes":
                return new_player.my_stats()

            else:
                exit()


    def add_lev(self, addlev):
        """adds a level on winning fight"""
        self.level += addlev

    def loose_lev(self, looselev):
        """removes a level"""
        self.level -= looselev






new_player = Player(1, 'Human', 'male', 'no class', 'no head gear', 'no armour', 'no knees protection',
                    'nothing on feet', 'nothing on hands')





#new_player.add_lev(1)
#new_player.loose_lev(1)
#print("you are now level", new_player.level)

#print(new_player.death())
print(new_player.my_stats())

####################################
from sys import exit
#import engine



win = False

class Player:

    """The attributes for any given player"""

    def __init__(self, level, race, classes, items, curses):
        self.level = level
        self.race = race
        self.classes = classes
        self.item = items
        self.curses = curses


    def death(self):
        if self.level == 0:
            print("You have been killed. Do you want to be reborn?")
            reborn = (input("Y or N"))
            if reborn == "Y" or reborn == "yes":
                new_player

            else:
                exit


    def level_cal(self):
        if  not win:
            self.level += 1
            # add items from monster class (random) and add to  list
        elif win:
            bad_stuff()
        else:
            run_away()


#new_player = engine.name


new_player = Player(1, 'none', 'none', 'items', 'curses')


print(new_player.level)
################################
""" This is the engine that takes the basic player and modifies weapons, levels and items to create a new object with
the new attributes"""
import random


player = []
s_dice = {}


def num_of_players():
    num_players = input("How many players? ")
    if num_players == "1":
        print(" Sadly this game requires 2 players. :-(")
    elif num_players != "1":
        for number in range(0, int(num_players)):
            name = input("What is your name? ")
            player.append(str(name))
            print(f"{name.title()} you role the dice..")
            number = random.randint(1, 6)
            print(f"{name.title()} you rolled a {number}.")
            s_dice[name] = number

    else:
        print("that is an invalid entry!")
        #num_of_players()


num_of_players()

for person in player:
    print(person.title())

print(s_dice)
print(max(zip(s_dice.keys(), s_dice.values())))
print("Has the highest roll")