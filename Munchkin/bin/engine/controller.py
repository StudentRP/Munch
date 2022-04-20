"""
Controller provudes backend logic to the view script and makes changes to variable library
Initiates player personalisation and runs game cycle for each player fetching cards and initiation
each scene of play

Contents functions:
    rand * picks single player from list of players
    varbinding * binds all player attribs to IPC script
    dealhandler *



"""


from Munchkin.bin.players.playermodel import Player
from Munchkin.bin.all_cards.table import dice # , cards
from random import randint, choice
import bin.GUI.variables_library as library
from itertools import cycle

from bin.GUI.variables_library import cards
print('controller', id(library.cards))
from time import sleep




##################################################################
# main loop
##################################################################
""" V4.0  """


class PlayerSetUp:
    """class to determine number of players and hand to player order"""
    card_from_engine = cards

    def __init__(self):
        self.cycle = 0 #needed?

# meths associated to play setup

    def active_player_creation(self):
        """ calls Player.factory creating player instances"""
        for person in range(library.StartVariables.new_players + 1):
            player = Player.factory()
            library.GameObjects.session_players.append(player)
        self.deal_handler("start")

    def player_name_gender(self, playerindex): # gui attrib, passes session_players index identifying specific instance
        """Gets player with list index and Sets name and gender to that player instance."""
        player = library.GameObjects.session_players[playerindex] #references a player objects from session_players
        player.char_setup() # call to set name and gender of player instance.

    def set_random_player(self):
        """Selects random player to start from session_players list. Binds player as active_player and calls
        method to load all attributes of the player (player_attrib_ipc_updater(). parameter is optional but explicit)"""
        player = choice(library.GameObjects.session_players) # selects random player from list of players
        library.GameObjects.active_player = player # assigns the selected player to active player in gamevar for gui to see
        library.GameObjects.message = f"The dice has been rolled. Random player selected is {player.name.title()}"
        self.player_attrib_ipc_updater(player) # arg not needed. Calls method to set all attribs in in gamevar of player

# class Game_Play:

    def player_order(self, current_player): # called with gameVar rand_index
        """Triggered at end of turn. Note 1st player was random and assigned to active_player after player creation.
        Current_player = active player"""
        play = True # win condition need method that will check all players
        player_gen = cycle(library.GameObjects.session_players) # generator function that cycles a list indefinitely
        y = next(player_gen) # yields players from the list, at start this would be first item = p1.
        while play:
            if current_player == y and current_player.alive: # conditions to see if x==y (x= player, y=list item)
                print(f"Current player {current_player.name} turn ended\n")
                library.GameObjects.active_player = next(player_gen) # binds next player to rand_player, (changes x)
                self.player_attrib_ipc_updater(library.GameObjects.active_player) #  binds new player
                print(f"{library.GameObjects.active_player.name} has been binded")
                break
            elif current_player == y and not current_player.alive and not library.Options.perm_death:
                print(f"print player {current_player} is dead") # move in to conditional for perm-a-death
                current_player.alive = True # resets player status ##########need per-a-death bit here
                library.GameObjects.active_player = next(player_gen) # changes x without binding and moves to next player
                continue
            else:
                print(f"{y.name.title()} did not match. Searching for player in list")
                y = next(player_gen) # changes y to find commonality to x

        library.GameObjects.message = f"{library.GameObjects.active_player.name.title()}'s turn..."

    def player_attrib_ipc_updater(self, playerinst=library.GameObjects.active_player): # defaults to gamevar active_player player
        """Binds all player atribs to gameVar for current player activity. Can take param of a player or grab active_player."""
        library.PlayerAtribs.player_name = playerinst.name.title()
        library.PlayerAtribs.player_gender = playerinst.gender.title()
        library.PlayerAtribs.player_level = playerinst.level
        library.PlayerAtribs.player_bonus = playerinst.bonus
        library.PlayerAtribs.player_wallet = playerinst.wallet
        library.PlayerAtribs.player_race = playerinst.race.title()
        library.PlayerAtribs.player_race2 = playerinst.race2.title()
        library.PlayerAtribs.player_klass = playerinst.klass.title()
        library.PlayerAtribs.player_klass2 = playerinst.klass2.title()
        library.PlayerAtribs.player_sack = playerinst.sack
        library.PlayerAtribs.player_l_hand = playerinst.update_bindings("L_hand")
        library.PlayerAtribs.player_r_hand = playerinst.update_bindings("R_hand")
        library.PlayerAtribs.player_two_hand = playerinst.update_bindings("two_hand")
        library.PlayerAtribs.player_headgear = playerinst.update_bindings("headgear")
        library.PlayerAtribs.player_armor = playerinst.update_bindings("armor")
        library.PlayerAtribs.player_knees = playerinst.update_bindings("knees")
        library.PlayerAtribs.player_footgear = playerinst.update_bindings("footgear")
        library.PlayerAtribs.player_necklace = playerinst.update_bindings("necklace")

# card handling class:

    def deal_handler(self, option, deal_amount=0):
        """ Sends requests to the dealer based on the option parameter to define card type.
        Deal_amount defines how many of the cards are to be returned to a player.
        """

        playerinst = library.GameObjects.active_player # gets current player. Not set at start default=None.

        if option == "start": # initial play selector to deal cards to each player. NO GOOD FOR RESURRECT OPTION as deals to all players
            for player in library.GameObjects.session_players: # loops over each player in session_players
                player.sack = cards.card_sop.deal_cards(option, cardnum=library.Options.cards_dealt) # deals cards with params "start" & num of cards to deal)

        elif option == "door": # Standard gameplay loop on door kick
            print("In deal_handler, retrieving door card & determining fate of card")  # test location
            door_card = cards.card_sop.deal_cards(option, cardnum=1) # fetches 1 door card,
            return door_card # for pic use only in gui

        elif option == "treasure": # Deal treasure, requires number for amount to deal.
            print("retrieving treasure card/s") # test location
            add_treasure = cards.card_sop.deal_cards(option, cardnum=deal_amount) # cardnum is usually determined by the treasures a monster holds.
            playerinst.sack = playerinst.sack + add_treasure # DUMPS ALL IN THE ACTIVE_PLAYER.....TODO::Sort how treasure is handled when used as currency for another players help

        elif option == "resurrect":
            if library.Options.perm_death:
                playerinst.sack = cards.card_sop.deal_cards("start", cardnum=library.Options.cards_dealt)
            else:
                print(f"Game over for {playerinst.name}, BUMMER!")

        else:
            print("option parameter not defined/matched in deal_handler")

    def door_card_designator(self, card, door_attempts=1): # for all door cards that are drawn from the pack or placed by another player.
        """Takes in door card and door_attempts as params to decide card fate.
        Cards have different fates dependent upon the type of card it is ie: monster, curse, other and the number of
        times the door button is clicked. Also update the message dependent on action
        """
        player = library.GameObjects.active_player

        if door_attempts: #On first kick of the door. Decides what to do with the cards dependent on situation

            # if monster, put on table ready to fight
            if card.get("type") == "monster": # if the cards a monster #1st/2nd kicks covered
                library.GameObjects.message = f"{card.get('name')} placed on table, Level {card.get('lvl')}" # updates broadcast message
                cards.in_play[0].append(card) # places card on table in the lol for the first fight.
                ## ACTIVATE CARD STATIC METHODS
                engine.card_activation(card, static='on')

                print("This is the card in play;", cards.in_play, 'id', id(cards.in_play)) # TEST INFO


            # WORK REQUIRED!!     if curse, activate effects. need check to see if conditions in place to stop cursing ie ork/ wishing ring.
            elif card.get("type") == "curse": # if the cards a monster #1st/2nd kicks covered
                library.GameObjects.message = f"The room you have entered has a curse {card.get('name').title()}.\n Lets hope you have protection!"
                print("In curse::", player.active_curses)
                # ~~~~~~~~~~~~~TODO  curse checker method required ie tin hat, ork ect
                if card.get("duration") == "persistent": # for constant effect curse
                    player.card_meths(card, "method", "on") # switches card on.
                    player.active_curses.append(card) # adds card to player curse list so method can be called o remove
                elif card.get("duration") == "one_shot": ########### matches card key to the one_shot action
                    player.card_meths(card, "method", "on")  ########## calls card method and switches it on TO BE REMOVED
                    cards.burn_pile.append(card) # disposes of to burn pile
                    print(f"card duration is one_shot, added to burn pile check:\nBurn pile {cards.burn_pile}")
                elif card.get("duration") == "timed": ########## for time dependent effect
                    library.GameObjects.message = f"timed curse card not configured yet" # overrides top message
                    #TODO meth for timed
                    cards.burn_pile.append(card) # disposes of to burn pile
                    print(f"card status is passive, should be added to burn pile!\nBurn pile {cards.burn_pile}")

            else: # for all other cards that have no direct effect or influence.
                print(f"Adding {card['name']}to sack.")
                player.sack.append(card)  # adds card to player's items
                library.GameObjects.message = f"Adding 2nd draw to sack." # need to be removed dont want to broadcast what other player gets
                return card  # to show if first time only 2nd it hides

        else:
            "2nd kick of door (looting room). Will need condition statement if player wants to fight mon from hand, rather than std flow to sack"
            print("adding to sack")
            library.GameObjects.message = "2nd kck, Adding card to sack"  # 2nd kick
            player.sack.append(card)  # adds to player sack

    def zipper(self, action):
        """zips card id's to checkbox bools from selected_list. Used for all card sorting regardless of card type.
        action is conduit for card_matcher"""
        library.GameObjects.zipped_tup.clear()  # clears tup list ready for new entry. not working...................
        for status in library.GameObjects.check_but_intvar_gen: # gets attribute from object then from the attribute which is an object gets the value stored (list>intvar>get()>1 or 0)
            library.GameObjects.check_but_boo.append(status.get()) # creates a list of 1s & 0s from check buttons status
            x, y = library.GameObjects.check_but_card_ids, library.GameObjects.check_but_boo
            library.GameObjects.zipped_tup = list(zip(x, y)) # result [(card_id,  bool), (card_id, bool)]
        # print("moving to player script", gameVar.GameObjects.zipped_tup) # checker shows all cleared lists
        self.card_matcher(action)

    def card_matcher(self, action):
        """compares tuple to selected_items searching for matching card ids and only passes on cards that contain
        a tuple with the boolean true. Action determines the whats happening to the cards next. """
        for card in library.GameObjects.selected_items: # for every card in selected_items
            for tup in library.GameObjects.zipped_tup: # go over every tuple in  zipped_tup. (card_id, bool tuples).
                if tup[0] == card["id"] and tup[1]: # if tup id matches card fid from selected items and bool is True from the checkbox
                    if action == "sell":
                        library.GameObjects.active_player.sell_item(card)
                    elif action in "equip, disposable ,use": # equip/disposable will be treasures
                        self.tri_qualifier(card) # test ~~ok~~
                    elif action == "remove":
                        player = library.GameObjects.active_player
                        player.equipped_items("removal", card)

    def tri_qualifier(self, card):
        """ Checks player attribs against an item card before it can be used by the player. Split into 2 parts:
        1st: checks card for a specific restriction that would count against a player due to a specific attrib, ie if u are human u cant use this card.
        2nd part: """

        player = library.GameObjects.active_player

        checks = {player.race: "race_requirement", player.race2: "race_requirement", player.klass: "klass_requirement",
                  player.klass2: "klass_requirement", player.gender: "gender_requirement"} # card specific requirements to use
        flag = 1 # True

        for player_attribs, card_requirement in checks.items():
            # checks card restrict method lexical for non use cases. If found player cant use.
            if card.get('restriction', False): # checks to see if there is a key named 'restriction' in card if not return False
                print("Searching card restriction method")
                if player_attribs in card.get('restriction'):  # checks all player attribs to see if in restricted treasure card list #
                    # THINK ABOUT CARDS YOU ARE APPLYING THEM TOO; TREASURE!
                    print('Restriction found in card')
                    if player.name == "The_Creator":  # dev mode
                        print(f"{player_attribs} - Restriction avoided: Dev path")
                        break
                    else: # sets flag so card cant be used
                        print('Restricted, card cant be used.')
                        flag = 0
                        break
            # checks cards for player dependent attribs to use card
            if card.get(card_requirement):  # checks card to see if requirement present
                if card.get(card_requirement) == player_attribs: # if race_requirement = 'human' == player.race = 'human' change flag and break out of loop
                    print(f"Main path for: {card_requirement}")
                    continue # checks next requirement parameter for conformance
                elif player.name == "The_Creator":  # dev mode
                    print(f"{player_attribs} - Dev path")
                    continue
                else:
                    library.GameObjects.message = f"You cant use this card, {card_requirement}"
                    flag = 0
                    # gameVar.StartVariables.message = f"{card.get('name')} can not be quipped: {val}." # not working
                    break

        if flag: # only if flag remains True, compliant to non restrictions.
            if card["category"] == "treasure":  # for all treasure cards the player uses that was from their hand
                self.player_treasure_cards(card) # for the use of treasure cards
            # elif card["category"] == "door":  # for all enhancers ect that the player has from their hand  DO DOOR CARDS REALLY COME DOWN THIS ROUTE! however thowables???
            #     self.player_door_cards(card) # for the use of door cards

    def player_treasure_cards(self, card):
        """method to sort the locations of treasure cards that the player has selected"""
        player = library.GameObjects.active_player
        if card.get("type") == "armor":
            player.equip_armor(card)  # leads to player meth for placing in right place
        elif card.get("type") == "weapon":
            player.equip_weapon(card)
        elif card.get("type") == "disposable":  # for disposable throwable only
            pass  # meth for selecting target and changing bonuses, # TODO
        else:
            pass # for all other cards ie steeds

    def player_door_cards(self, card): #card meth#####################################################
        player = library.GameObjects.active_player
        player.card_meths(card, "method", "on")  # link to player to card meths.
        print(player.klass_unlock, player.race_unlock)  # only shows at end of turn due to meth restriction in class,
        # meths added at end_turn

    def scrub_lists(self):
        """Clears all appended list that are not capable of clearing."""
        library.GameObjects.selected_items.clear()  # clears the card objects list
        library.GameObjects.check_but_intvar_gen.clear()  # clears list of intVar objects from check buttons
        library.GameObjects.check_but_boo.clear()  # clears boolean list
        library.GameObjects.check_but_card_ids.clear()  # clears card id list
        library.GameObjects.zipped_tup.clear()  # clears tup list

##################################################################
    def fight(self, helper=0, additional=0):# helper would be other player interactions. additional is anything else
        """for cards that are monsters and placed on the table"""
        print("In the fight!")
        card = cards.in_play.pop() # end of cards on table
        player = library.GameObjects.active_player
        player.card_meths(card, 'static', 'on') # turns on card static content for fight TODO change to something more relevant than "static"
        if player.bonus + player.level + helper + library.Fight_enhancers.player_aid \
                >= card["lvl"] + library.Fight_enhancers.monster_aid: # consideration required for player consumables and enhancers
            print("Player wins!")
            reward = card['treasure']
            self.deal_handler('treasure', deal_amount=reward) # fetches treasure for player
            library.GameObjects.message = f"You win! You have found {reward} treasures for your trouble."
            player.level += card["level_up"]
            cards.burn_pile.append(card) # removes card
            player.card_meths(card, 'static', 'off') # turns off static card content
            print(f"cards in the burn pile: {len(cards.burn_pile)}")
            return "win"
        # need action to go up lvl note some cards do more than one level!
        else:
            library.GameObjects.message = "Fight lost"
            print("Fight lost")
            player.card_meths(card, 'method', 'on') # calls card bad stuff
            player.card_meths(card, 'static', 'off') # turns off static effect of card in play
            return "lose"

    def card_method_activator(self, scenario, action, table_card_index): # will need to be a selector
        """method to activate a card dependent upon the scenario of having a specific monster/ curse/ item in play and action to
        switch on or off the condition"""
        card = cards.in_play[int(table_card_index)][0] # selects the monster in the fight on the table
        player = library.GameObjects.active_player
        if scenario == "persistent":
            player.card_meths(card, 'static', action)  ######## will cause probs with monster individuality ######################

    def card_activation(self, card, *args, **kwargs):
        player = library.GameObjects.active_player
        print('card received for processing..................')
        print('Action required for:', player.name, args, kwargs)
        pass

    def run(self):
        roll = dice.dice_sop.roll()
        player = library.GameObjects.active_player
        print(f"You rolled a {roll}.")
        if roll >= player.run:
            print(f"You rolled a {roll}. You out ran your pursuer.")
            remove = cards.in_play.pop(0)
            player.card_meths(remove, 'static', 'off')# turns off static card content
            cards.burn_pile.append(remove)
            return "success"
        else:
            print("Tried to run and slipped. Things are gona get ugly!\n")
            # only fight is available now so that cna handle all the logic
            return "fail"

engine = PlayerSetUp()

if __name__ == "__main__":

    # NumberOfPlayers().select_players() # starts game by activating NOP building the objects, and activating select_players
    # running wach line.
    engine.player_name_gender()






# old
# def door_card_designator(self, card, door_attempts=1):  # for all door cards that are drawn from the pack
#     """method that sort the cards that the player draws from the deck during play. This could be monster, curse ect.
#     door0-attempts is used to determine how many times the door has been kicked in a turn and in 2nd instance the door is put into the
#     players hand unseen. Mechanism is also used to trigger a curse
#     """
#     player = gameVar.GameObjects.active_player
#
#     if door_attempts:
#         if card.get("type") == "monster":  # if the cards a monster #1st/2nd kicks covered
#             if door_attempts:  # determines if first kick of door (T or F), if 1 = first kick
#                 gameVar.GameObjects.message = f"{card.get('name')} placed on table, Level {card.get('lvl')}"
#                 cards.in_play.append(
#                     card)  # adds to table # careful as cards selected from hand will go strait to table
#                 print(
#                     f"In door_card_designator, monster added to table. Returned card is: {[x['name'] for x in cards.in_play]}\n")
#             else:
#                 print("adding to sack")
#                 gameVar.GameObjects.message = "Adding card to sack"  # 2nd kick
#                 player.sack.append(card)  # adds to player sack
#
#         elif card.get("type") == "curse":  # if the cards a monster #1st/2nd kicks covered
#             if door_attempts:  # 1st kick
#                 print("In curse::", player.curses)
#                 gameVar.GameObjects.message = "You have been cursed!"  # look at card meth and action
#                 player.card_meths(card, "method", "on")  # actions curs card as soon as picked up
#                 if card.get("status") == "active":  # for constant effect curse
#                     player.curses.append(card)  # adds card to player curse list
#                 elif card.get("status") == "passive":  # for one shot effect
#                     cards.burn_pile.append(card)  # disposes of to burn pile
#                     print(f"card status is passive, should be added to burn pile!\nBurn pile {cards.burn_pile}")
#             else:
#                 gameVar.GameObjects.message = "Adding card to sack"
#                 player.sack.append(card)
#
#         else:  # for all other cards that have no direct effect or influence.
#             print(f"Adding {card['name']}to sack.")
#             if door_attempts:
#                 player.sack.append(card)  # adds card to player's items
#                 gameVar.GameObjects.message = f"Adding/using {card.get('name')}."
#                 return card  # to show if first time only 2nd it hides
#             else:
#                 gameVar.GameObjects.message = "Adding 2nd card to sack"
#                 player.sack.append(card)
