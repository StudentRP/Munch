""" GUI as class to be imported into the working script. Accommodated for scope issues with get()


"""
from tkinter import *


class StartScreen():
    def __init__(self):
        self.root = Tk()# main root window. Current thinking = need spawns of Toplevel for main game loop
        self.title = self.root.title("Munchkin World")
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


r = StartScreen # instance

r() # calling the instance