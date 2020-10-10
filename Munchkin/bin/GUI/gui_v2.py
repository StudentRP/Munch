""" GUI as class to be imported into the working script. Accommodated for scope issues with get()

requiremets:
    starting gui (welcome screen) timed delay to open
    number of players select
    name and sex, sex maybe check box..
    main game loop window

"""


from tkinter import *



class StartScreen:
    """This will be the start screen, will need door pic."""
    def __init__(self):
        self.root = Tk()# main root window. Current thinking = need spawns of Toplevel for main game loop
        self.title = self.root.title("Munchkin World")
        self.screensize = self.root.geometry("600x300")
        self.frame = Frame(self.root)
        self.frame.pack()
        self.fl = Label(self.frame, text="hi class")
        self.fl.pack()
        self.enter = Entry()
        self.enter.pack()
        self.but = Button(self.root, text="get text", command=self.getobj)
        self.but.pack()
        self.mainloop = mainloop()

    def getobj(self):
        Label(self.root, text=f"{self.enter.get()}").pack()


# r = StartScreen() # instance

# r() # calling the instance


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

n = NumOfPlayers()

