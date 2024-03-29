"""
..IPC script..
local area for all tkinter variables use in the game linking view.py with engine(controller.py).
This script is updated by gui_v3 with game-loop_v2 requesting data for the logic.


"""
from bin.all_cards.table import cards



class StartVariables:

    # Start game variables
    new_players = 1 # (int) number associated to total players in current game
    player_rand = 1  # number for random player generator for PlayerSelect.player_set_up
    selected_items = [] # list of playing cards ready to be looped over. ie all weapons from player items
    cards = cards


class GameObjects:
    """Main game objects"""
    message = ""
    message2 = ""

    session_players = []  # holds player instances
    active_player = None # points to current player instance
    interfering_player = [] # player instances that are interefearing with play.
    all_cards = [] # simple list of all cards #  for listing whole inventory
    selected_items = []  # list of playing cards of particular type . ie all weapons from player.unsorted
    checkbut_intvar_obj = [] # populated with callable objects from checkbutton
    check_but_boo = [] # populated with checkbutton return values from intVar() objects
    check_but_card_ids = [] # populated with card id's
    zipped_tup = [] # populated with bools of card ids & fetched checkbutton from (check_but_card_ids, check_but_boo)
    card_transfer = [] # intermediate storage for cards from player selection to a method action ie monster for wandering monster NOT USED YET!
    session_index = None # during gameplay used to index session_players

class FightComponents:
    assists = [] # list of player instances that are helping in the fight.
    player_aid = [] # list of int to be summed and added in the players favor
    monster_aid = [] # list of ints to be summed and used against the player
    # consumables = [] # for all objects that are thrown #loop over to run card_meth(method='off') ad add to burn # NOT USED
    card_selector_index = 0 # complementary to card_list_selection
    card_list_selection = [] # holds the list of cards/players associated to the radio selection process ready for index selection


class Interfering:
    card_storage = '' # for a card to be held temporarily
    card_storage2 = ''


class Options:
    """variables associated to start options that may be manipulated changing win parameters ect"""
    win_lvl = 10 # sets the leve that triggers win
    carry_weight = 6 # number of cards allowed in player sack. #6 std
    cards_dealt = 2 # >>>>>>>>>>>>> number of each card type delt at start or on resurrection. #4 std
    perm_death = False # dead players do not come back


class CardDraw:
    """card variables associated to game play."""
    door_attempts_remaining = 1 #default = 1 (True)


class PlayerAttribs:
    """Must mirror what's in controller.PlayerSetUp.verbinding and call to bind here!"""
    player_ref = 0
    player_name = 'BOB' # default
    player_gender = 'Male'  # default
    player_level = 1
    player_bonus = 0
    player_wallet = 0

    player_race = ""
    player_race2 = ""
    player_klass = ""
    player_klass2 = ""

    player_l_hand = ""
    player_r_hand = ""
    player_two_hand = ""

    player_headgear = ""
    player_necklace = ""
    player_armor = ""
    player_knees = ""
    player_footgear = ""

    player_sack = []
    player_visible_cards = []
    player_hireling = []
    player_undefined = []
    player_unsorted = []
    player_alive = True
    player_longevity = 1


