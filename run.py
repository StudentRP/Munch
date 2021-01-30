""" calling this will trigger the game to start"""


from Munchkin.bin.engine.game_loop_v2 import NumberOfPlayers

if __name__ == "__main__":
    """function call to start game """
    NumberOfPlayers().select_players() # starts game