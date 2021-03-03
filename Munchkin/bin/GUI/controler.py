import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v2 import gamefile
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar
from tkinter import messagebox



gamefont=('castellar', 12, 'bold')
window_color = "#160606" # Would like pic here of door
text_color ="#7A0600"
but_color = "#3EB0A1"

# number = 0

##########################################################################
# Main controller
##########################################################################


class Main(tk.Tk):
    """main controller class that interchanges frames, updates variables with the frames"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('500x200') # adding +x+y to the end provide window location
        self.title("Munchkin")
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        #### all player atribs to bind ####
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.level = tk.IntVar()
        self.bonus = tk.IntVar()
        self.wallet = tk.IntVar()
        # self.l_hand = tk.IntVar()

        "fills the dictionary, snapshot built instance frames"
        for frm in StartPg, PlayerSelect, MainLoop:
            frame = frm(container, self) # passes container as the parent
            self.frames[frm] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPg)

    def show_frame(self, content):
        """brings the fame to the fore front"""
        frame = self.frames[content]
        frame.tkraise()

    def update_frame(self):
        """binds all the labels to the gamevar"""
        self.geometry("800x500") # changes the geometry when called
        self.name.set(gameVar.PlayerAtribs.player_name)
        self.gender.set(gameVar.PlayerAtribs.player_gender)
        self.level.set(gameVar.PlayerAtribs.player_level)
        self.bonus.set(gameVar.PlayerAtribs.player_bonus)
        self.wallet.set(gameVar.PlayerAtribs.player_wallet)
        # self.l_hand.set(gameVar.PlayerAtribs.player_weapons["L_hand"])


##########################################################################
# frames to build up interface
##########################################################################

class StartPg(tk.Frame):
    """Starting page with options to enhance game play"""
    # window_color = "#160606" # Would like pic here of door
    # text_color ="#7A0600"
    # but_color = "#3EB0A1"

    def __init__(self, parent, controller): # access to Main methods through the controller
        tk.Frame.__init__(self, parent)
        self.config(bg=window_color)

        label = tk.Label(self, text=f"{cs.start()}") # massage
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)

        but1 = tk.Button(self, text='Continue', command=lambda: controller.show_frame(PlayerSelect))
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack()
        but1.focus_set()

        but2 = tk.Button(self, text="Options", command=self.options)
        but2.config(bg=but_color, fg=text_color, padx=40, activebackground='yellow', relief="raised")
        but2.pack(side="bottom")

    def options(self):
        """top level options screen"""
        GameOptions()


class GameOptions(tk.Toplevel):
    """Toplevel window for setting in game options at start""" # WORKS need others added and style tidying
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.inital_deal = tk.IntVar()
        self.maxlvl = tk.IntVar()
        self.permadeath = tk.BooleanVar()
        self.carry_weight = tk.IntVar()


        self.geometry("275x275+400+50")

        lf = tk.LabelFrame(self, text="Game Options")
        lf.config(font=gamefont)
        lf.pack(fill='both', expand=True)

        l1 = tk.Label(lf, text="Number of starting cards")
        l1.grid(column=0, row=0)
        e1 = tk.Entry(lf, textvariable=self.inital_deal)
        self.inital_deal.set(4)
        e1.icursor(1) # sets index of cursor ready for change
        e1.focus() # focuses on entry
        e1.grid(column=1, row=0)

        l2 = tk.Label(lf, text="Set max level")
        l2.grid(column=0, row=1)
        e2 = tk.Entry(lf, textvariable=self.maxlvl)
        self.maxlvl.set(10)
        e2.grid(column=1, row=1)

        l2 = tk.Label(lf, text="Max sack capacity")
        l2.grid(column=0, row=2)
        e2 = tk.Entry(lf, textvariable=self.carry_weight)
        self.carry_weight.set(10) # change when cards are categorised, should be 6
        e2.grid(column=1, row=2)

        l3 = tk.Label(lf,text="Perm-a-death")
        l3.grid(column=0, row=3)
        cbut = tk.Checkbutton(lf, variable=self.permadeath)
        cbut.grid(column=1, row=3, sticky="w")

        b1 = tk.Button(lf, text="OK", command=self.setopts)
        b1.config(padx=20)
        b1.grid(column=0, row=4, columnspan=2)

    def setopts(self):
        """binds sack size to gameVar changing the number of cards you can carry"""
        gameVar.Options.cards_delt = self.inital_deal.get()
        gameVar.Options.win_lvl = self.maxlvl.get()
        gameVar.Options.perm_death = self.permadeath.get()
        gameVar.Options.carry_weight = self.carry_weight.get()
        message = f"Starting deal: {gameVar.Options.cards_delt}\nWin level:{gameVar.Options.win_lvl}\n" \
                  f"Carry weight: {gameVar.Options.carry_weight}\nPerm_a_death: {gameVar.Options.perm_death}"
        messagebox.showinfo("Settings Changed!", message)
        GameOptions.destroy(self)


class PlayerSelect(tk.Frame):
    """Selection on number of players """
    def __init__(self, parent, controller): # controller always passed in from main
        tk.Frame.__init__(self, parent)
        self.Num_of_players = tk.IntVar() # (int) of players in session
        self.count = tk.IntVar() # gameVar.StartVariables.new_players
        self.config(bg=window_color)

        label = tk.Label(self, text="Select number of players")
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.Num_of_players)
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="Confirm", command=self.playersetter)
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack(side="bottom")

    def playersetter(self):
        """Binds values from spinbox to gui_var for later use and calls next stage"""
        gameVar.StartVariables.new_players = self.Num_of_players.get() # int for Playerinfo toplevel window generation per player
        gameVar.StartVariables.player_rand = self.Num_of_players.get() # binds in 2nd location for later used in indexing
        gamefile.select_players() # sets in motion player slice in game_loop..
        PlayerInfo() # calls toplevel for name and gender entry for each player


class PlayerInfo(tk.Toplevel):
    """Top level for players to enter names and gender. Must: update title label with player number, store variables
    from entries, call game_loop with index para, increment index"""
    counter = 1 # player identity title number for arbitrary label
    indexing = 0 # index to access correct player instance in list. Ensures player details are bound to the correct instance

    def __init__(self):
        tk.Toplevel.__init__(self)
        """throw-away vars for names/gender """
        self.instname = tk.StringVar() # does not use Main self.name as no access as no controller passed on
        self.instgender = tk.StringVar()
        """main toplevel setup"""
        self.geometry('350x150+500+300')
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side='top', fill='both', expand=True)
        self.mainframe.focus_set()  # foucus on this window objects
        self.mainframe.grab_set()  # modal form

        self.arbitary = tk.Label(self.mainframe, text=f"Player {PlayerInfo.counter}") #title
        self.arbitary.config(font=('castellar', 15, 'bold'), fg='blue')
        self.arbitary.grid(column=0, row=0, columnspan=2, sticky='n,e,s,w')

        self.namelab = tk.Label(self.mainframe, text='Name: ')
        self.namelab.grid(column=1, row=1, sticky='w')
        self.nameent = tk.Entry(self.mainframe, textvariable=self.instname)
        self.nameent.grid(column=2, row=1, sticky='w,e')
        self.nameent.focus_set()

        self.genderlab = tk.Label(self.mainframe, text='Gender: ')
        self.genderlab.grid(column=1, row=2, sticky='w')
        self.nameent = ttk.Combobox(self.mainframe, textvariable=self.instgender, values=["Male", "Female"])
        self.nameent.grid(column=2, row=2, sticky='w')

        self.but2 = tk.Button(self.mainframe, text='Confirm', command=self.inital_set)
        self.but2.config(bd=10, activebackground='green')
        self.but2.grid(column=2, row=4, columnspan=2, sticky='n,e,s,w')
        self.bind('<Return>', self.inital_set)  # creates event to be passed to test

    def inital_set(self, event=None):
        """button handler, binds name/gender to gameVar, increments arbitrary label and index for ensuring correct player instance,
         """
        number = gameVar.StartVariables.new_players # (int) derived from gui_var .
        if number >= 1:
            number -= 1 # decreases the num of new pLayer integer
            PlayerInfo.counter += 1 # increase player counter for arbitrary label in __init__
            gameVar.PlayerAtribs.player_name = self.instname.get() # entered name binds to gameVar
            gameVar.PlayerAtribs.player_gender = self.instgender.get() # entered gender binds to gameVar
            gamefile.player_name_gender(PlayerInfo.indexing) # call game_loop with index for player instance
            PlayerInfo.indexing = PlayerInfo.indexing + 1 # increases player index ensuring correct player attribute assignment
            print("Destroying toplevel")
            PlayerInfo.destroy(self) #destoys toplevel window
            gameVar.StartVariables.new_players = number # reduces number in gameVar for next  player in loop

            if number != 0: # loop for next player
                PlayerInfo() # rebuilds toplevel anew for next player
            else:
                PlayerInfo.destroy(self)
                #~~~~~~~~ TO BE REMOVED + LOOP BELOW
                print("Players in game:")
                for players in gameVar.StartVariables.session_players: # loop to see all player names
                    print(players.name.title()) # checks all players names for activity
                #~~~~~~~~~~~~~~~

                gamefile.rand() # gets a random player from the active player list, auto calls varbinging binding all variables.
                app.update_frame() # updates all lable variables from gameVar
                app.show_frame(MainLoop) # calls next frame to raise by controller
                ########## deal cards to all players required


####################################################################################################################
class MainLoop(tk.Frame):
    """3 frames with game loop, function required to set index at random place """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        "frame for buttons - may create some buttons to inherit style from "
        self.butframe = tk.LabelFrame(self, text='Navigation')
        self.butframe.config(bg=but_color)
        self.butframe.pack(side='bottom', fill='x', ipady=80)

        self.b1 = tk.Button(self.butframe, text="End Turn", command=self.end_turn)
        self.b1.config(activebackground='#0ABF28', bg="#B40BEE", padx=15, pady=20)
        self.b1.place(x=600, y=45)

        self.b2 = tk.Button(self.butframe, text="Kick Door", command=self.door)
        self.b2.config(activebackground='#0ABF28', bg="#082EF6", padx=5)
        self.b2.place(x=350, y=45)

        self.b3 = tk.Button(self.butframe, text="Weapons", command=self.list_weapons)
        self.b3.place(x=250, y=10)
        self.b4 = tk.Button(self.butframe, text="Armour", command=self.list_armour)
        self.b4.place(x=225, y=45)
        self.b5 = tk.Button(self.butframe, text="Consumables", command=self.consumables)
        self.b5.place(x=250, y=80)

        self.b6 = tk.Button(self.butframe, text="Sell", command=self.list_sell)
        self.b6.config(padx=15)
        self.b6.place(x=450, y=10)
        self.b7 = tk.Button(self.butframe, text="Sack", command=self.list_sack) ########### used as dummy atm
        self.b7.config(padx=10)
        self.b7.place(x=475, y=45)
        self.b8 = tk.Button(self.butframe, text="Visible", command=self.list_visible)
        self.b8.place(x=450, y=80)

        self.b9 = tk.Button(self.butframe, text="Interfere", command=self.interfere)
        self.b9.place(x=10, y=10)
        self.b10 = tk.Button(self.butframe, text="Help", command=self.ask_for_help)
        self.b10.place(x=10, y=10)

        "frame player attribs"
        self.plframe = tk.LabelFrame(self, text='Player Info')
        self.plframe.config(pady=20)
        self.plframe.pack(side='left', fill="y", ipadx=50)

        self.l1 = tk.Label(self.plframe, text="Name: ")
        self.l1.grid(row=0, column=1, sticky='nsew')
        self.l1b = tk.Label(self.plframe, textvariable=controller.name)  ## works binding strait to stringvar in Main
        self.l1b.grid(row=0, column=2, sticky='nsew')

        self.l2 = tk.Label(self.plframe, text="Gender: ")
        self.l2.grid(row=1, column=1, sticky='nsew')
        self.l2b = tk.Label(self.plframe, textvariable=controller.gender)  ## works binding strait to stringvar in Main
        self.l2b.grid(row=1, column=2, sticky='nsew')

        self.l3 = tk.Label(self.plframe, text="Level: ")
        self.l3.grid(row=2, column=1, sticky='nsew')
        self.l3b = tk.Label(self.plframe, textvariable=controller.level)  ## works binding strait to stringvar in Main
        self.l3b.grid(row=2, column=2, sticky='nsew')

        self.l4 = tk.Label(self.plframe, text="Bonus: ")
        self.l4.grid(row=3, column=1, sticky='nsew')
        self.l4b = tk.Label(self.plframe, textvariable=controller.bonus)  ## works binding strait to stringvar in Main
        self.l4b.grid(row=3, column=2, sticky='nsew')

        self.l5 = tk.Label(self.plframe, text="Wallet: ")
        self.l5.grid(row=4, column=1, sticky='nsew')
        self.l5b = tk.Label(self.plframe, textvariable=controller.wallet)  ## works binding strait to stringvar in Main
        self.l5b.grid(row=4, column=2, sticky='nsew')

        # self.l6 = tk.Label(self.plframe, text="Left hand")
        # self.l6.grid(row=5, column=1, sticky='nsew')
        # self.l6b = tk.Label(self.plframe, text=controller.l_hand)
        # self.l6b.grid(row=5, column=2, sticky='nsew')


        "Game Window"
        self.tblframe = tk.LabelFrame(self, text='Table')
        self.tblframe.config(bg='lightgrey'),
        self.tblframe.pack(side="left", fill="both", expand=True)

    "Handlers"
    def end_turn(self):
        """require method to be called from gameloop to rebase all variables in guivar. this should update the var in Mainloop
        with app.update_frame() method call"""
        gamefile.player_order(gameVar.StartVariables.active_player) # sends active player rebind new player in game_loop
        app.update_frame() # updates the tk.vars in Main under the instance controller.

    def door(self):
        """game actions for door. cards drawn from door"""
        print(f"{app.name.get()} has kicked open the door!")

    def list_weapons(self):
        """method calling toplevel that details all weapons currently owned with options to add/remove, sell and charity"""
        print("This will be the weapons toplevel")
        player = gameVar.StartVariables.active_player
        player.inventory("type", "weapon")
        print(gameVar.StartVariables.selected_items)
        OwnedItems()

    def list_armour(self):
        print("This will be the armour toplevel")
        player = gameVar.StartVariables.active_player
        player.inventory("type", "armor")
        print(gameVar.StartVariables.selected_items)
        OwnedItems()

    def consumables(self):
        print("This will be the toplevel for throwable and other once only objects")

    def list_sell(self):
        print("This will be the toplevel for sellable items with radio/tick boxes")
        player = gameVar.StartVariables.active_player
        player.item_by_key("sell")
        print(gameVar.StartVariables.selected_items)
        OwnedItems()

    def interfere(self):
        print("Toplevel window where another player can interfere with play")

    def ask_for_help(self):
        print("Toplevel window where another player can help... for a price..")

    def list_sack(self):
        print("Your sack contains:")
        print(f"{gameVar.PlayerAtribs.player_unsorted}") #~~~~~~~~~~~~to change to sack
        gameVar.StartVariables.selected_items = gameVar.PlayerAtribs.player_unsorted
        OwnedItems()

    def list_visible(self):
        print("This will be the visible cards toplevel")


class OwnedItems(tk.Toplevel):

    def __init__(self, key= None):
        tk.Toplevel.__init__(self)
        self.key = key

        if not gameVar.StartVariables.selected_items:
            f = tk.Frame(self)
            tk.Label(f, text="No cards to shop").grid(row=0, column=0)

        else:
            f = tk.Frame(self)
            f.pack(side="top", expand=True)
            tk.Label(f, text="Name").grid(row=0, column=0, sticky="nw")
            tk.Label(f, text="Des").grid(row=0, column=1, sticky="nw")
            tk.Label(f, text="Sell").grid(row=0, column=2, sticky="nw")
            tk.Label(f, text="Equip").grid(row=0, column=3, sticky="nw")

            for lab in gameVar.StartVariables.selected_items:
                f1 = tk.Frame(self)
                f1.pack(side="top", expand=True)
                l1 = tk.Label(f1, text=lab['name'])
                l1.grid(row=0, column=0, sticky="nw")
                l2 = tk.Label(f1, text=lab['type'])
                l2.grid(row=0, column=1, sticky="nw")
                tk.Checkbutton(f1, text=" ").grid(row=0, column=2, sticky="nw")
                tk.Radiobutton(f1, text=" ").grid(row=0, column=3, sticky="nw")

app = Main()

app.mainloop()

# Main().mainloop(),