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
from PIL import Image, ImageTk
import bin.engine.game_loop_v2 as engine
import bin.engine.cut_scenes as cs


# variables
# NumOfPlayers = tk.IntVar()



class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("300x200")
        self.title("Munchkin Dungeon")

        ## for background image on main start win
        # self.canvas = tk.Canvas(self, width=300, height=400)
        # self.canvas.pack()
        # self.img = ImageTk.PhotoImage(Image.open().resize((WIDTH, HEIGTH), Image.ANTIALIAS))
        # self.canvas.background = self.img  # Keep a reference in case this code is put in a function.
        # self.bg = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)
        # button_window = self.canvas.create_window(10, 10, anchor=tk.NW, window=self.start)
        # label_window = self.canvas.create_window(10, 10, anchor=tk.NW, window=self.self.welcome)

        self.welcome = tk.Label(self, text=f"{cs.start()}")
        self.welcome.pack()

        self.start = tk.Button(self, text="Start", command=self.launch)
        self.start.pack()

        # game variables .to be called by export
        self.NumOfPlayers = tk.IntVar()
        self.player_name = tk.StringVar()


    def setplayers(self):
        print(f'player: {self.NumOfPlayers.get()}')
        y = self.NumOfPlayers.get()
        engine.gui_num_of_players = self.NumOfPlayers.get() # sets the num of players in engine script
        engine.NumberOfPlayers() # calls class in engine scrip setting up all class attribs  #####################
        #need to start engine class without passing self to it!

    def launch(self):

        self.player_select = tk.Toplevel(self)
        # player_select.attributes('-fullscreen', True) # makes full screen
        self.player_select.geometry("600x600")
        self.player_select.title("Player Select")

        tk.Label(self.player_select, text="Please select number of players").pack()
        l1 = ttk.Spinbox(self.player_select, from_=1, to=10, increment=1, textvariable=self.NumOfPlayers)
        l1.focus()
        l1.set(1)
        l1.pack()
        tk.Button(self.player_select, text='Confirm', command=self.setplayers).pack()  ##### move val
        tk.Button(self.player_select, text="Continue", command=self.player_setup).pack()

    def player_setup(self):
        self.player_select.destroy() # destroys old toplevel window
        self.player_set = tk.Toplevel(self)
        self.player_set.focus_set() # focuses on window
        # player_set.attributes('-fullscreen', True) # makes full screen
        self.player_set.geometry("600x600")
        self.player_set.title("Player Info")
        tk.Label(self.player_set, textvariable=self.NumOfPlayers).pack(side=tk.BOTTOM)
        tk.Label(self.player_set, textvariable=self.player_name).pack(side=tk.BOTTOM)
        print(self.NumOfPlayers)

# app = Main() # having this will run the script twice. in any other script it will cause them to trigger when imported!!

if __name__ == '__main__':
    app = Main()
    app.mainloop()
