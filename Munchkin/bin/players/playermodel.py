"""
Class to build model players and assign new attributes associated with cards through gameplay.

Considerations:
    Player model
    Death
    New build
    save -- most likely shelve objects
    stats access

"""


from Munchkin.bin.all_cards.table import Table # most likely not used here (pos for cross talk bypassing circular
# import but may require for adding to player inventory and stats (note same card in engine will return here)
from Munchkin.bin.all_cards.treasure_cards.treasurecards import Treasure

from Munchkin.bin.players.playersetup import P_tools
import bin.GUI.gui_variables as gameVar




"""adding items to player"""
################### CHECKER (works)
# cards = Handler()
# x = cards.card.grabber() # to be called further up stream for sorting
# print("RETURNED VALUE:", x)
#####################

"""This is the player class. It will have all setting to configure players and modify attributes that are set to that
player. It will inherit from moncurse and treasure so that a player can add items to their attributes and modify
attributes based on action outcomes."""


##########################################################################
# Player attributes and methods
##########################################################################


# class Player_atribs:
#
#
#
#     @classmethod
#     def card_choice(cls, card):
#         """card options"""
#         print(card)
#         choice = input("Options:\n1: Store card\n2: Use card\n3: equip.\n>>> ")
#         while True:
#             if choice == "1":
#                 return 'store'
#             elif choice == "2":
#                 return 'use'
#             elif choice == "3":
#                 return 'equip'
#             elif choice == "q":
#                 print("Missed opportunity!")
#                 quit()
#             else:
#                 print("Type number!")
#                 continue


#####################################################################
# MAIN PLAYER CLASS
#####################################################################


class Player(P_tools):
    """Main player class"""

    def __init__(self, ref):
        self.ref = ref # simple form to keep track of players
        self.name = None
        self.sex = None
        self.level = 1 # win lvl 10, make changeable so edit score to win
        self.bonus = 0
        self.wallet = 0
        self.race = {'r1': True, 'r2': False} # string eval to True so will show
        self.klass = {'c1': True, 'c2': False}
        self.weapons = {"L_hand": None, "R_hand": None, "big": None, "special_1": None, "special_2": False}
        self.armor = {"headgear": None, "armor": None, "armor1": False, "armor2": False, "footgear": None,
                      "special_1": None, "special_2": False, "special_3": False}
        self.sack = [] # 5 max
        self.visible_cards = [] # will need to sort, simple branch on the return objs
        self.hireling = []
        self.undefined = [] # unclassified objects for all the things i want but dont know it
        self.alive = True
        self.longevity = 1 # counts cycles alive, if 0 player misses go

    def __repr__(self):
        """developer aid"""
        return f"\nPLAYER REF:{self.ref}\nName:{self.name}\nSex:{self.sex}\nLevel:{self.level}" \
               f"\nBonus:{self.bonus}\nWallet:{self.wallet}\n"

    # def __str__(self):
    #     """developer aid"""
    #     return f"\nPLAYER INFO:\nName:{self.name}\nSex:{self.sex}\nLevel:{self.level}" \
    #            f"\nBonus:{self.bonus}\nvisible_cards:{self.visible_cards}\n"

    def char_setup(self):
        """sets up name and sex when called"""
        na = P_tools.name() # method to set name
        self.name = na  # makes change to player
        xy = P_tools.sex()
        self.sex = xy

        if self.name == "The_Creator": # ................................................................... dev mode
            self.sex = "bob"
            self.bonus = 200
            self.wallet = 20000
            gameVar.StartVariables.player_gender = self.sex

        print(f"Your name is {self.name.title()} and you are {self.sex.title()}.")
        print("moving back to game_loop")
        # print(self.__repr__())


    def inventory(self): # GUI to take control
        """Presents options for player inventory and equipped items."""
        x = str(input("\nView player:\n1: Details\n2: Weapons & armour\n3: Sack\nQ: exit\n>>>  "))
        """About self"""
        if x == "1":
            print(f"Name:{self.name}\nSex:{self.sex.title()}\nLevel:{self.level}\nBonus:{self.bonus}"
                  f"\nWallet:{self.wallet}")
            for key1, value1 in self.race.items():
                if value1: # will show other val when string (Good)
                    print('Race:', value1)
                else:
                    continue
            for key2, value2 in self.klass.items():
                if value2:
                    print('Class:', value2)
                else:
                    continue
            Player.inventory(self)

            """equipped armor and weapons"""
        elif x == "2":
            for key3, value3 in self.weapons.items():
                print(key3.title(), ':', value3) # to equip items call method
            for key4, value4 in self.armor.items():
                print(key4.title(), ':', value4)
            Player.inventory(self) # ################ another method to change inventory/sell items

            "Player sack"
        elif x == "3":
            # method for removal, sell, equip, gift
            print("You are carrying:")
            for val, contents in enumerate(self.sack, start=1):
                print(f"{val}: {contents['name']}, "
                      f"Level:{contents.get('lvl')}, Bonus:{contents.get('bonus')}") # print card objects in sack
            pick = input("Choose card\n>>>")
            if pick:
                print(f"picked {self.sack[int(pick) - 1]['name']}")
                card = self.sack[int(pick) - 1]
                n = P_tools.card_options(self, card)
            if n == "back":
                Player.inventory(self)



            Player.inventory(self) #up menu
            "Dev mode"
        elif x == "007": # ................................................................................. dev mode
            cheat = int(input("Select bonus level"))
            self.bonus = cheat
            Player.inventory(self)
        else:
            return f"leaving {self.name}'s player info"

    # def card_handler(self, obj):
    #     """handles cards handled from the engine class"""
    #     pass

    # def get_treasure(self):
    #     """calls Treasure card dict template for wins"""
    #     cards = Handler() # create instance for handler
    #     x = cards.card.get_treasure() # instance calls card return method assigning obj to x
    #     print(f"Here is your card: {x}")
    #     y = Player_atribs.card_choice(x)
    #     if y == "store":
    #         if len(self.sack) <= 5:
    #             self.sack.append(x) # adds to players inventory
    #         else:
    #             Player_atribs.card_choice(x)
    #     elif y == "equip":
    #         print("equip it to be configured")
    #     elif y == "use":
    #         try:
    #             n = int(x['bonus']) + self.bonus
    #             self.bonus = int(n)
    #         except IndexError:
    #             print("could not add to bonus")

        # for key, value in x.items():
        #     if key == "des":
        #         v = value.split(" ")
        #         if 'wizards' in v and "only" in v:  # searches for wizards only item
        #             print("usable by wizards only dude!!")
                # print(v)

            # print(key.title(), ":", value)




p1 = Player(1) #passes reference (ref)
p2 = Player(2)
p3 = Player(3)
p4 = Player(4)
p5 = Player(5)
p6 = Player(6)
p7 = Player(7)
p8 = Player(8)
p9 = Player(9)
p10 = Player(10)
# p1.get_treasure()



if __name__ == '__main__':
    p1 = Player(1)
    print(p1)
    # p1.get_treasure() # duplicate val is print state from Handler class method (note is same: GOOD)
    # p1.char_setup() # calls player name/sex setup, to be called after player number select
    # p1.inventory() # shows inventory of new built char





