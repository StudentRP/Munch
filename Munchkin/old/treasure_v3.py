"""draft module for Treasure class"""
from random import randint


#x = randint(0, 6)


class T_tools:
    """ methods for special objects"""

    @classmethod
    def immune(cls):
        """immune to curses"""
        print("I love my Tinfoil Hat")

    @classmethod
    def once(cls):
        """Send item to 'used' list"""
        print("This item has been depleted")

    @classmethod
    def escape(cls):
        """roll to escape combat, may need: return once()"""
        print("You make a dash for it! This item has now been depleted")

    @classmethod
    def deflect(cls):
        """1-3 deflect curse, 4-6 run, 6 go up level"""
        print("The curse rebounds")

#####################################################################
# MAIN TREASURE CLASS
#####################################################################


class Treasure(T_tools):
    """Base class for treasure, required to hold all Treasure cards and return card/attribute objects to children"""

    burn_card = [] # The use-only-once pile that can not be reused

    stack = [] # Re-usable cards

    special_list = {'once': T_tools.once, 'escape': T_tools.escape, 'deflect': T_tools.deflect,
                    'immune': T_tools.immune}


    """General order: name[0], description[1], bonus[2], sell[3], type/special[4], Dict to loop
    use only once, armour, weapons, """
    treasure_cards = [
        #once only
        {"name": "Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
         "bonus": 5, "sell": 200, 'type': "once"},
        {"name": "Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100, 'type': "once"},
        {'name': "Instant Wall", 'des': 'Automatic escape for 1 or 2 players', 'sell': 300, 'type': "once"},
        {"name": "Flask Of Glue", "des": "Use during combat, must re-roll escape even if auto last time", "bonus": 0,
         "sell": 100, "special": "escape"},

        #armour/head
        {"name": "The Occasionally Reliable Amulet", 'des': 'If equipped, chance to deflect curse', 'sell': 600,
         'special': "deflect"},
        {"name": "Tinfoil Hat", "des": "Immune to curses, curses by kicking down doors still effect", "bonus": 0,
         "sell": 800, "special": "immune"},
        {"name": "Pointy Hat Of Power", "des": "Usable by wizards only", "bonus": 3, "sell": 400,
         "special": "headgear"},
        {"name": "Helm Of Peripheral Vision", "des": "can not be back stabbed or stolen from by thief",
         "bonus": 2, "sell": 600, "special": "headgear"},
        # armour/armour
        {"name": "Short Wide Armour", "des": "usable by dwarf only", "bonus": 3, "sell": 400, "special": "armour"},

        #armour/boots
        {"name": "Boots Of Running Really Fast", "des": "run away + 2", "bonus": 0, "sell": 400, "special": "footgear"},

        #weapons
        {"name": "Staff Of Napalm", "des": "Usable by wizards only", "bonus": 5, "sell": 800,
         "special": "1 hand"},
    ]


    def get_all(self):
        """Gives all key/val associated to a specific card"""
        for key, value in self.treasure_cards[x].items():
            print(key, ":", value)

    def specific(self):
        """Directory to special/type methods and card main pack removal"""
        for key, value in self.treasure_cards[x].items(): #searches for 'type' in dict
            if key == "type" and value == "once" or value == 'escape':
                Treasure.burn_card.append(self.treasure_cards[x]) # adds current t_card to burn_cards list
                Treasure.special_list[value]() #value becomes key for special_list calling value method.
                del Treasure.treasure_cards[x] #del card from t_cards to stop reuse
            elif key == 'special':
                try:
                    Treasure.special_list[value]()
                except KeyError:
                    print("This has not been configured for armour and weapons yet")
                    #call method to sort this section out for wep and armour
            else:
                pass

    def card_return(self):
        """Returns card to caller for sorting"""
        print(f"T{self.treasure_cards[x]} card has been returned to the caller.")
        c = self.treasure_cards[x]
        return c
        # return self.treasure_cards[x]

    @classmethod
    def formated(cls):
        """provides liner view of card"""
        for key, value in cls.treasure_cards[x].items():
            print(key.title(), ':', value)

    def set_card(self):
        pass



"""reload import statement for random """
y = int(len(Treasure.treasure_cards) - 1)

x = randint(0, y)

#instance
c1 = Treasure() # instance object is the vessel that contains other objects


"""Ensures tests below only run when script is run directly and not when imported"""
if __name__ == '__main__':
    # print(f"Num of cards in pack: {y + 1}")
    # print(c1.treasure_cards[x]['name'])
    # """check to see card migration and removal"""
    # #print(Treasure.treasure_cards) #prints all cards
    # #print(c1.get_all())
    # c1.specific()
    # try:
    #     print(f"The '{Treasure.burn_card[-1]['name']}' has been depleted.") #if added to burn list will show card
    # except IndexError:
    #     print(f"The '{c1.treasure_cards[x]['name']}' lives on!")
    #
    #
    #
    # '''all silenced or will run when child runs.... problem solved by top __name__ == '__main__' statement'''
    # c1.card_return()# object to be sent to other classes need return statement
    # # c1.specific() #print statement executed from top methods
    # Treasure.formated() # card view test
    import class_tree

    class_tree.instancetree(c1)



"""p
NOTES:

Use a lexicon scanner on des to determine action for player is 'wizards only', head gear,  ect. 
Set armour location (knees0)  under 'special', former under des,    

"""
