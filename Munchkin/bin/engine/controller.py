"""
Controller provides backend logic to the view script and makes changes to variable library
Initiates player personalisation and runs game cycle for each player fetching cards and initiation
each scene of play

Contents functions:
    rand * picks single player from list of players
    varbinding * binds all player attribs to IPC script
    dealhandler *



"""

from bin.players.playermodel import Player
from bin.all_cards.table import dice
from random import choice
import bin.GUI.variables_library as library
from itertools import cycle
from bin.GUI.variables_library import cards
import Tests.process_logger as logger # std output
print('controller', id(library.cards))

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
        """ Calls Player factory creating player instances"""
        logger.log_note('active_player_creation. x2 >>\n')
        for person in range(library.StartVariables.new_players):
            player = Player.factory() # << Player instance Returned
            library.GameObjects.session_players.append(player) # players added to session players
        self.deal_handler("start") # >> GO TO

    def player_name_gender(self, playerindex): # expects index for session_players
        """Gets player with list index and Sets name and gender to that player instance."""
        player = library.GameObjects.session_players[playerindex] #references a player objects from session_players
        player.char_setup() # call to set name and gender of player instance.
        logger.log_note(f'Player_name_gender creation complete.')

    def set_random_player(self):
        """Selects random player to start from session_players list. Binds player as active_player and calls
        method to load all attributes of the player (player_attrib_ipc_updater(). parameter is optional but explicit)"""
        player = choice(library.GameObjects.session_players) # selects random player from list of players
        library.GameObjects.active_player = player # assigns the selected player to active player in library for gui to see
        library.GameObjects.session_index = library.GameObjects.session_players.index(library.GameObjects.active_player) #sets index
        self.player_attrib_ipc_updater(player)  # arg not needed. Calls method to set all attribs in library of player
        library.GameObjects.message = f"The dice has been rolled. Random player selected is {player.name.title()}"
        logger.log_note(f"Setting Random player to start:{player.name}\n")
# class Game_Play:

    def player_order(self, current_player): # called with library rand_index
        """Triggered at end of turn. Note 1st player was random and assigned to active_player after player creation.
        Current_player = active player"""
        play = True # win condition need method that will check all players #TODO create new end pg with winner on it
        player_gen = cycle(library.GameObjects.session_players) # address for generator function object
        y = next(player_gen) # yields players from the list, at start this would be first item = p1.
        while play:
            if current_player == y and current_player.alive: # if current player == next(player_gen)
                logger.log_note(f"\nPlayer {library.GameObjects.active_player.name} turn ended\n")
                library.GameObjects.active_player = next(player_gen) # binds next player to rand_player, (changes x)
                logger.log_note(f"New player:{library.GameObjects.active_player.name} bound\n")
                break
            elif current_player == y and not current_player.alive and not library.Options.perm_death:
                logger.log_note(f"Player {current_player.name} is dead. Spawned next round.\n") # move in to conditional for perm-a-death
                current_player.alive = True # resets player status
                library.GameObjects.active_player = next(player_gen) # changes x without binding and moves to next player
                continue
            else:
                logger.log_note(f"{y.name.title()} did not match. Searching for player in list\n")
                y = next(player_gen) # changes y to find commonality to x

        library.GameObjects.message = f"{library.GameObjects.active_player.name.title()}'s turn..."

    def player_attrib_ipc_updater(self, player_instant):
        """Binds all player attribs to library for current player activity. Can take param of a player or grab active_player.
            player_attrib_ipc_updater >> library << app.update_attrib_frame.
        """

        library.PlayerAttribs.player_name = player_instant.name.title()
        library.PlayerAttribs.player_gender = player_instant.gender.title()
        library.PlayerAttribs.player_level = player_instant.level
        library.PlayerAttribs.player_bonus = player_instant.bonus
        library.PlayerAttribs.player_wallet = player_instant.wallet
        library.PlayerAttribs.player_race = player_instant.race.title()
        library.PlayerAttribs.player_race2 = player_instant.race2.title()
        library.PlayerAttribs.player_klass = player_instant.klass.title()
        library.PlayerAttribs.player_klass2 = player_instant.klass2.title()
        library.PlayerAttribs.player_sack = player_instant.sack
        library.PlayerAttribs.player_l_hand = player_instant.update_bindings("L_hand")
        library.PlayerAttribs.player_r_hand = player_instant.update_bindings("R_hand")
        library.PlayerAttribs.player_two_hand = player_instant.update_bindings("two_hand")
        library.PlayerAttribs.player_headgear = player_instant.update_bindings("headgear")
        library.PlayerAttribs.player_armor = player_instant.update_bindings("armor")
        library.PlayerAttribs.player_knees = player_instant.update_bindings("knees")
        library.PlayerAttribs.player_footgear = player_instant.update_bindings("footgear")
        library.PlayerAttribs.player_necklace = player_instant.update_bindings("necklace")

# card handling class:

    def deal_handler(self, option, deal_amount=1):
        """ Sends requests to the dealer based on the option parameter to define card type.
        Deal_amount defines how many of the cards are to be returned to a player.
        """
        logger.log_note(f"\t> Deal_handler({option}) >>")

        playerinst = library.GameObjects.active_player # gets current player. Not set at start default=None.

        if option == "start": # initial play selector to deal cards to each player. NO GOOD FOR RESURRECT OPTION as deals to all players
            for player in library.GameObjects.session_players: # loops over each player in session_players
                player.sack = cards.card_sop.deal_cards(option, deal_amount=library.Options.cards_dealt) # deals cards with params "start" & num of cards to deal) >> GO TO
            logger.log_note(f"Cards added to player sack. END\n")

        elif option == "door": # Standard gameplay loop on door kick
            print("In deal_handler, retrieving door card & determining fate of card")  # test location
            door_card = cards.card_sop.deal_cards(option, deal_amount) # fetches 1 door card defined by the default,
            return door_card # for pic use only in gui

        elif option == "treasure": # Deal treasure, requires number for amount to deal dependent on win.
            print("retrieving treasure card/s") # test location
            add_treasure = cards.card_sop.deal_cards(option, deal_amount=deal_amount) # cardnum is usually determined by the treasures a monster holds.
            playerinst.sack = playerinst.sack + add_treasure # DUMPS ALL IN THE ACTIVE_PLAYER.....TODO::Sort how treasure is handled when used as currency for another players help

        elif option == "resurrect":
            if library.Options.perm_death:
                playerinst.sack = cards.card_sop.deal_cards("start", deal_amount=library.Options.cards_dealt)
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
        if door_attempts: # On first kick of the door. Decides what to do with the cards dependent on situation

            # if monster, put on table ready to fight
            if card.get("type") == "monster": # if the cards a monster #1st/2nd kicks covered
                library.GameObjects.message = f"{card.get('name')} placed on table, Level {card.get('lvl')}" # updates broadcast message
                # cards.in_play[0].append(card) # places card on table in the lol for the first fight.
                cards.in_play.append([card]) # places the card into play creating lol structure
                logger.log_note(f"Cards in play{cards.in_play}\n")
                player.card_meths(card, static='on') # activates any static meths for the card. TESTED WITH 2 CARDS. OK!

            # WORK REQUIRED!!     if curse, activate effects. need check to see if conditions in place to stop cursing ie ork/ wishing ring.
            elif card.get("type") == "curse": # if the cards a monster #1st/2nd kicks covered
                library.GameObjects.message = f"The room you have entered has a curse {card.get('name').title()}.\n Lets hope you have protection!"
                logger.log_note(f"In curse:: {player.active_curses}")

                player.card_meths(card, method='on') # turns on curse method on ## TEST

                # # ~~~~~~~~~~~~~TODO  curse checker method required ie tin hat, ork ect
                ### think moving all this to the cards
                # if card.get("duration") == "persistent": # for constant effect curse
                #     player.card_meths(card, "method", "on") # switches card on.
                #     player.active_curses.append(card) # adds card to player curse list so method can be called o remove
                # elif card.get("duration") == "one_shot": ########### matches card key to the one_shot action
                #     player.card_meths(card, "method", "on")  ########## calls card method and switches it on TO BE REMOVED
                #     cards.burn_pile.append(card) # disposes of to burn pile
                #     print(f"card duration is one_shot, added to burn pile check:\nBurn pile {cards.burn_pile}")
                # elif card.get("duration") == "timed": ########## for time dependent effect
                #     library.GameObjects.message = f"timed curse card not configured yet" # overrides top message
                #     #TODO meth for timed
                #     cards.burn_pile.append(card) # disposes of to burn pile
                #     print(f"card status is passive, should be added to burn pile!\nBurn pile {cards.burn_pile}"),

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

    def zipper(self, action): # passes action on to next meth
        """zips card id's to checkbox ints from check_but_obj. Used for all card sorting regardless of card type.
        action is conduit for card_matcher"""
        library.GameObjects.zipped_tup.clear()  # clears tup list ready for new card_id/ checkbut value pair.
        for status in library.GameObjects.checkbut_intvar_obj: # loops all tk intVar objects stored in checkbut_intvar_obj list
            library.GameObjects.check_but_boo.append(status.get()) # creates a list of 1s & 0s from check buttons status (True|False)
            x, y = library.GameObjects.check_but_card_ids, library.GameObjects.check_but_boo
            library.GameObjects.zipped_tup = list(zip(x, y)) # >>>>> binds card id to the checkbuttion result forming: [(card_id,  bool), (card_id, bool), ect] <<<<<<
        # print("moving to player script", gameVar.GameObjects.zipped_tup) # checker shows all cleared lists
        self.card_matcher(action)

    def card_matcher(self, action):
        """compares tuple to selected_items searching for matching card ids and only passes on cards that contain
        a tuple with the boolean true. Action determines the whats happening to the cards next. """
        for card in library.GameObjects.selected_items: # for every card in selected_items
            for tup in library.GameObjects.zipped_tup: # go over every tuple in  zipped_tup. (card_id, bool tuples).
                if tup[0] == card["id"] and tup[1]: # if tup[0] (card_id) matches card id in selected_items and bool is True (1) from the checkbox
                    if action == "sell":
                        library.GameObjects.active_player.sell_item(card)
                    elif action in "equip, disposable ,use": # equip/disposable will be treasures
                        self.tri_qualifier(card)
                    elif action == "remove":
                        player = library.GameObjects.active_player
                        player.equipped_items("removal", card)
                    elif action == 'interfere': # test needed
                        if not library.Interfering.card_storage:
                            library.Interfering.card_storage = card
                        else:
                            library.Interfering.card_storage2 = card

    def tri_qualifier(self, card, player_obj=None):
        """ Checks player attribs against an item card before it can be used by the player. Split into 2 parts:
        1st: checks card for a specific restriction that would count against a player due to a specific attrib, ie if u are human u cant use this card.
        2nd part: """

        player = library.GameObjects.active_player

        checks = {player.race: "race_requirement", player.race2: "race_requirement", player.klass: "klass_requirement",
                  player.klass2: "klass_requirement",
                  player.gender: "gender_requirement"}  # card specific requirements to use
        flag = 1  # True

        for player_attribs, card_requirement in checks.items():
            # checks card restrict method lexical for non use cases. If found player cant use.
            if card.get('restriction',
                        False):  # checks card to see if there is a key named 'restriction'. if not return False
                print("Searching card restriction method")
                if player_attribs in card.get(
                        'restriction'):  # checks all player attribs to see if in restricted treasure card list # Returns True if match
                    print('Restriction found')
                    if player.name == "The_Creator":  # dev mode
                        print(f"{player_attribs} - Restriction avoided: Dev path")
                        break
                    else:  # sets flag so card cant be used
                        print('Restricted, card cant be used.')
                        flag = 0
                        break
            # checks cards for player dependent attribs to use card
            if card.get(card_requirement):  # checks card to see if requirement present
                if card.get(
                        card_requirement) == player_attribs:  # if race_requirement = 'human' == player.race = 'human' change flag and break out of loop
                    print(f"Main path for: {card_requirement}")
                    continue  # checks next requirement parameter for conformance
                elif player.name == "The_Creator":  # dev mode
                    print(f"{player_attribs} - Dev path")
                    continue
                else:
                    library.GameObjects.message = f"You cant use this card, {card_requirement}"
                    flag = 0
                    # gameVar.StartVariables.message = f"{card.get('name')} can not be quipped: {val}." # not working
                    break

        if flag:  # only if flag remains True, compliant to non restrictions.

            if card["category"] == "treasure":  # for all treasure cards the player uses that was from their hand
                self.player_treasure_cards(card)  # for the use of treasure cards
            elif card["category"] == "door":  # for all enhancers ect that the player has from their hand  DO DOOR CARDS REALLY COME DOWN THIS ROUTE! however thowables???
                self.player_door_cards(card)  # for the use of door cards

    def player_treasure_cards(self, card):
        """method to sort the locations of treasure cards that the player has selected"""
        player = library.GameObjects.active_player
        if card.get("type") == "armor":
            player.equip_armor(card)  # leads to player meth for placing in right place
        elif card.get("type") == "weapon":
            player.equip_weapon(card)
        elif card.get("type") == "disposable":  # for disposable throwable only
            player.card_meths(card, methood='on')
        else:
            pass # for all other cards ie steeds

    def player_door_cards(self, card): #card meth #####################################################

        player = library.GameObjects.active_player
        player.card_meths(card, method="on")  # link to player to card meths.
        print('unlocking:', player.klass_unlock, player.race_unlock)  # only shows at end of turn due to meth restriction in class,
        # meths added at end_turn

    def scrub_lists(self):
        """Clears all appended list that are not capable of clearing."""
        library.GameObjects.selected_items.clear()  # clears the card objects list
        library.GameObjects.checkbut_intvar_obj.clear()  # clears list of intVar objects from check buttons
        library.GameObjects.check_but_boo.clear()  # clears boolean list
        library.GameObjects.check_but_card_ids.clear()  # clears card id list
        library.GameObjects.zipped_tup.clear()  # clears tup list

##################################################################
    def fight(self, card_set, helpers=False):
        """for cards that are monsters and placed on the table."""
        # if can send card meths athe set for processing would solve lots of probs
        # notes; card meths will be switched on in interfere and kick door, no meths to activate here other than loose

        print("\nIn the fight!")
        self.flag = None # fight outcome
        player = library.GameObjects.active_player

        if helpers: # adds ints of player stats to player_aid ready for final sum !!!!!!! WIPE LIST AT THE END
            for assist in helpers:
                '''adds all players bonuses/ lvls to to the player_aid list'''
                library.FightComponents.player_aid.append(assist.level)
                library.FightComponents.player_aid.append(assist.bonus)

        #TODO send set to burn pile after
        for card in card_set:
            if card['type'] == 'monster':
                library.FightComponents.monster_aid.append(card['lvl']) # adds monster level to monster_aid list
            else:
                '''turns all cards methods'''
                if card.get['target', False]: # add to cards a target for the interfere option
                    if isinstance(card['target'], dict):
                        library.FightComponents.player_aid.append(card['bonus'])
                    else:
                        player.card_meths(card, method='on') #

        sum_of_all_positives = player.bonus + player.level + sum(library.FightComponents.player_aid) # All +ves added by player/s
        sum_of_all_negatives = sum(library.FightComponents.monster_aid) # All -ves added by cards through interfere
        print('sum_of_all_positives:', sum_of_all_positives)
        print('sum_of_all_negatives:', sum_of_all_negatives)

        card = card_set[0] # monster card
        print('card 0 is::::::::')
        print(card)

        if sum_of_all_positives >= sum_of_all_negatives: # consideration required for player consumables and enhancers
            print("Player wins!")
            reward = card['treasure']
            self.deal_handler('treasure', deal_amount=reward) # fetches treasure for player
            library.GameObjects.message = f"You win! You have found {reward} treasures for your trouble."
            player.level += card["level_up"]
            # cards.burn_pile.append(card) # removes card
            # player.card_meths(card, 'static', 'off') # turns off static card content
            print(f"cards in the burn pile: {len(cards.burn_pile)}")
            self.flag = "win"
        # need action to go up lvl note some cards do more than one level!
        else:
            library.GameObjects.message = "Fight lost"
            print("Fight lost")
            player.card_meths(card, 'method_bs', 'on') # calls card bad stuff
            player.card_meths(card, 'static', 'off') # turns off static effect of card in play
            self.flag = "lose"

        for disposed_card in card_set:
            library.cards.add_to_burn(disposed_card)

        # if card set in position 0 activate all static meths
        if library.cards.in_play: # if cards still in play
            library.FightComponents.card_selector_index = 0 # index reset to 0 for next card_set unless another monster is selected
            print('final call to loop:', cards.in_play[library.FightComponents.card_selector_index])
            for card in cards.in_play[library.FightComponents.card_selector_index]:
                player.card_meths(card, 'static') # turns on all static meths for the next fight

        return self.flag

    def radio_selector_handler(self, index, obj_list):
        """takes in index and a list of monster/mon/players where the index has relevance"""
        print('RadioSelector list and index are now bound')
        library.FightComponents.card_selector_index = index # stores the index in the library
        library.FightComponents.card_list_selection = obj_list # list of all selected

        player = library.GameObjects.active_player
        print(f'index:', index)
        if index == 0: # turn off door activated meths and any interfering card meths in that set
            for card in library.cards.in_play[0]:
                player.card_meths(card, static='off')
        else: # turns on new set
            for card in library.cards.in_play[index]:
                player.card_meths(card, static='on')

    # def card_method_activator(self, scenario, action, table_card_index): # deprecated method
    #     """method to activate a card dependent upon the scenario of having a specific monster/ curse/ item in play and action to
    #     switch on or off the condition"""
    #     card = cards.in_play[int(table_card_index)][0] # selects the monster in the fight on the table
    #     player = library.GameObjects.active_player
    #     if scenario == "persistent":
    #         player.card_meths(card, 'static', action)  ######## will cause probs with monster individuality ######################
    def interfere(self, player, target): # TODO finalise
        """ working progress"""
        card1 = library.Interfering.card_storage
        card2 = library.Interfering.card_storage2
        if isinstance(target, dict): # for targeting a monster
            if card1['type'] == 'wondering monster': # may need more conditions dependent on the cards that require more than 1 card
                target.card_meths(card1, card2, method='on') # wandering + monster
            elif card1['type'] == 'modifier':
                pass # needs to be added to the card_set but which one....

        else: # target is player
            # target.card_meths(card1, method='on') ## not quite right need meth to consider items given,
            if card1['type'] == 'curse': # most use case..
                target.card_meths(card1, method='on') # card does check on player

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
