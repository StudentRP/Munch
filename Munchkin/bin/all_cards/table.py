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
    """simulates a dice roll"""
    def roll(self, max=6): # max added for methods that change the likelihood of running from a fight
        roll = int(randint(1, max))
        return roll


class Dealer:

    def deal_cards(self, option, deal_amount): # option = set card type, deal_amount=number of cards to deal set by game  options
        """Method for dealing cards to players at start or during play. params: option selects the type/situation of
        dealing specific cards. deal_amount specific to the start/resurrect determines the amount of cards to of each type
        to deal players. REQUIRES ALL PARAMS TO BE PASSED BY CALLER."""

        print(f"In deal cards. Num of cards in: \nDoor stack: {len(Moncurse.door_cards)}\nTreasure stack: {len(Treasure.treasure_cards)}\n"
              f"Burn pile: {len(cards.burn_pile)}\nIn-play stack: {len(cards.in_play)}\n") # dev print

        # Checks # CHANGE TO A FIRST IN FIRST OUT ALGORITHM FOR THE BURN CARDS SO ONLY GETTING WHAT IS NEEDED
        if deal_amount > len(Moncurse.door_cards):
            print(f"Not enough Door cards\nRESTOCKING WITH {[x['name'] for x in cards.burn_pile]}")
            cards.restock()
            print(f"cards left in burn pile after restock {cards.burn_pile}") # test for change
        if deal_amount > len(Treasure.treasure_cards):
            print(f"Not enough Treasure cards\nRESTOCKING WITH {[x['name'] for x in cards.burn_pile]}")
            cards.restock()

        # Main actions
        try:
            if option == "start":
                """called at start to deal specific number of cards to pass to player"""
                starter_set = []
                for i in range(deal_amount): # takes attrib of number of loops for card dealing (set by gameVar.Options)
                    dobj = Moncurse.door_cards.pop(randint(0, len(Moncurse.door_cards) - 1))
                    starter_set.append(dobj) # adds door card to list
                    tobj = Treasure.treasure_cards.pop(randint(0, len(Treasure.treasure_cards) - 1)) # gets card. better rand required
                    starter_set.append(tobj) # adds treasure card to list,
                    # print(f" num of cards in pack:{len(Moncurse.door_cards)}, rand gen tres:{tpack} door:{dpack}") # should go down
                return starter_set # returns starter_set list to caller (player.unsorted)

            elif option == "door":
                """Deal Door cards""" # will need condition for kicking door (placed on table) 2nd draw (player hand)
                print('Dealing from Door pile:')
                card = Moncurse.door_cards.pop(randint(0, len(Moncurse.door_cards) - 1))
                print(f"Your card is: {card['name']}\nCards left in Door deck: {len(Moncurse.door_cards)}\n")
                return card

            elif option == "treasure":
                """Deal Treasure cards"""
                print('Dealing from treasure pile')
                card_list = []
                for _amount in range(deal_amount): # supplies a number of treasure
                    card = Treasure.treasure_cards.pop(randint(0, len(Treasure.treasure_cards) - 1))
                    print(f"Treasure cards is: {card['name']}\nCards left in Door deck: {len(Treasure.treasure_cards)}\n")
                    card_list.append(card)
                return card_list
            else:
                print("CARD ERROR!!!!!")
        except ValueError:
            print("DECK EMPTY! NO CARDS AVAILABLE!!!!")


class Table(Treasure, Moncurse): # inherits from
    """This is the table model and the attributes expected from the game table"""
    def __init__(self):
        self.card_sop = Dealer() # has-a dealer
        self.burn_pile = []
        self.in_play = [[], [{'id': 301, "category": "door", 'type': 'monster', 'name': 'Dinosaur', 'lvl': 2, "static": ["no_outrun", 'test_meth']}]] # lol for first monster TEST MONSTER TODO REMOVE TEST
        self.fight_index = 0 # index of the monster to fight. 0 = standard first monster
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

    def restock(self):
        for card in self.burn_pile: # cards is the instance
            if card.get("category") == "door":
                Moncurse.door_cards.append(card)
                print(Moncurse.door_cards)
            else:
                Treasure.treasure_cards.append(card)
        print("Card decks refilled", "\nmonster cards =", len(Moncurse.door_cards),  "\nTreasure cards =", len(Treasure.treasure_cards),
              "\nBurn pile = ", len(self.burn_pile))


cards = Table() # ID PROBLEM ACROSS SCRIPTS THINK DOWN TO IMPORTS
dice = Table()


if __name__ == "__main__":

    z = cards.card_sop.deal_cards() # to be called further up stream for sorting
    # print("RETURNED VALUE:", z)

    print(dice.dice_sop.roll())


    # print(f"This is your treasure card:\n{y}")



