import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v2 import gamefile
# import bin.engine.game_loop_v2 as engine
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
        # self.NumOfPlayers = tk.IntVar()

        "fills the dictionary"
        for frm in StartPg, PlayerSelect, MainLoop:
            frame = frm(container, self) # passes container as the parent
            self.frames[frm] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPg)

    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()

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
        but1.focus()


class PlayerSelect(tk.Frame):
    """player number select"""
    def __init__(self, parent, controller): # controller always passed in from main
        tk.Frame.__init__(self, parent)
        self.NumOfPlayers = tk.IntVar()
        self.instname = tk.StringVar()
        self.instgender = tk.StringVar()
        self.counter = tk.IntVar() #gameVar.StartVariables.player_counter
        self.counter.set(1)
        self.count = tk.IntVar() #gameVar.StartVariables.new_players

        label = tk.Label(self, text="Select number of players")
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.NumOfPlayers)
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="Confirm", command=self.playersetter)
        but1.pack()
        #but2 for window progression move to final player setup
        # but2 = tk.Button(self, text='Confirm', command=lambda: controller.show_frame(MainLoop)) # change method but use
        # this setup for moving onto next frame
        # but2.pack()

    def playersetter(self):
        """ isolates the StringVar from setplayers()"""
        gameVar.StartVariables.new_players = self.NumOfPlayers.get()
        gamefile.select_players() # sets in motion player slice in game_loop
        Playerinfo() #calls toplevel
        # self.setplayers()


class Playerinfo(tk.Toplevel):
    """must: update title label with player number, store variables from entries, call game_loop with index para,
    increment index,  """
    counter = 1
    indexing = 0


    def __init__(self):
        tk.Toplevel.__init__(self)
        self.instname = tk.StringVar()
        self.instgender = tk.StringVar()

        self.geometry('350x150+500+300')
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side='top', fill='both', expand=True)
        self.mainframe.focus_set()  # foucus on this window objects
        self.mainframe.grab_set()  # modal form

        self.arbitary = tk.Label(self.mainframe, text=f"Player {Playerinfo.counter}")
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
        number = gameVar.StartVariables.new_players
        # number = x
        print(number)

        if number >= 1:
            print('setting up player: ', number)
            number -= 1 # decreases the num of new pLayer integer
            Playerinfo.counter += 1 # increase player counter for arbitrary label in __init__
            gameVar.StartVariables.player_name = self.instname.get() # changes name in gameVar script
            gameVar.StartVariables.player_gender = self.instgender.get() # changes name in gameVar script
            gamefile.player_name_gender(Playerinfo.indexing) # call game loop for name to instance # indexing works ~~~~OK~~~
            Playerinfo.indexing = Playerinfo.indexing + 1
            print("destroying toplevel")
            Playerinfo.destroy(self) #destoys toplevel window
            gameVar.StartVariables.new_players = number
            # conditional needed to stop window building for non existant player
            if number != 0:
                Playerinfo() # recalls toplevel anew

            else:
                Playerinfo.destroy(self)
                print("no players left")
                for players in gameVar.StartVariables.active_players:
                    print(players.name) # checks all players names for activity


####################################################################################################################
class MainLoop(tk.Frame):
    """3 frames with game loop"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        plframe = tk.LabelFrame(self, text='Player Info')
        plframe.config(bg='green')
        plframe.pack(side='left', fill='y', expand=True)

        # b1 = tk.Button(plframe, text='hi')
        # b1.config(bg='red')
        # b1.grid(row=0, column=0, sticky='nsew')
        l1 = tk.Label(plframe, text='Name: ')
        l1.grid(row=0, column=1, sticky='nsew')
        l2 = tk.Label(plframe, text='BOB')
        l2.grid(row=0, column=2, sticky='nsew')
        b1 = tk.Button(self, text="change", command=lambda:changename())

        #
        # cmdframe = tk.Frame(self)
        # cmdframe.config(bg='blue')
        # cmdframe.pack(side=tk.LEFT, fill=tk.X, expand=tk.Y)
        # l3 = tk.Label(cmdframe, text='ho')
        # l3.pack()
        # l4 = tk.Label(cmdframe, text='foo')
        # l4.pack()

        # crdframe = tk.Frame(self)
        # crdframe.config(bg='red')
        # crdframe.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.Y)




# app = Main()
#
# app.mainloop()

Main().mainloop()