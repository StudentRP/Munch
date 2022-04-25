""" Class to define all treasure cards"""

from random import randint


#x = randint(0, 6)


class T_tools:
    """ Specific methods for Treasure cards"""

    def test_meth(self, *args):
        print('In test T_tools meth expecting bonus change to 50')
        if "on" in args:
            print('Bonus changed')
            self.bonus += 50
        else:
            self.bonus -= -50

    def unknown(self, *args, **kwargs):
        print(f"Problem found in  Treasure method {args}, {kwargs}")

    def radioactive(self, *args):
        if "on" in args:
            print('using Radioactive meth')
            self.bonus += 5
            print(f"bonus changed to {self.bonus} increased by 5")
        elif "off" in args:
            print(self.bonus)
            self.bonus -= 5
            print(f"bonus changed to {self.bonus} decreased by 5")
        else:
            self.unknown("radioactive")



    method_types = {
        'radioactive': radioactive,

                    }
#####################################################################
# MAIN TREASURE CLASS
#####################################################################


class Treasure(T_tools):
    """Base class for treasure, required to hold all Treasure cards and return card/attribute objects to children"""

    burn_card = [] # The use-only-once pile that can not be reused

    stack = [] # Re-usable cards

    """ special methods associated to cards"""
    # special_list = {'once': T_tools.restriction, 'deflect': T_tools.deflect,
    #                 'immune': T_tools.immune}


    """General order: id, type, name, description, bonus, sell, special/restriction/, Dict to loop
    use only once, armour, weapons, 
    MAY NEED SOME FORM OF CATEGORY KEY FOR THE SORTER FUNCT REQUIRED WHEN DECIDING WHERE OR WHAT THE CARDS BELONG TOO.
     
    ALL items require bonus status
    """
    treasure_cards = [
        # type disposable #no 2 add!! #key ideas effects=['fire',]
        {"id": 1, "category": "treasure", "type": "disposable", "name": "Electric Radioactive Acid Potion", "sell": 200, "bonus":5, 'method': ['radioactive']},# need on off activation after play
        # {"id": 0, "category": "treasure", "type": "disposable", "name": "Magic Missile", "sell": 300, "bonus": 5},
        # {"id": 3, "category": "treasure", "type": "disposable", "name": "Flaming Poison Potion", "sell": 100, "bonus":3, "lexical": ["fire"]},
        # {"id": 0, "category": "treasure", "type": "disposable", "name": "Royal Oil", "sell": 100, "bonus": 3},
        # {"id": 0, "category": "treasure", "type": "disposable", "name": "Freezing Explosive Potion", "sell": 100, "bonus": 3, 'lexical': ['freeze']},
        # {"id": 4, "category": "treasure", "type": "disposable", 'name': "Instant Wall", 'sell': 300, 'method': ['auto_escape']},
        # {"id": 5, "category": "treasure", "type": "disposable", "name": "Flask Of Glue", "sell": 100, 'method': ["re-roll_escape"]},
        # {"id": 0, "category": "treasure", "type": "disposable", "name": "Tasty Pie", "sell": 100, 'bonus': 2, "method": 'tasty_pie'},

        #type armor/head, all should have: id, type, subtype, name, des, sell, bonus
        # {"id": 6, "category": "treasure", "name": "The Occasionally Reliable Amulet", "type": "armor", "sub_type": "necklace",
        #  'des': 'chance to deflect curse', 'sell': 600, 'special': "deflect", "bonus": 0},
        # {"id": 7, "category": "treasure", "name": "Tinfoil Hat", "type": "armor", "sub_type": "headgear",
        #  "des": "Immune to curses when  curses by kicking down doors still effect", "bonus": 0, "sell": 800, "special": "cast immune"},
        # {"id": 8, "category": "treasure", "name": "Pointy Hat Of Power", "type": "armor", "sub_type": "headgear", "des": "Usable by wizards only",
        #  "bonus": 3, "sell": 400, "klass_requirement": "wizard"},
        # {"id": 9, "category": "treasure", "name": "Helm Of Peripheral Vision", "type": "armor", "sub_type": "headgear",
        #  "des": "can not be back stabbed or stolen from by thief", "bonus": 2, "sell": 600, "special": "headgear",
        #  "restriction": "no backstab, no steal"},
        # {"id": 10, "category": "treasure", "name": "Badass Bandanna", "type": "armor", "sub_type": "headgear",
        #  "des": "Usable by humans only", "bonus": 3, "sell": 400, "race_requirement": "human"}, #humans only can use

        # armor/armor (complete set)
        #race_requirements= needs to be this, restriction = cant be this, or have this
        # {"id": 11, "category": "treasure", "name": "Short Wide Armour", "type": "armor", "sub_type": "armor", "bonus": 3, "sell": 400, "race_requirement": "dwarfs"},
        # {"id": 12, "category": "treasure", "name": "Raincoat", "type": "armor", "sub_type": "armor", "sell": 100, "special": "over armor",
        #  "restrictions": "loose with armour", "bonus": 0},
        # {"id": 13, "category": "treasure", "name": "Slimy Armour", "type": "armor", "sub_type": "armor", "bonus": 1, "sell": 200},
        {"id": 14, "category": "treasure", "name": "Mithril Armor", "type": "armor", "sub_type": "armor", "bonus": 3, "sell": 600, "restriction": ['big', 'wizard', 'human']},####not wizards
        # {"id": 15, "category": "treasure", "name": "Budget Armour", "type": "armor", "sub_type": "armor", "bonus": 1, "sell": 100},
        # {"id": 16, "category": "treasure", "name": "Flaming Armour", "type": "armor", "sub_type": "armor", "bonus": 2, "sell": 400},
        # {"id": 17, "category": "treasure", "name": "Spudded Leather Armor", "type": "armor", "sub_type": "armor", "bonus": 2, "sell": 400},
        # {"id": 18, "name": "Gnomex Suit", "type": "armor", "sub_type": "armor", "bonus": 4, "sell": 600,
        #  "special": "over armor", "restrictions": "loose with armour", "race_requirement": "gnome"},
        # {"id": 19, "category": "treasure", "name": "Chainmail Bikini", "type": "armor", "sub_type": "armor", "bonus": 3, "sell": 600},
        # {"id": 20, "category": "treasure", "name": "Leather Armor", "type": "armor", "sub_type": "armor", "bonus": 1, "sell": 200},
        #
        #
        # #armor/boots
        # {"id": 21, "category": "treasure", "type": "armor", "sub_type": "footgear", "name": "Boots Of Running Really Fast", "des": "run_away + 2",
        #  "bonus": 0, "sell": 400},

        #weapons: id, type, sub_type, name, des, bonus, klass_requirement, hold_weight, sell, asso_meth
        # {"id": 22, "category": "treasure", "name": "Staff Of Napalm", "type": "weapon", "sub_type": "1hand", "hold_weight": 1, "des": "Usable by wizards only",
        #  "bonus": 5, "sell": 800, "klass_requirement": "wizard"},
        # # {"id": 23, "name": "Blessed ", "type": "enhancer", "subtype": "start", "des": "Usable by wizards only", "bonus": 2,
        # #  "sell": 800, "klass_restriction": "wizard", meth_call:"enhancer"},
        # {"id": 24, "category": "treasure", "name": "Broad Sword", "type": "weapon", "sub_type": "1hand", "hold_weight": 1, "des": "Not for females",
        #  "bonus": 3, "sell": 400, "special": "", "klass_requirement": "male"},
        # {"id": 25, "category": "treasure", "name": "Sword Of Slaying Everything\nExcept squid..", "type": "weapon", "sub_type": "1hand",
        #  "hold_weight": 1,  "des": "long", "bonus": 4, "sell": 800},
        # {"id": 26, "category": "treasure", "name": "Vorpal Blade", "type": "weapon", "sub_type": "1hand", "hold_weight": 1, "des": "+10 with anything beginning with j",
        #  "bonus": 3, "sell": 400, "special": "item enhancer"},
        # {"id": 27, "category": "treasure", "name": "Huge Rock", "type": "weapon", "sub_type": "2hand", "hold_weight": 2, "bonus": 3, "sell": 0},
        # {"id": 28, "category": "treasure", "name": "Board of Education", "type": "weapon", "sub_type": "1hand", "hold_weight": 1, "bonus": 2, "sell": 500}
    ]
    
    @classmethod
    def __repr__(cls):
        return cls.treasure_cards[0]["name"]

#     def get_all(self):
#         """Gives all key/val associated to a specific card"""
#         for key, value in self.treasure_cards[x].items():
#             print(key, ":", value)
#
#     def specific(self):
#         """Directory to special/type methods and card main pack removal"""
#         for key, value in self.treasure_cards[x].items(): #searches for 'type' in dict
#             if key == "type" and value == "once" or value == 'escape':
#                 Treasure.burn_card.append(self.treasure_cards[x]) # adds current t_card to burn_cards list
#                 Treasure.special_list[value]() #value becomes key for special_list calling value method.
#                 del Treasure.treasure_cards[x] #del card from t_cards to stop reuse
#             elif key == 'special':
#                 try:
#                     Treasure.special_list[value]()
#                 except KeyError:
#                     print("This has not been configured for armour and weapons yet")
#                     #call method to sort this section out for wep and armour
#             else:
#                 pass
#
#     def card_return(self):
#         """Returns card to caller for sorting"""
#         print(f"T{self.treasure_cards[x]} card has been returned to the caller.")
#         c = self.treasure_cards[x]
#         return c
#         # return self.treasure_cards[x]
#
#     @classmethod
#     def formated(cls):
#         """provides liner view of card"""
#         for key, value in cls.treasure_cards[x].items():
#             print(key.title(), ':', value)
#
#     def set_card(self):
#         pass
#
#
#
# """reload import statement for random """
# y = int(len(Treasure.treasure_cards) - 1)
#
# x = randint(0, y)
#
# #instance
# c1 = Treasure() # instance object is the vessel that contains other objects
#
#
# """Ensures tests below only run when script is run directly and not when imported"""
# if __name__ == '__main__':
#     # print(f"Num of cards in pack: {y + 1}")
#     # print(c1.treasure_cards[x]['name'])
#     # """check to see card migration and removal"""
#     # #print(Treasure.treasure_cards) #prints all cards
#     # #print(c1.get_all())
#     # c1.specific()
#     # try:
#     #     print(f"The '{Treasure.burn_card[-1]['name']}' has been depleted.") #if added to burn list will show card
#     # except IndexError:
#     #     print(f"The '{c1.treasure_cards[x]['name']}' lives on!")
#     #
#     #
#     #
#     # '''all silenced or will run when child runs.... problem solved by top __name__ == '__main__' statement'''
#     # c1.card_return()# object to be sent to other classes need return statement
#     # # c1.specific() #print statement executed from top methods
#     # Treasure.formated() # card view test
#     import class_tree
#
#     class_tree.instancetree(c1)



"""
NOTES:

Use a lexicon scanner on des to determine action for player is 'wizards only', head gear,  ect. 
Set armour location (knees0)  under 'special', former under des,  """