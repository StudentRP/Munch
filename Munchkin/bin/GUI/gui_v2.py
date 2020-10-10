""" GUI as class to be imported into the working script. Accommodated for scope issues with get()

requiremets:
    starting gui (welcome screen) timed delay to open
    number of players select
    name and sex, sex maybe check box..
    main game loop window

"""


from tkinter import *



class MainScreen:
    """This will be the start screen, will need door pic."""
    def __init__(self):
        self.root = Tk()# main root window. Current thinking = need spawns of Toplevel for main game loop
        self.topmenu = Menu(self.root)
        self.title = self.root.title("Munchkin World")
        self.screensize = self.root.geometry("600x300")
        self.frame = Frame(self.root)
        self.frame.pack()
        self.fl = Label(self.frame, text="hi class")
        self.fl.pack()
        self.ent = Entry()
        self.ent.pack()
        self.but = Button(self.root, text="get text", command=self.get_obj)
        self.but.pack()
        self.mainloop = mainloop()

    def get_obj(self):
        Label(self.root, text=f"{self.ent.get()}").pack()


# win = MainScreen() # instance




class NumOfPlayers:
    """dropdown menu for player select"""
    def __init__(self):
        self.root = Tk()
        self.title = self.root.title("Player select")
        self.screensize = self.root.geometry("600x300")
        self.frame = Frame(self.root)
        self.frame.pack()
        self.fl = Label(self.frame, text="Please select number of players")
        self.fl.pack(side=TOP, fill=X)

        self.mainloop = mainloop()

# n = NumOfPlayers()

# class MainWinPlayerinfo:
#     player_info =[(x, y)]
#     for attrib, value in player_info:


class TestWin:
    def __init__(self, person='JB', level=0): # P(n) from player class will be instances for this
        self.root = Tk()
        self.title = self.root.title("Test Window")
        self.label = Label(self.root, text='Should show name and level')
        self.label.grid(column=0, row=0, columnspan=2)

        self.name = Label(self.root, text='Name')
        self.name.grid(column=0, row=1)
        self.nameval = Label(self.root, text=f'{person}') #location for player name
        self.nameval.grid(column=1, row=1)

        self.level = Label(self.root, text='Level')
        self.level.grid(column=0, row=2)
        self.levelval = Label(self.root, text=f'{level}')
        self.levelval.grid(column=1, row=2)

        self.root.mainloop()


# p = TestWin()