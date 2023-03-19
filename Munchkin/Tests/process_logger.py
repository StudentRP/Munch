########################################################
#### fault finding process logger
########################################################
import os

log = "log.txt"


def log_creator(msg):
    print('Creating log', msg)
    with open("log.txt", 'w') as f: # opens new if not exists and truncates
        f.write(msg + '\n')
        f.close()


def log_note(msg):
    with open(log, "a+") as f: # position at the end
        f.write(msg)
        f.close()
#
# log_creator('hello')
# log_note("this is a test")
# log_note("second test")


# def f(*args):
#   print(args)  #tuple
#     for x in args:
#       print(x) #lol
#         for y in x:
#             print(y) # specific
#
# l= [[1],[2]]
# f(l)



