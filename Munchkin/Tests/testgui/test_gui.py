"""sets teh variable"""
from tkinter import *


# class Holder:
#     def __init__(self):
#         self.name = StringVar()

    # def caller(self):
    #     print(self.name.get())




class Mains(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title('test gui')
        self.name = StringVar()
        self.geometry('200x200')
        Label(self, text='Player: ').pack(side='left')
        Button(self, text='get', command=lambda:self.change()).pack(side='bottom')

    def change(self):

        Label(self, textvariable=self.name).pack(side='right')




# tester = Holder()

if __name__ == '__main__':
    g = Mains()
    g.mainloop()
