"""sets teh variable"""
from tkinter import *
import time


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
        Button(self, text='Auto', command=self.autoupdate).pack(side='bottom')
        self.run = 0

        # print(self.run)
        Label(self, textvariable=self.name).pack(side='right')
        # print(x['textvariable'])  # specifies what is in the key val pair

    def change(self):
        """ if i move player instance here i must import them!"""
        from Munchkin.Tests.testengine.test_engine import p1,p2

        if self.run == 0:
            self.name.set(p1.name)
            print(f'herein 1 {self.name}')
            self.run = 1

        elif self.run == 1:
            self.name.set(p2.name)
            print(f'herein 2 {self.name}')
            self.run = 0

        """here creates problems in duplication and not clearing the var!! Moved to top."""
        # print(self.run)
        # x = Label(self, textvariable=self.name)
        # x.pack(side='right')
        # print(x['textvariable']) # specifies what is in the key val pair

    def autoupdate(self):
        for x in range(5):
            self.change()
            time.sleep(1)





# tester = Holder()

if __name__ == '__main__':
    g = Mains()
    g.mainloop()
