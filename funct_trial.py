""" Area to test algorithms"""
import tkinter as tk
app = tk.Tk()

"""Design for engine for returning a nested dict of call associated cards and possible toplevel design for gui"""

l = [{'type':'weap', 'des':'sword'},{'type':'hat', 'des':'fluffy'}, {'type':'weap', 'des':'axe'}]

caller = "weap" #to be called as a param in the method (specific to caller!)

x = [obj for obj in l if obj['type'] == caller]

print(x)


main = tk.Frame(app)
main.pack()
f = tk.Frame(main)
f.pack(side="top", expand=True)
tk.Label(f, text="Name").grid(row=0, column=0, sticky="nw")
tk.Label(f, text="Des").grid(row=0, column=1, sticky="nw")
tk.Label(f, text="Sell").grid(row=0, column=2, sticky="nw")
tk.Label(f, text="Equip").grid(row=0, column=3, sticky="nw")

for lab in x:
    f1 = tk.Frame(main)
    f1.pack(side="top", expand=True)
    l1 = tk.Label(f1, text=lab['type'])
    l1.grid(row=0, column=0, sticky="nw")
    l2 = tk.Label(f1, text=lab['des'])
    l2.grid(row=0, column=1, sticky="nw")
    tk.Checkbutton(f1, text=" ").grid(row=0, column=2, sticky="nw")
    tk.Radiobutton(f1, text=" ").grid(row=0, column=3, sticky="nw")



app.mainloop()