"""Main GUI interface for munchkin.

Requires hierarchy structure with frameview swapping

"""
import tkinter as tk

class InfoRefresh:
    """class to set reconfigure label widgets"""
    def refresh(self, playerinstace):
        Build.name.config(text=playerinstace.name)





class Build(tk.Tk):
    """build of frames"""
    def __init__(self, parent):
        tk.Tk().__init__(parent)
        name = tk.Label()