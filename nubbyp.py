from common import players_to_str
import console_colors as cc
import players as p


def generate_header(title):
    return f"""{cc.HEADER}=========================================
{title}
========================================={cc.ENDC}"""


def generate_m_bloodbound_horror():
    odd_affinity = [
        p.Mew,
        p.Mord,
        p.Patch,
        p.Jordan,
        p.Nik,
        p.Inenta,
        p.Zac,
        p.Zargrul,
        p.Fran,
        p.Musty,
        p.Bug,
    ]
    even_affinity = [
        p.Andrew,
        p.Jenn,
        p.Zwarg,
        p.Zerg,
        p.Jump,
        p.Horn,
        p.David,
        p.Soss,
        p.Kyreoss,
        p.Doug,
        p.Hidrag,
    ]
    playing = [
        p.Jordan,
        p.Nik,
        p.Zaur,
        p.Inenta,
        p.Zac,
        p.Froll,
        p.Zwarg,
        p.Zerg,
        p.Jump,
        p.Horn,
        p.Zargrul,
        p.Mew,
        p.Mord,
        p.Fran,
        p.Musty,
        p.David,
        p.Andrew,
        p.Jenn,
        p.Soss,
        p.Kyreoss,
    ]
    odds = [p.Zaur]
    evens = [p.Froll]

    # tanks and healers first
    for healer in p.Healers:
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
        p.Froll,
        p.Zaurdk,
        p.Zac,
        p.Kyreoss,
        p.Andrew,
        p.Inenta,
        p.Mew,
        p.Jenn,
        p.Zwarg,
        p.Zargrul,
        p.Nik,
        p.Horn,
        p.Doug,
        p.Soss,
        p.Bug,
        p.Mord,
        p.Jump,
        p.Jordan,
        p.Patch,
        p.Fran,
    ]

    # add CC
    cc_rotation = [p.Zerg, p.Horn, p.Inenta]

    # kicks
    square_kicks = [p.Zwarg, p.Kyreoss, p.Horn, p.Inenta]
    moon_kicks = [p.Soss, p.Fran, p.Zac, p.Zerg]
    cross_kicks = [p.Zargrul, p.Jump, p.Nik, p.Zargrul]

    filler_kicks = [
        p.Doug,
        p.Musty,
        p.Jordan,
        p.David,
    ]

    for i in range(len(filler_kicks) - 1, -1, -1):
        if filler_kicks[i] not in playing:
            filler_kicks.pop(i)

    moon_kicks.insert(1, filler_kicks[0])
    cross_kicks.insert(0, filler_kicks[1])

    # knockbacks
    purple_knocks = [p.Nik]
    green_knocks = [p.Jenn]

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
