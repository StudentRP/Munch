"""This is the player class. It will have all setting to configure players and modify attributes that are set to that
player. It will inherit from moncurse and treasure so that a player can add items to their attributes and modify
attributes based on action outcomes."""


from treasure_v3 import Treasure, T_tools
from moncurse import Moncurs


class P_tools():
    """Tools associated to the player class"""
    @classmethod
    def sex(cls):
        """Sets sex"""
        x = str(input("Please choose a sex: 1 = Male, 2 = Female.\n>>> "))
        if x == '1':
            y = input("You have chosen Male. Is this correct?\n>>> ")
            if y.lower() == "y" or y.lower() == "yes" or y.lower() == "":
                return str("male")
            else:
                P_tools.sex()
        elif x == '2':
            y = input("you have chosen Female. Is this correct?\n>>> ")
            if y.lower() == "y" or y.lower() == "yes" or y.lower() == "":
                return str("female")
            else:
                P_tools.sex()

    @classmethod
    def name(cls):
        """Sets name"""
        x = input("What is your name?\n>>>")
        print(f"Thank you {x.title()}")
        if x == "ninja":
            y = "The_Creator"
            return y
        return x.title()

    @classmethod
    def card_choice(cls, card):
        """card options"""
        print(card)
        choice = input("Options:\n1: Store card\n2: Use card\n3: equip.\n>>> ")
        while True:
            if choice == "1":
                return 'store'
            elif choice == "2":
                return 'use'
            elif choice == "3":
                return 'equip'
            elif choice == "q":
                print("Missed opportunity!")
                quit()
            else:
                print("Type number!")
                continue


#####################################################################
# MAIN PLAYER CLASS
#####################################################################


class Player(P_tools, Treasure):
    """Main player class"""

    def __init__(self):
        self.name = None
        self.sex = None
        self.level = 1
        self.bonus = 0
        self.wallet = 0
        self.race = {'r1': None, 'r2': False}
        self.clss = {'c1': None, 'c2': False}
        self.weapons = {"L_hand": None, "R_hand": None, "big": None, "special_1": None, "special_2": False}
        self.armour = {"headgear": None, "armour": None, "knees": None, "legs": None, "footgear": None,
                       "special_1": None, "special_2": False, "special_3": False}
        self.sack = [] #5 max
        self.hireling = []
        self.undefined = [] # unclassified objects


    def char_setup(self):
        """sets up name and sex when called"""
        na = P_tools.name()
        self.name = na
        xy = P_tools.sex()
        self.sex = xy
        if self.name == "The_Creator":
            self.sex = "bob"
            self.bonus = 200
            self.wallet = 20000


    def inventory(self):
        x = str(input("\nView player:\n1: Details\n2: Weapons & armour\n3: Sack,\nQ: exit\n>>> \n"))
        if x == "1":
            print(f"Name:{self.name}\nSex:{self.sex.title()}\nLevel:{self.level}\nBonus:{self.bonus}"
                  f"\nWallet:{self.wallet}")
            for key1, value1 in self.race.items():
                print('Race:', value1)
            for key2, value2 in self.clss.items():
                print('Class:', value2)
            Player.inventory(self)
        elif x == "2":
            for key3, value3 in self.weapons.items():
                print(key3.title(), ':', value3)
            for key4, value4 in self.armour.items():
                print(key4.title(), ':', value4)
            Player.inventory(self)
        elif x == "3":
            print(self.sack)
            Player.inventory(self)
        elif x == "007":
            cheat = int(input("Select bonus level"))
            self.bonus = cheat
            Player.inventory(self)
        else:
            print(f"leaving {self.name}'s player info")



    def get_treasure(self):
        """calls Treasure card dict template"""
        x = self.card_return()# instance calls card return method assigning obj to x
        print(f"Here is your card: {x}")
        y = P_tools.card_choice(x)
        if y == "store":
            if len(self.sack) <= 5:
                self.sack.append(x)
            else:
                P_tools.card_choice(x)
        elif y == "equip":
            print("equip it to be configured")
        elif y == "use":
            try:
                n = int(x['bonus']) + self.bonus
                self.bonus = int(n)
            except IndexError:
                print("could not add to bonus")


        # for key, value in x.items():
        #     if key == "des":
        #         v = value.split(" ")
        #         if 'wizards' in v and "only" in v:  # searches for wizards only item
        #             print("usable by wizards only dude!!")
                # print(v)

            # print(key.title(), ":", value)


    def __repr__(self):
        """user friendly printout"""
        return f"Name:{self.name}\nSex:{self.sex}\nLevel:{self.level}\nBonus:{self.bonus}\nWallet:{self.wallet}"



p1 = Player()
p2 = Player()



c1 = Treasure()  # instance from Treasure class
# m1 = Moncurs()

# p1.card_call() # with instance i can access method directly of parent


if __name__ == '__main__':

    """checks card migration from treasure"""
    d = c1.card_return() # encapsulated for self attribute returns raw card, self can be any instance
    Treasure.specific(c1)
    Treasure.formated() # returns formatted card as expected data from Treasure class.
    """checks player setup"""
    # p1.char_setup()
    # print(p1.name)
    # print(p1.sex.title())
    """inventory check"""
    # p1.char_setup()
    # p2.char_setup()
    # p1.inventory()
    # p2.inventory()
    """Creator check"""
    #print(p1.sex, p1.name, p1.wallet, p1.bonus)
    """change specific item"""
    # print(p1.weapons["R_hand"])
    # p1.weapons["R_hand"] = "toothpick"
    # print(p1.weapons["R_hand"])
    """add card to sack"""
    # print(p1.sack)
    # x = p1.card_return()
    # p1.sack.append(x) #note can also append burn_card list from here
    # print(p1.sack)
    """equip card"""
    # print(p1.bonus, p1.sack)
    # p1.get_treasure()
    # print(p1.bonus, p1.sack)
    # print(p1.card_return())
    # print(p1) # for __repr__ funct call, changes print from object to more user friendly output





    # p1.card_call()  # calls card from Treasure