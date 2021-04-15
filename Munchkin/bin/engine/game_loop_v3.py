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
from Munchkin.bin.all_cards.table import cards, dice
# from Munchkin.bin.engine import cut_scenes as cs
from random import randint, choice
import bin.GUI.gui_variables as gameVar
from itertools import cycle

from time import sleep


##################################################################
# main loop
##################################################################
# first = True
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
        gameVar.GameObjects.message = f"The dice has been rolled. Random player selected is {player.name.title()}"
        self.varbinding(player) # set all gameVar to this player

    def varbinding(self, playerinst=gameVar.StartVariables.active_player):
        """Method to bind all player atribs to gameVar, to be called with player instance when ever
        communication is required to gui"""
        gameVar.PlayerAtribs.player_name = playerinst.name.title()
        gameVar.PlayerAtribs.player_gender = playerinst.gender.title()
        gameVar.PlayerAtribs.player_level = playerinst.level
        gameVar.PlayerAtribs.player_bonus = playerinst.bonus
        gameVar.PlayerAtribs.player_wallet = playerinst.wallet
        gameVar.PlayerAtribs.player_race = playerinst.race.title()
        gameVar.PlayerAtribs.player_race2 = playerinst.race2.title()
        gameVar.PlayerAtribs.player_klass = playerinst.klass.title()
        gameVar.PlayerAtribs.player_klass2 = playerinst.klass2.title()
        gameVar.PlayerAtribs.player_sack = playerinst.sack
        gameVar.PlayerAtribs.player_sack = playerinst.sack
        gameVar.PlayerAtribs.player_l_hand = playerinst.update_bindings("L_hand")
        gameVar.PlayerAtribs.player_r_hand = playerinst.update_bindings("R_hand")
        gameVar.PlayerAtribs.player_two_hand = playerinst.update_bindings("two_hand")
        gameVar.PlayerAtribs.player_headgear = playerinst.update_bindings("headgear")
        gameVar.PlayerAtribs.player_armor = playerinst.update_bindings("armor")
        gameVar.PlayerAtribs.player_knees = playerinst.update_bindings("knees")
        gameVar.PlayerAtribs.player_footgear = playerinst.update_bindings("footgear")
        gameVar.PlayerAtribs.player_necklace = playerinst.update_bindings("necklace")

    def deal_handler(self, option, call=1, num=0):
        """ Gets cards, type dependent on option parameter."""
        playerinst = gameVar.StartVariables.active_player
        if option == "start": # initial play or resurrection. called at player slice (select_players and resurrection
            for player in gameVar.StartVariables.session_players:
                player.sack = cards.card_sop.deal_cards("start", gameVar.Options.cards_dealt) # links to table.py, called from PlayerSetUp.select_players
        elif option == "door": # Standard gameplay loop
            door_card = cards.card_sop.deal_cards("door", 1) # returns card, 1 =  amount required in pack
            self.card_designator(door_card, call=call) # call needed to define where card goes dependent on how many timed door button pushed
            return door_card
        elif option == "treasure": # Deal treasure, requires number for amount to deal.
            print("dealt a treasure card") # test location
            card = cards.in_play[-1] # last on on stack
            my_treasure = cards.card_sop.deal_cards("treasure", num) # params = type of card, num of cards
            playerinst.sack.append(my_treasure) # adds strait to sack no ponit in card_desig
        else:
            print("I guess the deck is empty....")

    def card_designator(self, card, call=1): # for all door cards that are drawn form the pack
        """method that sort the cards that the player draws form the deck during play. this could be monster, curse ect.
        Call is used to determine how many times the door has been kicked in a turn and in 2nd instance the door is put into the
        players hand unseen. Mechanism is also used to trigger a curse
        """
        player = gameVar.StartVariables.active_player
        if card.get("type") == "monster": # if the cards a monster #1st/2nd kicks covered
            if call: # determines if first kick of door (T or F), if 1 = first kick
                gameVar.GameObjects.message = f"{card.get('name')} placed on table, Level {card.get('lvl')}"
                cards.in_play.append(card) # adds to table # careful as cards selected from hand will go strait to table
            else:
                gameVar.GameObjects.message = "Adding card to sack" # 2nd kick
                player.sack.append(card) # adds to player sack
        elif card.get("type") == "curse": # if the cards a monster #1st/2nd kicks covered
            if call: # 1st kick
                print("In curse::", player.curses)
                gameVar.GameObjects.message = "You have been cursed!" # look at card meth and action
                player.card_meths(card, "add")  # actions card effect ............ almost complete
                if card.get("status") == "active": # for constant effect cures
                    player.curses.append(card) # adds card to player curse list
                elif card.get("status") == "passive": # for one shot effect
                    cards.burn_card.append(card) # disposes of to burn pile
            else:
                gameVar.GameObjects.message = "Adding card to sack"
                player.sack.append(card)
        else: # for all other cards that have no direct effect or influence.
            print(f"Adding {card['name']}to sack.")
            if call:
                player.sack.append(card)  # adds card to player's items
                gameVar.GameObjects.message = f"Adding/using {card.get('name')}."
                return card  # to show if first time only 2nd it hides
            else:
                gameVar.GameObjects.message = "Adding 2nd card to sack"
                player.sack.append(card)

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
                print(f"print player {current_player} is dead") # move in to conditional for perm-a-death
                current_player.alive = True # resets player status ##########need per-a-death bit here
                gameVar.StartVariables.active_player = next(player_gen) # changes x without binding and moves to next player
                continue
            else:
                print(f"{y.name.title()} did not match. Searching for player in list")
                y = next(player_gen) # changes y to find commonality to x

        gameVar.GameObjects.message = f"{gameVar.StartVariables.active_player.name.title()}'s turn..."

    def select_players(self): # slices num of available players with gui entry
        """called from gui (playersetter method) takes gameVar int and uses to slice list of player instances and binds to new gameVar (active_players).
         deal_handler is called to provide starting number of cards for each player"""
        num_of_players = gameVar.StartVariables.new_players # get int representing num of players in current session (from spinbox)
        print(f"number of players in session: {num_of_players}") ## GUI test for number acceptance# remove at end. calls __repr__ for each instance
        gameVar.StartVariables.session_players = gameVar.StartVariables.players_available[:num_of_players] # slice creates new list of players in
        # session binding to new variable gamevar
        self.deal_handler("start") # Starts process of dealing cards to all players. results in putting in player.sack. Does not bind to gameVar

    def player_name_gender(self, playerindex=0): #push in index for the number of players from controller gui script
        """Call active player list, use index to ref each player instance, call """
        player = gameVar.StartVariables.session_players[playerindex]
        player.char_setup() # calls playermodel.py method.
        # print(player) # __repr__ method

    def zipper(self, action=None):
        """zips card id's to checkbox bools from selected_list. Used for all card sorting regardless of card type.
        action is conduit for card_matcher"""
        gameVar.GameObjects.zipped_tup.clear()  # clears tup list ready for new entry. not working...................
        for create_boo in gameVar.GameObjects.check_but_intvar_gen:
            gameVar.GameObjects.check_but_boo.append(create_boo.get()) # creates a list of 1s & 0s from check buttons status
            x, y = gameVar.GameObjects.check_but_card_ids, gameVar.GameObjects.check_but_boo
            gameVar.GameObjects.zipped_tup = list(zip(x, y))
        # print("moving to player script", gameVar.GameObjects.zipped_tup) # checker shows all cleared lists
        self.card_matcher(action)

    def card_matcher(self, action):
        """compares tuple to selected_items searching for matching card ids and only passes on cards that contain
        a tuple with the boolean true. Action determines the whats happening to the cards next. """
        for card in gameVar.GameObjects.selected_items: # loops over specific card items
            for tup in gameVar.GameObjects.zipped_tup: # loops over coupled (card_id, bool tuples).
                if tup[0] == card["id"] and tup[1]:
                    if action == "sell":
                        gameVar.StartVariables.active_player.sell_item(card)
                    elif action in "equip, disposable ,use": # equip/disposable will be treasures
                        self.tri_qualifier(card) # test ~~ok~~
                    elif action == "remove":
                        player = gameVar.StartVariables.active_player
                        player.equipped_items("removal", card)

    def tri_qualifier(self, card):
        """Combines the 3 qualifier methods in to one tidy loop. Checks the player against the card for the 3 qualifiers
        race, class, gender."""
        player = gameVar.StartVariables.active_player
        checks = {player.race: "race_restriction", player.race2: "race_restriction", player.klass: "klass_restriction",
                  player.klass2: "klass_restriction", player.gender: "gender_restriction"}
        flag = 1 # True
        for key, val in checks.items():
            if card.get(val):  # if present in dict do this. Dont put string return in get meth. Must return none!!!
                if card.get(val) == key:
                    print(f"Main path for: {val}")
                    continue
                elif player.name == "The_Creator":  # dev mode
                    print(f"{key} - Dev path")
                    continue
                else:
                    gameVar.GameObjects.message = f"You cant use this card, {val}"
                    flag = 0
                    # gameVar.StartVariables.message = f"{card.get('name')} can not be quipped: {val}." # not working
                    break
        if flag: # only if flag remains True.
            if card["category"] == "treasure":  # for all treasure cards the player uses that was from their hand
                self.player_treasure_cards(card) # for the use of treasure cards
            elif card["category"] == "door":  # for all enhancers ect that the player has from their hand
                self.player_door_cards(card) # for the use of door cards

    def player_treasure_cards(self, card):
        """method to sort the locations of treasure cards that the player has selected"""
        player = gameVar.StartVariables.active_player
        if card.get("type") == "armor":
            player.equip_armor(card)  # leads to player meth for placing in right place
        elif card.get("type") == "weapon":
            player.equip_weapon(card)
        elif card.get("type") == "disposable":  # for disposable throwable only
            pass  # meth for selecting target and changing bonuses,
        else:
            pass # for all other cards ie steeds

    def player_door_cards(self, card):
        player = gameVar.StartVariables.active_player
        player.card_meths(card, "add")  # link to player to card meths. WORKS
        print(player.klass_unlock, player.race_unlock)  # only shows at end of turn due to meth restriction in class,
        # meths added at end_turn

    def scrub_lists(self):
        """Clears all appended list that are not capable of clearing."""
        gameVar.GameObjects.selected_items.clear()  # clears the card objects list
        gameVar.GameObjects.check_but_intvar_gen.clear()  # clears list of intVar objects from check buttons
        gameVar.GameObjects.check_but_boo.clear()  # clears boolean list
        gameVar.GameObjects.check_but_card_ids.clear()  # clears card id list
        gameVar.GameObjects.zipped_tup.clear()  # clears tup list

    def card_type(self):
        """meth for checking the presents of table cards"""
        if cards.in_play: # checks to see if cards in play
            print("card_type", cards.in_play)
            return True
        else: # if list is empty the last card must have not been a monster
            return False

    def fight(self, helpper=None):
        print("In the fight!")
        card = cards.in_play.pop(-1) # end of cards on table
        player = gameVar.StartVariables.active_player
        if player.bonus + player.level >= card["lvl"]: # consideration required for player consumables and enhancers
            print("You win!")
            player.card_meths(card) #####
            cards.burn_card.append(card)
        else:
            print("fight lost")


        gameVar.GameObjects.message = f"You are fighting {card['name']}, level {card['lvl']}"

    def run(self):
        roll = dice.dice_sop.roll()
        player = gameVar.StartVariables.active_player
        print(f"You rolled a {roll}.")
        if roll >= player.run:
            print(f"You rolled a {roll}. You out ran your pursuer.")
            remove = cards.in_play.pop(0)
            cards.burn_pile.append(remove)
        else:
            print("Tried to run and slipped. Things are gona get ugly!")
            # method for card bad stuff. check player alive.
            # If dead remove all other cards to burn


engine = PlayerSetUp()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    engine.player_name_gender()


