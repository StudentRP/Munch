"""Initiates player personalisation and runs game cycle for each player fetching cards and initiation
each scene of play

Considerations;
    sets num of players                                         = = DONE
    triggers player setup                                       = = DONE
    triggers character play order                               = = DONE
    starts game loop                                            = = DONE
    triggers card calls                                         = = WORKING PROGRESS
    correlation of player vs cards                              = = move to game logic
    player intervention mechanics                               = = move to game logic
    exports treasure/curse objects to player self               = = move to game logic
    start GUI loop here and import from gui the inherited bits  = = to do
"""


# from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10 # creates circular
# from Munchkin.bin.engine.game_logic import start_choice as game_logic_start_choice
from Munchkin.bin.all_cards.table import cards
# from Munchkin.bin.engine import cut_scenes as cs
from random import randint, choice
import bin.GUI.gui_variables as gameVar
from itertools import cycle

from time import sleep


##################################################################
# main loop
##################################################################
first = True
""" V3.0  """


class PlayerSetUp:
    """class to determine number of players and hand to player order"""

    def __init__(self):
        self.cycle = 0

    def rand(self):
        """Game start, picks a random player in the session_players list. Setts player as active_player and calls meth
        to load player atribs gor gui"""
        player = choice(gameVar.StartVariables.session_players)
        gameVar.StartVariables.active_player = player # send to game var for accessibility
        print(f"The dice has been rolled. Random player selected is {player.name.title()}")
        self.varbinding(player) # set all gameVar to this player

    def varbinding(self, playerinst=gameVar.StartVariables.active_player):
        """Method to bind all player atribs to gameVar, to be called with player instance when ever
        communication is required to gui"""
        gameVar.PlayerAtribs.player_name = playerinst.name.title()
        gameVar.PlayerAtribs.player_gender = playerinst.sex.title()
        gameVar.PlayerAtribs.player_level = playerinst.level
        gameVar.PlayerAtribs.player_bonus = playerinst.bonus
        gameVar.PlayerAtribs.player_wallet = playerinst.wallet
        gameVar.PlayerAtribs.player_sack = playerinst.sack
        gameVar.PlayerAtribs.player_unsorted = playerinst.unsorted
        gameVar.PlayerAtribs.player_l_hand = playerinst.update_bindings("L_hand")
        gameVar.PlayerAtribs.player_r_hand = playerinst.update_bindings("R_hand")
        gameVar.PlayerAtribs.player_headgear = playerinst.update_bindings("headgear")
        gameVar.PlayerAtribs.player_armor = playerinst.update_bindings("armor")
        gameVar.PlayerAtribs.player_knees = playerinst.update_bindings("knees")
        gameVar.PlayerAtribs.player_footgear = playerinst.update_bindings("footgear")

    def deal_handler(self, option, instance=None): # instance for future use in case of player specific demand.
        """ Calls meth to deal cards for players dependent on option parameter."""
        if option == "start": # initial play or resurrection. called at player slice (select_players and resurrection
            for player in gameVar.StartVariables.session_players:
                player.unsorted = cards.card_sop.deal_cards("start", gameVar.Options.cards_dealt) # links to table.py, called from PlayerSetUp.select_players
        elif option == "door": # Standard gameplay loop
            print("your not at the start")
        elif option == "treasure": # Deal treasure, requires number for amount to deal.
            print("You have been dealt a treasure card")
        else: # Require check to see how many in deck and in burn pile for prob solving
            print("I guess the deck is empty....")

    def player_order(self, current_player): # called with gameVar rand_index
        """Note initial player is set at this point+bound.
        Player cycle loop for calling next player and call binding on new player"""
        play = True # win condition need method that will check all players
        player_gen = cycle(gameVar.StartVariables.session_players) # generator function that cycles a list indefinitely
        y = next(player_gen) # yields players from the list, at start this would be first item = p1.
        while play:
            if current_player == y and current_player.alive: # conditions to see if x==y (x= player, y=list item)
                print(f"Current player {current_player.name} turn ended")
                gameVar.StartVariables.active_player = next(player_gen) # binds next player to rand_player, (changes x)
                self.varbinding(gameVar.StartVariables.active_player) #  binds new player
                print(f"{gameVar.StartVariables.active_player.name} has been binded")
                break
            elif current_player == y and not current_player.alive and not gameVar.Options.perm_death:
                print(f"print player {current_player} is dead") #move in to conditional for permadeath
                current_player.alive = True # resets player status ##########need peradeath bit here
                gameVar.StartVariables.active_player = next(player_gen) # changes x without binding and moves to next player
                continue
            else:
                print(f"{y.name} did not match. Searching for player in list")
                y = next(player_gen) # changes y to find commonality to x

    def select_players(self): # slices num of available players with gui entry
        """called from gui (playersetter method) takes gameVar int and uses to slice list of player instances and binds to new gameVar (active_players).
         deal_handler is called to provide starting number of cards for each player"""
        num_of_players = gameVar.StartVariables.new_players # get int representing num of players in current session (from spinbox)
        print(f"number of players in session: {num_of_players}") ## GUI test for number acceptance# remove at end. calls __repr__ for each instance
        gameVar.StartVariables.session_players = gameVar.StartVariables.players_available[:num_of_players] # slice creates new list of players in
        # session binding to new variable gamevar
        self.deal_handler("start") # Starts process of dealing cards to all players. results in putting in player.unsorted. Does not bind to gameVar

    def player_name_gender(self, playerindex=0): #push in index for the number of players from controller gui script
        """Call active player list, use index to ref each player instance, call """
        player = gameVar.StartVariables.session_players[playerindex]
        player.char_setup() # calls playermodel.py method.
        # print(player) # __repr__ method

    def zipper(self, action=None):
        """zips card id's to checkbox bools. Used for all card sorting regardless of card type.
        action is conduit for card_matcher"""
        gameVar.GameObjects.zipped_tup.clear()  # clears tup list ready for new entry. not working...................
        for create_boo in gameVar.GameObjects.check_but_intvar_gen:
            gameVar.GameObjects.check_but_boo.append(create_boo.get()) # creates a list of 1s & 0s from check buttons status
            x, y = gameVar.GameObjects.check_but_card_ids, gameVar.GameObjects.check_but_boo
            gameVar.GameObjects.zipped_tup = list(zip(x, y))
        print("moving to player script", gameVar.GameObjects.zipped_tup) # checker shows all cleared lists
        self.card_matcher(action)

    def card_matcher(self, action):
        """compares tuple to selected_items searching for matching card ids and only passes on cards that contain
        a tuple with the boolean true. Action determines the whats happening to the cards next. """
        for card in gameVar.GameObjects.selected_items: # loops over specific card items
            for tup in gameVar.GameObjects.zipped_tup: # loops over coupled card_id, bool tuples.
                if tup[0] == card["id"] and tup[1]:
                    if action == "sell":
                        gameVar.StartVariables.active_player.sell_item(card)
                    elif action == "equip":
                        # self.qualifier_race(card) # old redundant meth
                        self.tri_qualifier(card) # test ~~ok~~
                    elif action == "use":
                        # gameVar.StartVariables.active_player.
                        pass
                    elif action == "remove":
                        player = gameVar.StartVariables.active_player
                        player.equipped_items("removal", card)


    def tri_qualifier(self, card):
        """Combines the 3 qualifier methods in to one tidy loop. Checks the player against the card for the 3 qualifiers
        race, class, gender """
        player = gameVar.StartVariables.active_player
        checks = {player.race: "race_restriction", player.race2: "race_restriction", player.klass: "klass_restriction",
                  player.klass2: "klass_restriction", player.sex:"sex_restriction"}
        flag = 1 # True
        for key, val in checks.items():
            if card.get(val):  # if present in dict do this. Dont put string. Must return none!!!
                if card.get(val) == key:
                    print(f"Main path for: {val}")
                    continue
                elif player.name == "The_Creator":  # dev mode
                    print(f"{key} - Dev path")
                    continue
                else:
                    print(f"You cant equip this card, {val}")
                    flag = 0
                    # gameVar.StartVariables.message(f"Card can not be quipped: {val}.")
                    break
            else:  # no restriction in card
                print(f"No {val} required path")
                continue
        if flag: # only if flag remains True
            player.add_player_item(card)
            # player.refined_adder(card)



    # def qualifier_race(self, card):
    #     """checks race compatibility of the cards against the player for equipping """
    #     player = gameVar.StartVariables.active_player
    #     if card.get("race_restriction"): # if present in dict do this
    #         if card.get("race_restriction") == player.race or card.get("race_restriction") == player.race2:
    #             print("get(race) main path")
    #             self.qualifyer_klass(card)
    #         elif player.name == "The_Creator": # dev mode
    #             print("race cheat path")
    #             self.qualifyer_klass(card)
    #         else:
    #             print("you cant equip this card, race restriction")
    #     else: # no restriction in card
    #         print("no race required path")
    #         self.qualifyer_klass(card)
    #
    # def qualifyer_klass(self, card):
    #     """checks race compatibility of the cards against the player for equipping """
    #     player = gameVar.StartVariables.active_player
    #     if card.get("klass_restriction"):  # if present in dict do this
    #         if card.get("klass_restriction") == player.klass or card.get("klass_restriction") == player.klass2:
    #             print("get(klass) main path")
    #             self.qualifyer_gender(card)
    #         elif player.name == "The_Creator": # dev mode
    #             print("klass cheat path")
    #             self.qualifyer_gender(card)
    #         else: # if card has no condition
    #             print("you cant equip this card class restriction")
    #     else:  # no restriction in card
    #         print("no klass required path")
    #         self.qualifyer_gender(card)
    #
    # def qualifyer_gender(self, card):
    #     """checks race compatibility of the cards against the player for equipping """
    #     player = gameVar.StartVariables.active_player
    #     if card.get("sex_restriction"):  # if present in dict do this.
    #         if card.get("sex_restriction") == player.sex: #for combining have this as dict(key, value) ("sr":p.sex)
    #             print("get(gender) main path")
    #             player.add_player_item(card, "add")
    #         elif player.name == "The_Creator": # dev mode
    #             print("sex cheat path")
    #             player.add_player_item(card, "add")
    #         else:  # if card has no condition
    #             print("you cant equip this card gender restriction")
    #     else:  # no restriction in card
    #         print("no gender required path")
    #         player.add_player_item(card, "add")


    def scrub_lists(self):
        """Clears all appended list that are not capable of clearing."""
        gameVar.GameObjects.selected_items.clear()  # clears the card objects list
        gameVar.GameObjects.check_but_intvar_gen.clear()  # clears list of intVar objects from check buttons
        gameVar.GameObjects.check_but_boo.clear()  # clears boolean list
        gameVar.GameObjects.check_but_card_ids.clear()  # clears card id list
        gameVar.GameObjects.zipped_tup.clear()  # clears tup list



engine = PlayerSetUp()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    engine.player_name_gender()


