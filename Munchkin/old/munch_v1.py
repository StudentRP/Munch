"""Quick trial version for game flow"""

from random import randint


class Mon_Curse():

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

    @staticmethod
    def get_mon():

        z = 2 #randint(1, 4) # choice
        a = randint(0, 3) # num of monster in list
        print("Random number selected is,:", a)
        if z == 2:
            y = Mon_Curse.mons[a]
            Mon_Curse.burn.append(y) # adds to burn list
            Mon_Curse.mons.remove(y) #removes form mons list
        else:
            pass #configure for curse



    @staticmethod
    def random_obj():
        pass


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

    def __init__(self, name, plvl, bonus):
        self.name = name
        self.plvl = plvl
        self.bonus = bonus

    def playlvl(self):
        x = self.plvl
        return x

    def power(self):
        x = self.plvl
        y = self.bonus
        z = x + y
        print(f"You have {z} hit points")


#print(p1.name) #test



class Eng(Player):

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



    def start(self):
        pass


    def kick_door(self):
        pass

############################################################################################


p1 = Player('Rory', 5, 1) # Can can instant directly as its not associated to class

p2 = Player('Ethan', 4, 4)


#####TEST CALLS################
#Mon_Curse.get_mon() # part of start, need to set mon before any calls for names ect

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
print("Original list", Mon_Curse.mons)
Mon_Curse.get_mon()
print("New dec", Mon_Curse.burn)
print("old list", Mon_Curse.mons)
Mon_Curse.mcname()
