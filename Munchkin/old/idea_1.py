"""What if monsters and players are part of the same class? They both have attributes of levels. This means monsters
will need a random element to call one either from a list and a new player will always start in a default manor"""
import random

additional_info = "additional stuff for monsters or items."
bonus_hp = "Additional moderators"
level_mod = 40 # need to associate to a source for modifier so the int is changeable. ie monster_call form return
# statement in another module that has random and list access to attribute that returns


class Characters:

    """Both playable and non-playable characters"""


    def __init__(self, ch_type = "monster and curse list ", level = 1):
        self.type = ch_type
        self.level = level
        self.additional = additional_info
        self.bonus = bonus_hp
        self.modlvl = level_mod



    # Death of both will be same but for player have if/elif statement to determine path. death resets level not
    # a new instance.
    def death(self):
        if type == "human":
            dice = input("Press enter to roll the dice.")
            dice = random.randint(1, 6)
            if dice <= 4:
                print("You cant run you need to fight for your life!")
            elif dice > 4:
                print("You have run away!")

    def defaultchk(self):
        print("works with method")

    def level_up(self):
        self.level += 1


    "with the level mod  may not need level_up method..."
    def level_modify(self):
        new_lvl = self.level + level_mod
        return new_lvl







char1 = Characters("monster", 20)
char2 = Characters("This over writes") # outline for all elements  change will be through variables

print(char2.level)
print(char2.type)

char2.defaultchk()

char2.level_up()
print(char2.level)

print(char2.additional)
print(char1.level)
# char1.level_modify()
print(char1.level_modify())
char1.level = 15 # mods directly note: char1.level_modify() - 15 will deduct from total
print(char1.level)





