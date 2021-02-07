"""
local area for all tkinter variables use in the game.
This script is updated by gui_v3 with game-loop_v2 requesting data for the logic.


"""
from Munchkin.bin.players.playermodel import p1, p2, p3, p4, p5, p6, p7, p8, p9, p10


class StartVariables:

    # Start game variables
    new_players = 1
    players_available = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10]
    active_players = []


    #Player varaibles
    player_name = 'BOB'
    player_gender = 'male'

