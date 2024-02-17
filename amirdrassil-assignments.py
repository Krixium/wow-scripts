from common import Players, Markers, players_to_str


def generate_igira_assignments():
    """
    Hard coded to back -> right -> left. Only change the "soakers" array.
    Doesn't do assignments for second weapon combo because this script doesn't
    support group numbers yet. Just click that in manually before you pull.
    """
    soakers = [
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Sossboy,
            Players.Thefranchise,
        ],
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Maranca,
            Players.Zef,
        ],
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Kyttn,
            Players.Hevansheal,
            Players.Mewmonkas,
        ],
    ]

    soak_title = "|cffff00ff--- Intermission Weapon Soakers ---|r" + "\n"

    headers = [
        "{time:00:09,SCS:422776:1} - Back - ",
        "{time:00:09,SCS:422776:2} - Right - ",
        "{time:00:09,SCS:422776:3} - Left - ",
    ]

    soak_msg = [
        "{text}Back Soak{/text}",
        "{text}Right Soak{/text}",
        "{text}Left Soak{/text}",
    ]

    note = f"{soak_title}\n"

    for i in range(0, 3):
        note += headers[i]
        for soaker in soakers[i]:
            note += f"{soaker} {soak_msg[i]}  "
        note += "\n\n"

    return note


def generate_council_assignments():
    """
    Shouldn't have to touch this. Just does melee first then ranged.
    """
    note = "liquidStart\n"
    note += players_to_str(Players.Melee)
    note += players_to_str(Players.Range)
    note += "liquidEnd\n"

    return note


def generate_larry_assignments():
    """
    Nothing fancy for fighter fighters. Just put 3 sets 3 players in the
    firefighters array. Same thing for CCers, put 2 sets for 4 players in
    there. Do NOT touch the cc_markers or add_timings array.
    """
    firefighters = [
        [Players.Teggyg, Players.Zef, Players.Bartemaeus],
        [Players.Kyttn, Players.Thefranchise],
        [Players.Hevansheal, Players.Zaur, Players.Maranca],
    ]

    ccers = [
        [Players.Kyttn, Players.Teggyg, Players.Maranca, Players.Thefranchise],
        [Players.Kyttn, Players.Teggyg, Players.Maranca, Players.Bartemaeus],
    ]

    cc_markers = [
        [Markers.Skull, Markers.Star],
        [Markers.Triangle, Markers.Diamond],
        [Markers.Cross, Markers.Circle],
        [Markers.Square, Markers.Moon],
    ]

    note = "hosestart\n"
    for rotation in firefighters:
        note += players_to_str(rotation)
    note += "hoseend\n"

    note += "\n"

    add_timings = [
        "{time:00:41,SCS:421316:1}{spell:421325} |cff654321Adds|r - ",
        "{time:01:34,SCS:421316:1}{spell:421325} |cff654321Adds|r - ",
    ]

    for i in range(0, 2):
        note += f"CC Set {i+1}:\n"
        for j in range(0, 4):
            note += f"{ccers[i][j]} {cc_markers[j][0]}{cc_markers[j][1]}\n"
        note += "\n"

    for i in range(0, 2):
        note += add_timings[i]
        for j in range(0, 4):
            note += f"{ccers[i][j]} {{text}}CC {cc_markers[j][0]} or {cc_markers[j][1]}{{/text}}  "
        note += "\n"

    return note


def generate_nymue_assignments():
    """
    Assign the two tanks and two healers to left_prefix and right_prefix. Fill
    the back array with the 3 groups of people you want to go do the mythic
    add. Put every dps in rotating_dps and put the remaining healers into
    rotation_healers. For rotating_dps and rotating_healers, players near the
    front will be prioritized going left while players near the end will be
    prioritized going right when it is not their turn to do the mythic add.
    """

    def ensure_no_mythic_add_duplicates(back):
        check = set()
        for rotation in back:
            for player in rotation:
                assert (
                    player not in check
                ), f"{player.name} was assigned twice to go to mythic add"
                check.add(player)

    def ensure_back_assignments_are_playing(back, dps, healers):
        length = len(rotating_dps) + len(rotating_healers)
        assert (
            length == 16
        ), f"Some people are missing from the rotation, found {length}"

        for rotation in back:
            for player in rotation:
                assert (
                    player in dps or player in healers
                ), f"{player} was assigned to the mythic add but isn't in on the fight"

    left_tank = [Players.Duravz]
    right_tank = [Players.Frollexy]
    left_healers = []
    right_healers = [Players.Teggyg]
    rotating_dps = [
        Players.Zef,
        Players.Felthpot,
        Players.Bartemaeus,
        Players.Sossboy,
        Players.Cowflaps,
        Players.Maranca,
        Players.Thefranchise,
        Players.Zaur,
        Players.Inenta,
        Players.Sanzensekai,
    ]
    rotating_healers = [
        Players.Mewmonkas,
        Players.Hevansheal,
        Players.Kyttn,
    ]
    back = [
        [
            Players.Hevansheal,
            Players.Sanzensekai,
            Players.Sossboy,
        ],
        [
            Players.Kyttn,
            Players.Bartemaeus,
            Players.Maranca,
            Players.Cowflaps,
            Players.Thefranchise,
        ],
        [
            Players.Mewmonkas,
            Players.Zaur,
            Players.Inenta,
            Players.Felthpot,
            Players.Zef,
        ],
    ]

    ensure_no_mythic_add_duplicates(back)
    ensure_back_assignments_are_playing(back, rotating_dps, rotating_healers)

    left_prefix = "left "
    right_prefix = "right "
    back_prefix = "back "

    left_assignments = []
    right_assignments = []
    for i in range(0, 3):
        # pick dps
        left_side_dps = []
        right_side_dps = []
        for dps in rotating_dps:
            if dps not in back[i]:
                if len(left_side_dps) < 4:
                    left_side_dps.append(dps)
                else:
                    right_side_dps.append(dps)

        # pick healers
        left_side_healers = left_healers.copy()
        right_side_healers = right_healers.copy()
        for healer in rotating_healers:
            if healer not in back[i]:
                if len(left_side_healers) < 2:
                    left_side_healers.append(healer)
                else:
                    right_side_healers.append(healer)

        # turn picks into strings
        left_assignment = left_prefix + players_to_str(
            left_tank + left_side_healers + left_side_dps
        )
        left_assignments.append(left_assignment)

        right_assignment = right_prefix + players_to_str(
            right_tank + right_side_healers + right_side_dps
        )
        right_assignments.append(right_assignment)

    back_assignments = []
    for rotation in back:
        back_assignments.append(back_prefix + players_to_str(rotation))

    note = "liquidStart\n"
    for i in range(0, 3):
        note += left_assignments[i]
        note += right_assignments[i]
        note += back_assignments[i]
        note += "\n"
    note = note[:-1]
    note += "liquidEnd\n"

    return note


def generate_tswift_assignments():
    """
    To do assignemnts for this boss, just change the arrays of players below.
    Everything is relative to list length. The only number to is tweak how many
    dispels you intend to play.
    """
    total_num_dispels = 10

    melee_groups = [
        [Players.Zaur, Players.Inenta, Players.Zargrul],
        [Players.Sanzensekai, Players.Wendywoo, Players.Warkami],
    ]

    first_freedoms = [Players.Gunnær]
    second_freedoms = [Players.Kyreoss]

    healer_dispel_order = [
        Players.Seraphemia,
        Players.Kyttn,
        Players.Hevansheal,
        Players.Mewmonkas,
    ]

    note = ""
    note += "liquidStart\n"
    for rotation in melee_groups:
        note += players_to_str(rotation)
    note += "liquidEnd\n"
    note += "\n"

    note += "liquidStart2\n"
    skip_freedom_on_disel = 5
    for i in range(0, total_num_dispels):
        if i < skip_freedom_on_disel:
            note += f"{first_freedoms[i % len(first_freedoms)]} {second_freedoms[i % len(second_freedoms)]}\n"

        if i == skip_freedom_on_disel:
            note += "nobody\n"

        if i > skip_freedom_on_disel:
            note += f"{first_freedoms[(i - 1) % len(first_freedoms)]} {second_freedoms[(i - 1) % len(second_freedoms)]}\n"
    note += "liquidEnd2\n"
    note += "\n"

    note += "liquidStart3\n"
    note += players_to_str(healer_dispel_order)
    note += "liquidEnd3\n"
    note += "\n"

    note += f"#group1 {players_to_str(melee_groups[0])}"
    note += f"#group2 {players_to_str(melee_groups[1])}"
    note += "\n"

    return note


def generate_groups():
    groups = [
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Maranca,
            Players.Bartemaeus,
            Players.Asianbigpump,
        ],
        [
            Players.Sossboy,
            Players.Thefranchise,
            Players.Gunnær,
            Players.Kyreoss,
            Players.Wendywoo,
        ],
        [
            Players.Sanzensekai,
            Players.Warkami,
            Players.Zaur,
            Players.Zargrul,
            Players.Inenta,
        ],
        [
            Players.Seraphemia,
            Players.Kyttn,
            Players.Hevansheal,
            Players.Mewmonkas,
            Players.Sobura,
        ],
    ]

    import_string = ""

    for group in groups:
        for player in group:
            import_string += f"{player.name}\n"

    return import_string


def format_section(title, content):
    bar = "=" * 120
    return f"{bar}\n{title}:\n{bar}\n{content}\n"


def main():
    """
    Generates and dumps assignments into a text file so that it can easily be
    copied into MRT note in game.
    """
    with open("amirdrassil-assignments.txt", "w") as output:
        # output.write(format_section("igira", generate_igira_assignments()))
        # output.write(format_section("council", generate_council_assignments()))
        # output.write(format_section("nymue", generate_nymue_assignments()))
        output.write(format_section("tswift", generate_tswift_assignments()))
        output.write(format_section("groups", generate_groups()))


if __name__ == "__main__":
    main()
