"""Classes to define player/s and specific attributes and mechanics (

Considerations:
    user name  ...............................Complete
    gender ......................................Complete
    play order, may be toplevel(engine)...........Complete, in engine!!
    number of players ........................... Complete in engine


    """

import bin.GUI.variables_library as gameVar


class P_tools():
    """Tools associated to the player class"""

    # def equip(self, card): #recieves player instance and card dict #todo
    #     # for name, component in card.items():
    #     #     print(f"{name}: {component}
    #     print(f'{card["name"]} to be equipped to {self.name}')
    #     # if card["lvl"]:
    #     #     print("can not equip monster")

    # def card_options(self, card): # receives card object #todo missing veiw for all cards in player sack
    #     """Options for cards: Equip, Use, Sell and Charity"""
    #     print(f"You have chosen: {card}")
    #     sack_menu = input("Sack options:\n1) Equip\n2) Use\n3) Sell\n4) Charity\n5) Back\n>>> ")
    #     if sack_menu.title() == "1" or "Equip":
    #         # print(contents)
    #         P_tools.equip(self, card)  # sends self and card to method
    #
    #     elif sack_menu.title() == "2" or "Use":
    #         print("used up")  # to method
    #     elif sack_menu.title() == "3" or "Sell":
    #         pass  # to method
    #     elif sack_menu.title() == "3" or "Charity":
    #         pass  # to method
    #     elif sack_menu.title() == "3" or "Back":
    #         print('returning back only')
    #         return 'back',
    #     else:
    #         print("Unknown command")


    @classmethod
    def gender(cls):
        """Sets gender"""
        x = gameVar.PlayerAttribs.player_gender
        return x

    @classmethod
    def name(cls):
        """Sets name"""
        x = gameVar.PlayerAttribs.player_name
        if x == "rory": # ......................................................................... dev mode
            y = "The_Creator"
            return y
        return x
