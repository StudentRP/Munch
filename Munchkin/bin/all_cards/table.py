""" This will define classes for the fetching of cards from treasurecards and monstercurse,
object attributes and returning a object/s that is used in play.

Considerations:
Burn pile, object o get cards


"""

from Munchkin.bin.all_cards.treasure_cards.treasurecards import Treasure
from Munchkin.bin.all_cards.door_cards.doorcards import Moncurse
# import Munchkin.bin.GUI.gui_variables as gameVar# creates circle import
from random import randint


class Dice:

    def roll(self):
        roll = int(randint(1, 6))
        return roll


class Dealer:

    def deal_cards(self, option=None, cardnum=4): # y= set card type, cardnum=number of cards to deal set by game  options
        """Selects card from pack either moncur or treasure and returns card object to caller"""
        x = randint(0, 10)
        dmax = len(Moncurse.door_cards) - 1     # total cards in Door pack
        dpack = randint(0, dmax)                # random card index from the Door pack
        tmax = len(Treasure.treasure_cards) - 1 # total cards in Treasure pack
        tpack = randint(0, tmax)                # random card from the Treasure pack

        if option == "start":
            """called at start to deal specific number of cards to pass to player"""
            starter_set = []
            # deal = cardnum # link to gameVar option for number of cards to deal at start
            for i in range(cardnum): # may need +=1
                dobj = Moncurse.door_cards.pop(-1) # may want more randomness than just number in first card
                starter_set.append(dobj) # adds door card to list
                tobj = Treasure.treasure_cards.pop(-1) # gets t card. better rand required
                starter_set.append(tobj) # adds treasure card to list
            return starter_set # passes list obj to caller

        elif option == 11 or x <= 5: # y specific for deck
            """Deal Door cards""" # will need condition for kicking door (placed on table) 2nd draw (player hand)
            print('From Door pile\n')
            card = Moncurse.door_cards.pop(dpack)
            print(f"Your card is: {card['name']}\nCards left in deck: {dmax}")
            return card

        elif option == 12 or x > 5:
            """Deal Treasure cards"""
            print('From Treasure pile\n')
            card = Treasure.treasure_cards.pop(tpack)
            # print(f"Card number: {pick},\nCard: {card}")
            return card

        else:
            pass


    """remove duplication with branch above and default arg"""
    def get_treasure(self):
        pack = len(Treasure.treasure_cards) - 1 # needs to - all curse cards
        pick = randint(1, pack)
        card = Treasure.treasure_cards[pick]
        print(f"Card number: {pick},\nCard: {card}")
        return card

    def start_deal(self):
        pass


    # def deal(self):
    #     for card in range(4):
    #         x = Selector.grabber(self)
    #         return x


class Table(Treasure, Moncurse): # inherits from
    """This is the table model and the attributes expected from the game tablel"""
    def __init__(self):
        self.card_sop = Dealer() # has-a dealer
        self.burn_pile = []
        self.in_play = []
        self.dice_sop = Dice()

    def add_to_burn(self, discard):
        """adding to burn pile"""
        self.burn_pile.append(discard)

    def remove_from_burn(self, pull_request):
        """digging through burn pile """
        try:
            return self.burn_pile[:-pull_request]

        except IndexError:
            x = len(self.burn_pile) -1
            return self.burn_pile[:x]

cards = Table() #main instance to use - gives access to all card classes and methods.
dice = Table()

if __name__ == "__main__":

    z = cards.card_sop.deal_cards() # to be called further up stream for sorting
    # print("RETURNED VALUE:", z)

    print(dice.dice_sop.roll())

    # y = cards.card.get_treasure() # calls grabs treasure card
    # print(f"This is your treasure card:\n{y}")



