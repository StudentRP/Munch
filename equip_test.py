class Player():
    """Main player class"""

    def __init__(self):
        self.level = 1 # win lvl 10, make changeable so edit score to win
        self.gender = "male"
        self.bonus = 0
        self.wallet = 0
        self.race = "human" # string eval to True so will show
        self.race2 = "fwizard"
        self.klass = {'c1': True, 'c2': False}
        self.hands = []
        self.armor = {"headgear": None, "armor": None, "armor1": False, "armor2": False, "footgear": None,
                       "special_1": None, "special_2": False, "special_3": False}  # open this out!
        self.sack = [] # 5 max, pos editable later in an options
        self.visible_cards = [] # will need to sort, simple branch on the return objs
        self.hireling = []
        self.cards_in_use = [] # enhances/curses applied, weapons/armour worn.
        self.unsorted = [] # list of all cards that are used to by sorting
        self.cheat = 0# set to true why not just put cheat card in hear and test isinstance() to allow access to
        self.cheating = False #opend up by above if occupied by cheat card
p1 = Player()

cards = [ {"id": 22, "type": "weapon", "name": "Staff Of Napalm", "qualification":"wizard and female only, ", "bonus": 5,
         "sell": 800, "restriction": "1hand"},
         {"id": 21, "type": "footgear", "name": "Boots Of Running Really Fast", "des": "run away + 2", "bonus": 0,
         "sell": 400} ]

card1 = {"id": 22, "type": "weapon", "name": "Staff Of Napalm", "qualification": "wizard only female only", "bonus": 5,
         "sell": 800, "restriction": "wizard"}

p1.armor["footgear"] = card1

# print(isinstance(p1.armor["footgear"], dict)) # check it had a dict attached
# print(p1.armor["footgear"]["name"]) # access to the contents
# for key, val in p1.armor.items():
#     # print(isinstance(val, dict))
#     if isinstance(val, dict):
#         print(val.get("qualification"))


if card1.get("restrction", True): # returns true if not there
    print("accessed")



print('*' * 10)
"""method for qualification"""

# card_matcher will return one card at a time that requires qualification testing against player attibs

def equiper(card=None):
    """ checks card slot is not occupied then removes from sack and equips to location, Also used to remove items."""
    if card["type"] == "weapon":
        if p1.hands == isinstance(p1.hands, dict):
            print("nope")
        else:
            print("empty")

# equiper(card1)


def card_action(card):
    """qualifier must either return card to sack or send card to equiper"""
    races = ["elf", "ork", "human", "dwarf"]
    klasses = ["wizard", "bard", "warrior", "spy"]
    if card["qualification"] not in card.keys():
        print("key in card") #screen card for attribs
        if "female" in card["qualification"]: # change the card and not this bit as female not in male
            print("female found") #check player sex
        for klass in klasses:
            if klass in card["qualification"]:
                print(klass, "found")

    else:
        print("key not found") # run generic method to attach

    # if card.get["qualification", ]
    # pass
# card_action(card1)

def equip():
    """simulates matcher"""
    for card in cards: # for each card in the list of cards
        card_action(card)



        # if card["type"] == "weapon": #checkes weapon qualification
        #     print(card["name"])
        #     if p1.race in card.get("qualification") or p1.race2 in card.get("qualification"):
        #     # if card.get("qualification") == p1.race or card.get("qualification") == p1.race2 or p1.cheat:
        #         print("you are a wizard harry")
        #     elif p1.gender in card.get("qualification"):
        #         print("its a girl!")
        #
        #     else:
        #         print("nope")



# equip()
# print("armor")
# print(p1.armor["footgear"]) # card added
# print("hands")
# print(p1.hands) # card added
print('*' * 10)



# print(isinstance(p1.armor, dict)) # good for checking if place is occupied
"""sum of bonuses"""

