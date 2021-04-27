"""
Contains all door cards.
Will need a processing level
"""


class MonTools:
    """methods for all cards associated to moncurse cards, self should be the player
    *items/curses will have add abd remove meth
    * monsters have "conditions" ie -2 for theifs ect and "badstuff" ie event of loosing fight,  params
    so far: 'add' = to add item f=rom pack, 'remove' = bs outcome or curse

    """

    def supermunch(self, action=None):
        """player class_unlock bool option;  ln 227 player_door_cards engine! """
        print(f"in supermuinch. action is {action}") # tester

        if action == "on":
            self.klass_unlock = True
            print("class unlocked!!!")
        else:
            self.klass_unlock = False
            print("return False")

    def half_breed(self, action=None):
        print("in halfbreed")
        if action == "on":
            self.race_unlock = True
            print("race unlocked!!")
        else:
            self.race_unlock = False
            print("return False")

    def no_run(self, action=None):
        print("monster method prevents run")
        if action == "on":
            self.run_away = False
        else:
            self.run_away = True

    def below_waist(self, action=None):
        print("in loose items below waist")
        pass #pos zipper meth

    def sex_change(self, action):
        print("curse change sex!")
        print(self.gender)
        if self.gender == "male":
            self.gender = "female"
        elif self.gender == "female":
            self.gender = "male"
        else:
            print("you are immune to sex change")
        print(f"Your sex is now: {self.gender}")

    def loose_level(self, action=None):
        print(f"remove level {self.level}")
        if self.level > 1:
            self.level -= 1
            print(f"level remove {self.level}")
        else:
            print("level not touched at not high enough")

    def loose_armor(self, action=None):
        print("in loose_armor")
        # self.equipped_items("curse")

    def loose_footgear(self, action=None):
        print("in loose_footgear")
        # self.equipped_items("curse")

    def loose_headgear(self, action=None):
        print("loose headgear meth to add")

    def monkey_business(self, action=None):
        """looses_level, loose_small_item"""
        print(f"player level is : {self.level}")
        if self.level > 1:
            self.level -= 1
        print(f"player level after is : {self.level}")

    method_types = {'supermunch': supermunch, 'half_breed': half_breed, "below_waist": below_waist,
                    "loose_level": loose_level, "monkey_business": monkey_business, "no_outrun": no_run, "sex_change": sex_change,
                    "loose-armor": loose_armor, 'loose_headgear': loose_headgear, 'loose_footgear': loose_footgear}

#may need to lambda these to pass args
#####################################################################
# MAIN MONCURS CLASS LISTING DOOR CARDS
#####################################################################


# class Moncurs(M_tools, C_tools, O_tools):
class Moncurse(MonTools):
    """class to list all monster and curse cards."""

    door_cards = [
        ## monster cards:id, category,  type, name, lexical, level, treasure, level_up method = bs, static = conditions at start of fight ie cant run.
        {'id': 300, "category": "door", 'type': 'monster', 'name': 'Crabs', 'lexical': ['Cant outrun'], 'lvl': 1, 'treasure': 1, "level_up":1, 'method': "below_waist", "static": "no_outrun"},
        {'id': 301, "category": "door", 'type': 'monster', 'name': 'Large Angry Chicken', 'lexical': ['kill with fire levelup'], 'lvl': 2, 'treasure': 1, "level_up":1, 'method': "loose_level"},
        {'id': 302, "category": "door", 'type': 'monster', 'name': 'Shade', 'lexical': ['undead -2 against thieves'], 'lvl': 3, 'treasure': 1, "level_up":1, 'method': "loose_level"},
        {'id': 303, "category": "door", 'type': 'monster', 'name': 'Barrel Of Monkeys', 'lexical': ['+ 2 to halflings'], 'lvl': 6, 'treasure': 2, "level_up":1, 'method': "monkey_business"},

        ## Curse cards: id, category, type, status, name, method, (status = active or passive for const effect that need to be added to player)
        # {'id': 401, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose footgear', 'method': 'loose_footgear'},
        # {'id': 402, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose armor!', 'method': 'loose_armor'},
        {'id': 403, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose level', 'method': 'loose_level'},
        {'id': 404, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'sex change', 'method': 'sex_change'},
        # {'id': 405, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose headgear', 'method': 'loose_headgear'},
        # {'id': 406, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'Loose 1 small item', 'method': 'loose_small_item'},
        # {'id': 407, "category": "door", 'type': 'curse', 'status': 'passive', 'name': 'income tax', 'method': 'income_tax'},

        ## Monster Enhancers

        ## player enhancers

        ## Joining cards
        {'id': 500, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 501, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 502, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 503, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 504, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},

        {'id': 600, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 601, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 602, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 603, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
        # {'id': 604, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},

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