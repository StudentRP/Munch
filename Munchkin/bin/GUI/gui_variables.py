"""
local area for all tkinter variables use in the game.
This script is updated by gui_v3 with game-loop_v2 requesting data for the logic.


"""
from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10


class StartVariables:

    # Start game variables
    new_players = 1 # (int) number associated to total players in current game
    player_rand = 1  # number for random player generator for PlayerSelect.playersetter
    players_available = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10] #all available players !to be sliced!
    session_players = None # (list) generated list slice from game_loop with all player instances in active session
    active_player = None # selected random player from active players. becomes next player
    # selected_items = [] # list of playing cards ready to be looped over. ie all weapons from player items
    message = None


class GameObjects:
    all_cards = [] # simple list of all cards
    selected_items = []  # list of playing cards of particular type . ie all weapons from player.unsorted
    check_but_intvar_gen = [] # populated with callable objects from checkbutton
    check_but_boo = [] # populated with checkbutton return values from intVar() objects
    check_but_card_ids = [] # populated with card id's
    zipped_tup = [] # populated with bools of card ids & fetched checkbutton from (check_but_card_ids, check_but_boo)


class Options:
    """variables associated to start options that may be manipulated changing win parameters ect"""
    win_lvl = 10 # sets the leve that triggers win
    carry_weight = 8 # number of cards allowed in sack
    cards_delt = 4 # number of each card type delt at start or on resurrection #4 std
    perm_death = False # dead players do not come back


class PlayerAtribs:
    """Must mirror whats in game_loop.PlayerSetUp.verbinding and call to bind here!"""
    player_ref = 0
    player_name = 'BOB' # current session player name
    player_gender = 'male'  # current session player gender
    player_level = 1
    player_bonus = 0
    player_wallet = 0
    player_race = {'r1': True, 'r2': False}
    player_weapons = {"L_hand": None, "R_hand": None, "big": None, "special_1": None, "special_2": False}
    player_armor = {"headgear": None, "armor": None, "armor1": False, "armor2": False, "footgear": None,
                  "special_1": None, "special_2": False, "special_3": False}
    player_sack = []
    player_visible_cards = []
    player_hireling = []
    player_undefined = []
    player_unsorted = []
    player_alive = True
    player_longevity = 1


