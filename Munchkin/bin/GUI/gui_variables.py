"""
local area for all tkinter variables use in the game.
This script is updated by gui_v3 with game-loop_v2 requesting data for the logic.


"""
from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10


class StartVariables:

    # Start game variables
    new_players = 1 # (int) number associated to total players in current game
    players_available = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    active_players = None # (list) generated list slice for all session players
    player_rand = 1 # number for random player generator
    rand_player = None # set to bind at game start a random player
    rand_index = 0 # for the above player
    message = None


class Options:
    """variables associated to start options that may be manipulated changing win parameters ect"""
    win_lvl = 10 # sets the leve that triggers win
    carry_weight = 8 # number of cards allowed in sack
    cards_delt = 4 # number of each card type delt at start or on resurrection #4 std
    perm_death = False # dead players do not come back


class PlayerAtribs:

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
    player_alive = True
    player_longevity = 1


