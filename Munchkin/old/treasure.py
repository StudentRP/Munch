""" Treasure module base class for v4 Munchkin"""
from random import randint

f = 0
card = None

"""
may shift functions and change dict function object to ref in another class
"""
def immune():
    """immune to curses"""
    print("I love my Tinfoil Hat")


def once():
    """Send item to 'used' list"""
    print("This item has been depleted")



def escape():
    """roll to escape combat, may need: return once()"""
    print("This item has been depleted")


def deflect():
    """1-3 deflect curse, 4-6 run, 6 go up level"""
    print("The curse rebounds")




class Treasure(object):
    """special methods"""

    used = [] # non-accessible list of used items (not to be used again during game play)

    """All treasure items, immutable tuple with dict, name, description, bonus, sell, special, type"""

    treasure_cards = [({"name":"Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
                       "bonus": 5, "sell": 200, 'type': once}),
                      ({"name":"Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100,
                        'type': once}),
                      ({'name':"Instant Wall", 'des': 'Automatic escape for 1 or 2 players', 'sell': 300,
                        'type': once}),
                      ({"name":"Flask Of Glue", "des": "Use during combat, must re-roll escape even if auto last time",
                       "bonus": 0, "sell": 100, "special": escape}),

                      ({"name":"The Occasionally Reliable Amulet", 'des':'If equipped, chance to deflect curse',
                        'sell': 600, 'special': deflect}),
                      ({"name":"Tinfoil Hat", "des": "Immune to curses", "bonus": 0, "sell": 800, "special": immune}),
                      ]



    @staticmethod
    def select():
        """get tupel from list and display contents"""
        global f
        global card
        f = randint(0, 5)
        card = Treasure.treasure_cards[f]
        # return card #return to child caller for sorting

        print(Treasure.treasure_cards[f])
        print(card.get('name'))
        print(card.get('des'))
        #print(card.get('bonus'))
        #print(card.get('sell'))
        try:
            x = Treasure.treasure_cards[f].get('special')
            x() # not work with class/static methods
        except TypeError:
            print("This item has no special")

            try:
                y = Treasure.treasure_cards[f].get('type')
                y()
                Treasure.used.append(card) # appends card to used list
            except TypeError:
                print("This item has no type")



Treasure.select()
print(f"\nCards in used pile:\n {Treasure.used}") # shows what card is in used pile, function object expected.
