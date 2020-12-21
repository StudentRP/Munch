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


from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
from Munchkin.bin.engine.game_logic import start_choice
from Munchkin.bin.all_cards.table import Dealer
from Munchkin.bin.engine import cut_scenes as cs
from random import randint
# from Munchkin.bin.GUI.gui_v2 import TestWin, PlayerInfo, Main
from Munchkin.bin.GUI.gui_interface import Root
from time import sleep


##################################################################
# main loop
##################################################################

""" V2.0  """


class NumberOfPlayers:
    """class to determine number of players and hand to player order"""

    def __init__(self):
        self.players_available = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        self.new_players = []
        self.cycle = 0

    def player_order(self, instance):
        """Main game loop, triggers events and cycles players from a list"""
        index = 0
        play = True # for ending game loop

        while self.cycle <= 4: # test scenario, to be removed (replace with play for game exit)
            try:
                "main game loop"
                if instance == self.new_players[index] and instance.alive: # checks instance(x) against index in list
                    # and if player alive (skips turn if not)
                    "Main pathway logic"

                    ###GUI####

                    # player = TestWin(instance.name, instance.level) ### GUI TEST (GOOD data moves to win!)
                    app = Root(instance) # not work. passes single object to gui class (hard work find way to pass whole instance)
                    app.mainloop()
                    # moreover scrit will call at wrong place of gui not launching the main application


                    print(f"{instance.name} Turn.")
                    # ..................... code calls for loop...............................
                    start_choice(instance, self.new_players) # triggers Kick Door and Inventory (1st step)


                    # .sack vol check/charity
                    # ... end game loop
                    index += 1
                    instance = self.new_players[index]  # changes player, if index error does not execute below
                    continue
                elif instance != self.new_players[index]:
                    "Logic to increment index in search for player, can strip allot of this put on finish"
                    print(f"Seeking index for {instance.name, instance.ref}")
                    index += 1
                    continue
                elif instance == self.new_players[index] and not instance.alive:
                    "Logic for player skip turn"
                    print(f"You are dead {instance.name}, your items have been looted!")
                    instance.alive = True
                    index += 1
                    instance = self.new_players[index] # changes player
                    continue
                else:
                    "Catch eventuality"
                    print('ERROR: Something has gone seriously wrong!')
                    break
            except IndexError:
                "Looping logic"
                index = 0
                instance = self.new_players[index]  # changes player
                print(f"Resetting index {index}, next player is: {instance.name}")
                print("\n######################## Cycle number:", self.cycle, "########################")
                self.cycle += 1 # test scenario, to be removed
                continue

    def select_players(self):
        """Setup for instances, names/gender and first deal. slices player instance list with new player list,
         for each player set them up with cards, rand player to go first and sends to player_order function"""
        print(cs.start())
        try:
            maxplayers = int(input("Please select number of players 1 - 10.\n>>> ")) # throws error with str, need catch
            if maxplayers < 1 or maxplayers > 10: #out of player limits
                print(cs.invalid())
                self.select_players() # restarts loop
            elif maxplayers:
                self.new_players = self.players_available[:maxplayers] # slices players_avail & adds to new_players
                for player in self.new_players: #sets each instance up with sets of cards to start
                    player.char_setup() # sets up players before game
                    print("\nGetting cards from dealer\n")
                    player.sack = Dealer.deal_cards(player, "start") # adds starting cards to player sack
                print("Dice rolled to see who goes first!\n")
                randomise = randint(0, len(self.new_players) - 1) # index correction
                gofirst = self.new_players[randomise] # gets instance at position[random]
                # print(self.new_players) # check to see if passing object and rand number
                self.player_order(gofirst) #passes instance to player_order() function
        except ValueError:
            print("Out of cards!")
            self.select_players()


if __name__ == "__main__":

    NumberOfPlayers().select_players() # starts game



