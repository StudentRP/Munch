"""This is the monster cures class and contains all monster and curse cards. Class will sort the cards and send one in
the form of a dict to the player class for sorting and use."""
from random import randint
# from treasure_v3 import Treasure



class M_tools():
    """process cards specific to monster"""

    pass


class C_tools():
    """process cards specific to curses"""
    pass


class O_tools():
    """process cards specific to miscellaneous"""
    pass


#####################################################################
# MAIN MONCURS CLASS
#####################################################################


class Moncurs(M_tools, C_tools, O_tools):
    """class to select card and hand to next layer child class."""

    """Order : name, description, level, treasure, badstuff, loose """
    mon = [
        {'name': 'Crabs', 'des': 'Cant outrun', 'lvl': 1, 'treasure': 1, 'bs': 'loose all armour below waist',
            'loose': "footgear legs knees"},
        {'name': 'Large Angry Chicken', 'des': 'fried chicken extra level if defeat with fire', 'lvl': 2, 'treasure': 1,
         'bs': 'loose level', 'loose': "one level"},
        {'name': 'Shade', 'des': 'undead -2 against thieves who are not fooled by shadows', 'lvl': 3, 'treasure': 1,
         'bs': 'loose level', 'loose': " -1 level"},
        {'name': 'Barrel Of Monkeys', 'des': '+ 2 to halflings', 'lvl': 6, 'treasure': 2,
         'bs': 'more fun than having poo thrown at you and hair pulled out', 'loose': "-1 level -1 small item"}
           ]

    """curse card list: name, des, bs"""
    cur = [{'name': 'curse', 'bs': 'loose footgear'}, {'curse': 'loose footgear'}]

    other = []


    def drawn(self):
        x = randint(1, 2) # mon or cur
        n = 1 # int(len(Moncurs.mon) - 1)
        y = randint(0, n)
        if x == 1:
            return Moncurs.mon[y]

        else:
            return Moncurs.cur[y]



m1 = Moncurs()

if __name__ == "__main__":
    print(m1.drawn())
    import class_tree
    class_tree.instancetree(m1)