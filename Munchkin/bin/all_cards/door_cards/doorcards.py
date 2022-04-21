"""
Contains all door cards.
Will need a processing level
"""


class MonTools:
    """methods for all cards associated to Door cards, self should be the player
    *items/ will have add abd remove meth
    * monsters have "conditions" ie -2 for theifs ect and "badstuff" ie event of loosing fight,  params
    so far: 'add' = to add item from pack, 'remove' = bs outcome or curse

    """

    def test_meth(self, *args):
        print('In test meth expecting level change to 500')
        if "on" in args:
            self.level = 500


    def wandering_mon(self, *args, **kwargs):
        """needs to take in a card and build a list with monster in it and put in Table.in_play lol"""



    def unknown(self, problem):
        print(f"Problem found in method {problem}")

    def level_up(self, action, value):
        if action == "on": # add level
            print(f"Current player level{self.level}", end=" ")
            self.level += value
            print(f"level changed to {self.level} increased by {value}")
        else: # remove level
            print(self.level)
            self.level -= value
            print(f"level changed to {self.level} decreased by {value}")

    def supermunch(self, action=None):
        """player class_unlock bool option;  ln 227 player_door_cards engine! """
        print(f"In supermunchkin. action is {action}") # location tester

        if action == "on":
            self.klass_unlock = True
            print("class unlocked!!!")
        elif action == "off":
            self.klass_unlock = False
            print("return False")
        else:
            self.unknown("SupperMunchkin")

    def half_breed(self, action=None):
        """method for changing player flag"""
        print("in halfbreed")
        if action == "on":
            self.race_unlock = True
            print("race unlocked!!")
        elif action == "off":
            self.race_unlock = False
            print("return False")
        else:
            self.unknown("half_breed")

    def klass_bonus(self, action=None, *args):
        if isinstance(self.klass, dict):
            if self.klass.get("name") == "thief" or self.klass2.get("name") == "theif":
                print("in thief meth")# location check
                pass
            elif self.klass.get("name") == "elf" or self.klass2.get("name") == "elf":
                print("You are an Elf")
        elif not isinstance(self.klass, dict):
            print("No class detected with player for static action\n")
            print(self.klass)
        else:
            self.unknown("klass_bonus error")

    def race_bonus(self, *args):
        if self.race.get("name") == "thief":
            pass

    def no_run(self, *args): # args sent include : ('static', 'on')
        print("monster method prevents run")
        if "on" in args:
            self.run_away = False
            print("run disabled")
        else:
            self.run_away = True
            print("run enabled")

    # def shade(self, action=None, *args):
    #     """Not used """
    #     import bin.GUI.gui_variables as gameVar
    #     if isinstance(self.klass, dict):
    #         if self.klass.get("name") == "thief":
    #             gameVar.Fight_enhancers.player_aid = 2
    #     else:
    #         print(f"not thief no bonus {gameVar.Fight_enhancers.player_aid}")

    def below_waist(self, action=None, *args):
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

    def loose_level(self, *args):
        print(f"Your level is {self.level}")
        if self.level > 1:
            self.level -= 1
            print(f"Level removed. You are now {self.level}")
        else:
            print("level not touched, not high enough")

    def loose_armor(self, action=None, *args):
        print("in loose_armor")
        if isinstance(self.armor.get("armor"), dict):
            print(f"Removing {self.name}'s armor") ###need meth to remove and add to burn pile
        else:
            print("No item to be removed by curse")
        # self.equipped_items("curse")

    def loose_footgear(self, *args):
        print("In loose_footgear")
        if isinstance(self.armor.get("footgear"), dict):
            print(f"Removing {self.name}'s foot gear")
        else:
            print("No item to be removed by curse")
        # self.equipped_items("curse")

    def loose_headgear(self, *args):
        print("Loose headgear meth to add")
        if isinstance(self.armor.get("headgear"), dict):
            print(f"Removing {self.name}'s head gear")
        else:
            print("No item to be removed by curse")

    def monkey_business(self, *args):
        """looses_level, loose_small_item"""
        print(f"player level is : {self.level}")
        if self.level > 1:
            self.level -= 1
        print(f"player level after is : {self.level}")

    method_types = {'test_meth': test_meth, 'level_up': level_up, 'supermunch': supermunch, 'half_breed': half_breed, "below_waist": below_waist,
                    "loose_level": loose_level, "monkey_business": monkey_business, "no_outrun": no_run, "sex_change": sex_change,
                    "loose-armor": loose_armor, 'loose_headgear': loose_headgear, 'loose_footgear': loose_footgear, "shade": klass_bonus,
                    'wandering_mon': wandering_mon
                    }

#may need to lambda these to pass args
#####################################################################
# MAIN MONCURS CLASS LISTING DOOR CARDS
#####################################################################


# class Moncurs(M_tools, C_tools, O_tools):
class Moncurse(MonTools):
    """class to list all monster and curse cards."""
    """ I think dif types of cards will have to have an array of different keys that can be searched with the get funct. ie weakness, ect """

    door_cards = [
        ## monster cards:id, category,  type, name, lexical, level, treasure, level_up method = bs, static = conditions at start of fight ie cant run.
        {'id': 300, "category": "door", 'type': 'monster', 'name': 'Crabs', 'lvl': 1, 'treasure': 1, "level_up": 1, 'lexical': ['Cant_outrun'], 'method': ["below_waist"], "static": ["no_outrun", 'test_meth']},
        # {'id': 301, "category": "door", 'type': 'monster', 'name': 'Large Angry Chicken', 'lvl': 2, 'treasure': 1, "level_up": 1, 'lexical': ['sensitive_to_fire', 'lvl_up1'], 'method': "loose_level"},
        # {'id': 302, "category": "door", 'type': 'monster', 'name': 'Shade', 'lvl': 3, 'treasure': 1, "level_up":1, 'lexical': ['undead', '-2 against_thieves'], 'method': "loose_level", "static":"shade"},
        # {'id': 303, "category": "door", 'type': 'monster', 'name': 'Barrel Of Monkeys', 'lvl': 6, 'treasure': 2, "level_up":1, 'lexical': ['+ 2 to halflings'], 'method': "monkey_business"},

        ## Curse cards: id, category, type, status, name, method, (status = active or passive for const effect that need to be added to player) # may need to add timed for card that last a certain amoun of time...
        # {'id': 401, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'Loose footgear', 'method': 'loose_footgear'},
        # {'id': 402, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'Loose armor!', 'method': 'loose_armor'},
        # {'id': 403, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'Loose level', 'method': 'loose_level'},
        # {'id': 404, "category": "door", 'type': 'curse', 'duration': 'timed', 'name': 'sex change', 'method': 'sex_change'}, # has another timed condition
        # {'id': 405, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'Loose headgear', 'method': 'loose_headgear'},
        # {'id': 406, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'Loose 1 small item', 'method': 'loose_small_item'},
        # {'id': 407, "category": "door", 'type': 'curse', 'duration': 'one_shot', 'name': 'income tax', 'method': 'income_one_shot'},
        # # Monster Enhancers
        # #
        # # card modifiers ## methods to add to list
        # {'id': 800, "category": "door", 'type': 'modifier', 'name': 'Intelligent +5 to monster', 'method': ['add_5'], 'win': 'extra_treasure'},
        # {'id': 801, "category": "door", 'type': 'modifier', 'name': 'Underdressed +5 to monster', 'method': ['add_5'], 'win': 'extra_treasure'},
        # {'id': 802, "category": "door", 'type': 'modifier', 'name': 'Enraged +5 to monster', 'method': ['add_5'], 'win': 'extra_treasure'},
        # {'id': 803, "category": "door", 'type': 'modifier', 'name': '....From Hell +5 to monster', 'method': ['add_5', 'ename_edit', 'add_5_if_cleric'], 'win': 'extra_treasure'},
        # {'id': 804, "category": "door", 'type': 'modifier', 'name': '....From Hell +5 to monster', 'method': ['add_5', 'ename_edit', 'add_5_if_cleric'], 'win': 'extra_treasure'},
        # {'id': 805, "category": "door", 'type': 'modifier', 'name': '....With Bagpipes +5 to monster', 'method': ['add_5', 'ename_edit', 'add_5_if_bard'], 'win': 'extra_treasure'},
        # {'id': 806, "category": "door", 'type': 'modifier', 'name': 'Armored +5 to monster', 'method': ['add_5', 'add_5_if_warrior'], 'win': 'extra_treasure'},
        # {'id': 807, "category": "door", 'type': 'modifier', 'name': 'Stealthy +5 to monster', 'method': ['add_5', 'add_5_if_thief'], 'win': 'extra_treasure'},
        # {'id': 808, "category": "door", 'type': 'modifier', 'name': 'Magic Resistant +5 to monster', 'method': ['add_5', 'add_5_if_wizard', 'immune_to_charm'], 'win': 'extra_treasure'},
        # {'id': 809, "category": "door", 'type': 'modifier', 'name': 'Brood +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 810, "category": "door", 'type': 'modifier', 'name': 'Ancient +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 811, "category": "door", 'type': 'modifier', 'name': 'Ravenous +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 812, "category": "door", 'type': 'modifier', 'name': 'Humongous +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 813, "category": "door", 'type': 'modifier', 'name': 'Saber-Toothed +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 814, "category": "door", 'type': 'modifier', 'name': 'Big Honking Sword of Character Whipping +10 to monster', 'method': ['add_10'], 'win': '2extra_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Undead +5 to monster', 'method': ['add_5', 'undead'], 'win': '2extra_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Undead +5 to monster', 'method': ['add_5', 'undead'], 'win': '2extra_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Baby -5 to monster', 'method': ['subtract_5'], 'win': '1less_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Half A .... -5 to monster', 'method': ['subtract_5', 'fname_edit'], 'win': '1less_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Very Depressed -5 to monster', 'method': ['subtract_5', 'not_compat_enraged'], 'win': '1less_treasure'},
        # {'id': 0, "category": "door", 'type': 'modifier', 'name': 'Sleeping -5 to monster',
        #  'method': ['subtract_5', 'not_compat_enraged', 'not_compat_friendly'], 'win': '1less_treasure'},
        #
        ## Joining cards
        # {'id': 500, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 501, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 502, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 503, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},
        # {'id': 504, "category": "door", 'type': 'super munchkin', 'name': 'Super Munchkin', "method": 'supermunch'},

        # {'id': 600, "category": "door", 'type': 'half breed', 'name': 'Half Breed', "method": 'half_breed'},
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


#############################################################
# TEST SUITE
#############################################################
    @classmethod
    def __repr__(cls):
        """Card test request check"""
        return cls.door_cards[0]["name"] # list index, dict name cls=

    def card_meth(self, card, action=None, value=None):
        """Test of cards with key values that associated to methods within method_types list located within MonTools class"""
        print("CARD METHOD TEST")
        test_type = "static" # card key.  method, This ois to be passed before play when selecting a monster to action
        if card.get(test_type, "Method not in card"): # checks to see if test_type in card.
            value = card[test_type] # gets value stored at card key (test_type)
            print(value)
            get_method = MonTools.method_types[value] # returns inactive method #looks up method with key assigning inactive value
            get_method(self, action, value) # action 'on' or 'off', value level to add/ remove

    def __getattr__(self, attrib):
        """simulates player attribs for the instance m1 when called by monster mehtods. Acts as attribute not found lookup."""
        if attrib == "level": # catches m1.level (FROM CARD METHS) setting to 4 mimicking a player with a level of 4.
            return 4 # provides m1 with player traits of level
        elif attrib == "gender":
            return "male" # change according to requirement
        elif attrib == "klass" or attrib == "klass2":
            return {"name": "elf"} # mock class card dict, Change elements according to the required class


m1 = Moncurse()
if __name__ == "__main__":
    print(m1)
    # print(Moncurse)
    card = m1.door_cards[0] # draws specific card
    print(card) # show card
    m1.card_meth(card, action="on") # for methods that require action to turn off or on.
    m1.card_meth(card, action="off")
    # print(dir(m1)) #shows all methods and inherited meths