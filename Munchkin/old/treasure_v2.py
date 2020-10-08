"""On start whatn class to return a single card. this card can then be deconstructed by child classes"""
from random import randint

class Treasure(object):
    """special methods"""

    used = [] # non-accessible list of used items (not to be used again during game play)

    """All treasure items, immutable tuple with dict, name, description, bonus, sell, special, type"""

    treasure_cards = [({"name":"Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
                       "bonus": 5, "sell": 200, 'type': once()}),
                      ({"name":"Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100,
                        'type': once()}),
                      ({'name':"Instant Wall", 'des': 'Automatic escape for 1 or 2 players', 'sell': 300,
                        'type': once()}),
                      ({"name":"Flask Of Glue", "des": "Use during combat, must re-roll escape even if auto last time",
                       "bonus": 0, "sell": 100, "special": escape()}),

                      ({"name":"The Occasionally Reliable Amulet", 'des':'If equipped, chance to deflect curse',
                        'sell': 600, 'special': deflect()}),
                      ({"name":"Tinfoil Hat", "des": "Immune to curses", "bonus": 0, "sell": 800, "special": immune()}),
                      ]

    def __init__(self, start_card):
        self.start_card = start_card


    def next_card(self):
        pass

    def starting(self):
        x = randint(0, 5)
        print(Treasure.treasure_cards[x])


p1 = Treasure()

p1.starting()