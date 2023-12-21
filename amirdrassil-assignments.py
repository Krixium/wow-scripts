from common import Players, Markers


def generate_igira_assignments():
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

    soakers = [
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Cowflaps,
            Players.Teggyg,
            Players.Sossboy,
        ],
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Maranca,
            Players.Bartemaeus,
            Players.Terprekt,
        ],
        [
            Players.Frollexy,
            Players.Duravz,
            Players.Zef,
            Players.Seraphemia,
            Players.Mewmonkas,
            Players.Hevansheal,
            Players.Pallydøn,
        ],
    ]

    note = f"{soak_title}\n"

    for i in range(0, 3):
        note += headers[i]
        for soaker in soakers[i]:
            note += f"{soaker} {soak_msg[i]}  "
        note += "\n\n"

    return note


def generate_council_assignments():
    note = "liquidStart\n"

    for player in Players.Melee:
        note += f"{player} "
    note += "\n"

    for player in Players.Range:
        note += f"{player} "
    note += "\n"

    note += "liquidEnd\n"

    return note


def generate_larry_assignments():
    firefighters = [
        [Players.Maranca, Players.Inenta, Players.Kev],
        [Players.Kyttn, Players.Thefranchise, Players.Cowflaps],
        [Players.Gunnær, Players.Sossboy, Players.Zaur],
    ]

    ccers = [
        [Players.Kyttn, Players.Cowflaps, Players.Bartemaeus, Players.Thefranchise],
        [Players.Kyttn, Players.Cowflaps, Players.Bartemaeus, Players.Kev],
    ]

    cc_markers = [
        [Markers.Skull, Markers.Star],
        [Markers.Triangle, Markers.Diamond],
        [Markers.Cross, Markers.Circle],
        [Markers.Square, Markers.Moon],
    ]

    add_timings = [
        "{time:00:41,SCS:421316:1}{spell:421325} |cff654321Adds|r - ",
        "{time:01:34,SCS:421316:1}{spell:421325} |cff654321Adds|r - ",
    ]

    note = "hosestart\n"
    for rotation in firefighters:
        for player in rotation:
            note += f"{player} "
        note += "\n"
    note += "hoseend\n"

    note += "\n"

    for i in range(0, 2):
        note += f"CC Set {i+1}:\n"
        for j in range(0, 4):
            note += f"{ccers[i][j]}{cc_markers[j][0]}{cc_markers[j][1]}\n"
        note += "\n"

    for i in range(0, 2):
        note += add_timings[i]
        for j in range(0, 4):
            note += f"{ccers[i][j]} {{text}}CC {cc_markers[j][0]} or {cc_markers[j][1]}{{/text}}  "
        note += "\n"

    return note


def generate_nymue_assignments():
    def ensure_no_mythic_add_duplicates(back):
        check = set()
        for rotation in back:
            for player in rotation:
                assert (
                    player not in check
                ), f"{player.name} was assigned twice to go to mythic add"
                check.add(player)

    def ensure_back_assignments_are_playing(back, dps, healers):
        assert (
            len(rotating_dps) + len(rotating_healers) == 16
        ), "Some people are missing from the rotation"

        for rotation in back:
            for player in rotation:
                assert (
                    player in dps or player in healers
                ), f"{player} was assigned to the mythic add but isn't in on the fight"

    rotating_dps = [
        Players.Zef,
        Players.Zargrul,
        Players.Cowflaps,
        Players.Thefranchise,
        Players.Kyreoss,
        Players.Bartemaeus,
        Players.Maranca,
        Players.Sossboy,
        Players.Zaur,
        Players.Inenta,
        Players.Skxyz,
        Players.Sanzensekai,
        Players.Kev,
    ]
    rotating_healers = [
        Players.Kyttn,
        Players.Hevansheal,
        Players.Teggyg,
    ]
    back = [
        [
            Players.Hevansheal,
            Players.Skxyz,
            Players.Sanzensekai,
            Players.Sossboy,
            Players.Kev,
        ],
        [
            Players.Kyttn,
            Players.Bartemaeus,
            Players.Cowflaps,
            Players.Maranca,
            Players.Zargrul,
            Players.Thefranchise,
        ],
        [
            Players.Teggyg,
            Players.Zaur,
            Players.Kyreoss,
            Players.Zef,
            Players.Inenta,
        ],
    ]

    ensure_no_mythic_add_duplicates(back)
    ensure_back_assignments_are_playing(back, rotating_dps, rotating_healers)

    left_prefix = f"left {Players.Duravz} {Players.Mewmonkas} "
    right_prefix = f"right {Players.Frollexy} {Players.Seraphemia} "
    back_prefix = "back "

    left_assignments = []
    right_assignments = []
    for i in range(0, 3):
        left_side_dps = []
        right_side_dps = []
        for dps in rotating_dps:
            if dps not in back[i]:
                if len(left_side_dps) < 4:
                    left_side_dps.append(dps)
                else:
                    right_side_dps.append(dps)

        left_side_healers = []
        right_side_healers = []
        for healer in rotating_healers:
            if healer not in back[i]:
                if len(left_side_healers) < 1:
                    left_side_healers.append(healer)
                else:
                    right_side_healers.append(healer)

        left_assignment = left_prefix
        for player in left_side_dps:
            left_assignment += f"{player} "
        for player in left_side_healers:
            left_assignment += f"{player} "
        left_assignment += "\n"
        left_assignments.append(left_assignment)

        right_assignment = right_prefix
        for player in right_side_dps:
            right_assignment += f"{player} "
        for player in right_side_healers:
            right_assignment += f"{player} "
        right_assignment += "\n"
        right_assignments.append(right_assignment)

    back_assignments = []
    for rotation in back:
        assignment = back_prefix
        for player in rotation:
            assignment += f"{player} "
        assignment += "\n"
        back_assignments.append(assignment)

    note = "liquidStart\n"
    for i in range(0, 3):
        note += left_assignments[i]
        note += right_assignments[i]
        note += back_assignments[i]
        note += "\n"
    note = note[:-1]
    note += "liquidEnd\n"

    return note


def main():
    with open("amirdrassil-assignments.txt", "w") as output:
        output.write("igira assignments:\n\n\n")
        output.write(generate_igira_assignments())
        output.write("\n\n")

        output.write("council assignments:\n\n\n")
        output.write(generate_council_assignments())
        output.write("\n\n")

        output.write("larry assignments:\n\n\n")
        output.write(generate_larry_assignments())
        output.write("\n\n")

        output.write("nymue assignments:\n\n\n")
        output.write(generate_nymue_assignments())
        output.write("\n\n")


if __name__ == "__main__":
    main()
