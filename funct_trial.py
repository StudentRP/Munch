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

# def x(n):
#     l = [1,2,3]
#     print(l[int(n)])
#
# x(-1)
#
# f = {'rest': ["tester", 'pop', 'not_man']}
#
# if 'not_man' in f.get('rest'):
#     print("yep")
#     print(f.get('res', False)) # none object, can now return false

# for x in f['rest']:
#     print(x)
#
# else:
#     print("nope")
# app.mainloop()

def card_meth(*arg, **kwargs):
    print(arg)
    for cardset in arg:
        print(cardset)
        for card in cardset:
            print(card)
            if 'mon' in card:
                print('monster found')
            else:
                print(card.get('enhancer', 'Not enhancer'))

    # if kwargs.get('foo'):
    #     print('in dict')
# card_meth('foo', 'bar', foo='foobar')

# f = [ [{'mon': ["a", 'aa', 'aaa']}, {'enhancer': ["x", 'xx', 'xxx']}], [{'mon': ["b", 'bb', 'bbb']}] ]
# n = {'mon': ["a"]}, {'enhancer': ['enhancer found']}, {'mon': ["b"]}, {'weap': ["w"]}  # simulates 3 cards in list
# # card_meth(n)
#
# # print(f[0][0].get('mon')) # [fight selector], [monster selector].dict atrib fetcher
# # print(f[0][0])
# # print(len(f[0][0]))
# # print(len(f))
# # x=f
# # print(id(f), id(x))
#
# armor = {"headgear": "", "armor": "", "knees": "", "footgear": "", "necklace": "", "ring": {'fireband': ['hot!']}, "ring2": ""}
#
# print(armor)
# print(armor.get('ring'))
# a = armor.pop('ring')
# a = armor['ring'] = "" # need to be added back in as pop removes
# print(armor)
# print(a)
# x = A

p= [['a'],['a']]

while len(p) >= 1:
    p.pop(-1)
    print('monster present')
