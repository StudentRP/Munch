import tkinter as tk
import tkinter.ttk as ttk
import bin.engine.game_loop_v2 as engine
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
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.NumOfPlayers = tk.IntVar()

        "fills the dictionary"
        for frm in StartPg, PlayerSelect, MainLoop:
            frame = frm(container, self)
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
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f"{cs.start()}")
        label.pack(pady=10, padx=10)
        but1 = ttk.Button(self, text='Continue', command=lambda: controller.show_frame(PlayerSelect))
        but1.pack()


class PlayerSelect(tk.Frame):
    """player number select"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.NumOfPlayers = tk.IntVar()
        label = tk.Label(self, text="Select number of players")
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.NumOfPlayers)
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="OK", command=self.setplayers)
        but1.pack()
        #but for window progression
        but2 = tk.Button(self, text='Confirm', command=lambda: controller.show_frame(MainLoop)) # change method but use
        # this setup for moving onto next frame
        but2.pack()

    def setplayers(self):
        print(f'player from setplayers: {self.NumOfPlayers.get()}')
        gameVar.StartVariables.new_players = self.NumOfPlayers.get() # sets in gui_variables
        engine.NumberOfPlayers() # calls class in engine script setting up all class attribs  #####################
                


class MainLoop(tk.Frame):
    """3 frames with game loop"""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main play area")
        label.pack(pady=10, padx=10)


# app = Main()
#
# app.mainloop()

Main().mainloop()