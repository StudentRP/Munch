
"""
Main gui for Munchkin, version 4 (legacy: gui_v3)

"""
import tkinter as tk
import tkinter.ttk as ttk
from bin.engine.game_loop_v3 import engine  # imports the instance
# import bin.engine.game_loop_v3 as engine #for game loop clean up
import bin.engine.cut_scenes as cs
import bin.GUI.gui_variables as gameVar
from tkinter import messagebox
from PIL import ImageTk, Image
import os
# import bin.GUI.gui_tools as tools

gamefont = ('castellar', 12, 'bold')
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
        self.geometry('500x200') # adding +x+y to the end provide window location, maybe create option slider in menu
        self.title("Munchkin")
        # main container for the different frames to be placed in
        container = tk.Frame(self)
        container.pack(side=tk.TOP, fill='both', expand=True) # creates frame that spans all of the main tk window
        container.grid_rowconfigure(0, weight=1) # params = row 0 expand(1, 0 for not expand)
        container.grid_columnconfigure(0, weight=1)
        # holds all the prebuilt frames for the container to look up
        self.frames = {} # app.frames

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

        "Creates 3 frames all with the same parent and fills the dictionary with snapshots of built instances"
        for frm in StartPg, PlayerSelect, MainLoop: # snapshot of the frames (classes) put into the dict
            frame = frm(container, self) # Instance creation. Passes container as the parent frame & self as controller (app)
            self.frames[frm] = frame  # adding to dict
            frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPg) # calling correct pg to top of the frame, last one stacked will show otherwise

    def show_frame(self, content):
        """ Brings the frame to the fore front within the pre packed parent frame. Content being name of frame class
        packed into the container """
        frame = self.frames[content] # looks up the frame in the dict
        frame.tkraise() # brings the child frame to the forefront to be seen within the main container frame

    def update_atrib_frame(self):
        """Binds all the labels to the gamevar for player change with the set method"""
        self.geometry("800x600+320+20") # changes the geometry when called ## need to move
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
            self.message.set(gameVar.GameObjects.message) # grabs message stored in gamevar messages
        elif action == "dev":
            self.message2.set(gameVar.GameObjects.message2)
        else:
            self.message.set("")
            self.message2.set("")


##########################################################################
# frames to build up interface
##########################################################################


class StartPg(tk.Frame):
    """Starting page linking buttons to game options and game start"""
    # window_color = "#160606" # Would like pic here of door
    # text_color ="#7A0600"
    # but_color = "#3EB0A1" # moved to top of script

    def __init__(self, parent, controller): # parent = container in Main class, controller = app object.
        tk.Frame.__init__(self, parent)
        self.config(bg=window_color)

        # welcome massage
        label = tk.Label(self, text=f"{cs.start()}")
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)

        #button to change frame seen in container
        but1 = tk.Button(self, text='Continue', command=lambda: controller.show_frame(PlayerSelect))
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack()
        but1.focus_set()

        # game options
        but2 = tk.Button(self, text="Options", command=GameOptions)
        but2.config(bg=but_color, fg=text_color, padx=40, activebackground='yellow', relief="raised")
        but2.pack(side="bottom")


class GameOptions(tk.Toplevel):
    """Toplevel window for setting in game options at start""" # WORKS need others added and style tidying
    def __init__(self):
        tk.Toplevel.__init__(self)
        self.geometry("275x275+400+50")

        # Editable options binding
        self.initial_deal = tk.IntVar()
        self.maxlvl = tk.IntVar()
        self.permadeath = tk.BooleanVar()
        self.carry_weight = tk.IntVar()

        #styling
        lf = tk.LabelFrame(self, text="Game Options")
        lf.config(font=gamefont)
        lf.pack(fill='both', expand=True)

        l1 = tk.Label(lf, text="Number of starting cards")
        l1.grid(column=0, row=0)
        e1 = tk.Entry(lf, textvariable=self.initial_deal)
        self.initial_deal.set(4) # if options opened, sets this as default
        e1.icursor(1) # sets blinking cursor to this index ready to change value in box
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
        """Sets gamevar options to the new values provided with the get() method used for tkvars. """
        gameVar.Options.cards_dealt = self.initial_deal.get() # gets value stored in the bound tkvar associated to initial_deal
        gameVar.Options.win_lvl = self.maxlvl.get()
        gameVar.Options.perm_death = self.permadeath.get()
        gameVar.Options.carry_weight = self.carry_weight.get()
        message = f"Starting deal: {gameVar.Options.cards_dealt}\nWin level:{gameVar.Options.win_lvl}\n" \
                  f"Carry weight: {gameVar.Options.carry_weight}\nPerm_a_death: {gameVar.Options.perm_death}"
        messagebox.showinfo("Settings Changed!", message) # tk built in message
        GameOptions.destroy(self) # destroys toplevel after all actions complete.


class PlayerSelect(tk.Frame):
    """Selection on number of players and meth to deal initial cards"""
    def __init__(self, parent, controller): # controller always passed in from main, parent is Main container
        tk.Frame.__init__(self, parent)
        self.Num_of_players = tk.IntVar() # (int) of players in session
        self.count = tk.IntVar() # gameVar.StartVariables.new_players
        self.config(bg=window_color)

        label = tk.Label(self, text="Select number of players")
        label.config(font=gamefont, bg=window_color, fg=text_color)
        label.pack(pady=10, padx=10)
        l1 = ttk.Spinbox(self, from_=1, to=10, increment=1, textvariable=self.Num_of_players) # num of players select
        l1.focus()
        l1.set(1)
        l1.pack()
        but1 = tk.Button(self, text="Confirm", command=self.playersetter)
        but1.config(bg=but_color, fg=text_color, padx=40, activebackground='red', relief="raised")
        but1.pack(side="bottom")

    def playersetter(self):
        """Binds values from spinbox to gui_var for later use and calls next stage. Calls player slice and meth to set
        initial player cards. COULD USE A INSTANCE FACTORY TO BUILD PLAYERS"""
        gameVar.StartVariables.new_players = self.Num_of_players.get() # int for Playerinfo toplevel window generation per player
        gameVar.StartVariables.player_rand = self.Num_of_players.get() # binds in 2nd location for later used in indexing
        engine.select_players() #creates slice object (session_players) and calls dealer to hand each a starting cards set
        PlayerInfo() # each player in session_players sets their name and gender in a toplevel window.


class PlayerInfo(tk.Toplevel):
    """Top level for players to enter names and gender. Must: update title label with player number, store variables
    from entries, call game_loop with index para, increment index"""
    label_counter = 1 # player identity title number for arbitrary label ie Player 1
    list_indexer = 0 # index to access correct player instance in list. Ensures player details are bound to the correct instance

    def __init__(self):
        tk.Toplevel.__init__(self)
        """throw-away vars for names/gender """
        self.instname = tk.StringVar()
        self.instgender = tk.StringVar()
        """main toplevel setup"""
        self.geometry('350x150+500+300')

        self.mainframe = tk.Frame(self)
        self.mainframe.pack(side='top', fill='both', expand=True)
        self.mainframe.focus_set()  # focus on this window objects
        self.mainframe.grab_set()  # make modal

        self.arbitary = tk.Label(self.mainframe, text=f"Player {PlayerInfo.label_counter}") # unique title
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
        self.bind('<Return>', self.initial_set)  # alternative to button press

    def initial_set(self, event=None):
        """Primary function: call method == session_players[list_indexer] for player instance setting name and gender,
        & set a random player binding to active_player.
        Secondary requirements: Increments arbitrary label_counter & counts down from the number of players in-game
        ensuring all get attribute assignment. """

        players_assign = gameVar.StartVariables.new_players # players_assign  = total players_assign of players in play ie 4.
        if players_assign >= 1: # loop wont work as branch needs to be restarted per player
            players_assign -= 1 # decreases the num of new pLayer integer to count down players_assign of players left to assign
            PlayerInfo.label_counter += 1 # increase player counter for arbitrary label in class scope
            gameVar.PlayerAtribs.player_name = self.instname.get() # gameVar atrib is used to store the entered player name.
            gameVar.PlayerAtribs.player_gender = self.instgender.get() # entered gender binds to gameVar
            engine.player_name_gender(PlayerInfo.list_indexer) # method to index session_players list for specific player and set name and gender attribs
            PlayerInfo.list_indexer = PlayerInfo.list_indexer + 1 # increases index value so looping will call next player in session_players list
            PlayerInfo.destroy(self) # destroys toplevel window wiping all entered info for next player to enter
            gameVar.StartVariables.new_players = players_assign # gamevar is bound to the new value for players_assign

            if players_assign != 0: # loop for next player
                PlayerInfo() # rebuilds toplevel anew for next player
            else:
                "once all player attribs have been set"
                PlayerInfo.destroy(self) # final destruction of top window
                #~~~~~~~~ debug loop
                print("\nPlayers in game:", end=" ")
                for players in gameVar.GameObjects.session_players: # loop to see all player names
                    print(players.name.title(), end=", ") # checks all players names assigned in session_players
                print("\n...............")
                #~~~~~~~~~~~~~~~

                engine.set_random_player() # gets a random player from the active player list, auto calls varbinging binding all variables.
                app.update_atrib_frame() # updates all label variables from gameVar to MainLoop frame.
                app.update_message("show")
                app.update_message("dev") # dev addition message from the creator
                app.show_frame(MainLoop) # calls next frame to raise by controller
                ########## deal cards to all players required


####################################################################################################################
class MainLoop(tk.Frame):
    """MainLoop configures main window presenting all buttons and handlers for gameplay. The gameplay area is split into
    3 domains player info, button console and table cards/message screen"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        "frame for buttons - may create some buttons to inherit style from "
        self.butframe = tk.LabelFrame(self, text='Navigation')
        self.butframe.config(bg="darkgrey", fg="red")
        self.butframe.pack(side='bottom', fill='x', ipady=80)

        self.end_turn_button = tk.Button(self.butframe, text="End Turn", command=self.end_turn)
        self.end_turn_button.config(activebackground='#0ABF28', bg="#B40BEE", padx=15, pady=20)
        self.end_turn_button.place(x=600, y=45)

        self.door_button = tk.Button(self.butframe, text="Kick Door", command=self.door)
        self.door_button.config(activebackground='#0ABF28', bg="#082EF6", padx=5, pady=10)
        self.door_button.place(x=350, y=45)

        self.weapons_button = tk.Button(self.butframe, text="Weapons", command=self.list_weapons)
        self.weapons_button.place(x=250, y=10)
        self.armor_button = tk.Button(self.butframe, text="Armour", command=self.list_armor)
        self.armor_button.place(x=225, y=45)
        self.consumables_button = tk.Button(self.butframe, text="Consumables", command=self.consumables)
        self.consumables_button.place(x=250, y=80)

        self.sell_button = tk.Button(self.butframe, text="Sell", command=self.list_sell)
        self.sell_button.config(padx=15)
        self.sell_button.place(x=450, y=10)
        self.sack_button = tk.Button(self.butframe, text="Sack", command=self.list_sack) ########### used as dummy atm
        self.sack_button.config(padx=10)
        self.sack_button.place(x=475, y=45)
        self.equipped_button = tk.Button(self.butframe, text="Equipped items", command=self.list_equipped)
        self.equipped_button.place(x=450, y=80)

        self.interfere_button = tk.Button(self.butframe, text="Interfere", command=self.interfere)
        self.interfere_button.place(x=10, y=50)
        self.ask_for_help_button = tk.Button(self.butframe, text="Help/Trade", command=self.ask_for_help)
        self.ask_for_help_button.place(x=10, y=100)

        self.fight_button = tk.Button(self.butframe, text="Fight!", command=self.fight, state="disabled")
        self.fight_button.place(x=100, y=50)
        self.run_away_button = tk.Button(self.butframe, text="Run!!", command=self.run, state="disabled")
        self.run_away_button.place(x=100, y=100)

        self.private_items_button = tk.Button(self.butframe, text="Hand", command=self.hand)  # for hidden objects
        self.private_items_button.place(x=365, y=100)

        self.satatus_effect_button = tk.Button(self.butframe, text="Status Effects", command=self.status_effect)# for player curses
        self.satatus_effect_button.place(x=600, y=10)

        # self.b14 = tk.Button(self.butframe, text="Update info", command=self.update_info)  # for hidden objects
        # self.b14.place(x=10, y=10)

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
        "To work with player supermunch/halfbreed meths to turn on"
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
        self.tblframe = tk.LabelFrame(self, text='Table') # main back window
        self.tblframe.config(bg='lightgrey')
        self.tblframe.pack(fill="both", expand=True)

        self.notifications = tk.Frame(self.tblframe)
        self.notifications.pack(side="top", fill="x", expand=True)

        self.message = tk.Label(self.notifications, textvariable=controller.message)
        self.message.pack(side="top", fill="x", expand=True)
        self.message2 = tk.Label(self.notifications, textvariable=controller.message2)
        self.message2.pack(side="top", fill="x", expand=True)

        self.canvas = tk.Canvas(self.tblframe, height=450) # canvas not dynamically expanding
        self.canvas.config(bg="black")
        self.canvas.pack(side="top", expand=True, fill="both") # without self should now be accessible for the class....
        self.pic = ""

    "Handlers"
    def end_turn(self):
        """require method to be called from gameloop to rebase all variables in guivar. this should update the var in Mainloop
        with app.update_frame() method call"""
        # meth for checking sack size of player
        gameVar.CardDraw.door_attempts = 1 # resets door kicks for next player.. Should change to false
        self.canvas.delete("all")  # clears the canvas(table) for new player
        # Methods that need to be applied to a player for next turn.
        self.door_button.config(state="normal") # enables kick door button
        self.weapons_button.config(state="normal")  # weapons
        self.armor_button.config(state="normal")  # armor
        self.sell_button.config(state="normal")  # sell
        self.fight_button.config(state="disabled")  # fight
        self.run_away_button.config(state="disabled")  # run
        # app.update_message() #clears all messages

        engine.player_order(gameVar.GameObjects.active_player) # sends active player rebind new player in game_loop
        Tools.fluid_player_info() # adds or removes player class2/race2 option
        app.update_message()  # clears all messages
        app.update_message("show") # updates main broadcast message
        # self.message2.destroy() # destroys message2 for the dev mode
        app.update_atrib_frame() # updates the tk.vars in Main under the instance controller.
        print(" Turn ended!\n", "."*10, "\n")

    def door(self):
        """game actions for door. cards drawn from door"""
        print("\nKicking door!")
        player = gameVar.GameObjects.active_player
        self.message2.destroy()  # removes dev label

        self.end_turn_button.config(state="disabled") # disables end turn button, enabled at end of fight

        #main actions
        door_card = engine.deal_handler("door") # fetch a door card
        engine.door_card_designator(door_card, door_attempts=gameVar.CardDraw.door_attempts)  # defines the actions to be taken with he card


        #card viewing
        if gameVar.CardDraw.door_attempts: # first kick of door (always get this at start of turn!)
            print("VIEWING CARD")

            self.pic = Tools.viewer(door_card["id"]) # gets card id. needs self or garbage collected!
            self.canvas.create_image(10, 10, image=self.pic, anchor="nw")# view card on canvas.. will need meth for this to add cards in linear fashion

            #broadcast
            if door_card.get('type') != 'monster' and door_card.get('type') != 'curse': # updated from door_card_designator if a monster
                gameVar.GameObjects.message = f"Your card is: {door_card.get('name')}"
            app.update_message("show") #update the broadcast message

            #if monster do this and turn off these buttons.
            if door_card["type"] == "monster":
                # player.card_meths(door_card, 'static', 'on')  ######## will cause probs with monster individuality ######################

                self.door_button.config(state="disabled") # kick door
                self.weapons_button.config(state="disabled") # weapons
                self.armor_button.config(state="disabled") # armor
                self.sell_button.config(state="disabled") # sell
                self.fight_button.config(state="normal") # fight
                self.run_away_button.config(state="normal") # run
                #meth to return card, use id to put card pic

        # 2nd attempt circumstance
        elif gameVar.CardDraw.door_attempts == 0:
            print("2nd kick activated")
            gameVar.GameObjects.message = f"You have drawn a face down card that is placed in your hand"
            app.update_message("show")  # update the broadcast message
            self.pic = Tools.viewer(0)  # gets card pic face down
            self.canvas.create_image(10, 10, image=self.pic, anchor="nw") # puts door card face down
            self.door_button.config(state="disabled") # disables door button
            self.end_turn_button.config(state="normal") # enables fight
            app.update_message("show")

        gameVar.CardDraw.door_attempts = 0  # set to false
        Tools.fluid_player_info() # updates any changes cause by curses
        print("num of kicks", gameVar.CardDraw.door_attempts)

    # def update_info(self): # may be redundant for TOOLS fluid_player_info just button link left
    #     """method to update a player info window with any changes ie halfbreed ect"""
    #     if gameVar.GameObjects.active_player.race_unlock: # packing for klass and race in the event of supermunch ect
    #         self.race2_option.grid(row=8, column=1, sticky='nsew')
    #         self.race2_optionb.grid(row=8, column=2, sticky='nsew')
    #     if gameVar.GameObjects.active_player.klass_unlock:
    #         self.klass2_option.grid(row=9, column=1, sticky='nsew')
    #         self.klass2_optionb.grid(row=9, column=2, sticky='nsew')

    def fight(self):
        print("Fight button pressed")
        selfobj = app.frames[MainLoop]
        result = engine.fight() # helper may be added when sorting it
        app.update_message("show") # name and lvl of monster
        if result == "win":
            self.canvas.delete("all") # clears the canvas, not quite right as will remove all cards
            print('remove off canvas?????? ')
            # pass # remove single card off tablecards off table
        elif result == "loose":
            pass # clears table runs card method

        self.fight_button.config(state="disabled")  # fight
        self.run_away_button.config(state="disabled")  # run
        self.door_button.config(state="disabled")  # kick door

        # remove card form list and canvas ect
        self.end_turn_button.config(state="normal") # end turn
        self.weapons_button.config(state="normal")  # weapons
        self.armor_button.config(state="normal")  # armor
        print("End of Fight\n")
        Tools.fluid_player_info()

    def run(self):
        engine.card_method_activator("persistent", "on", card_num=0) # grabs the 1st card put on the table to run persistent method. TODO: change card_num for a card selector

        player = gameVar.GameObjects.active_player
        if player.run_away: # checks ability to run from player attrib
            result = engine.run()
            if result == "success":
                self.end_turn_button.config(state="normal")  # end turn
                self.fight_button.config(state="disabled")  # fight
                self.run_away_button.config(state="disabled")  # run
                self.canvas.delete("all")  # clears the canvas, not quite right as will remove all cards TAG maybe?
            else:
                gameVar.GameObjects.message = "You are trapped! All that is left is to fight!"
                app.update_message("show")
                self.run_away_button.config(state="disabled")  # run

        else:
            gameVar.GameObjects.message = "This is not a fight you can run from!"
            app.update_message("show")
            self.run_away_button.config(state="disabled")  # run

    def list_weapons(self):
        """ builds a list of cards that meet the the weapons criterion. List is bound to gameVar..selected_items """
        gameVar.GameObjects.message = "Weapons list"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.GameObjects.active_player
        player.inventory("type", "weapon")
        # print(gameVar.GameObjects.selected_items)  list all items
        OwnedItems("Weapons owned", "weap")

    def list_armor(self):
        gameVar.GameObjects.message = "Armour list"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.GameObjects.active_player
        player.inventory("type", "armor") # load all weapons items into gamevar.selected_items
        OwnedItems("Armor Owned", "armor")

    def consumables(self):
        gameVar.GameObjects.message = "Consumable items"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.GameObjects.active_player
        player.inventory("type", "disposable")
        OwnedItems("One shot items", "consume")

    def list_sell(self):
        """builds toplevel with sellable items"""
        gameVar.GameObjects.message = "Sell selected"
        app.update_message("show")
        engine.scrub_lists() # resets all lists for next action
        player = gameVar.GameObjects.active_player # gets current player
        player.item_by_key("sell") # generates list of sellable cards passed on to gameVar.selected_items
        # print(gameVar.StartVariables.selected_items) # call method that in gamefile that creates zip
        OwnedItems("Sellable Items", "sell") # calls toplevel with window title

    def hand(self):
        gameVar.GameObjects.message = "Hidden items selected"
        app.update_message("show")
        engine.scrub_lists()
        player = gameVar.GameObjects.active_player
        player.inventory("category", "door")
        OwnedItems("Hidden Items", "hidden")

    def interfere(self): #will link to player select toplvl window that then add an action . may need to look at card_matcher to be more flexible
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
        player = gameVar.GameObjects.active_player
        player.inventory("category", "treasure")
        OwnedItems("Sack Items")

    def list_equipped(self):
        """list showing all items that are equipped"""
        engine.scrub_lists()
        player = gameVar.GameObjects.active_player
        player.equipped_items("list_equipped")
        OwnedItems("Equipped Items", "remove")

    def status_effect(self):
        """method for showing what status effect are active on the current player"""
        pass


class OwnedItems(tk.Toplevel):
    """generates toplevel from cards place in gameVar.GameObjects.selected_items where selections can be made on those cards"""
    def __init__(self, wind_title="Template", set_but="No Buttons"): #title and buttons to be used for items
        tk.Toplevel.__init__(self)
        self.wind_title = wind_title
        self.title(self.wind_title)
        # self.geometry("350x250+200+200")
        self.set_but = set_but
        print(f"Top level self: {self}")

        if not gameVar.GameObjects.selected_items: # not work
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
                b1 = tk.Button(f, text="Info", command=lambda c=card["id"]: self.showcard(c))
                b1.grid(row=set_row, column=4)

                gameVar.GameObjects.check_but_intvar_gen.append(status) # creates list of IntVars for each item in list
                gameVar.GameObjects.check_but_card_ids.append(card["id"]) # sends card ids int to list
                set_row += 1

        if self.set_but in "weap, armor, sell":
            tk.Button(self, text="Sell", command=self.sell).pack(side="left")
        if self.set_but in "consume, hidden":
            tk.Button(self, text="Use item", command=self.use_item).pack(side="left")
        if self.set_but in "weap, armor": # == "weap" or self.set_but == "armor":##### added hidden for wandering mon ect
            tk.Button(self, text="Equip", command=self.equip).pack(side="left")
        if self.set_but == "remove":
            tk.Button(self, text="Remove", command=self.remove).pack(side="left")

    def showcard(self, card_id):
        """ Method for showing the card in a toplevel window"""
        CardVeiw(card_id)

    def sell(self):
        """triggers sell event when pushed"""
        Tools.common_set("sell")# calls zipper with param
        Tools.fluid_player_info() # calls an update method for gui to show all player changes, also cleans lists from zipper
        OwnedItems.destroy(self) # destroys toplevel window
        app.update_message("show")

    def equip(self):
        Tools.common_set("equip")
        Tools.fluid_player_info()
        OwnedItems.destroy(self)

        app.update_message("show")

    def use_item(self): #hidden items path hand and consume lead here
        """for consumables and hidden objects"""
        Tools.common_set("disposable") #
        Tools.fluid_player_info() # adds or removes player class2/race2 option
        OwnedItems.destroy(self)
        app.update_message("show")

    def remove(self):
        Tools.common_set("remove")
        Tools.fluid_player_info()
        OwnedItems.destroy(self)
        app.update_message("show")


class CardVeiw():
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
        # engine.varbinding(gameVar.GameObjects.active_player)
        # app.update_frame()

    @staticmethod
    def fluid_player_info():
        """class for showing individual player info ie klass2 race2"""
        selfid = app.frames[MainLoop]  # simplifies attachment to value for direct access.

        if not gameVar.GameObjects.active_player.race_unlock:
            selfid.race2_option.grid_forget()
            selfid.race2_optionb.grid_forget()
        else:
            selfid.race2_option.grid(row=8, column=1, sticky='nsew')
            selfid.race2_optionb.grid(row=8, column=2, sticky='nsew')
        if not gameVar.GameObjects.active_player.klass_unlock:
            selfid.klass2_option.grid_forget()
            selfid.klass2_optionb.grid_forget()
        else:
            selfid.klass2_option.grid(row=9, column=1, sticky='nsew')
            selfid.klass2_optionb.grid(row=9, column=2, sticky='nsew')

        engine.player_attrib_ipc_updater(gameVar.GameObjects.active_player) # ensures all player info is up to
        # date and sent to gameVar
        app.update_atrib_frame() # updates the GUI with the new player info
        engine.scrub_lists() # clears all the lists for zipper ect for fresh search

    @staticmethod #not working Yet
    def viewer(card_id=None):
        path = "..\\imgs\\cards\\"
        img = ImageTk.PhotoImage(file=f"{path}{str(card_id)}.png")
        return img



if __name__ == "__main__":
    app = Main()

    app.mainloop()

# Main().mainloop(), # removes the instance (self) which is needed for later activities
