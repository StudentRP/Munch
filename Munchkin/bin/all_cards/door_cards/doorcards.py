""" This folder will lay out the monster and curse card only  """


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
        {'id': 100, 'type': 'monster', 'name': 'Crabs', 'des': 'Cant outrun', 'lvl': 1, 'treasure': 1, 'bs': 'loose all armour below waist',
            'loose': "footgear legs knees"},
        {'id': 100, 'type': 'monster', 'name': 'Large Angry Chicken', 'des': 'fried chicken extra level if defeat with fire', 'lvl': 2, 'treasure': 1,
         'bs': 'loose level', 'loose': "one level"},
        {'id': 100, 'type': 'monster', 'name': 'Shade', 'des': 'undead -2 against thieves who are not fooled by shadows', 'lvl': 3, 'treasure': 1,
         'bs': 'loose level', 'loose': " -1 level"},
        {'id': 100, 'type': 'monster', 'name': 'Barrel Of Monkeys', 'des': '+ 2 to halflings', 'lvl': 6, 'treasure': 2,
         'bs': 'more fun than having poo thrown at you and hair pulled out', 'loose': "-1 level -1 small item"},

        # Curse cards,curse card list: name, des, bs
        {'id': 100, 'type': 'cures', 'name': 'curse', 'bs': 'loose footgear'},

        # Monster Enhancers

        # player enhancers

        # Joining cards
        {'id': 100, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 100, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 100, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 100, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 100, 'type': 'super munchkin', 'name': 'Super Munchkin', 'des': 'You may have two class cards',
         'choice': 'super choice'},
        {'id': 100, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 100, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 100, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 100, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 100, 'type': 'half bread', 'name': 'Half Bread', 'des': 'You may have two race cards',
         'choice': 'bread choice'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},
        {'id': 100, 'type': 'wandering monster', 'name': 'Wandering Monster', 'des': 'Adds monster to the fight',
         'choice': 'choose monster'},

        #
    ]
    @classmethod
    def __repr__(cls):
        return cls.door_cards[0]["name"]


#     def drawn(self):
#         x = randint(1, 2) # mon or cur
#         n = 1 # int(len(Moncurs.mon) - 1)
#         y = randint(0, n)
#         if x == 1:
#             return Moncurs.mon[y]
#
#         else:
#             return Moncurs.cur[y]
#
#
#
# m1 = Moncurs()
#
# if __name__ == "__main__":
#     print(m1.drawn())
#     import class_tree
#     class_tree.instancetree(m1)