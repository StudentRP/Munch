"""
Class to build model players and assign new attributes associated with cards through gameplay.

Considerations:
    Player model
    Death
    New build
    save -- most likely shelve objects
    stats access

"""


from Munchkin.bin.all_cards.table import Table # most likely not used here (pos for cross talk bypassing circular
# import but may require for adding to player inventory and stats (note same card in engine will return here)
from Munchkin.bin.all_cards.treasure_cards.treasurecards import Treasure

from Munchkin.bin.players.playersetup import P_tools
import bin.GUI.gui_variables as gameVar
from bin.all_cards.table import cards
from bin.all_cards.door_cards.doorcards import MonTools
from bin.all_cards.treasure_cards.treasurecards import T_tools
from  itertools import cycle




"""adding items to player"""
################### CHECKER (works)
# cards = Handler()
# x = cards.card.grabber() # to be called further up stream for sorting
# print("RETURNED VALUE:", x)
#####################

"""This is the player class. It will have all setting to configure players and modify attributes that are set to that
player. It will inherit from moncurse and treasure so that a player can add items to their attributes and modify
attributes based on action outcomes."""


##########################################################################
# Player attributes and methods
##########################################################################



#####################################################################
# MAIN PLAYER CLASS
#####################################################################

class Player(MonTools, T_tools): # inherits off card methods
    """Main player class"""

    def __init__(self, ref):
        self.ref = ref # simple form to keep track of players
        self.name = ""
        self.gender = "male" # default required..dont think it works like this...
        self.level = 1 # win lvl 10, make changeable so edit score to win
        self.bonus = 0
        self.other_bonuses = [] # shoulder drag ect
        self.enhancers = "" # most likely loose. to work on equip mode to run
        self.wallet = 0
        self.race = "human" # string eval to True so will show
        self.race2 = ""
        self.race_unlock = False # DEFAULT = False method by halfbread triggers this a True state (method to be added)
        self.klass = "No class"
        self.klass2 = ""
        self.klass_unlock = False # method by supermunchkin triggers this a True state
        self.big = "" # can carry only 1 big item
        self.big2 = []
        self.big_unlock = False
        self.weapons = {"L_hand": "", "R_hand": "", "two_hand": ""}
        self.weapon_count = 2  # 1 per hand, can add to with cheat. adding +=, removal -=.
        self.armor = {"headgear": "", "armor": "", "knees": "", "footgear": "",
                      "necklace": "", "ring": "", "ring2": ""} # fill with card
        self.sack = [] # 5 max, pos editable later in an options
        self.active_cards = [] # cards that elicit an effect ie supermunch armor enhancers ect
        self.hireling = []
        # self.unsorted = [] # Old! list of all cards that are used to by sorting
        self.alive = True
        self.longevity = 0 # counts cycles alive, if 0 player misses go
        self.cheat = 0 # set to false
        self.cheat_card = 0 # card the player is cheating with
        self.curses = [] # list of all active curses cards on player, can be removed with ork/wishing ring
        self.curse_allowed = True #switched off with tin hat ect
        self.run = 4 # ability to run, manipulable.
        self.run_away = True

    def __repr__(self):
        """developer aid"""
        return f"\nPLAYER REF:{self.ref}\nName:{self.name}\ngender:{self.gender}\nLevel:{self.level}" \
               f"\nBonus:{self.bonus}\nSack:{self.wallet}\n"

    # def __str__(self):
    #     """developer aid"""
    #     return f"\nPLAYER INFO:\nName:{self.name}\ngender:{self.gender}\nLevel:{self.level}" \
    #            f"\nBonus:{self.bonus}\n"

    def update_bindings(self, carried):
        """just gets whats attached to the player"""

        category = [self.weapons, self.armor]  # locations to search
        for sub_cat in category:  # is the dict as a whole
            for key in sub_cat:
                if isinstance(sub_cat[key], dict) and key == carried:
                    # gameVar.GameObjects.message = f'{sub_cat.get(key).get("name")} has been bound to {key}'
                    return sub_cat.get(key).get("name")

    def char_setup(self):
        # complete, prints to be removed
        """sets up name and gender in gameVar and player instance when called"""
        na = P_tools.name() # method to set name
        self.name = na  # makes change to player
        xy = P_tools.gender()
        self.gender = xy

        if self.name == "The_Creator": # ................................................................... dev mode
            self.gender = "bob"
            self.bonus = 200
            self.wallet = 20000
            gameVar.PlayerAtribs.player_gender = self.gender
            gameVar.GameObjects.message2 = f"{self.name} is in play, a god among mer mortals!"

        print(f"Your name is {self.name.title()} and you are {self.gender.title()}.")

    def inventory(self, key, cardtype): # called from GUI on button press
        """Returns list of dict from player sack cards that have a specific key and specific value.
        (ie sub_type == armour). returns all sub_types with the val of armor"""
        gameVar.GameObjects.selected_items = [obj for obj in self.sack if obj[key] == cardtype]

    def item_by_key(self, key):# generalised meth for key search
        """Returns list of cards form player sack list that contain the key x. (ie "sell").
        This is generalised meth for key search """
        gameVar.GameObjects.selected_items = [obj for obj in self.sack if obj.get(key)]

    def sell_item(self, card): # called by player.sell_item so self bound to player
        """Call from zipper to sell items, remove cards, reset gameVars and call to add to burn pile"""
        self.wallet += card["sell"] #adds worth of card to player
        gameVar.GameObjects.message = f"Selling sack {card['name']}, Card added to burn pile. Depth: {len(cards.burn_pile)}"
        x = self.sack.pop(self.sack.index(card)) # removes card from player sack deck
        cards.add_to_burn(x)# adds card to burn pile on table
        gameVar.GameObjects.message = f"Selling sack {card['name']}, " \
                                      f"\nCard added to burn pile. Depth: {len(cards.burn_pile)}"
        # print("tup list: ", gameVar.GameObjects.zipped_tup)

    def sum_of_bonuses(self): # pos multi usage and use as player item searcher. limited by equipped_items as caller
        """ Adds up all bonuses and bind to player in weapons and armour"""
        tot_bonus = 0
        locations = [self.weapons, self.armor] #locations to search
        for obj in locations: # looks at each object in list
            for sub_menu in obj:
                if isinstance(obj[sub_menu], dict): #checks submenu for card attachment in the form of a dict
                    # print(obj.get(sub_menu, "No sub menu").get("bonus", "No bonus found"))
                    tot_bonus += obj.get(sub_menu, "").get("bonus", "Problem getting bonus")
                    continue
        if self.name == "The_Creator":
            tot_bonus = 200 + tot_bonus
        self.bonus = tot_bonus

    def equipped_items(self, action, my_cards=None, card_id=None): # in use by gui list_equipped meth
        """Shows all items that have been equipped to the player. If remove, Sorts through equipped items,
        removing items that have been selected"""
        locations = [self.weapons, self.armor]  # locations to search
        for obj in locations:  # looks at each object in list. obj is the dict of all the poss locations as seen in player attrbs
            for sub_menu in obj:  # sub_menu is the keys which link to the card is placed in: armor = {}
                if isinstance(obj[sub_menu], dict):  # checks submenu for card attachment in the form of a dict
                    card = obj.get(sub_menu) # x is the card object
                    if action == "list_equipped":
                        gameVar.GameObjects.selected_items.append(card) #adds cards to selected_items list in gameVar
                        continue
                    elif action == "removal":
                        if card["id"] == my_cards["id"]:
                            self.sack.append(card) # adds card back to player inventory
                            obj[sub_menu] = "" # resets player atrib location
                            self.sum_of_bonuses() # recalculates bonuses
                            self.weapon_count += card.get("hold_weight", 0) # adds the cards carry_weight for available hands, if available.
                            continue
                    elif action == "curse": # not tested
                        print("In equipped items remove cured item")
                        pass

    def equip_armor(self, card):
        """ Equips armor to the player"""
        location = self.armor
        print("in armor")
        for sub_type in location.keys():
            if card["sub_type"] == sub_type:  # matches card["sub_type] to list
                occupied = isinstance(self.armor[sub_type], dict)
                if not occupied:
                    x = self.sack.pop(self.sack.index(card))  # removes cards from sack list
                    self.armor[sub_type] = x  # adds to player's attribs
                    break
                elif occupied:
                    card_removed = self.armor.pop(sub_type)  # removing card from player's attrib
                    self.sack.append(card_removed)
                    x = self.sack.pop(self.sack.index(card))  # removes cards from sack list
                    self.armor[sub_type] = x  # binds now card to player attribute
                    break
        gameVar.GameObjects.message = f"Equipping {card['name']}"
        self.sum_of_bonuses()

    def equip_weapon(self, card):
        """New simplified model. Checks L/R hands to see if full, equipping if not.
        Two hand items will not work when other hands full. """
        if self.weapon_count > 0:
            if card["sub_type"] == "1hand" and not isinstance(self.weapons["L_hand"], dict): # not equipped
                added_card = self.sack.pop(self.sack.index(card))
                self.weapons["L_hand"] = added_card
                self.weapon_count -= card.get("hold_weight")
                gameVar.GameObjects.message = f"Equipping {card['name']} to left hand"
            elif card["sub_type"] == "1hand" and not isinstance(self.weapons["R_hand"], dict): # not equipped
                gameVar.GameObjects.message = f"Equipping {card['name']} to right hand"
                added_card = self.sack.pop(self.sack.index(card))
                self.weapons["R_hand"] = added_card
                self.weapon_count -= card.get("hold_weight")
            elif card["sub_type"] == "2hand" and not isinstance(self.weapons["two_hand"], dict):
                if isinstance(self.weapons["L_hand"], dict) or isinstance(self.weapons["R_hand"], dict):
                    gameVar.GameObjects.message = "You can not equip this item while you have items in your other hands"
                elif not isinstance(self.weapons["L_hand"], dict) and not isinstance(self.weapons["R_hand"], dict):
                    gameVar.GameObjects.message = f"Equipping {card['name']} to both hands"
                    added_card = self.sack.pop(self.sack.index(card))
                    self.weapons["two_hand"] = added_card
                    self.weapon_count -= card.get("hold_weight")
            else: # cheat card section
                pass
        else:
            gameVar.GameObjects.message = "You are at max capacity. Remove some weapons to attach others!"
        print("capacity count", self.weapon_count)
        self.sum_of_bonuses()

    def card_meths(self, card, calltype=None, action=None): # calltype = setter(action = a/r), static(no action),
        """link to card methods for active effect on player
        action =add, contitions or remove"""
        print("in player card_meth")
        """will use add/remove suited to door cards, loose cases and curse canceling"""
        for key, val in MonTools.method_types.items(): # look up meth
            if key == card.get(calltype): # calltype either 'method for general, and 'static' for const effects while in use
                print(f"the key is {key}")
                val(self, action) # action is on or off


"""
card meth to handle curse, monsters ect. must handle both a static action and methods associated to add and remove.
calls required from; player select card, door kick for static ie no run, and loose scenario  


"""


p1 = Player(1) #passes reference (ref)
p2 = Player(2)
p3 = Player(3)
p4 = Player(4)
p5 = Player(5)
p6 = Player(6)
p7 = Player(7)
p8 = Player(8)
p9 = Player(9)
p10 = Player(10)
# p1.get_treasure()



if __name__ == '__main__':
    p1 = Player(1)
    print(p1)
    # p1.get_treasure() # duplicate val is print state from Handler class method (note is same: GOOD)
    # p1.char_setup() # calls player name/gender setup, to be called after player number select
    # p1.inventory() # shows inventory of new built char





