""" Game visuals that co-inside gameplay and choices

Considerations:
    all_cards visuals
    Choices
    Whats in inventory
    Player interaction/intervention

"""

from tkinter import *

#
# "Main window"
# rt = Tk()
#
# rt.title("Munchkin world")
#
# "presets"
# preset1 = ('curlz MT', 20, 'bold')
#
# ####################################################
# "lower choice window/interactions"
# selection = Frame(rt)
# ls = Label(selection, text='Options Selection:', font=preset1)
#
# selection.config(bg="skyblue", highlightbackground="black", highlightthickness=1)
# ls.config(bg="skyblue", fg="black")
#
# selection.pack(side=BOTTOM, anchor=S, fill=X)
# ls.pack(side=TOP, anchor=NW)
#
# ###################################################
# "left player info pane detailing visual info"
# playerinfo = Frame(rt)
# lp = Label(playerinfo, text="Player Info")
# subf1 = Frame(playerinfo)
# subf2 = Frame(playerinfo)
# Label(subf1, text='Player:').pack(side=LEFT)
# Label(subf2, text="self.name var").pack(side=RIGHT)
#
#
# playerinfo.config(bg='yellow', highlightbackground="black", highlightthickness=1)
# lp.config(bg='yellow', font=preset1)
#
#
# subf1.pack(side=LEFT)
# subf2.pack(side=RIGHT)
# playerinfo.pack(side=LEFT, anchor=NW, fill=Y)
# lp.pack(side=TOP, anchor=NW)
#
# ###############################################
# "main card window"
# cardsInPlay = Frame(rt)
# lc = Label(cardsInPlay, text='Cards In Play.', font=preset1)
#
#
# cardsInPlay.config(bg="green", highlightbackground="black", highlightthickness=1)
# lc.config(bg='green', font=preset1)
#
# lc.pack(side=TOP, anchor=NW)
# cardsInPlay.pack(anchor=NE, expand=Y, fill=BOTH)
#
#


# rt.mainloop()


l =[]

def start():
    rt=Tk()

    Button(rt, text='get data', command=test).pack()
    e = Entry()
    Label(rt, text="name").pack()
    e.pack()
    l.append(e)
    rt.mainloop()

def test():
    print(l[0].get())

# start()


class StartScreen():
    def __init__(self):
        self.root = Tk()
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


r = StartScreen

r()
