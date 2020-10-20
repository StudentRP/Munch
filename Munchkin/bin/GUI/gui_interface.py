"""Main GUI interface for munchkin.

Requires hierarchy structure with frameview swapping

Goals:
    need to accept the instance of a class and dismantle it accordingly

"""
import tkinter as tk
from Munchkin.bin.players.playermodel import p1  # to show player instance in field
import tkinter.ttk as ttk

preset1 = ('curlz MT', 12, 'bold')
preset2 = ('curlz MT', 12, 'bold italic')

# customisation classes of buttons and Labels

#############################################################
# labels
#############################################################
class BaseLabel(tk.Label):
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.config(bg='yellow')


class Title_lab(BaseLabel):  # inherits from parent Label
    """customises labels for frame titles"""

    def __init__(self, *args, **kwargs):
        BaseLabel.__init__(self, *args, **kwargs)  # passes all args and kwargs to parent to sort
        self.config(font=preset1, fg='blue')


class LabStyle(BaseLabel):  # inherits from parent Label
    """customises labels for column data names"""

    def __init__(self, *args, **kwargs):
        BaseLabel.__init__(self, *args, **kwargs)  # passes all args and kwargs to parent to sort
        self.config(font=preset2, fg='grey')





################################################################
# buttons
################################################################


# first container object
class StartScreen(tk.Frame):
    """player select dropdown"""
    def __init__(self, *args, **kwargs):  # takes instance arg to feed into gui frame
        tk.Frame.__init__(self, *args, **kwargs)
        first_win = tk.Frame()
        first_win.pack(fill='both', expand='yes')
        self. player = tk.IntVar
        select = tk.Menubutton(first_win, text='Number of players')
        select.pack()
        combobox = ttk.Combobox(first_win, values=["Option 1", "Option 2", "Option 3"])
        combobox.pack()






class PlayerSetup(tk.Frame):
    """player name and gender setup """
    pass


class Playerinfo(tk.Frame):
    """fits in container1"""

    def __init__(self, instance, *args, **kwargs):  # takes instance arg to feed into gui frame
        tk.Frame.__init__(self, *args, **kwargs)
        cont1 = tk.Frame()
        self.main_title = Title_lab(cont1,  text='Player info')  # tk.Label(text="Player info")
        self.main_title.grid(row=0, column=0, columnspan=2)
        cont1.pack(side='left') #dictates where ethe frame goes in main window
        cont1.config(bg='yellow')

        self.name = LabStyle(cont1, text="Name: ", font=preset1)
        self.name.grid(row=1, column=0)
        self.show_name = tk.Label(cont1, text=f'{instance.name}', font=preset2)
        self.show_name.grid(row=1, column=1)

        self.gender = LabStyle(cont1, text="Gender: ", font=preset1)
        self.gender.grid(row=2, column=0)
        self.show_gender = tk.Label(cont1, text=f'{instance.sex}', font=preset2)
        self.show_gender.grid(row=2, column=1)

        self.level = LabStyle(cont1, text="Level: ", font=preset1)
        self.level.grid(row=3, column=0)
        self.show_level = tk.Label(cont1, text=f'{instance.level}', font=preset2)
        self.show_level.grid(row=3, column=1)

        self.bonus = LabStyle(cont1, text="Bonus: ", font=preset1)
        self.bonus.grid(row=4, column=0)
        self.show_bonus = tk.Label(cont1, text=f'{instance.bonus}', font=preset2)
        self.show_bonus.grid(row=4, column=1)

        self.show_sack = tk.Button(cont1, text="Sack", command=lambda: self.my_sack(instance), fg='red')
        self.show_sack.grid(row=5, column=0)

        self.show_weapons = tk.Button(cont1, text="Weapons", command=lambda: self.my_weapons(instance), fg='red')
        self.show_weapons.grid(row=5, column=1)

    def my_sack(self, instance):
        tl1 = tk.Toplevel() # new main window
        tl1.title('Sack Contents')
        tl1.geometry('300x400')
        tl = tk.Frame(tl1) # frame within toplevel
        tl.pack()


        tk.Label(tl, text='My Gold: ').grid(row=0, column=0)
        tk.Label(tl, text=f'{instance.wallet}').grid(row=0, column=1)

        print(instance.armor)

        for key, val in enumerate(instance.armor.items(), start=1):
            print(type(val))
            if val[1] == False:
                pass
            else:
                tk.Label(tl, text=f'{val[0]}: ').grid(row=key, column=0)
                tk.Label(tl, text=f'{val[1]}').grid(row=key, column=1)

    def my_weapons(self, instance):
        tl2 = tk.Toplevel()
        tl2.title('Weapons')
        tl2.geometry('300x400')
        tl = tk.Frame(tl2)
        tl.pack()
        print(instance.weapons)

        for key, val in enumerate(instance.weapons.items(), start=1):
            print(type(val))
            if val[1] == False:
                pass
            else:
                tk.Label(tl, text=f'{val[0]}: ').grid(row=key, column=0)
                tk.Label(tl, text=f'{val[1]}').grid(row=key, column=1)


# root setup

class Root(tk.Tk):
    """Customises the main tk window, takes in instance from game_loop"""

    def __init__(self, instance, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)  # passed to parent to handle
        self.title("Munchkin time")  # overrides parent name space from default
        self.geometry("600x600")  # overrides default geometry
        ### may have some form of bring to front object here for starting interfaces and method to switch between.
        """really important below. shows that i can pass info to other classes through this one"""
        self.container1 = Playerinfo(instance)  # passes p1 to another class.instance passed on from engine script.

        # does not do anything
        # c2 = tk.Frame()
        # self.container2 = c2
        # tk.Label(c2, text='Play area')
        # self.container2.grid(row=3, column=1, columnspan=2)
        #
        # c3 = tk.Frame()
        # self.container3 = c3
        # tk.Label(c3, text='Multi choice buttons')
        # self.container3 = c3
        # self.container3.grid(row=0, column=1, columnspan=2, rowspan=2)

    def container_getter(self):
        """changes over container objects"""



app = StartScreen()
app.mainloop()
