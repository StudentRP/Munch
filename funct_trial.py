""" Area to test algorithms"""
# import tkinter as tk
# app = tk.Tk()

"""Design for engine for returning a nested dict of call associated cards and possible toplevel design for gui"""

# l = [{"id": 1, 'type':'weap', 'des':'sword'},
#      {"id": 2, 'type':'hat', 'des':'fluffy'},
#      {"id": 3, 'type':'weap', 'des':'axe'}]

# caller = "hat" #to be called as a param in the method (specific to caller!)
#
# x = [obj for obj in l if obj['type'] == caller]

# print(x)
# print(l[0]["type"])

# result = [] #dont forget to clear after use
# boo = []
# ids = []
# zipper = []
# main = tk.Frame(app)
# main.pack()
#
# def remove():
#     for item in x:
#         print(f"item is {item}")
#         print(zipper)
#         print(l)
#         for tup in zipper:
#             print(tup)
#             if tup[0] == item["id"] and tup[1]: # tup[1] should be 1or 0 thus true or false
#                 print(f"removing item {item['des']}")
#                 l.pop(l.index(item))
#                 print(l)
#             else:
#                 continue
#
# def grab():
#     global zipper
#     for var in result:
#         boo.append(var.get())
#     # print(boo)
#     # print(ids)
#     zipper = list(zip(ids, boo))
#     # print(zipper)
#     remove()
#
#
#
# f = tk.Frame(main)
# f.pack(side="top", expand=True)
# tk.Label(f, text="Name").grid(row=0, column=0, sticky="nw")
# tk.Label(f, text="Des").grid(row=0, column=1, sticky="nw")
# tk.Label(f, text="Sell").grid(row=0, column=2, sticky="nw")
# tk.Label(f, text="Equip").grid(row=0, column=3, sticky="nw")
#
# for lab in x:
#     status = tk.IntVar()
#     f1 = tk.Frame(main)
#     f1.pack(side="top", expand=True)
#     l1 = tk.Label(f1, text=lab['type'])
#     l1.grid(row=0, column=0, sticky="nw")
#     l2 = tk.Label(f1, text=lab['des'])
#     l2.grid(row=0, column=1, sticky="nw")
#     tk.Checkbutton(f1, text=" ", variable=status).grid(row=0, column=2, sticky="nw")
#     result.append(status)
#     ids.append(lab["id"])
#     # tk.Radiobutton(f1, text=" ").grid(row=0, column=3, sticky="nw")
#
# tk.Button(f, text="sell", command=grab).grid(row=1, column=0, columnspan=3)
#
#

# d = {"hat": "", "chair": {"p":"winner"}}
#
# if isinstance(d.get("chair"), dict):
#     print("true")
# else:
#     print("false")

def x(n):
    l = [1,2,3]
    print(l[int(n)])

x(-1)
# app.mainloop()