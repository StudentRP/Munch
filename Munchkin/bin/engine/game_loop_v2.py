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
""" V2.0  """


class PlayerSetUp:
    """class to determine number of players and hand to player order"""

    def __init__(self):
        self.cycle = 0

    def rand(self):
        """called to pick a random player in the active player list"""
        player = choice(gameVar.StartVariables.session_players)
        gameVar.StartVariables.active_player = player # send to game var for accessibility
        print(f"random player selected is {player.name.title()}")
        self.varbinding(player) # set all gameVar to this player

    def varbinding(self, playerinst=gameVar.StartVariables.active_player):
        """Method to bind all player atribs to gameVar, to be called with player instance when ever communication is required to gui"""
        gameVar.PlayerAtribs.player_name = playerinst.name.title()
        gameVar.PlayerAtribs.player_gender = playerinst.sex.title()
        gameVar.PlayerAtribs.player_level = playerinst.level
        gameVar.PlayerAtribs.player_bonus = playerinst.bonus
        gameVar.PlayerAtribs.player_wallet = playerinst.wallet
        gameVar.PlayerAtribs.player_sack = playerinst.sack
        gameVar.PlayerAtribs.player_unsorted = playerinst.unsorted

    def deal_handler(self, option, instance=None):
        """ Provides cards to players dependent on option parameter."""
        if option == "start": # initial play or resurrection
            for player in gameVar.StartVariables.session_players:
                #!!!!!!!!!!! player.unsorted neads sorting and assigning to other buttons like armor weapons ect.
                player.unsorted = cards.card_sop.deal_cards("start", gameVar.Options.cards_delt) # links to table.py, called from PlayerSetUp.select_players
        elif option == "door": # Standard gameplay loop
            print("your not at the start")
        elif option == "treasure": # Deal treasure, requires number for amount to deal.
            print("You have been dealt a treasure card")
        else: # Require check to see how many in deck and in burn pile for prob solving
            print("I guess the deck is empty....")

    def player_order(self, current_player): # called with gameVar rand_index
        """Note initial player is set at this point+bound.
        Player cycle loop for calling next player and call binding on new player"""
        play = True # win condition
        player_gen = cycle(gameVar.StartVariables.session_players) # generator function that cycles a list indefinitely
        y = next(player_gen) # yields players from the list, at start this would be first item = p1.
        while play:
            if current_player == y and current_player.alive: # conditions to see if x==y (x= player, y=list item)
                print(f"Current player {current_player.name} turn ended")
                gameVar.StartVariables.active_player = next(player_gen) # binds next player to rand_player, (changes x)
                self.varbinding(gameVar.StartVariables.active_player) #  binds new player
                print(f"{gameVar.StartVariables.active_player.name} has been binded")
                break
            elif current_player == y and not current_player.alive:
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

    def zipper(self):
        "zips checkbox bools to card ids"
        gameVar.GameObjects.zipped_tup.clear()  # clears tup list ready for new entry. not working...................
        for create_boo in gameVar.GameObjects.check_but_ids:
            gameVar.GameObjects.check_but_boo.append(create_boo.get()) # creates a list of 1s & 0s from check buttons status
            x, y = gameVar.GameObjects.check_but_cards, gameVar.GameObjects.check_but_boo
            gameVar.GameObjects.zipped_tup = list(zip(x, y))

        player = gameVar.StartVariables.active_player  # things start to get bit funny here on 2nd person go
        print("moving to player script", gameVar.GameObjects.zipped_tup)
        player.sell_item() # calls player method to sell card
        self.varbinding(player) # reloads player atribs


gamefile = PlayerSetUp()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    gamefile.player_name_gender()


