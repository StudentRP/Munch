"""
Contains all door cards.
Will need a processing level
"""


# from random import randint
# # from treasure_v3 import Treasure
#
#
#
# class M_tools():
#     """process cards specific to monster"""
#
#     pass
#
#
# class C_tools():
#     """process cards specific to curses"""
#     pass
#
#
# class O_tools():
#     """process cards specific to miscellaneous"""
#     pass


#####################################################################
# MAIN MONCURS CLASS LISTING DOOR CARDS
#####################################################################


# class Moncurs(M_tools, C_tools, O_tools):
class Moncurse():
    """class to list all monster and curse cards."""

    door_cards = [
        # monster cards, Order : name, description, level, treasure, badstuff, loose
        {'id': 200, 'type': 'monster', 'name': 'Crabs', 'des': 'Cant outrun', 'lvl': 1, 'treasure': 1, 'bs': 'loose all armour below waist',
            'loose': "footgear legs knees"},
        {'id': 201, 'type': 'monster', 'name': 'Large Angry Chicken', 'des': 'fried chicken extra level if defeat with fire', 'lvl': 2, 'treasure': 1,
         'bs': 'loose level', 'loose': "one level"},
        {'id': 202, 'type': 'monster', 'name': 'Shade', 'des': 'undead -2 against thieves who are not fooled by shadows', 'lvl': 3, 'treasure': 1,
         'bs': 'loose level', 'loose': " -1 level"},
        {'id': 203, 'type': 'monster', 'name': 'Barrel Of Monkeys', 'des': '+ 2 to halflings', 'lvl': 6, 'treasure': 2,
         'bs': 'more fun than having poo thrown at you and hair pulled out', 'loose': "-1 level -1 small item"},

        # Curse cards,curse card list: name, des, bs
        {'id': 204, 'type': 'cures', 'name': 'curse', 'bs': 'loose footgear'},

        # Monster Enhancers

        # player enhancers

        # Joining cards
        {'id': 205, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 205, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 206, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 207, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 208, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},

        {'id': 209, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 210, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 211, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 212, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 213, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},

        {'id': 214, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 215, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 216, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 217, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 218, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 219, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 220, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 221, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 222, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},

    ]

    @classmethod
    def __repr__(cls):
        return cls.door_cards[0]["name"] # list index, dict name


m1 = Moncurse()

if __name__ == "__main__":
    print(m1)