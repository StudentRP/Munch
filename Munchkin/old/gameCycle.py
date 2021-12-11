"""Initiates player personalisation and runs game cycle for each player fetching cards and initiation
each scene of play

Considerations;
    sets num of players
    triggers player setup
    triggers character play order
    starts game loop
    triggers card calls
    correlation of player vs cards
    player intervention mechanics
    exports treasure/curse objects to player self


"""


from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
from old.game_logic import start_choice, deal_cards
from Munchkin.bin.engine import cut_scenes as cs
from random import randint
from time import sleep


##################################################################
# main loop
##################################################################

"""prob build this as class passing instance as first arg"""


def game_cycle(start, num): # gCycle(instance, str(num_of_players))
    """game cycle very verbose. accepts args instance and num of players converting to int. Each instance has an if
    statement. each if statement calls startChoice function that garbs door card    """
    num = int(num)
    if start == p1 and start.alive or num <=1: # health represents dead/alive player
        print("Player 1 mode")
        #startChoice(start) # kick door and inventory
        deal_cards(start)# ...................................................Left off need to stop dupes remove from pack
        start_choice(start) # kick door and inventory
        # cycle options
        if num =="01": # check kick, check inventory
            game_cycle(start, -1) # will cycle cards when kicking
        start = p2
        game_cycle(start, num)
    elif start == p2 and start.alive: # health represents dead/alive player
        print("Player 2 mode")
        start_choice(start)
        if int(num) == 2:
            start = p1
            game_cycle(start, num)
        else:
            start = p3
            game_cycle(start, num)
    elif start == p3 and start.alive: # health represents dead/alive player
        print("Player 3 mode")
        start.inventory()
        if int(num) == 3:
            start = p1
            game_cycle(start, num)
        else:
            start = p4
            game_cycle(start, num)
    elif start == p4 and start.alive: # health represents dead/alive player
        print("Player 4 mode")
        start.inventory()
        if int(num) == 4:
            start = p1
            game_cycle(start, num)
        else:
            print("Fatal error")

###########################################################################
# users to instances
###########################################################################


def users():
    """assigns instances to players and links to gCycle(instance, numOfPlayers) All very verbose"""
    num = str(input("Please select number of players \n>>> "))
    if num == '1':
        print("Not enough players. Please select number between 2-4")
        sleep(2.0)
        users()
    elif num == '2': # player 2 setup
        p1.char_setup() # runs class method associated to p1 = Player()
        p2.char_setup()
        print("\nA Player will be selected at random to go first!\n")
        x = randint(1, 2) # random select of which player goes first
        if x == 1:
            return game_cycle(p1, num)
        else:
            return game_cycle(p2, num)
    elif num == '3': # set up for 3 players
        p1.char_setup()
        p2.char_setup()
        p3.char_setup()
        print("\nA Player will be selected at random to go first!\n")
        x = randint(1, 3)
        if x == 1:
            return game_cycle(p1, num)
        elif x == 2:
            return game_cycle(p2, num)
        else:
            return game_cycle(p3, num)
    elif num == '4': # setup for 4 players
        p1.char_setup()
        p2.char_setup()
        p3.char_setup()
        p4.char_setup()
        print("\nA Player will be selected at random to go first!\n")
        x = randint(1, 4)
        if x == 1:
            return game_cycle(p1, num)
        elif x == 2:
            return game_cycle(p2, num)
        elif x == 3:
            return game_cycle(p3, num)
        else:
            return game_cycle(p4, num)
    elif num == "01": # ............................................................................. dev mode
        print("Entering Developer mode")
        p1.char_setup()
        return game_cycle(p1, num)
        #assign 4 cards from each set
    else:
        print("Please enter valid number between 2-4.")
        users()



###################################################################################################

""" V2  """

class NumberOfPlayers:
    """class to determine number of players and hand to player order"""

    def __init__(self):
        self.players_available = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
        self.new_players = []
        self.cycle = 0


    def player_order(self, instance):
        """cycles player order and triggers next event"""
        index = 0
        play = True

        while self.cycle <= 4: #test scenario, to be removed (replace with play for game exit)
            try:
                if instance == self.new_players[index] and instance.alive:
                    print(f"p{instance.ref} in game loop.")
                    print('index before;', index)
                    #... code calls for loop
                    if self.cycle == 0:
                        instance.char_setup()

                    index += 1
                    instance = self.new_players[index]  # changes player, if index error does not execute below
                    print('index after;', index, 'instance after change: p', instance.ref)
                    continue
                elif instance != self.new_players[index]:
                    print('index;', index)
                    print(f"Wrong index for p{instance.ref}")
                    index += 1
                    continue
                elif instance == self.new_players[index] and not instance.alive:
                    print(f"you are dead p{instance.ref}, your items have been looted!")
                    # method for new cards
                    instance.alive = True
                    index += 1
                    instance = self.new_players[index] # changes player
                    continue
                else:
                    print('error')
                    break
            except IndexError:
                index = 0
                instance = self.new_players[index]  # changes player
                print(f"resetting index {index}, and starting player : p{instance.ref}")
                print("\n######################## Cycle number:", self.cycle, "########################")
                self.cycle += 1 #test scenario, to be removed
                continue






    def select_players(self):
        x = int(input("Please select number of players 1 - 10.\n>>> "))
        if x < 1 or x > 10:
            cs.invalid()
            self.select_players()
        elif x:
            self.new_players = self.players_available[:x]
            randomise = randint(0, len(self.new_players) - 1) # index correction
            gofirst = self.new_players[randomise]
            # print(self.new_players) # check to see if passing object and rand number
            self.player_order(gofirst)







if __name__ == "__main__":
    # print(cs.start())
    # users()
    NumberOfPlayers().select_players() # starts game



