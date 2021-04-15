"""
Contains all door cards.
Will need a processing level
"""


class MonTools:
    """methods for all cards associated to moncurse cards, self should be the player"""

    def supermunch(self, action):
        """player class_unlock bool option"""
        print("in supermuinch")

        if action == "add":
            self.klass_unlock = True
            print("class unlocked!!!")
        else:
            self.klass_unlock = False
            print("return False")

    def half_breed(self, action):
        print("in halfbreed")
        if action == "add":
            self.race_unlock = True
            print("race unlocked!!")
        else:
            self.race_unlock = False
            print("return False")


    def loose_footgear(self):
        print("in loose_footgear")
        pass #pos zipper meth

    def loose_armor(self):
        print("in loose_armor")
        # self.equipped_items("curse")


    def loose_level(self):
        print("in loose_level")
        pass

    method_types = {'supermunch': supermunch, 'half_breed': half_breed, 'loose_footgear': loose_footgear,
                    "loose_level": loose_level}


#####################################################################
# MAIN MONCURS CLASS LISTING DOOR CARDS
#####################################################################


# class Moncurs(M_tools, C_tools, O_tools):
class Moncurse(MonTools):
    """class to list all monster and curse cards."""

    door_cards = [
        # monster cards, Order : name, description, level, treasure, badstuff, loose
        {'id': 300, "category": "door", 'type': 'monster', 'name': 'Crabs', 'des': 'Cant outrun', 'lvl': 1, 'treasure': 1, 'bs': 'loose all armour below waist',
            'method': "footgear legs knees"},
        {'id': 301, "category": "door", 'type': 'monster', 'name': 'Large Angry Chicken', 'des': 'fried chicken extra level if defeat with fire', 'lvl': 2, 'treasure': 1,
         'bs': 'loose level', 'loose': "one level"},
        {'id': 302, "category": "door", 'type': 'monster', 'name': 'Shade', 'des': 'undead -2 against thieves who are not fooled by shadows', 'lvl': 3, 'treasure': 1,
         'bs': 'loose level', 'loose': " -1 level"},
        {'id': 303, "category": "door", 'type': 'monster', 'name': 'Barrel Of Monkeys', 'des': '+ 2 to halflings', 'lvl': 6, 'treasure': 2,
         'bs': 'more fun than having poo thrown at you and hair pulled out', 'loose': "-1 level -1 small item"},

        # Curse cards: id, catagory, type, status, name, method,
        {'id': 401, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose footgear', 'method': 'loose_footgear'},
        {'id': 402, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose armor!', 'method': 'loose_armor'},

        # Monster Enhancers

        # player enhancers

        # Joining cards
        {'id': 500, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 501, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 502, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 503, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        {'id': 504, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},

        {'id': 601, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 602, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 603, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 604, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 605, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},7
        # {'id': 701, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 702, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 703, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 7wandering'},
        # {'id': 704, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 705, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 7wandering'},
        # {'id': 706, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 707, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 708, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},
        # {'id': 709, "category": "door", 'type': 'wondering monster', 'name': 'Wondering Monster', "method": 'wandering'},

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