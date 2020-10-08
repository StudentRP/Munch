"""Quick trial version for game flow"""

from random import randint


class Treasure():
    """All treasure items"""

    treasure_cards = [({"name":"Electric Radioactive Acid Potion", "des": "Use during any combat. +5 to either side.",
                       "bonus": 5, "sell": 200}),
                      ({"name":"Flask of glue", "des": "Use during combat, must re-roll escape (even if auto last time",
                       "bonus": 0, "sell": 100}),
                      ({"name":"Flaming Poison Potion", "des": "Use during combat", "bonus": 3, "sell": 100}),
                      ({"name":"Tinfoil hat", "des": "Immune to curses", "bonus": 0, "sell": 800, "immune": "curse"})
                      ]

    """test"""
    # a = treasure_cards[0]["name"]
    # print(a)

    def get_treasure(self):
        """ meth for getting treasure, to be passed to player after win or other"""
    pass


class Mon_Curse(Treasure):

    """Class that defines monsters"""

    mons = [
        [['Crabs'], [{'lvl': 1}], [{'run': 100}], [{'bs_armour': -1, 'bs_legs': -1, 'bs_feet': -1}],
         [{'lvlup': 1, 'treasure': 1}]],

        [['Large Angry Chicken'], [{'lvl': 2}], [{'run': 4}], [{'bs_lvl': -1}], [{'lvlup': 1, 'treasure': 1}],
         [{'add': 0, 'firelvl': 1}]],
        [['Shade'], [{'lvl': 3}], [{'run': 4}], [{'bs_lvl': -2}], [{'lvlup': 1, 'treasure': 1, 'gs_thief': +2}],
         [{'use_fire_lvlup': 1}]],
        [['Undead Horse'], [{'lvl': 4}], [{'run': 4}], [{'bs_lvl': -2, 'dwarves': -5}],
         [{'lvlup': 1, 'treasure': 2}]]
                 ]
    curse_list = [
        [['Curse! Loose small item!'], [{'bs_small_item': 1, 'remove': 0}]],
        [['Curse! Chicken on your head!'], [{'dice': -1, 'remove_bs_helmet': -1}]]
    ]

    """set of cards used from the pack. last added will be feature of play"""
    burn = []
    in_play = [] # for all current cards on table. will need to be sent to burn at end of turn

    @classmethod # denotes class method
    def get_mon(cls):
        """branch for 1st rand mon or curse, 2nd rand for item in list"""

        z = randint(1, 4) # choice, mon or curse
        a = randint(0, 3) # num of monster in list
        b = randint(0, 1) # num or curses in list
        print("Random number selected is,:", a)
        if z <= 2:
            y = Mon_Curse.mons[a]
            Mon_Curse.burn.append(y) # adds to burn list
            Mon_Curse.mons.remove(y) #removes form mons list
            print(f"The monster you have is {y[0][0]}")
        else:
            y = Mon_Curse.curse_list[b]
            Mon_Curse.burn.append(y)  # adds to burn list
            Mon_Curse.curse_list.remove(y)
            print(f"you have a curse {y[0][0]}")


    @classmethod
    def treasure(cls):
        """ calls treasure card from base class adds to burn list, removes from treasure list"""
        a = randint(0, 3)
        print(a)
        tc = Treasure.treasure_cards[a]
        nam = tc.get('name')
        print(f"You have picked up a {nam}")
        Mon_Curse.burn.append(tc) #adds to burn list
        print(f"I am in the burn pile {Mon_Curse.burn[-1].get('name')}") # gets last entry from burn list
        Treasure.treasure_cards.remove(tc) # note if call is max index, calling with same index will result in error as
        #asking for card out of range of list





    @staticmethod
    def monlvl():
        x = Mon_Curse.burn[-1][1][0]['lvl'] # to be changed under burn structure
        #print(x)
        return x
    @staticmethod
    def mcname():
        x = Mon_Curse.burn[-1][0]
        print(x)

#Mon_Curse.monlvl() #test


class Player(Mon_Curse):
    """player class, contains all methods for adding to player"""

    def __init__(self, plvl=1, bonus=0):
        self.plvl = plvl
        self.bonus = bonus
        self.name = {"name": "ninja"}
        self.sex = {"sex": "male"}
        self.race = {"race": "human"}
        self.half_bread = {"race": None}
        self.classes = {"Classes": "unskilled"}
        self.gear = {"hand": [], "belt": [], "armour": []}
        self.rucksack = {"once": [], "other": []}


    def playlvl(self):
        x = self.plvl
        return x

    def power(self):
        x = self.plvl
        y = self.bonus
        z = x + y
        print(f"You have {z} hit points")

    def back_pack(self):
        """update() perm adds to dict while script is active"""
        pass

    def gear(self):
        pass

    def name_change(self):
        """Sets player name and sex. WORKS"""
        i = input("what is your name?")
        self.name["name"] = i
        b = self.name["name"]
        a = input(f"what is your sex {b.title()}?")
        self.sex["sex"] = a

    def death_rest(self):
        """Reset all attributes"""
        pass


p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

#print(p1.name) # test



class Eng(Player):
    """all game actions """


    @staticmethod
    def comparelvl():
        z = p1 # changeable due to player
        x = Mon_Curse.monlvl()
        y = Player.playlvl(z)
        print(x, "This is from Eng, parent Mon_Curse")
        print(y, "This is from Eng, parent Player")

    @staticmethod
    def lvlmod():
        z = p1
        x = Mon_Curse.monlvl()
        y = Player.playlvl(z)

        if y > x:
            print(f'You win. You destroyed a level {Mon_Curse.monlvl(), Mon_Curse.burn[-1][0]}') # change to name
            z.plvl += 1
            print(z.plvl)


    @staticmethod
    def player_setup(): # Start here. STEP: 1
        """Starts game, choose num of players, sets name and sex."""

        print("*"*51, "\nWelcome to the Dungeon, Are you cunning enough to survive?\nYou will need all your wits to "
              "survive.\nBe sure not to trust anyone!\n","*"*50)
        player_set = False
        a = input("\n Please select number of players between 1 and 4.\n>>")

        while not player_set:
            if a == '1':
                p1.name_change()
                player_set = True
                continue
            elif a == '2':
                p1.name_change(); p2.name_change()
                player_set = True
                continue
            elif a == '3':
                p1.name_change(); p2.name_change(); p3.name_change()
                break
            elif a == '4':
                p1.name_change(); p2.name_change(); p3.name_change(); p4.name_change()
                break
            else:
                print('*'*60)
                print("You fluffed something up! Try again! Fool.")
                print('*' * 60)
                b = Eng.player_setup()
                return b
        if player_set:
            """random player select, returns player order"""
            print(f"lets go!!!!!!!!! {a}")


    def starting_player(self):
        pass


    def kick_door(self):
        pass

############################################################################################


#p1 = Player(5, 1) # Can can instant directly as its not associated to class

#p2 = Player('Ethan', 4, 4)



##############TEST CALLS################
#Mon_Curse.get_mon() # !!part of start, need to set mon before any calls for names ect
Mon_Curse.treasure()

# #Eng.comparelvl()
#Eng.lvlmod()
#print(Mon_Curse.burn)
#p1.power()
#p2.power()
#print(Mon_Curse.mons)
#print(Mon_Curse.burn)
#print(Mon_Curse.mons)
#Mon_Curse.mcname()


"""Trial complete. Test functional"""

#print("Original list", Mon_Curse.mons)
#Mon_Curse.get_mon()
#print("New dec", Mon_Curse.burn)
#print("old list", Mon_Curse.mons)
#Mon_Curse.mcname()
#print("*" * 30)
#p1.name_change()

################## Test game/player calls ##############

#Eng.player_setup()# setts player up

#print(p1.name["name"].title(), p1.sex["sex"].title())
#print(p2.name["name"].title(), p2.sex["sex"].title())
#print(p3.name["name"].title())
#print(p4.name["name"].title())
#print(p1.race["race"].title())

#import munch_v3
#help(munch_v3)
#print(dir(munch_v3))


