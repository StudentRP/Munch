import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v2 import gamefile
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar


##########################################################################
# Main controller
##########################################################################


class Main(tk.Tk):
    """main controller class that interchanges frames"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('600x600') # adding +x+y to the end provide window location
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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.NumOfPlayers = tk.IntVar()
        self.instname = tk.StringVar()
        self.instgender = tk.StringVar()

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
        gamefile.select_players()
        self.setplayers()

    def setplayers(self,):
        """form for player info, counter linked to gui_var """
        count = gameVar.StartVariables.new_players # count down for if loop for players (to be reduced in engine)

        if count >= 1:

            playobj = tk.Toplevel()
            playobj.geometry('350x150+500+300')
            mainframe = tk.Frame(playobj)
            mainframe.pack(side='top', fill='both', expand=True)
            mainframe.focus_set() #foucus on this window objects
            mainframe.grab_set() # modal form

            arbitary = tk.Label(mainframe, text=f"Player {count}")
            arbitary.config(font=('castellar', 15, 'bold'), fg='blue')
            arbitary.grid(column=0, row=0, columnspan=2, sticky='n,e,s,w')

            namelab = tk.Label(mainframe, text='Name: ')
            namelab.grid(column=1, row=1, sticky='w')
            nameent = tk.Entry(mainframe, textvariable=self.instname)
            nameent.grid(column=2, row=1, sticky='w,e')
            nameent.focus()

            genderlab = tk.Label(mainframe, text='Gender: ')
            genderlab.grid(column=1, row=2, sticky='w')
            nameent = ttk.Combobox(mainframe, textvariable=self.instgender, values=["Male", "Female"])
            nameent.grid(column=2, row=2, sticky='w')

            but2 = tk.Button(mainframe, text='Confirm', command=self.test)
            but2.config(bd=10, activebackground='green')
            but2.grid(column=2, row=4, columnspan=2, sticky='n,e,s,w')

        else:
            Main.controller.show_frame(MainLoop)

    def test(self):
        # bind entries, call player class method, clear entries and recall set players
        gameVar.StartVariables.player_name = self.instname.get()
        gameVar.StartVariables.player_gender = self.instgender.get()
        gamefile.player_name_gender() # iteration required to


        print(f"player name: {self.instname.get().title()}\nplayer gender: {gameVar.StartVariables.player_gender}")
        print(f'player are set to: {self.NumOfPlayers.get()}')

        # engine.NumberOfPlayers.player_name_gender()
        # gameVar.StartVariables.new_players = self.NumOfPlayers.get() # sets in gui_variables
        # engine.NumberOfPlayers() # moved to player setter method

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