
"""
Main gui for Munchkin, version 4 (old: gui_v3)

"""
import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v3 import engine
# import bin.engine.game_loop_v3 as engine #for game loop clean up
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar
from tkinter import messagebox
from PIL import ImageTk
import os

gamefont=('castellar', 12, 'bold')
window_color = "#160606" # Would like pic here of door
text_color ="#7A0600"
but_color = "#3EB0A1"

##########################################################################
# Main controller
##########################################################################

class Main(tk.Tk):
    """main controller class that interchanges frames, updates variables with the frames"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry('500x200') # adding +x+y to the end provide window location
        self.title("Munchkin")
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        #### all Game notifications ####
        self.message = tk.StringVar()
        self.message2 = tk.StringVar()
        #### all player atribs to bind ####
        self.name = tk.StringVar()
        self.gender = tk.StringVar()
        self.race = tk.StringVar()
        self.race2 = tk.StringVar()
        self.klass = tk.StringVar()
        self.klass2 = tk.StringVar()
        self.level = tk.IntVar()
        self.bonus = tk.IntVar()
        self.wallet = tk.IntVar()
        self.r_hand = tk.StringVar()
        self.l_hand = tk.StringVar()
        self.two_hand = tk.StringVar()
        self.headgear = tk.StringVar()
        self.armor = tk.StringVar()
        self.knees = tk.StringVar()
        self.footgear = tk.StringVar()
        self.necklace = tk.StringVar()

        "fills the dictionary, snapshot built instance frames"
        for frm in StartPg, PlayerSelect, MainLoop:
            frame = frm(container, self) # passes container as the parent
            self.frames[frm] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPg)

    def show_frame(self, content):
        """brings the fame to the fore front"""
        frame = self.frames[content]
        frame.tkraise()

    def update_frame(self):
        """binds all the labels to the gamevar"""
        self.geometry("800x600+720+50") # changes the geometry when called
        self.name.set(gameVar.PlayerAtribs.player_name)
        self.gender.set(gameVar.PlayerAtribs.player_gender)
        self.race.set(gameVar.PlayerAtribs.player_race)
        self.race2.set(gameVar.PlayerAtribs.player_race2)
        self.klass.set(gameVar.PlayerAtribs.player_klass)
        self.klass2.set(gameVar.PlayerAtribs.player_klass2)
        self.level.set(gameVar.PlayerAtribs.player_level)
        self.bonus.set(gameVar.PlayerAtribs.player_bonus)
        self.wallet.set(gameVar.PlayerAtribs.player_wallet)

        self.l_hand.set(gameVar.PlayerAtribs.player_l_hand)
        self.r_hand.set(gameVar.PlayerAtribs.player_r_hand)
        self.two_hand.set(gameVar.PlayerAtribs.player_two_hand)

        self.headgear.set(gameVar.PlayerAtribs.player_headgear)
        self.armor.set(gameVar.PlayerAtribs.player_armor)
        self.knees.set(gameVar.PlayerAtribs.player_knees)
        self.footgear.set(gameVar.PlayerAtribs.player_footgear)
        self.necklace.set(gameVar.PlayerAtribs.player_necklace)

    def update_message(self, action=None):
        if action == "show":
            self.message.set(gameVar.GameObjects.message)
        elif action == "dev":
            self.message2.set(gameVar.GameObjects.message2)
        else:
            self.message.set("")
            self.message2.set("")

##########################################################################
# frames to build up interface
##########################################################################


class StartPg(tk.Frame):
    """Starting page with options to enhance game play"""
    # window_color = "#160606" # Would like pic here of door
    # text_color ="#7A0600"
    # but_color = "#3EB0A1"

    def __init__(self, parent, controller): # access to Main methods through the controller
        tk.Frame.__init__(self, parent)
        self.config(bg=window_color)

        label = tk.Label(self, text=f"{cs.start()}") # massage
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)

        but1 = tk.Button(self, text='Continue', command=lambda: controller.show_frame(PlayerSelect))
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack()
        but1.focus_set()

        but2 = tk.Button(self, text="Options", command=GameOptions)
        but2.config(bg=but_color, fg=text_color, padx=40, activebackground='yellow', relief="raised")
        but2.pack(side="bottom")


class GameOptions(tk.Toplevel):
    """Toplevel window for setting in game options at start""" # WORKS need others added and style tidying
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.inital_deal = tk.IntVar()
        self.maxlvl = tk.IntVar()
        self.permadeath = tk.BooleanVar()
        self.carry_weight = tk.IntVar()


        self.geometry("275x275+400+50")

        lf = tk.LabelFrame(self, text="Game Options")
        lf.config(font=gamefont)
        lf.pack(fill='both', expand=True)

        l1 = tk.Label(lf, text="Number of starting cards")
        l1.grid(column=0, row=0)
        e1 = tk.Entry(lf, textvariable=self.inital_deal)
        self.inital_deal.set(4)
        e1.icursor(1) # sets index of cursor ready for change
        e1.focus() # focuses on entry
        e1.grid(column=1, row=0)

        l2 = tk.Label(lf, text="Set max level")
        l2.grid(column=0, row=1)
        e2 = tk.Entry(lf, textvariable=self.maxlvl)
        self.maxlvl.set(10)
        e2.grid(column=1, row=1)

        l2 = tk.Label(lf, text="Max Hand capacity") # cards not visible to all players.
        l2.grid(column=0, row=2)
        e2 = tk.Entry(lf, textvariable=self.carry_weight)
        self.carry_weight.set(10) # change when cards are categorised, should be 6
        e2.grid(column=1, row=2)

        l3 = tk.Label(lf,text="Perm-a-death")
        l3.grid(column=0, row=3)
        cbut = tk.Checkbutton(lf, variable=self.permadeath)
        cbut.grid(column=1, row=3, sticky="w")

        b1 = tk.Button(lf, text="OK", command=self.setopts)
        b1.config(padx=20)
        b1.grid(column=0, row=4, columnspan=2)

    def setopts(self):
        """sets in game options. Binds sack size to gameVar changing the number of cards you can carry"""
        gameVar.Options.cards_dealt = self.inital_deal.get()
        gameVar.Options.win_lvl = self.maxlvl.get()
        gameVar.Options.perm_death = self.permadeath.get()
        gameVar.Options.carry_weight = self.carry_weight.get()
        message = f"Starting deal: {gameVar.Options.cards_dealt}\nWin level:{gameVar.Options.win_lvl}\n" \
                  f"Carry weight: {gameVar.Options.carry_weight}\nPerm_a_death: {gameVar.Options.perm_death}"
        messagebox.showinfo("Settings Changed!", message)
        GameOptions.destroy(self)


class PlayerSelect(tk.Frame):
    """Selection on number of players and meth to deal initial cards"""
    def __init__(self, parent, controller): # controller always passed in from main
        tk.Frame.__init__(self, parent)
        self.Num_of_players = tk.IntVar() # (int) of players in session
        self.count = tk.IntVar() # gameVar.StartVariables.new_players
        self.config(bg=window_color)

        label = tk.Label(self, text="Select number of players")
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.Num_of_players)
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="Confirm", command=self.playersetter)
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack(side="bottom")

    def playersetter(self):
        """Binds values from spinbox to gui_var for later use and calls next stage. calls player slice and meth to set
        initial player cards"""
        gameVar.StartVariables.new_players = self.Num_of_players.get() # int for Playerinfo toplevel window generation per player
        gameVar.StartVariables.player_rand = self.Num_of_players.get() # binds in 2nd location for later used in indexing
        engine.select_players() # sets in motion player slice in game_loop.. and calls meth to deal firs set of cards
        PlayerInfo() # calls toplevel for name and gender entry for each player


class PlayerInfo(tk.Toplevel):
    """Top level for players to enter names and gender. Must: update title label with player number, store variables
    from entries, call game_loop with index para, increment index"""
    counter = 1 # player identity title number for arbitrary label
    indexing = 0 # index to access correct player instance in list. Ensures player details are bound to the correct instance

    def __init__(self):
        tk.Toplevel.__init__(self)
        """throw-away vars for names/gender """
        self.instname = tk.StringVar() # does not use Main self.name as no access as no controller passed on
        self.instgender = tk.StringVar()
        """main toplevel setup"""
        self.geometry('350x150+500+300')
        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side='top', fill='both', expand=True)
        self.mainframe.focus_set()  # foucus on this window objects
        self.mainframe.grab_set()  # modal form

        self.arbitary = tk.Label(self.mainframe, text=f"Player {PlayerInfo.counter}") #title
        self.arbitary.config(font=('castellar', 15, 'bold'), fg='blue')
        self.arbitary.grid(column=0, row=0, columnspan=2, sticky='n,e,s,w')

        self.namelab = tk.Label(self.mainframe, text='Name: ')
        self.namelab.grid(column=1, row=1, sticky='w')
        self.nameent = tk.Entry(self.mainframe, textvariable=self.instname)
        self.nameent.grid(column=2, row=1, sticky='w,e')
        self.nameent.focus_set()

        self.genderlab = tk.Label(self.mainframe, text='Gender: ')
        self.genderlab.grid(column=1, row=2, sticky='w')
        self.instgender.set("male") # creates default
        self.nameent = ttk.Combobox(self.mainframe, textvariable=self.instgender, values=["Male", "Female"])
        self.nameent.grid(column=2, row=2, sticky='w')

        self.but2 = tk.Button(self.mainframe, text='Confirm', command=self.initial_set)
        self.but2.config(bd=10, activebackground='green')
        self.but2.grid(column=2, row=4, columnspan=2, sticky='n,e,s,w')
        self.bind('<Return>', self.initial_set)  # creates event to be passed to test

    def initial_set(self, event=None):
        """button handler, binds name/gender to gameVar, increments arbitrary label and index for ensuring correct player instance,
         """
        number = gameVar.StartVariables.new_players # (int) derived from gui_var .
        if number >= 1:
            number -= 1 # decreases the num of new pLayer integer
            PlayerInfo.counter += 1 # increase player counter for arbitrary label in __init__
            gameVar.PlayerAtribs.player_name = self.instname.get() # entered name binds to gameVar
            gameVar.PlayerAtribs.player_gender = self.instgender.get() # entered gender binds to gameVar
            engine.player_name_gender(PlayerInfo.indexing) # call game_loop with index for player instance
            PlayerInfo.indexing = PlayerInfo.indexing + 1 # increases player index ensuring correct player attribute assignment
            print("Destroying toplevel")
            PlayerInfo.destroy(self) #destoys toplevel window
            gameVar.StartVariables.new_players = number # reduces number in gameVar for next  player in loop

            if number != 0: # loop for next player
                PlayerInfo() # rebuilds toplevel anew for next player
            else:
                PlayerInfo.destroy(self)
                #~~~~~~~~ TO BE REMOVED + LOOP BELOW
                print("Players in game:")
                for players in gameVar.StartVariables.session_players: # loop to see all player names
                    print(players.name.title()) # checks all players names for activity
                #~~~~~~~~~~~~~~~

                engine.rand() # gets a random player from the active player list, auto calls varbinging binding all variables.
                app.update_frame() # updates all label variables from gameVar
                app.update_message("show")
                app.update_message("dev") # dev addition message from the creator
                app.show_frame(MainLoop) # calls next frame to raise by controller
                ########## deal cards to all players required


####################################################################################################################
class MainLoop(tk.Frame):
    """3 frames with game loop, function required to set index at random place """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        "frame for buttons - may create some buttons to inherit style from "
        self.butframe = tk.LabelFrame(self, text='Navigation')
        self.butframe.config(bg=but_color, fg="blue")
        self.butframe.pack(side='bottom', fill='x', ipady=80)

        self.b1 = tk.Button(self.butframe, text="End Turn", command=self.end_turn)
        self.b1.config(activebackground='#0ABF28', bg="#B40BEE", padx=15, pady=20)
        self.b1.place(x=600, y=45)

        self.b2 = tk.Button(self.butframe, text="Kick Door", command=self.door)
        self.b2.config(activebackground='#0ABF28', bg="#082EF6", padx=5, pady=10)
        self.b2.place(x=350, y=45)

        self.b3 = tk.Button(self.butframe, text="Weapons", command=self.list_weapons)
        self.b3.place(x=250, y=10)
        self.b4 = tk.Button(self.butframe, text="Armour", command=self.list_armor)
        self.b4.place(x=225, y=45)
        self.b5 = tk.Button(self.butframe, text="Consumables", command=self.consumables)
        self.b5.place(x=250, y=80)

        self.b6 = tk.Button(self.butframe, text="Sell", command=self.list_sell)
        self.b6.config(padx=15)
        self.b6.place(x=450, y=10)
        self.b7 = tk.Button(self.butframe, text="Sack", command=self.list_sack) ########### used as dummy atm
        self.b7.config(padx=10)
        self.b7.place(x=475, y=45)
        self.b8 = tk.Button(self.butframe, text="Equipped items", command=self.list_equipped)
        self.b8.place(x=450, y=80)

        self.b9 = tk.Button(self.butframe, text="Interfere", command=self.interfere)
        self.b9.place(x=10, y=50)
        self.b10 = tk.Button(self.butframe, text="Help/Trade", command=self.ask_for_help)
        self.b10.place(x=10, y=100)

        self.b11 = tk.Button(self.butframe, text="Fight!", command=self.fight, state="disabled")
        self.b11.place(x=100, y=50)
        self.b12 = tk.Button(self.butframe, text="Run!!", command=self.run, state="disabled")
        self.b12.place(x=100, y=100)

        self.b13 = tk.Button(self.butframe, text="Hand", command=self.hand)  # for hidden objects
        self.b13.place(x=365, y=100)


        "frame player attribs"
        self.plframe = tk.LabelFrame(self, text='Player Info')
        self.plframe.config(pady=20)
        self.plframe.pack(side='left', fill="y", ipadx=50)

        player_info = {"Name: ": controller.name, "Gender: ": controller.gender,
                       "Level: ": controller.level, "Bonus: ": controller.bonus, "Wallet: ": controller.wallet,
                       "Race: ": controller.race, "Class: ": controller.klass}

        player_defence = {"L_hand: ": controller.l_hand, "R_hand: ": controller.r_hand, "two_hand: ": controller.two_hand,
                           "Head Gear: ": controller.headgear, "Armor: ": controller.armor, "Knees: ": controller.knees,
                           "Foot gear: ": controller.footgear, "Necklace": controller.necklace}
        row = 0
        for key, val in player_info.items():
            self.l1 = tk.Label(self.plframe, text=key.title())
            self.l1.grid(row=row, column=1, sticky='nsew')
            self.l1b = tk.Label(self.plframe, textvariable=val)  ## works binding strait to stringvar in Main
            self.l1b.grid(row=row, column=2, sticky='nsew')
            row += 1
        " To work with player supermunch/halfbreed meths to turn on"
        self.race2_option = tk.Label(self.plframe, text="Race_2:")
        self.race2_optionb = tk.Label(self.plframe, textvariable=controller.race2)
        self.klass2_option = tk.Label(self.plframe, text="Class_2:")
        self.klass2_optionb = tk.Label(self.plframe, textvariable=controller.klass2)
        row = 10
        for key, val in player_defence.items():
            self.l1 = tk.Label(self.plframe, text=key.title())
            self.l1.grid(row=row, column=1, sticky='nsew')
            self.l1b = tk.Label(self.plframe, textvariable=val)  ## works binding strait to stringvar in Main
            self.l1b.grid(row=row, column=2, sticky='nsew')
            row += 1

        "Game Window"
        self.tblframe = tk.LabelFrame(self, text='Table')
        self.tblframe.config(bg='lightgrey'),
        self.tblframe.pack( fill="both", expand=True)

        self.message = tk.Label(self.tblframe, textvariable=controller.message)
        self.message.pack(anchor="n", fill="x", expand=True)
        self.message = tk.Label(self.tblframe, textvariable=controller.message2)
        self.message.pack(anchor="n", fill="x", expand=True)

        self.canvas = tk.Canvas(self.tblframe, bg='black')
        self.canvas.pack(anchor="n", expand="yes", fill=tk.BOTH)
        self.canvas.pack(anchor="n", expand="yes", fill=tk.BOTH)

    "Handlers"
    def end_turn(self):
        """require method to be called from gameloop to rebase all variables in guivar. this should update the var in Mainloop
        with app.update_frame() method call"""
        gameVar.CardDraw.num_of_kicks = 0 # resets door kicks
        self.b2.config(state="normal") # enables kick door button
        self.b3.config(state="normal")  # weapons
        self.b4.config(state="normal")  # armor
        self.b6.config(state="normal")  # sell
        self.b11.config(state="disabled")  # fight
        self.b12.config(state="disabled")  # run
        # app.update_message() #clears all messages
        engine.player_order(gameVar.StartVariables.active_player) # sends active player rebind new player in game_loop
        app.update_message()  # clears all messages
        app.update_message("show")
        app.update_frame() # updates the tk.vars in Main under the instance controller.
        # Methods that need to run at start of every next player turn.
        # if gameVar.StartVariables.active_player.race_unlock: # packing for klass and race in the event of supermunch ect
        #     self.race2_option.grid(row=8, column=1, sticky='nsew')
        #     self.race2_optionb.grid(row=8, column=2, sticky='nsew')
        # if gameVar.StartVariables.active_player.klass_unlock:
        #     self.klass2_option.grid(row=9, column=1, sticky='nsew')
        #     self.klass2_optionb.grid(row=9, column=2, sticky='nsew')

    def door(self):
        """game actions for door. cards drawn from door"""
        gameVar.GameObjects.message = f"{app.name.get()} has kicked open the door!"
        app.update_message("show")
        self.b1.config(state="disabled") # disables end turn button, enables at end of fight
        if gameVar.CardDraw.num_of_kicks == 0:
            door_card = engine.deal_handler("door", call=1) # returns card for pic, sorts card either to table, hand, or curse meth
            app.update_message("show")
            if engine.card_type(): # if monster on table
                self.b2.config(state="disabled") # kick door
                self.b3.config(state="disabled") # weapons
                self.b4.config(state="disabled") # armor
                self.b6.config(state="disabled") # sell
                self.b11.config(state="normal") # fight
                self.b12.config(state="normal") # run
                # place door_card on canvas

            # need to show first time so raise pic, Cardview class
            app.update_message("show")
            gameVar.CardDraw.num_of_kicks += 1 # always increments after first kick

        elif gameVar.CardDraw.num_of_kicks == 1:
            self.b2.config(state="disabled") # disables door button
            engine.deal_handler("door", call=0)# call set to false
            self.b1.config(state="normal") # enables fight
            app.update_message("show")

    def fight(self):
        engine.fight() # helper may be added when sorting it
        app.update_message("show") # name and lvl of monster

        engine.varbinding(gameVar.StartVariables.active_player) #####
        app.update_frame() ###

        # remove card form list and canvas ect
        self.b1.config(state="normal") #end of fight enables end turn

    def run(self):
        engine.run()

    def list_weapons(self):
        """ builds a list of cards that meet the the weapons criterion. List is bound to gameVar..selected_items """
        gameVar.GameObjects.message = "Weapons list"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.inventory("type", "weapon")
        # print(gameVar.GameObjects.selected_items)  list all items
        OwnedItems("Weapons owned", "weap")

    def list_armor(self):
        gameVar.GameObjects.message = "Armour list"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.inventory("type", "armor") # load all weapons items into gamevar.selected_items
        OwnedItems("Armor Owned", "armor")

    def consumables(self):
        gameVar.GameObjects.message = "Consumable items"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.inventory("type", "disposable")
        OwnedItems("One shot items", "consume")

    def list_sell(self):
        """builds toplevel with sellable items"""
        gameVar.GameObjects.message = "Sell selected"
        app.update_message("show")
        engine.scrub_lists() # resets all lists for next action
        player = gameVar.StartVariables.active_player # gets current player
        player.item_by_key("sell") # generates list of sellable cards passed on to gameVar.selected_items
        # print(gameVar.StartVariables.selected_items) # call method that in gamefile that creates zip
        OwnedItems("Sellable Items", "sell") # calls toplevel with window title

    def hand(self):
        gameVar.GameObjects.message = "Hidden items selected"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.inventory("category", "door")
        OwnedItems("Hidden Items", "hidden")

    def interfere(self): #not set
        gameVar.GameObjects.message = "Toplevel window where another player can interfere with play\n NOT SET UP"
        app.update_message("show")

    def ask_for_help(self): #mot set
        gameVar.GameObjects.message = "Toplevel window where another player can help... for a price.."
        app.update_message("show")

    def list_sack(self):
        """shows all items in sack"""
        gameVar.GameObjects.message = "The contents of sack:"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.inventory("category", "treasure")
        OwnedItems("Sack Items")

    def list_equipped(self):
        """list showing all items that are equipped"""
        engine.scrub_lists()
        player = gameVar.StartVariables.active_player
        player.equipped_items("list_equipped")
        OwnedItems("Equipped Items", "remove")


class OwnedItems(tk.Toplevel):
    """generates toplevel from cards place in gameVar.GameObjects.selected_items where selections can be made on those cards"""
    def __init__(self, wind_title="Template", set_but="No Buttons"): #title and buttons to be used for items
        tk.Toplevel.__init__(self)
        self.wind_title = wind_title
        self.title(self.wind_title)
        # self.geometry("350x250+200+200")
        self.set_but = set_but

        if not gameVar.GameObjects.selected_items:
            fm = tk.Frame(self)
            tk.Label(fm, text="No cards to show").pack()
        else:
            f = tk.Frame(self)
            f.pack(side="top", expand=True)
            tk.Label(f, text="Name").grid(row=0, column=0, sticky="nw")
            tk.Label(f, text="Type").grid(row=0, column=1, sticky="nw")
            if self.set_but == "sell":
                tk.Label(f, text="Value").grid(row=0, column=2, sticky="nw")
            # elif self.set_but == "hidden":
            #     pass
            elif self.set_but in " weap, armor, consume, equip, remove":
                tk.Label(f, text="Bonus").grid(row=0, column=2, sticky="nw")
            # else:
            #     tk.Label(f, text="Bonus").grid(row=0, column=2, sticky="nw")
            tk.Label(f, text="Select").grid(row=0, column=3, sticky="nw")
            set_row = 1
            for card in gameVar.GameObjects.selected_items:
                status = tk.IntVar() # for keeping track of check buttons
                l1 = tk.Label(f, text=card['name'])
                l1.grid(row=set_row, column=0, sticky="nw")
                l2 = tk.Label(f, text=card['type'])
                l2.grid(row=set_row, column=1, sticky="nw")
                if self.set_but == "sell":
                    l3 = tk.Label(f, text=card['sell'])
                    l3.grid(row=set_row, column=2, sticky="nw")
                elif self.set_but in " weap, armor, consume, equip, remove":
                    l3 = tk.Label(f, text=card['bonus'])
                    l3.grid(row=set_row, column=2, sticky="nw")
                if set_but != "No Buttons":
                    tk.Checkbutton(f, text=" ", variable=status).grid(row=set_row, column=3, sticky="nw")
                b1 = tk.Button(f, text="info", command=lambda c=card["id"]: self.showcard(c))
                b1.grid(row=set_row, column=4)

                gameVar.GameObjects.check_but_intvar_gen.append(status) # creates list of IntVars for each item in list
                gameVar.GameObjects.check_but_card_ids.append(card["id"]) # sends card ids int to list
                set_row += 1

        if self.set_but in "weap, armor, sell":
            tk.Button(self, text="Sell", command=self.sell).pack(side="left")
        if self.set_but in "consume, hidden":
            tk.Button(self, text="Use item", command=self.use_item).pack(side="left")
        if self.set_but == "weap" or self.set_but == "armor":
            tk.Button(self, text="Equip", command=self.equip).pack(side="left")
        if self.set_but == "remove":
            tk.Button(self, text="Remove", command=self.remove).pack(side="left")

    def showcard(self, card_id):
        """ Method for showing the card in a toplevel window"""
        CardVeiw(card_id)

    def sell(self):
        """triggers sell event when pushed"""
        engine.zipper("sell") # calls meth to make tuple from card ids and checkbutton converted bools
        OwnedItems.destroy(self) # destroys toplevel window
        engine.scrub_lists() # note lists are scrubbed when but pushed on main screen
        engine.varbinding(gameVar.StartVariables.active_player) # explicitly ensures all vars ar correct
        app.update_frame() # updates player info
        app.update_message("show")

    def equip(self):
        Tools.common_set("equip")
        OwnedItems.destroy(self)
        # app.update_message("show")
        engine.scrub_lists()
        app.update_message("show")

    def use_item(self):
        """for consumables and hidden objects"""
        Tools.common_set("disposable")
        OwnedItems.destroy(self)

        engine.scrub_lists()
        app.update_message("show")

    def remove(self):
        Tools.common_set("remove")
        OwnedItems.destroy(self)
        engine.scrub_lists()
        app.update_message("show")


class CardVeiw(): # not currently working
    def __init__(self, card_id=None):
        # path = "..\\imgs\\cards\\"
        PIC = os.path.abspath(r"..\imgs\cards")

        win = tk.Toplevel()
        win.title("Card Info")
        # img = ImageTk.PhotoImage(file=f"{path}{str(card_id)}.png") # does not require pil but in case change format
        img = ImageTk.PhotoImage(file=PIC + f"\\{str(card_id)}.png")
        can = tk.Canvas(win)
        can.pack(fill=tk.BOTH)
        can.config(width=img.width(), height=img.height())
        can.create_image(2, 2, image=img, anchor=tk.NW)  # x, y coordinates
        win.mainloop()


class Tools:
    """method sets to uphold dry programing"""

    # def __init__(self, keyword):
    #     self.key_word = keyword
    @staticmethod
    def common_set(keyword):
        engine.zipper(keyword)  # calls card_matcher() passing the parameter to it.
        engine.varbinding(gameVar.StartVariables.active_player)
        app.update_frame()

    # @staticmethod #not working Yet
    # def viewer(parent, card_id=None):
    #     path = "..\\imgs\\cards\\"
    #     win = tk.Frame(parent)
    #     img = ImageTk.PhotoImage(file=f"{path}{str(card_id)}.png")
    #     can = tk.Canvas(win)
    #     can.pack(fill=tk.BOTH)
    #     can.config(width=img.width(), height=img.height())
    #     can.create_image(2, 2, image=img, anchor=tk.NW)



if __name__ == "__main__":
    app = Main()

    app.mainloop()

# Main().mainloop(),
