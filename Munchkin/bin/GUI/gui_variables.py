"""
local area for all tkinter variables use in the game.
This script is imported in gui_v3 and game-loop_v2 so variable may be passed around


"""

from tkinter import *


class Starting:
    root =Tk()
    player_numbers = IntVar(root)
    pass
