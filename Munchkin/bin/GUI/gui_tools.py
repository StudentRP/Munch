import tkinter


class Picture:
    pass


class ButStyle(tkinter.Button):
    def __init__(self, parent=None, **kwargs):
        tkinter.Button.__init__(self, parent, **kwargs)
        self.config(fg="red", bg="black", padx=15, pady=20)
