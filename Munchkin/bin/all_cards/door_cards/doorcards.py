"""
Contains all door cards.
Will need a processing level
"""


class MonTools:
    """methods for all cards associated to moncurse cards"""

    def supermunch(self, action):
        """player class_unlock bool option"""

        if action == "add":
            print("return True")
        else:
            print("return False")

    def half_breed(self, action):
        if action == "add":
            print("return True")
        else:
            print("return False")

    method_types = {'supermunch': supermunch, 'half_breed': half_breed}


#####################################################################
# MAIN MONCURS CLASS LISTING DOOR CARDS
#####################################################################


# class Moncurs(M_tools, C_tools, O_tools):
class Moncurse(MonTools):
    """class to list all monster and curse cards."""


    door_cards = [
        # monster cards, Order : name, description, level, treasure, badstuff, loose
        {'id': 200, "category": "door", 'type': 'monster', 'name': 'Crabs', 'des': 'Cant outrun', 'lvl': 1, 'treasure': 1, 'bs': 'loose all armour below waist',
            'loose': "footgear legs knees"},
        {'id': 201, "category": "door", 'type': 'monster', 'name': 'Large Angry Chicken', 'des': 'fried chicken extra level if defeat with fire', 'lvl': 2, 'treasure': 1,
         'bs': 'loose level', 'loose': "one level"},
        {'id': 202, "category": "door", 'type': 'monster', 'name': 'Shade', 'des': 'undead -2 against thieves who are not fooled by shadows', 'lvl': 3, 'treasure': 1,
         'bs': 'loose level', 'loose': " -1 level"},
        {'id': 203, "category": "door", 'type': 'monster', 'name': 'Barrel Of Monkeys', 'des': '+ 2 to halflings', 'lvl': 6, 'treasure': 2,
         'bs': 'more fun than having poo thrown at you and hair pulled out', 'loose': "-1 level -1 small item"},

        # Curse cards,curse card list: name, des, bs
        {'id': 204, "category": "door", 'type': 'cures', 'name': 'curse', 'bs': 'loose footgear'},

        # Monster Enhancers

        # player enhancers

        # Joining cards
        {'id': 205, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 206, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 207, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 208, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 209, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},

        {'id': 210, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        {'id': 211, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        {'id': 212, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        {'id': 213, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        {'id': 214, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},

        {'id': 215, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 216, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 217, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 218, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 219, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 220, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 221, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 222, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        {'id': 223, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},

    ]

    @classmethod
    def __repr__(cls):
        return cls.door_cards[0]["name"] # list index, dict name

    def card_meths(self, card, action=None):
        if card["method"]:
            x = MonTools.method_types[card["method"]]
            x(self, action)



m1 = Moncurse()

if __name__ == "__main__":
    card = m1.door_cards[6]
    m1.card_meths(card, "add")
    m1.card_meths(card, "remove")