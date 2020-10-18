"""Main GUI interface for munchkin.

Requires hierarchy structure with frameview swapping

"""
import tkinter as tk


# customisation classes of buttons and Labels


class CustomLab(tk.Label):

    preset1 = ('curlz MT', 15, 'bold')
    def __init__(self, *args, **kwargs):
        tk.Label.__init__(self, *args, **kwargs)
        self.config(font=self.preset1, fg='blue')


# first container object

class Playerinfo(tk.Frame):
    """fits in contaier1"""
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.main_title = CustomLab(text='Player info') #tk.Label(text="Player info")
        self.main_title.grid(row=0, column=0, columnspan=2)





# root setup

class Root(tk.Tk):
    """Customises the main tk window"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs) # passed to parent to handle
        self.title("Munch time") # overrides parent name space from default
        self.geometry("600x600") # overrides default geometry
        self.container1 = Playerinfo() #tk.Label(text='Test label') #replace and adds new class as object
        self.container1.grid()# if created in class requires string format

    def container_getter(self):
        """changes over container objects"""



app = Root()

app.mainloop()