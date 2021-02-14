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
from random import randint
import bin.GUI.gui_variables as gameVar

from time import sleep



##################################################################
# main loop
##################################################################
first = True
""" V2.0  """




class NumberOfPlayers:
    """class to determine number of players and hand to player order"""

    def __init__(self):
        self.cycle = 0

    def varseter(self, index):
        """method to generate randomplayer from the list and bind instance to all gui_var script"""
        global first
        if first: # too run on first call
            rand = randint(0, index - 1)
            print(f" ############### The random num is: {rand} ######################")
            instance = gameVar.StartVariables.active_players[rand]
            print(f"player activated {instance.name}")
            first = False
        else: # second call will need to provide an index
            print("else branch")
            instance = gameVar.StartVariables.active_players[index - 1]

        gameVar.PlayerAtribs.player_ref = instance.ref
        gameVar.PlayerAtribs.player_name = instance.name.title()
        gameVar.PlayerAtribs.player_gender = instance.sex.title()
        gameVar.PlayerAtribs.player_level = instance.level
        gameVar.PlayerAtribs.player_bonus = instance.bonus

        return instance # returns instance to caller



    def player_order(self, instance):
        """Main game loop, triggers events and cycles players from a list"""
        index = 0
        play = True # for ending game thus loop

        while self.cycle <= 4: # play bool to be here
            try:
                "main game loop"
                if instance == gameVar.StartVariables.active_players[index] and instance.alive: # checks instance(x) against returned index in list
                    # and if player alive (skips turn if not)
                    "Main pathway logic"
                    # instance.name = gui_main.player_name


                    print(f"{instance.name} Turn.")
                    # ..................... code calls for loop...............................
                    # game_logic_start_choice(instance, gameVar.StartVariables.active_players) # triggers Kick Door and Inventory (1st step)


                    # .sack vol check/charity
                    # ... end game loop
                    index += 1 #increments index for next player
                    instance = gameVar.StartVariables.active_players[index]  # changes player, if index error does not execute below

                    continue
                elif instance != gameVar.StartVariables.active_players[index]:
                    "Logic to increment index in search for player, can strip allot of this put on finish"
                    print(f"Seeking index for {instance.name, instance.ref}")
                    index += 1
                    continue
                elif instance == gameVar.StartVariables.active_players[index] and not instance.alive:
                    "Logic for player skip turn"
                    print(f"You are dead {instance.name}, your items have been looted!")
                    instance.alive = True
                    index += 1
                    instance = gameVar.StartVariables.active_players[index] # changes player
                    continue
                else:
                    "Catch eventuality"
                    print('ERROR: Something has gone seriously wrong!')
                    break
            except IndexError:
                "Looping logic"
                index = 0
                instance = gameVar.StartVariables.active_players[index]  # changes player
                print(f"Resetting index {index}, next player is: {instance.name}")
                print("\n######################## Cycle number:", self.cycle, "########################")
                self.cycle += 1 # test scenario, to be removed
                continue

    def initaliseplay(self):
        """method to """

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
        print(player)





        #
        # try:
        #     for player in gameVar.StartVariables.active_players: # sets each instance up with sets of cards to start
        #         player.char_setup() # calls meth from Player setting up char name/sex before game
        #         print("\nGetting cards from dealer\n")
        #         player.sack = Dealer.deal_cards(player, "start") # adds starting cards to player sack in Player class
        #     print("Dice rolled to see who goes first!\n")
        #     randomise = randint(0, len(gameVar.StartVariables.active_players) - 1) # index correction
        #     gofirst = gameVar.StartVariables.active_players[randomise] # gets instance at position[random]
        #     # print(self.new_players) # check to see if passing object and rand number
        #     self.player_order(gofirst) #passes instance to player_order() function
        # except ValueError:
        #     print("Out of cards!") # crude catch stemming from the ue of random card deals #TODO find better way
        #     self.select_players()

gamefile = NumberOfPlayers()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    gamefile.player_name_gender()


