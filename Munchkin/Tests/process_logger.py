########################################################
#### fault finding process logger
########################################################

log = "log.txt"


def log_creator(msg):
    print('Creating log', msg)
    with open("log.txt", 'w') as f: # opens new if not exists and truncates
        f.write(msg + '\n')
        f.close()


def log_note(msg):
    print('writing')
    with open(log, "a+") as f: # position at the end
        f.write(msg + '\n')
        f.close()
#
# log_creator('hello')
# log_note("this is a test")
# log_note("second test")
