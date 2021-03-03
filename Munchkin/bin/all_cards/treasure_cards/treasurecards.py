""" Class to define all treasure cards"""

from random import randint


#x = randint(0, 6)


class T_tools:
    """ methods for special card objects """

    # @classmethod
    # def immune(cls):
    #     """immune to curses"""
    #     print("I love my Tinfoil Hat")

    @classmethod
    def restriction(cls): #maybe name restriction
        """kwrd search to determine restriction
        to add:
        once
        specific users
        with item
        any combat
        reroll escape
        no backstab
        no steal
        loose with armour
        big
        """
        print("This item has been depleted")

    @classmethod
    def special(cls, word, dictkeyname):
        """kwrd search to determine nature of special:
        escape
        auto escape
        fire
        cast immune
        deflect
        over armour
        gnome only
        """
        if word in dictkeyname:
            pass

    # @classmethod
    # def escape(cls):
    #     """roll to escape combat, may need: return once()"""
    #     print("You make a dash for it! This item has now been depleted")

    # @classmethod
    # def deflect(cls):
    #     """1-3 deflect curse, 4-6 run, 6 go up level"""
    #     print("The curse rebounds")

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
     
    
    """
    treasure_cards = [
        # type disposable
        {"type": "disposable", "id": 1, "name": "Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
         "bonus": 2, "sell": 200, 'restriction': ["once, any combat"]},
        {"type": "disposable", "id": 3, "name": "Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100,
         "special": "fire", 'restriction': ["once"]},
        {"type": "disposable", "id": 4, 'name': "Instant Wall", 'des': 'Automatic escape for 1 or 2 players', 'sell': 300,
         "special": "auto escape 2 players", 'restriction': ["once"]},
        {"type": "disposable", "id": 5, "name": "Flask Of Glue", "des": "Use during combat, must re-roll escape even if auto last time",
         "sell": 100, "special": "escape", 'restriction': ["once", "reroll escape"]},

        #type armor/headm
        {"id": 6, "type": "necklace", "name": "The Occasionally Reliable Amulet",
         'des': 'If equipped, chance to deflect curse', 'sell': 600, 'special': "deflect"},

        {"id": 7, "type": "headgear", "name": "Tinfoil Hat",
         "des": "Immune to curses, curses by kicking down doors still effect", "bonus": 0, "sell": 800,
         "special": "cast immune"},
        {"id": 8, "type": "headgear", "name": "Pointy Hat Of Power", "des": "Usable by wizards only",
         "bonus": 3, "sell": 400, "restriction": ["wizards only"]},
        {"id": 9, "type": "headgear", "name": "Helm Of Peripheral Vision",
         "des": "can not be back stabbed or stolen from by thief", "bonus": 2, "sell": 600, "special": "headgear",
         "restriction": ["no backstab", "no steal"]},
        {"id": 10, "type": "headgear", "name": "Badass Bandana",
         "des": "Usable by humans only", "bonus": 3, "sell": 400, "restriction": ["humans only"]},

        # armor/armor (complete set)
        {"id": 11, "type": "armor", "name": "Short Wide Armour", "des": "usable by dwarf only", "bonus": 3,
         "sell": 400, "restriction": ["dwarfs only"]},
        {"id": 12, "type": "armor", "name": "Raincoat",
         "des": "Others can not use potions to interfere with your combat unless joins fight.", "sell": 100,
         "special": "over armor", "restrictions": ["loose with armour"]},
        {"id": 13, "type": "armor", "name": "Slimy Armour", "des": "Found in a stagnant pool of water.",
         "bonus": 1, "sell": 200},
        {"id": 14, "type": "armor", "name": "Mithril Armor", "des": "Oooo Shiny!", "bonus": 3,
         "sell": 600, "restriction": ["big"]},
        {"id": 15, "type": "armor", "name": "Budget Armour", "des": "Get what you pay for..", "bonus": 1,
         "sell": 100},
        {"id": 16, "type": "armor", "name": "Flaming Armour", "des": " Its Really Hot!", "bonus": 2, "sell": 400},
        {"id": 17, "type": "armor", "name": "Spudded Leather Armor", "des": "When best no available",
         "bonus": 2, "sell": 400},
        {"id": 18, "type": "armor", "name": "Gnomex Suit", "des": "Usable by Gnome only", "bonus": 4, "sell": 600,
         "special": "over armor", "restrictions": ["loose with armour", "gnome only"]},
        {"id": 19, "type": "armor", "name": "Chainmail Bikini", "des": "Strangely not just for women",
         "bonus": 3, "sell": 600},
        {"id": 20, "type": "armor", "name": "Leather Armor", "des": "Its leather.", "bonus": 1, "sell": 200},


        #armor/boots
        {"id": 10, "type": "footgear", "name": "Boots Of Running Really Fast", "des": "run away + 2", "bonus": 0,
         "sell": 400, "special": "footgear"},

        #weapons
        {"id": 11, "type": "weapon", "name": "Staff Of Napalm", "des": "Usable by wizards only", "bonus": 5,
         "sell": 800, "restriction": "1hand"},
        {"id": 11, "type": "weapon", "name": "Blessed", "des": "Usable by wizards only", "bonus": 2,
         "sell": 800,
         "special": "item enhancer", "restriction": "1hand, wizards only, with item"}
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