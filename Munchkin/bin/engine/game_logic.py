"""All logic associated to main loop delegation pulling cards from dealer augmenting with player objects
TO MAKE AS CLASS!!!
Considerations:
    choice 1
    choice 2
    choice 3
    correlation of player vs cards
    player intervention mechanics
    exports treasure/curse objects to player self
    fight
    fight menu

    """

from Munchkin.bin.players.playermodel import Player, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10
from Munchkin.bin.all_cards.table import cards, dice


def fight(pobj, *args):#todo
    """Receives player object and door card""" # have  use for player
    print('in fight method')


def fight_menu(pobj, *args):
    """menu for fighting"""# need to ad separator for monster and curse cards
    run = True
    while cards.in_play:

        choice2 = input(f"{pobj.name} What will you do?\n1) Run\n2) others interfere\n3) Current player info\n"
                        f"4) Fight\n5) Inspect monster") # inspect players open cards, others interferer will have use
        # select
        if choice2 == "1" and run:
            "choice to run from first monster on list"
            escape = dice.dice_sop.roll()
            print(f"You rolled a {escape}!")
            if escape >= 4:
                print(f"Monster alluded {pobj.name}")
                removed = cards.in_play.pop(0)
                cards.burn_pile.append(removed)
                print("You do not get any treasure and you get no level.")
                print(f"{cards.burn_pile[-1]['name']} moved to burn pile")
                run = True # ensures flag is reset
            elif escape < 4:
                "Failed escape"
                run = False
                print("Cant run, must fight!")

        elif choice2 == "2": #todo
            print("Others now involved Fab!") # test script only
            current_fight = cards.card_sop.deal_cards(11)  # test script only
            cards.in_play.append(current_fight) # test script only

        elif choice2 == "3":#todo
            print("\nCurrent player open cards and stats\n")
            run = True ## for debug to be removed
            print(pobj.__str__())

        elif choice2 == "4": #todo
            fight(pobj)

        elif choice2 == "5":
            print('\n', cards.in_play)
            for monster in cards.in_play:
                print(monster["name"], '\n')

        else:
            print("\nYou cant run from this!\n")


def monster_or_curse(pobj, all_players):
    """Determines if you get in fight or get cursed""" # maybe add sect for visible cards #todo
    for card in cards.in_play:
        if card["name"] == "curse":
            print('you have been cursed')
            break
        elif card["name"] != "cures":
            print("fighting monster!")
            fight_menu(pobj, all_players)
        else:
            print("card distinction fail")


def start_choice(pobj, all_players):# takes player instance
    """First choice of player. """
    choice1 = str(input("\nYou can:\n1) Kick open door\n2) Inventory\n>>> "))
    if choice1 == "1":
        "leads to fight"
        # 11 is door deck, 12 is treasure deck (see table.start_deal)
        current_fight = cards.card_sop.deal_cards(11) #  grabs single door card. Fails when not enough cards!!!
        cards.in_play.append(current_fight) # places card on table,
        monster_or_curse(pobj, all_players) # OPTIONS REQUIRED: interference, run, use item

        return f"{current_fight} is fighting:"
        # for card in cards.in_play:
        #     "4 options: fight, run, intervention or curse/other action on current card"
        #     print(f"\nCARD IN PLAY: {card['name']} LEVEL: {card['lvl']}")

    elif choice1 == "2":
        "Player info and player setup and view"
        # OPTIONS REQUIRED: equip,

        Player.inventory(pobj)
        start_choice(pobj)

    else:
        print("Command not recognised")
        start_choice(pobj)



