""" calling this will trigger the game to start"""


from Munchkin.bin.engine.game_loop_v3 import PlayerSetUp

if __name__ == "__main__":
    """function call to start game """
    PlayerSetUp().select_players() # starts game