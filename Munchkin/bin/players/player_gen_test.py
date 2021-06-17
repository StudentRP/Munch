""" Consideration to build players on the fly instead of set amount.
Limiting factor consider card numbers when shared thus can have 50 players.."""


class Player:

    players = []

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        print(f"changing name from {self.name} to {new_name}.")
        self.name = new_name
        print(f"your new name is now {self.name}")

    @classmethod
    def show_list(cls):
        print("players in list:\n ")
        for x in Player.players:
            print(x.name.title())
    @staticmethod
    def make_player(name, age):
        p = Player(name, age)

        Player.players.append(p)


Player.make_player("rory", 38)
Player.make_player("ethan", 13)
Player.show_list()
x = Player.players[0]
x.change_name("Master")
Player.show_list()
