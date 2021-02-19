import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v2 import gamefile
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar


# number = 0

##########################################################################
# Main controller
##########################################################################


class Main(tk.Tk):
    """main controller class that interchanges frames"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('400x400') # adding +x+y to the end provide window location
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

        "fills the dictionary, snapshot built frames"
        for frm in StartPg, PlayerSelect, MainLoop:
            frame = frm(container, self) # passes container as the parent
            self.frames[frm] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPg)

    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()

    def update_frame(self):
        """binds all the labels to the gamevar"""
        self.geometry("600x600") # changes the geometry when called
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
    """Starting page """
    def __init__(self, parent, controller): # access to Main methods through the controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f"{cs.start()}") # massage
        label.pack(pady=10, padx=10)
        but1 = ttk.Button(self, text='Continue', command=lambda: controller.show_frame(PlayerSelect))
        but1.pack()
        but1.focus_set()


class PlayerSelect(tk.Frame):
    """player number select"""
    def __init__(self, parent, controller): # controller always passed in from main
        tk.Frame.__init__(self, parent)
        self.Num_of_players = tk.IntVar() # (int) of players in session
        self.count = tk.IntVar() # gameVar.StartVariables.new_players

        label = tk.Label(self, text="Select number of players")
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.Num_of_players)
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="Confirm", command=self.playersetter)
        but1.pack()

    def playersetter(self):
        """ isolates the StringVar from setplayers()"""
        gameVar.StartVariables.new_players = self.Num_of_players.get() # int for Playerinfo toplevel window generation per player
        gameVar.StartVariables.player_rand = self.Num_of_players.get() # binds in 2nd location for later used in indexing
        gamefile.select_players() # sets in motion player slice in game_loop
        PlayerInfo() #calls toplevel
        # self.setplayers()


class PlayerInfo(tk.Toplevel):
    """must: update title label with player number, store variables from entries, call game_loop with index para,
    increment index,  """
    counter = 1 # player identity title number
    indexing = 0 # index to pass to game loop for player list index. Ensures player details are bound to the correct instance

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.instname = tk.StringVar() # does not use Main self.name as no access as no controller passed on
        self.instgender = tk.StringVar()

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
        number = gameVar.StartVariables.new_players # (int) devrived for playersetter.
        if number >= 1:
            number -= 1 # decreases the num of new pLayer integer
            PlayerInfo.counter += 1 # increase player counter for arbitrary label in __init__
            gameVar.PlayerAtribs.player_name = self.instname.get() # changes name in gameVar script
            gameVar.PlayerAtribs.player_gender = self.instgender.get() # changes name in gameVar script
            gamefile.player_name_gender(PlayerInfo.indexing) # call game loop for name to instance # indexing works ~~~~OK~~~
            PlayerInfo.indexing = PlayerInfo.indexing + 1
            print("destroying toplevel")
            PlayerInfo.destroy(self) #destoys toplevel window
            gameVar.StartVariables.new_players = number
            # conditional needed to stop window building for non existant player
            if number != 0:
                PlayerInfo() # rebuilds toplevel anew
            else:
                PlayerInfo.destroy(self)
                print("Players in game:") # TO BE REMOVED + LOOP BELOW
                for players in gameVar.StartVariables.active_players: # loop to see all player names
                    print(players.name.title()) # checks all players names for activity

                gamefile.rand() # gets a random player from the active player list, auto calls varbinging.
                app.update_frame() # updates all lable variables from gameVar
                app.show_frame(MainLoop) # calls next frame to raise by controller
                ########## deal cards to all players required


####################################################################################################################
class MainLoop(tk.Frame):
    """3 frames with game loop, function required to set index at random place """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        "frame for buttons - may create some buttons to inherit style from "
        self.butframe = tk.LabelFrame(self, text='Buttons')
        self.butframe.config(bg='#C7D6D8'),
        self.butframe.pack(side='bottom', fill='x', ipady=80)

        self.b1 = tk.Button(self.butframe, text="End Turn", command=self.rebuild)
        self.b1.config(activebackground='#0ABF28', bg="#F60808", padx=20, pady=30)
        self.b1.place(x=700, y=45)

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
        self.b7= tk.Button(self.butframe, text="Sack", command=self.list_sack)
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
    def rebuild(self):
        """require method to be called from gameloop to rebase all variables in guivar. this should update the var in Mainloop
        with app.update_frame() method call"""
        # gamefile.rand() # change for pick up order methods
        gamefile.player_order(gameVar.StartVariables.rand_player) # sends random player to method for order creation
        app.update_frame() # updates the tk.vars in Main under the instance controller.

    def door(self):
        """game actions for door. cards drawn from door"""
        print(f"{app.name.get()} has kicked open the door!")

    def list_weapons(self):
        print("This will be the weapons toplevel")
        # gameVar.PlayerAtribs.player_weapons["L_hand"]="Big hammer"
        # app.update_frame()

    def list_armour(self):
        print("This will be the armour toplevel")

    def consumables(self):
        print("This will be the toplevel for throwable and other once only objects")

    def list_sell(self):
        print("This will be the toplevel for sellable items with radio/tick boxes")

    def interfere(self):
        print("Toplevel window where another player can interfere with play")

    def ask_for_help(self):
        print("Toplevel window where another player can help... for a price..")

    def list_sack(self):
        print("This will be the sack toplevel")

    def list_visible(self):
        print("This will be the visible cards toplevel")


app = Main()

app.mainloop()

# Main().mainloop(),