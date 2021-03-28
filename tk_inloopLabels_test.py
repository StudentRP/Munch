
"""
test to determine the effect of the pack_forget()
"""
import tkinter as tk

class Main(tk.Tk):
    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)
        self.title("wizard")
        self.frm = tk.Frame(self)
        self.frm.pack()
        self.con = tk.Label(self.frm, text="hello")
        self.con.pack(side="top")

        Main.l1 = tk.Label(self.frm, text="cheesepuff")
        # Main.l1.pack()

        self.b1 = tk.Button(self.frm, text="remove", command=self.remove_me)
        self.b1.pack()

    def remove_me(self):
        # Main.l1.pack_forget()
        Main.l1.pack()

app = Main()

app.mainloop()

# from tkinter import *
# class Alarm(Frame):
#
#     def __init__(self, msecs=1000): # default = 1 second
#         Frame.__init__(self)
#         self.msecs = msecs
#         self.pack()
#         stopper = Button(self, text='Stop the beeps!', command=self.quit)
#         stopper.pack()
#         stopper.config(bg='navy', fg='white', bd=8)
#         self.stopper = stopper
#         self.repeater()
#
#     def repeater(self): # on every N millisecs
#         print("running this meth A")
#         self.bell() # beep now
#         self.stopper.flash() # flash button now
#         self.after(self.msecs, self.repeater) # reschedule handler
#
# class Alarm2(Alarm): # change alarm callback
#     def __init__(self, msecs=1000): # default = 1 second
#         self.shown = False
#         Alarm.__init__(self, msecs)
#
#     def repeater(self): # on every N millisecs
#         print("running meth B")
#         self.bell() # beep now
#         if self.shown:
#             self.stopper.pack_forget() # hide or erase button now
#         else: # or reverse colors, flash...
#             self.stopper.pack()
#         self.shown = not self.shown # toggle state for next time !!!!switch mechanism for flipping between bool!!!
#         self.after(self.msecs, self.repeater) # reschedule handler
#
# if __name__ == '__main__': Alarm2(msecs=900).mainloop()

