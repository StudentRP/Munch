import os
import pathlib


# print(pathlib.Path(__file__).parent.resolve())
# print(str(pathlib.Path().resolve()))

#
# print(str(Path(__file__).resolve().parent.parent))
# BASE_DIR = Path(__file__).resolve().parent.parent
#
# print(os.path.join(BASE_DIR, 'bin', 'imgs', 'cards', f'{str(card_id)}.png'))

def p(*args, **kwargs):
    # for a in args:
    print(args, kwargs)
    if 'thio' in args:
        print(True)

    if 'mop' in kwargs:
        print(True)




p('thio', 'door', mop='boo')