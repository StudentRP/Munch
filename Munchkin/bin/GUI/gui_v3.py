""" New format gui
imports all scripts

Main tasks:
    create main start/exit window
    create player select toplevel
    create player name/sex entery toplevel
    create main toplevel window with 3 main frames(nav, player info, action window)


sub tasks:
    save/load capability


"""

import tkinter as tk
import tkinter.ttk as ttk





class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("200x200")
        self.title("Munchkin Dungeon")

        self.welcome = tk.Label(self, text="Welcome")
        self.welcome.pack()

        self.start = tk.Button(self, text="Start", command=self.launch)
        self.start.pack()
        self.num_of_players_IV = tk.IntVar()

    def launch(self):

        self.player_select = tk.Toplevel(self)
        # player_select.attributes('-fullscreen', True) # makes full screen
        self.player_select.geometry("600x600")
        self.player_select.title("Player Select")

        tk.Label(self.player_select, text="Please select number of players").pack()
        l1 = ttk.Spinbox(self.player_select, from_=1, to=6, increment=1, textvariable=self.num_of_players_IV)
        l1.focus()
        l1.pack()

        tk.Button(self.player_select, text="Continue", command=self.player_setup).pack()

    def player_setup(self):
        self.player_select.destroy() # destroys old toplevel window
        self.player_set = tk.Toplevel(self)
        self.player_set.focus_set() # focuses on window
        # player_set.attributes('-fullscreen', True) # makes full screen
        self.player_set.geometry("600x600")
        self.player_set.title("Player Info")


if __name__ == '__main__':
    app = Main()
    app.mainloop()
