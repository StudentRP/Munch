""" GUI as class to be imported into the working script. Accommodated for scope issues with get()

requiremets:
    starting gui (welcome screen) timed delay to open
    number of players select
    name and sex, sex maybe check box..
    main game loop window

"""
""" maybe consider building frames and and replacing with changing players. """

from tkinter import *

preset1 = ('curlz MT', 15, 'bold')


#####################################################
"""thought process: build tk class, class that puts all classes in tk from a dict, build each frame that
   goes in the main window."""


# class MainWind:
#     """main window for other widget to occupy"""
#     def __init__(self):
#         self.root = Tk()  # main root window. Current thinking = need spawns of Toplevel for main game loop
#         self.topmenu = Menu(self.root)
#         self.title = self.root.title("Munchkin World")
#         self.screensize = self.root.geometry("600x300")
#         self.root.mainloop()


# class PlayerInfo(Frame):
#     """Idea is to change this part instead of shutting down main window and rebuilding """
#     def __init__(self, name='Unknown', gender='Male', level=1, bonus=0, race=None, klass=None, lhand=None,
#                  rhand=None, big=None, hgear=None, armour=None, ftgear=None,
#                  parent=None, **options ):
#         Frame.__init__(self, parent, **options)
#         self.pack()
#         Label(self, text='Player Info', font=preset1, fg="blue").grid(column=0, row=0, columnspan=2)
#         Label(self, text="---------------------").grid(column=0, row=1, columnspan=2)
#         Label(self, text="Player").grid(column=0, row=2)
#         Label(self, text=f'{name}').grid(column=1, row=2)
#         Label(self, text="Gender").grid(column=0, row=3)
#         Label(self, text=f'{gender}').grid(column=1, row=3)
#         Label(self, text="Level").grid(column=0, row=4)
#         Label(self, text=f'{level}').grid(column=1, row=4)
#         Label(self, text="Bonus").grid(column=0, row=5)
#         Label(self, text=f'{bonus}').grid(column=1, row=5)
#         Label(self, text="Race").grid(column=0, row=6)
#         Label(self, text=f'{race}').grid(column=1, row=6)
#         Label(self, text="Class").grid(column=0, row=7)
#         Label(self, text=f'{klass}').grid(column=1, row=7)
#         Label(self, text="---------------------").grid(column=0, row=8, columnspan=2)
#
#         Label(self, text='Armour & Weapons', font=preset1, fg="blue").grid(column=0, row=9, columnspan=2)
#         Label(self, text="Left hand").grid(column=0, row=10)
#         Label(self, text=f'{lhand}').grid(column=1, row=10)
#         Label(self, text="Right hand").grid(column=0, row=11)
#         Label(self, text=f'{rhand}').grid(column=1, row=11)
#         Label(self, text="Big item").grid(column=0, row=12)
#         Label(self, text=f'{big}').grid(column=1, row=12)
#         Label(self, text="Head gear").grid(column=0, row=13)
#         Label(self, text=f'{hgear}').grid(column=1, row=13)
#         Label(self, text="Armour").grid(column=0, row=14)
#         Label(self, text=f'{armour}').grid(column=1, row=14)
#         Label(self, text="Feet").grid(column=0, row=15)
#         Label(self, text=f'{ftgear}').grid(column=1, row=15)
#         Label(self, text="---------------------").grid(column=0, row=16, columnspan=2)



# PlayerInfo().mainloop()

#######################################################

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

#########################################################################################################
#########################################################################################################
# Design tests
#########################################################################################################
#########################################################################################################
"""Use within package and detailing specific data"""


class TestWin:
    """Test complete. runs and changes info per cycle. window must be destroyed before script continues."""
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

"""gui structure """


LARGE_FONT = ("Verdana", 12)


# class MainTest(Tk):
# 
#     def __init__(self, *args, **kwargs):
#         Tk.__init__(self, *args, **kwargs)
#         self.title("Top TK window") # tk title
#         self.geometry("600x600") # tk window size
#         container1 = Frame(self) # frame space 1
#         container1.pack(side=LEFT, fill=Y, expand=True)
#         container2 = Frame(self) # frame space 2
#         container2.pack(side=BOTTOM, fill=X, expand=True)
#         container3 = Frame(self) # frame space 3
#         container3.pack(side=RIGHT, fill=BOTH, expand=True)
# 
#         self.frames = {}
# 
#         frame = PlayerInfo(container1, self)
#         self.frames[PlayerInfo] = frame
#         frame.grid()
#         self.show_frame(PlayerInfo)
# 
#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()


class PlayerInfo(Frame):
    """Playerinfo frame to be placed in main window. """

    def __init__(self, parent, name='Unknown', gender='Male', level=1, bonus=0, race=None, klass=None,
                 lhand=None, rhand=None, big=None, hgear=None, armour=None, ftgear=None):
        Frame.__init__(self, parent)
        label.grid(column=1, row=2)
        Label(self, text='Player Info', font=preset1, fg="blue").grid(column=0, row=0, columnspan=2)
        Label(self, text="---------------------").grid(column=0, row=1, columnspan=2)
        Label(self, text="Player").grid(column=0, row=2)
        # Label(self, text=f'{name}').grid(column=1, row=2)
        Label(self, text="Gender").grid(column=0, row=3)
        Label(self, text=f'{gender}').grid(column=1, row=3)
        Label(self, text="Level").grid(column=0, row=4)
        Label(self, text=f'{level}').grid(column=1, row=4)
        Label(self, text="Bonus").grid(column=0, row=5)
        Label(self, text=f'{bonus}').grid(column=1, row=5)
        Label(self, text="Race").grid(column=0, row=6)
        Label(self, text=f'{race}').grid(column=1, row=6)
        Label(self, text="Class").grid(column=0, row=7)
        Label(self, text=f'{klass}').grid(column=1, row=7)
        Label(self, text="---------------------").grid(column=0, row=8, columnspan=2)

        Label(self, text='Armour & Weapons', font=preset1, fg="blue").grid(column=0, row=9, columnspan=2)
        Label(self, text="Left hand").grid(column=0, row=10)
        Label(self, text=f'{lhand}').grid(column=1, row=10)
        Label(self, text="Right hand").grid(column=0, row=11)
        Label(self, text=f'{rhand}').grid(column=1, row=11)
        Label(self, text="Big item").grid(column=0, row=12)
        Label(self, text=f'{big}').grid(column=1, row=12)
        Label(self, text="Head gear").grid(column=0, row=13)
        Label(self, text=f'{hgear}').grid(column=1, row=13)
        Label(self, text="Armour").grid(column=0, row=14)
        Label(self, text=f'{armour}').grid(column=1, row=14)
        Label(self, text="Feet").grid(column=0, row=15)
        Label(self, text=f'{ftgear}').grid(column=1, row=15)
        Label(self, text="---------------------").grid(column=0, row=16, columnspan=2)


class ThemedButton(Button):
    """class that modifies the original button"""
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.pack()
        self.config(bg='blue', font=preset1)


class ControlPannel(Frame):
    """Frame containing all the buttons for player actions"""
    def __init__(self, parent=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        ThemedButton(self, text="one").pack() # inherits from created class that in turn inherits from button
        Button(self, text="two").pack()# box standard button no frills

        self.pack(side=BOTTOM, fill=X)


class BattleGround(Frame):
    """card area on table and all cards in play"""
    def __init__(self, parent=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        Label(self, text="Card viewer", bg="yellow").pack(side=RIGHT, fill=BOTH, expand=YES)



class Main(Tk):
    """Main window that takes in frames and puts them into place"""
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Munch time")
        self.geometry("600x600")
        # ControlPannel(self).pack(side=BOTTOM, fill=X)
        # PlayerInfo(self).pack(side=LEFT, fill=Y)
        # BattleGround(self).pack(side=RIGHT, fill=BOTH, expand=YES)





# Main()
app = Main()
#
#

#
app.mainloop()

"""close but not winning!! Trouble addresing in script"""