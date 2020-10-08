"""goal: to get card as instance attribute then call parts of the attribute like name and type method"""

class Treasure(object):
    """simple test to get instance attribute as card """



    def __init__(self):
        self.card = Treasure.getcard(self)


    def getcard(self):
        """retrieves card value with self.key"""
        val = Treasure.cards[1]
        return val



    def once():
        return "fire in the house"


    def action(self):
        return Treasure.cards[1].get('type')








    cards = [
        ({"name":"Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
               "bonus": 5, "sell": 200, 'type': once()}),
             ({"name":"Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100,
               'type': once()})
    ]



p1 = Treasure()


print(p1.card)

print(p1.action())