"""
Class to build model players and assign new attributes associated with cards through gameplay.

Consider what the player class is responsible for...

Considerations:
    Player model
    player setup name & gender
    Death and reset
    accessing player and changing player resources
    save -- most likely shelve objects
    stats access

"""


from Munchkin.bin.all_cards.table import Table # most likely not used here (pos for cross talk bypassing circular
# import but may require for adding to player inventory and stats (note same card in engine will return here)
from Munchkin.bin.all_cards.treasure_cards.treasurecards import Treasure

from Munchkin.bin.players.playersetup import P_tools # OF LITTLE USE. Methods name/gender moved to this script.
import bin.GUI.variables_library as library
from bin.GUI.variables_library import cards # single location to same memory address
from bin.all_cards.door_cards.doorcards import MonTools
from bin.all_cards.treasure_cards.treasurecards import T_tools
from itertools import cycle

"""This is the player class. It will have all setting to configure players and modify attributes that are set to that
player. It will inherit from moncurse and treasure so that a player can add items to their attributes and modify
attributes based on action outcomes."""

#####################################################################
# MAIN PLAYER CLASS
#####################################################################


class Player(MonTools, T_tools):
    """Main player class, inherits off card methods making changes to the player."""
    num_of_instances = 0

    def __init__(self):
        Player.num_of_instances = Player.num_of_instances + 1
        self.ref = Player.num_of_instances
        self.name = ""
        self.gender = "male" # default required..dont think it works like this...
        self.level = 1 # win lvl 10, make changeable so edit score to win
        self.bonus = 0
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
        self.weapons = {"L_hand": "", "R_hand": "", "two_hand": ""} # values will be cards
        self.weapon_count = 2  # 1 per hand, can add to with cheat. adding +=, removal -=.
        self.armor = {"headgear": "", "armor": "", "knees": "", "footgear": "",
                      "necklace": "", "ring": "", "ring2": ""}
        # self.armor = {"headgear": "", "armor": "", "knees": "", "footgear": {'testcard': 'armor'},
        #               "necklace": "", "ring": "", "ring2": ""} test set
        self.sack = [] # 5 max, editable in options
        self.hireling = []
        # self.unsorted = [] # Old! list of all cards that are used to by sorting
        self.alive = True
        self.longevity = 0 # counts cycles alive, if 0 player misses go
        self.cheat = 0 # set to false
        self.cheat_card = 0 # card the player is cheating with
        self.enhancer_lexical = []  # all positive effects strings for comparative evaluation. only added when card installed on player.
        self.negative_lexical = [] # all negative effects strings for comparative evaluation. only added when card installed/used on player.
        # self.active_curses = []  # place to store all curse cards effecting player that are not one shot .....
        self.run = 4 # ability to run, manipulable. note elf must change this. !!! use as bool and escape value!
        self.run_away = True # locks ability toi run or not dependent on some monsters

    def __repr__(self):
        """developer aid"""
        return f"\nPLAYER Ref:{self.ref}\nName:{self.name}\nGender:{self.gender}\nLevel:{self.level}" \
               f"\nBonus:{self.bonus}\nSack:{self.wallet}\n"

    @classmethod
    def factory(cls):
        return Player()

    @classmethod
    def gender(cls):
        """Sets gender"""
        x = library.PlayerAttribs.player_gender # grabs string stored in in game var
        return x

    @classmethod
    def name(cls):
        """Sets name"""
        x = library.PlayerAttribs.player_name
        if x == "rory":  # ......................................................................... dev mode
            y = "The_Creator"
            return y
        return x

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
        na = Player.name() # method to set name
        self.name = na  # makes change to player
        xy = Player.gender()
        self.gender = xy

        if self.name == "The_Creator": # ................................................................... dev mode
            self.gender = "bob"
            self.bonus = 200
            self.wallet = 20000
            library.PlayerAttribs.player_gender = self.gender
            library.GameObjects.message2 = f"{self.name} is in play, A God among mortals!"

        #~~~~~~~~~~~~ info
        print(f"The player {self.name.title()} with the gender {self.gender.title()} has been created.")
        # ~~~~~~~~~~~~

    def inventory(self, key, cardtype): # called from GUI on button press
        """Returns list of dict from player sack cards that have a specific key and specific value.
        (ie sub_type == armour). returns a copy of all sub_types with the val of armor."""
        # could replace clear_list method by rebind list to an empty list here.
        library.GameObjects.selected_items = [obj for obj in self.sack if obj[key] == cardtype]

    def item_by_key(self, key):# generalised meth for key search
        """Returns list of cards form player sack list that contain the key x. (ie "sell").
        This is generalised meth for key search """
        library.GameObjects.selected_items = [obj for obj in self.sack if obj.get(key)]

    def sell_item(self, card): # called by player.sell_item so self bound to player
        """Call from zipper to sell items, remove cards, reset gameVars and call to add to burn pile"""
        self.wallet += card["sell"] #adds worth of card to player
        library.GameObjects.message = f"Selling sack {card['name']}, Card added to burn pile. Depth: {len(cards.burn_pile)}"
        x = self.sack.pop(self.sack.index(card)) # removes card from player sack deck
        cards.add_to_burn(x)# adds card to burn pile on table
        library.GameObjects.message = f"Selling sack {card['name']}, " \
                                      f"\nCard added to burn pile. Depth: {len(cards.burn_pile)}"
        # print("tup list: ", gameVar.GameObjects.zipped_tup)

    def sum_of_bonuses(self):  # pos multi usage and use as player item searcher. limited by equipped_items as caller ############
        # TODO: DISSOLVE THIS METH ONTO THE CARD_METH FOR ACTIVATION WITH METHOD='ON'/'OFF') TO MAKE CHANGES TO PLAYER
        """ Adds up all bonuses and bind to player.bonus. searches weapons and armor"""
        tot_bonus = 0
        locations = [self.weapons, self.armor]  # locations to search
        for obj in locations:  # looks at each dict object in list
            print(obj.keys())
            for sub_menu in obj:
                if isinstance(obj[sub_menu], dict):  # checks submenu for card attachment in the form of a dict
                    # print(obj.get(sub_menu, "No sub menu").get("bonus", "No bonus found"))
                    # print(f"bonus::: {obj.get(sub_menu).get('bonus', 0)} at location: {obj}, in submenu; {sub_menu}\n")
                    tot_bonus += obj.get(sub_menu).get("bonus", 0)
                    continue
        if self.name == "The_Creator":
            tot_bonus = 200 + tot_bonus
        self.bonus = tot_bonus
        print(f"sum of bonus: {self.bonus}")

    def equipped_items(self, action, selected_card=None, card_id=None):  # in use by gui list_equipped meth
        """Shows all items that have been equipped to the player. If remove, Sorts through equipped items,
        removing items that have been selected"""
        print(f"in equipped_items\n")
        atrib_locations = [self.weapons, self.armor]  # locations to search
        for dict_obj in atrib_locations:  # looks at each object in list. dict_obj is the player dict of locations a card can be placed
            for location_key in dict_obj:  # location_key is the keys which link to the card is placed in: armor = {}
                if isinstance(dict_obj[location_key], dict):  # checks dict_obj for card occupancy
                    equipped_card = dict_obj.get(location_key) # card stored at dict location

                    if action == "list_equipped":
                        library.GameObjects.selected_items.append(equipped_card)  # adds cards to selected_items list in gameVar
                        continue
                    elif action == "removal":
                        if equipped_card["id"] == selected_card["id"]: # compares equipped card id to selected card id
                            self.sack.append(equipped_card)  # puts card back in player inventory
                            # self.card_meths(card, method='off') ################################### NEED SWITCHING ON WHEN ARMOUR METHS HAVE BEEN SORTED <<<<<<<<<<<<<<<
                            dict_obj[location_key] = ""  # resets player atrib location (re-assigning key required as removal destroys it)
                            self.sum_of_bonuses()  # recalculates bonuses
                            self.weapon_count += equipped_card.get("hold_weight", 0)  # adds the cards carry_weight for available hands, if available.
                            continue
                    elif action == "curse":  # not tested
                        print("In equipped items remove cursed item")
                        pass

    def equip_armor(self, card):
        """ Equips armor to the player and calls card meths to activate"""
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
                    # self.card_meths(card_removed, method='off') # switches off card meths ################################### NEED SWITCHING ON WHEN ARMOUR METHS HAVE BEEN SORTED
                    self.sack.append(card_removed)
                    x = self.sack.pop(self.sack.index(card))  # removes cards from sack list
                    self.armor[sub_type] = x  # binds now card to player attribute
                    break
        library.GameObjects.message = f"Equipping {card['name']}"
        # self.card_meths(card, method='on') # switches card meths on################################### NEED SWITCHING ON WHEN ARMOUR METHS HAVE BEEN SORTED
        self.sum_of_bonuses()

    def equip_weapon(self, card):
        """New simplified model. Checks L/R hands to see if full, equipping if not.
        Two hand items will not work when other hands full. """
        if self.weapon_count > 0:
            if card["sub_type"] == "1hand" and not isinstance(self.weapons["L_hand"], dict): # if 1handed weap and no card in players left hand...
                added_card = self.sack.pop(self.sack.index(card)) # gets list index for pop by calling index() on object thus returning index
                self.weapons["L_hand"] = added_card
                self.weapon_count -= card.get("hold_weight")
                library.GameObjects.message = f"Equipping {card['name']} to left hand"
            elif card["sub_type"] == "1hand" and not isinstance(self.weapons["R_hand"], dict): # not equipped
                library.GameObjects.message = f"Equipping {card['name']} to right hand"
                added_card = self.sack.pop(self.sack.index(card))
                self.weapons["R_hand"] = added_card
                self.weapon_count -= card.get("hold_weight")
            elif card["sub_type"] == "2hand" and not isinstance(self.weapons["two_hand"], dict):
                if isinstance(self.weapons["L_hand"], dict) or isinstance(self.weapons["R_hand"], dict):
                    library.GameObjects.message = "You can not equip this item while you have items in your other hands"
                elif not isinstance(self.weapons["L_hand"], dict) and not isinstance(self.weapons["R_hand"], dict):
                    library.GameObjects.message = f"Equipping {card['name']} to both hands"
                    added_card = self.sack.pop(self.sack.index(card))
                    self.weapons["two_hand"] = added_card
                    self.weapon_count -= card.get("hold_weight")
            else: # cheat card section/ big item
                pass
        else:
            library.GameObjects.message = "You are at max capacity. Remove some weapons to attach others!"
        print("capacity count", self.weapon_count)
        # self.card_meths(card, method='on') # switches card meths on################################### NEED SWITCHING ON WHEN ARMOUR METHS HAVE BEEN SORTED
        self.sum_of_bonuses() # TODO sum of bonuses to be desolved

    def card_meths(self, *args, **kwargs):  # expects (card/s) dict('static'='on')
        """ link to card methods, args should be the card/s, kwards the different card meths and actions to take
        ie 'static':'on'. end result is to activate method on card and return to location card need to be."""

        print(f"In player card_meth. Num of cards: {len(args)}, kwargs: {kwargs}")  # args are the cards sent, info on meth used and status
        for method, state in kwargs.items():  # for each kwarg given do this loop
            print(f'Card is {args[0].get("name", "NOT FOUND")}. Searching for a {method} method') # all cards have a name
            # checker = args[0].get(method, False)# returns false if not present
            if args[0].get(method, False):  # checks 1st card in tuple for the kwrd key method ( 1st card is the 1 to action, any others are for work later on).
                for listed_meth in args[0].get(method):  # loops over the list the key returns. ie: "static": ["no_outrun", 'test_meth']
                    print(listed_meth)  # leave in to make sure I made it a list!!! ******* TEST PRINT
                    if listed_meth in MonTools.method_types:  # checks if method (the value from above) is in monster_types dict     (we can pretty much garentee the meth will be in the list...)
                        method_call = MonTools.method_types.get(listed_meth)  # returns method associated to the value of monster_types WILL NEED ANOTHER CONDITIONAL DEPENDENT ON CARD TYPE
                        outcome = method_call(self, state, args[1:])  # pushes any other cards to the first cards methods.
                        # returns None, or [card_destination, card] method_call(self, on, all other cards in the tuple)

                        # handle returned objects MOST SHOULD BE RETURNED TO SPECIFIC TABLE LISTS AFTER ACTIVATION
                        if outcome:  # screens out non types. Received args back are in form of list when given. ['burn', removed_item]
                            if outcome[0] == 'burn': # curses, non influencing cards that belong to the turn and fight
                                cards.add_to_burn(outcome[1])  # recycles any card that has been removed from a player from a method
                            elif outcome[0] == 'wondering': # special case
                                print('Outcomes in card_meths with wondering m')
                                cards.in_play.append([outcome[1]])  # adds new monster to the table starting a new card_set list
                                cards.add_to_burn(args[0])  # disposes of original card ie wandering monster card
                            elif outcome[0] == 'in_play': # monsters
                                cards.in_play[library.FightComponents.card_selector_index].append(args[0]) # adds the original card back to the in_play card_set for later use (turn off)
                            elif outcome[0] == 'in_turn': # cards that influence the turn
                                cards.in_turn[library.FightComponents.card_selector_index].append(args[0]) # adds the card to the in_turn list for later use


            else:
                print(f'CARD METHOD {method} NOT AVAILABLE WITH {args[0]["name"]} CARD')


"""
card meths need to handle  


"""


if __name__ == '__main__':
    p1 = Player()
    print(p1)
    # p1.get_treasure() # duplicate val is print state from Handler class method (note is same: GOOD)
    # p1.char_setup() # calls player name/gender setup, to be called after player number select
    # p1.inventory() # shows inventory of new built char





