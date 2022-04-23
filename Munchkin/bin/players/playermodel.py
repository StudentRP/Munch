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
# from bin.all_cards.table import cards
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
        self.armor = {"headgear": "", "armor": "", "knees": "", "footgear": {'testcard': 'armor'},
                      "necklace": "", "ring": "", "ring2": ""}
        self.sack = [] # 5 max, editable in options
        self.hireling = []
        # self.unsorted = [] # Old! list of all cards that are used to by sorting
        self.alive = True
        self.longevity = 0 # counts cycles alive, if 0 player misses go
        self.cheat = 0 # set to false
        self.cheat_card = 0 # card the player is cheating with
        self.enhancer_cards = []  # cards that elicit an effect ie supermunch/class card, ect. card lexical must be added to enhancer lexical
        self.enhancers_lexical = set() # all positive effects strings for comparative evaluation. only added when card installed on player.
        self.active_curses = []  # place to store all curse cards effecting player. card remove meth should reverse player change
        self.negative_lexical = set() # all negative effects strings for comparative evaluation. only added when card installed on player.
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
        (ie sub_type == armour). returns all sub_types with the val of armor"""
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
                        library.GameObjects.selected_items.append(card) #adds cards to selected_items list in gameVar
                        continue
                    elif action == "removal":
                        if card["id"] == my_cards["id"]:
                            self.sack.append(card) # adds card back to player inventory
                            obj[sub_menu] = "" # resets player atrib location
                            self.sum_of_bonuses() # recalculates bonuses
                            self.weapon_count += card.get("hold_weight", 0) # adds the cards carry_weight for available hands, if available.
                            continue
                    elif action == "curse": # not tested
                        print("In equipped items remove cursed item")
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
        library.GameObjects.message = f"Equipping {card['name']}"
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
        self.sum_of_bonuses()

    def card_meths(self, *args, **kwargs): # expects (card/s) dict('static'='on')
        """ link to card methods, args should be the card/s, kwards the different card meths and actions to take
        ie 'static':'on' """
        print(f"In player card_meth. Num of cards: {len(args)}, kwargs: {kwargs}") # args are the cards sent, info on meth used and status
        for method, state in kwargs.items(): # loops supplied kwards which contain card meth search and an action to take
            print(f'Card is {args[0]["name"]}. Searching for a {method} method')
            if args[0].get(method): # checks 1st card in args for the kward key method
                for listed_meth in args[0].get(method): # loops over the list values. "static": ["no_outrun", 'test_meth']
                    print(listed_meth) # leave in to make sure I made it a list!!! TEST
                    if listed_meth in MonTools.method_types: # checks if method (the value from above) is in monster_types dict
                        method_call = MonTools.method_types.get(listed_meth) # returns method associated to the value of monster_types
                        dispose_card = method_call(self, state, args[1:]) # returns None, or [card_destination, card] method_call(self, on, all other cards in the tuple)

                        if dispose_card: # screens out non types. Received args back are in form of list when given. ['burn', removed_item]
                            if dispose_card[0] == 'burn':
                                cards.add_to_burn(dispose_card[1]) # recycles any card that has been removed from a player from a method
                            elif dispose_card[0] == 'wondering':
                                print(' are wee here?')
                                cards.in_play.append(dispose_card[1]) # places new monster on table
                                cards.add_to_burn(args[0]) # disposes of original card ie wandering monster card
                            elif dispose_card[0] == 'enhancer':
                                cards.add_to_burn(args[0])
                                return dispose_card[1] # returns to caller for processing further, usually enhancer to monster will be added to specific fight



    # def card_meths(self, *args, **kwargs): #card meth to take in all card formats whether as single card/series of cards or presented as a list of cards
    #     """ link to card methods, args should be the card, kwards the different card meths and actions to take
    #     ie 'static':'on' """
    #     print(f"In player card_meth. Args: {args}, kwargs: {kwargs}") #  args are the cards sent, info on meth used and status
    #
    #     for cardset in args: # takes in as many cards in args tuple. Also works if cards are wrapped in list
    #         for card in cardset: # if args list of cards iterates over each card, IF single card iterates over the keys!
    #             for k, v in kwargs.items(): # loops supplied kwards which contain card meth search and an action to take
    #                 print(k, v)
    #                 # if k in card: # 1st arg of tuple. Looks for kward key in provided card. ie is there a static key in card? (kward key == card key)
    #                 print('card is', card)
    #                 print(f'confirmed match of {k}')
    #                 if isinstance(cardset, list):
    #                     method = card.get(k) # gets method of the found key in card ie static : no_run........ THIS COULD VERY EASILY BE A LIST THAT CAN BE LOOPED OVER TO IMPLEMENT SEVERAL METHS
    #                 else:
    #                     method = cardset.get(k)
    #
    #                 for action in method: # loops over the list value  in card provided by the key.
    #                     print(f"this card has {method} methods that will all be {v}")
    #                     if action in MonTools.method_types: # checks to see if method (the value from above) is in dict
    #                             method_call = MonTools.method_types.get(action)
    #                             method_call(self, k, v) # self=player, static, on .. need to think. do i need the k? am i only supplying the values: on, off, ect





"""
card meth to handle curse, monsters ect. must handle both a static action and methods associated to add and remove.
calls required from; player select card, door kick for static ie no run, and loose scenario  


"""


if __name__ == '__main__':
    p1 = Player()
    print(p1)
    # p1.get_treasure() # duplicate val is print state from Handler class method (note is same: GOOD)
    # p1.char_setup() # calls player name/gender setup, to be called after player number select
    # p1.inventory() # shows inventory of new built char





