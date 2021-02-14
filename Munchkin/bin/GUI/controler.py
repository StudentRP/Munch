import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v2 import gamefile
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar
from random import randint

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

        "fills the dictionary"
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
        self.name.set(gameVar.PlayerAtribs.player_name)
        self.gender.set(gameVar.PlayerAtribs.player_gender)

    # def other(self, updates):
    #     app.update(updates)



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
        Playerinfo() #calls toplevel
        # self.setplayers()


class Playerinfo(tk.Toplevel):
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

        self.arbitary = tk.Label(self.mainframe, text=f"Player {Playerinfo.counter}") #title
        self.arbitary.config(font=('castellar', 15, 'bold'), fg='blue')
        self.arbitary.grid(column=0, row=0, columnspan=2, sticky='n,e,s,w')

        self.namelab = tk.Label(self.mainframe, text='Name: ')
        self.namelab.grid(column=1, row=1, sticky='w')
        self.nameent = tk.Entry(self.mainframe, textvariable=self.instname)
        self.nameent.grid(column=2, row=1, sticky='w,e')
        self.nameent.focus()

        self.genderlab = tk.Label(self.mainframe, text='Gender: ')
        self.genderlab.grid(column=1, row=2, sticky='w')
        self.nameent = ttk.Combobox(self.mainframe, textvariable=self.instgender, values=["Male", "Female"])
        self.nameent.grid(column=2, row=2, sticky='w')

        self.but2 = tk.Button(self.mainframe, text='Confirm', command=self.test)
        self.but2.config(bd=10, activebackground='green')
        self.but2.grid(column=2, row=4, columnspan=2, sticky='n,e,s,w')
        self.bind('<Return>', self.test)  # creates event to be passed to test

    def test(self, event=None):
        number = gameVar.StartVariables.new_players # (int) devrived for playersetter.
        if number >= 1:
            number -= 1 # decreases the num of new pLayer integer
            Playerinfo.counter += 1 # increase player counter for arbitrary label in __init__
            gameVar.PlayerAtribs.player_name = self.instname.get() # changes name in gameVar script
            gameVar.PlayerAtribs.player_gender = self.instgender.get() # changes name in gameVar script
            gamefile.player_name_gender(Playerinfo.indexing) # call game loop for name to instance # indexing works ~~~~OK~~~
            Playerinfo.indexing = Playerinfo.indexing + 1
            print("destroying toplevel")
            Playerinfo.destroy(self) #destoys toplevel window
            gameVar.StartVariables.new_players = number
            # conditional needed to stop window building for non existant player
            if number != 0:
                Playerinfo() # rebuilds toplevel anew
            else:
                Playerinfo.destroy(self)
                print("No players left")
                for players in gameVar.StartVariables.active_players: # loop to see all player names
                    print(players.name) # checks all players names for activity

                # HERE!!! call some sort of random funct to deside which player goes first. and sets a gamevar.
                playerinstance = gamefile.varseter(gameVar.StartVariables.player_rand)
                print(f" player Level IS::: {playerinstance.level}")

                app.update_frame() # updates all tk Vars in Main class.
                print(app.name.get(), "call to main class")
                app.show_frame(MainLoop) # calls next frame to raise by controller


####################################################################################################################
class MainLoop(tk.Frame):
    """3 frames with game loop, function required to set index at random place """

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.plframe = tk.LabelFrame(self, text='Player Info')
        self.plframe.config(bg='green'),
        self.plframe.pack(side='left', fill='both', expand=True)

        self.l1 = tk.Label(self.plframe, text="Name: ")
        self.l1.grid(row=0, column=1, sticky='nsew')
        self.l2 = tk.Label(self.plframe, textvariable=controller.name) ## works binding strait to stringvar in Main
        self.l2.grid(row=0, column=2, sticky='nsew')

        self.l3 = tk.Label(self.plframe, text="Gender: ")
        self.l3.grid(row=1, column=1, sticky='nsew')
        self.l4 = tk.Label(self.plframe, textvariable=controller.gender)  ## works binding strait to stringvar in Main
        self.l4.grid(row=1, column=2, sticky='nsew')

        self.b1 = tk.Button(self.plframe, text="next player", command=self.rebuild)
        self.b1.grid(row=3, column=0, columnspan=2)

    def rebuild(self):
        """require method to be called from gameloop to rebase all variables in guivar. this should update the var in Mainloop"""
        # method to pass new instance index to gameloop.
        playerinst = gamefile.varseter(gameVar.StartVariables.player_rand)
        app.update_frame() # updates the tk.vars in Main under the instance controller.
        gamefile.player_order(playerinst) # calls main game loop to loop over game cycle
        print(f"in rebuld: {playerinst.bonus}") # this works, creator = 200



app = Main()

app.mainloop()

# Main().mainloop(),