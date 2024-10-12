from common import players_to_str
from console_colors import *
from players import *


def generate_header(title):
    return f"""{HEADER}=========================================
{title}
========================================={ENDC}"""


def generate_m_bloodbound_horror():
    odd_affinity = [ Mew, Mord, Patch, Jordan, Nik, Inenta, Zac, Zargrul, Fran, Musty, Bug, ]
    even_affinity = [ Andrew, Jenn, Zwarg, Zerg, Jump, Horn, David, Soss, Kyreoss, Doug, ]
    playing = [
        Jordan, Nik, Zaur, Inenta, Zac,
        Froll, Zwarg, Zerg, Jump, Horn,
        Zargrul, Mew, Mord, Fran, Musty,
        David, Andrew, Jenn, Soss, Kyreoss,
    ]
    odds = [ Zaur ]
    evens = [ Froll ]

    # tanks and healers first
    for healer in Healers:
        if healer in playing:
            if healer in odd_affinity and len(odds) < 3:
                odds.append(healer)
            elif healer in even_affinity and len(evens) < 3:
                evens.append(healer)
            elif len(odds) <= len(evens):
                odds.append(healer)
            else:
                evens.append(healer)

    # fill with dps
    for player in playing:
        if player in odds or player in evens:
            continue
        if len(odds) >= 10:
            evens.append(player)
        elif len(evens) >= 10:
            odds.append(player)
        elif player in odd_affinity:
            odds.append(player)
        elif player in even_affinity:
            evens.append(player)
        elif len(odds) <= len(evens):
            odds.append(player)
        else:
            evens.append(player)

    groups = "\n"
    for player in odds[:5]:
        groups += f"{player.name(colored=False)}\n"
    for player in evens[:5]:
        groups += f"{player.name(colored=False)}\n"
    for player in odds[5:]:
        groups += f"{player.name(colored=False)}\n"
    for player in evens[5:]:
        groups += f"{player.name(colored=False)}\n"
    return groups


def generate_m_ovinax():
    playing = [
        Froll, Zaurdk, Zac, Kyreoss, Andrew,
        Inenta, Mew, Jenn, Zwarg, Zargrul,
        Nik, Horn, Doug, Soss, Bug,
        Mord, Jump, Jordan, Patch, Fran,
    ]

    # add CC
    cc_rotation = [ Zerg, Horn, Inenta ]

    # kicks
    square_kicks = [ Zwarg, Kyreoss, Horn, Inenta ]
    moon_kicks = [ Soss, Fran, Zac, Zerg ]
    cross_kicks = [ Zargrul, Jump, Nik, Zargrul ]

    filler_kicks = [ Doug, Musty, Jordan, David, ]

    for i in range(len(filler_kicks) - 1, -1, -1):
        if filler_kicks[i] not in playing:
            filler_kicks.pop(i)

    moon_kicks.insert(1, filler_kicks[0])
    cross_kicks.insert(0, filler_kicks[1])

    # knockbacks
    purple_knocks = [ Nik ]
    green_knocks = [ Jenn ]

    return f"""
CC Order: {cc_rotation[0]} -> {cc_rotation[1]} -> {cc_rotation[2]}

intstart
npc:219046
spell:446700
{{square}} {players_to_str(square_kicks)}
{{moon}} {players_to_str(moon_kicks)}
{{cross}} {players_to_str(cross_kicks)}
intend

liquidStart
{{rt3}} {players_to_str(purple_knocks)}
{{rt4}} {players_to_str(green_knocks)}
liquidEnd

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

if __name__ == "__main__":
    print(generate_header("Mythic Bloodbound Horror"))
    print(generate_m_bloodbound_horror())
    print(generate_header("Mythic Ovinax"))
    print(generate_m_ovinax())
