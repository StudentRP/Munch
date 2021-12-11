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


"""


from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
from old.game_logic import start_choice
from Munchkin.bin.all_cards.table import Dealer
from Munchkin.bin.engine import cut_scenes as cs
from random import randint

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
        play = True

        while self.cycle <= 4: # test scenario, to be removed (replace with play for game exit)
            try:
                "main game loop"
                if instance == self.new_players[index] and instance.alive: #checks instance against index if player alive
                    "Main pathway logic"
                    print(f"{instance.name} Turn.")
                    # ..................... code calls for loop...............................
                    start_choice(instance, self.new_players) # triggers Kick Door and Inventory (1st step), passes on self and list of instances


                    # .sack vol check/charity
                    # ... end game loop
                    index += 1
                    instance = self.new_players[index]  # changes player, if index error does not execute below
                    continue
                elif instance != self.new_players[index]:
                    "Logic to increment index in search for player"
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
        """Setup for instances, names/gender and first deal"""
        print(cs.start())
        try:
            playersselect = int(input("Please select number of players 1 - 10.\n>>> ")) # throws error with str, need catch
            if playersselect < 1 or playersselect > 10: # out of num of player parameters
                print(cs.invalid())
                self.select_players() # restarts loop
            elif playersselect:
                self.new_players = self.players_available[:playersselect]
                for player in self.new_players:
                    player.char_setup() # sets up players before game
                    print("\nGetting cards from dealer\n")
                    player.sack = Dealer.deal_cards(player, "start") # add stating cards to player sack
                print("Dice rolled to see who goes first!\n")
                randomise = randint(0, len(self.new_players) - 1) # index correction
                gofirst = self.new_players[randomise] #gets instance at position[x]
                # print(self.new_players) # check to see if passing object and rand number
                self.player_order(gofirst) #passes instance to player_order()
        except ValueError:
            print("Out of cards!")
            self.select_players()



if __name__ == "__main__":

    NumberOfPlayers().select_players() # starts game



