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
# from Munchkin.bin.all_cards.table import Dealer
# from Munchkin.bin.engine import cut_scenes as cs
from random import randint, choice
import bin.GUI.gui_variables as gameVar

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
        x = choice(gameVar.StartVariables.active_players)
        gameVar.StartVariables.rand_player = x # send to game var for accessibility
        gameVar.StartVariables.rand_index = gameVar.StartVariables.active_players.index(x)
        # print(f"player: {x.name} index: {gameVar.StartVariables.rand_index}")
        print(f"random player selected is {x.name}")
        self.varbinding(x)

    def varbinding(self, playerinst):
        """method to bind all atribs to gameVar, to be called with player instance"""
        gameVar.PlayerAtribs.player_name = playerinst.name.title()
        gameVar.PlayerAtribs.player_gender = playerinst.sex.title()
        gameVar.PlayerAtribs.player_level = playerinst.level
        gameVar.PlayerAtribs.player_bonus = playerinst.bonus
        gameVar.PlayerAtribs.player_wallet = playerinst.wallet

    def deal_cards(self):
        pass


    def player_order(self, instance):
        """Player cycle loop for ending turns and loading new player"""
        for index in range(len(gameVar.StartVariables.active_players)):
            if gameVar.StartVariables.active_players.index(instance) == index and instance.alive: # gets instance index from list and compares to loop value
                # self.varbinding(instance)
                try:
                    index += 1
                    gameVar.StartVariables.rand_player = gameVar.StartVariables.active_players[index]  # binds rand_player to next in order
                    nextplayer = gameVar.StartVariables.rand_player
                    print(f"binding next player from try {nextplayer.name}")
                    self.varbinding(nextplayer)
                    break
                except IndexError:
                    index = 0
                    gameVar.StartVariables.rand_player = gameVar.StartVariables.active_players[index]
                    nextplayer = gameVar.StartVariables.rand_player
                    print(f"binding next player {nextplayer.name}")
                    self.varbinding(nextplayer)
                    break

            elif gameVar.StartVariables.active_players.index(instance) == index and not instance.alive:
                "Logic for player skip turn"
                print(f"You are dead {instance.name}, your body will be looted!") # send as message
                instance.alive = True
                index += 1
                gameVar.StartVariables.rand_player = gameVar.StartVariables.active_players[index]
                continue

    def select_players(self): # slices num of availabel players with gui entry
        """Setup for instances, names/gender and first deal. slices player instance list with new player list,
         for each player set them up with cards, rand player to go first and sends to player_order function"""
        session_players = gameVar.StartVariables.new_players
        maxplayers = session_players
        print(f"number of players in session: {session_players}") ## GUI test for number acceptance# remove at end
        gameVar.StartVariables.active_players = gameVar.StartVariables.players_available[:maxplayers] # slices players_avail list creating new list

    def player_name_gender(self, playerindex=0): #push in index for the number of players from controller gui script
        """call active player list, use index to ref each player instance, call """
        player = gameVar.StartVariables.active_players[playerindex]
        player.char_setup()
        # print(player)


gamefile = PlayerSetUp()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    gamefile.player_name_gender()


