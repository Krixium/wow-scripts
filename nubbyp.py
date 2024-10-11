from common import Players, Player, PlayerClass, Role, players_to_str

def generate_ovinax():
    # add CC
    cc_rotation = [ Players.Zerg, Players.Horn, Players.Inenta ]

    # kicks
    square_kicks = [ Players.Zwarg, Players.Kyreoss, Players.Horn, Players.Inenta ]
    moon_kicks = [ Players.Soss, Players.Doug, Players.Fran, Players.Zac, Players.Zerg ]
    cross_kicks = [ Players.Jordan, Players.Zargrul, Players.Jump, Players.Nik, Players.Zargrul ]

    # knockbacks
    purple_knocks = [ Players.Nik ]
    green_knocks = [ Players.Jenn ]

    note = ""
    note += f"CC Order: {cc_rotation[0]} -> {cc_rotation[1]} -> {cc_rotation[2]}\n"
    note += "\n"
    note += "intstart\n"
    note += "npc:219046\n"
    note += "spell:446700\n"
    note += f"{{square}} {players_to_str(square_kicks)}\n"
    note += f"{{moon}} {players_to_str(moon_kicks)}\n"
    note += f"{{cross}} {players_to_str(cross_kicks)}\n"
    note += "intend\n"
    note += "\n"
    note += "liquidStart\n"
    note += f"{{rt3}} {players_to_str(purple_knocks)}\n"
    note += f"{{rt4}} {players_to_str(green_knocks)}\n"
    note += "liquidEnd\n"
    note += """
liquidStart2
0 5 0 6
6 5 0 0
5 0 0 0

0 5 0 6
7 6 5 0
0 0 0 0

6 5 0 6
6 5 0 0
0 6 7 5
liquidEnd2
        """

    return note


if __name__ == "__main__":
    print(generate_ovinax())
