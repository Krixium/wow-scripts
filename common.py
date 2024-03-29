import json


class Markers:
    Circle = "{circle}"
    Cross = "{cross}"
    Diamond = "{diamond}"
    Moon = "{moon}"
    Skull = "{skull}"
    Square = "{square}"
    Star = "{star}"
    Triangle = "{triangle}"


class PlayerClass:
    DeathKnight = "ffc31d39"
    DemonHunter = "ffa330c9"
    Druid = "fffe7b09"
    Evoker = "ff33937f"
    Hunter = "ffaad372"
    Mage = "ff3fc7eb"
    Monk = "ff00fe97"
    Paladin = "fff48cba"
    Priest = "fffefefe"
    Rogue = "fffff468"
    Shaman = "ff0070dd"
    Warlock = "ff8788ee"
    Warrior = "ffc69b6d"


class Role:
    Tank = "Tank"
    Healer = "Healer"
    MeleeHealer = "Melee Healer"
    Healer = "Healer"
    Melee = "Melee"
    Range = "Range"


class Player:
    def __init__(self, name, playerClass, role) -> None:
        self.name = name
        self.playerClass = playerClass
        self.role = role

    def __str__(self):
        return "|c{color}{name}|r".format(color=self.playerClass, name=self.name)


class Players:
    Duravz = Player("Duravz", PlayerClass.DemonHunter, Role.Tank)
    Frollexy = Player("Frollexy", PlayerClass.DeathKnight, Role.Tank)

    Hevansheal = Player("Hevansheal", PlayerClass.Paladin, Role.MeleeHealer)
    Kyttn = Player("Kyttn", PlayerClass.Druid, Role.Healer)
    Mewmonkas = Player("Mewmonkas", PlayerClass.Monk, Role.MeleeHealer)
    Seraphemia = Player("Seraphemia", PlayerClass.Priest, Role.Healer)

    Asianbigpump = Player("Asianbigpump", PlayerClass.DemonHunter, Role.Melee)
    Felthpot = Player("Felthpot", PlayerClass.DemonHunter, Role.Melee)
    Gunnær = Player("Gunnær", PlayerClass.Paladin, Role.Melee)
    Inenta = Player("Inenta", PlayerClass.Warrior, Role.Melee)
    Kyreoss = Player("Kyreoss", PlayerClass.Paladin, Role.Melee)
    Sanzensekai = Player("Sanzensekai", PlayerClass.Shaman, Role.Melee)
    Warkami = Player("Warkami", PlayerClass.Rogue, Role.Melee)
    Wendywoo = Player("Wendywoo", PlayerClass.Monk, Role.Melee)
    Zargrul = Player("Zargrulwr", PlayerClass.Warrior, Role.Melee)
    Zaur = Player("Zaur", PlayerClass.Warrior, Role.Melee)

    Bartemaeus = Player("Bartemaeus", PlayerClass.Warlock, Role.Range)
    Cowflaps = Player("Cowflaps", PlayerClass.Druid, Role.Range)
    Maranca = Player("Maranca", PlayerClass.Warlock, Role.Range)
    Sobura = Player("Sobura", PlayerClass.Druid, Role.Range)
    Sossboy = Player("Sossboy", PlayerClass.Mage, Role.Range)
    Teggyg = Player("Teggyg", PlayerClass.Druid, Role.Range)
    Thefranchise = Player("Thefranchise", PlayerClass.Hunter, Role.Range)
    Zef = Player("Zefraniu", PlayerClass.Evoker, Role.Range)

    Tanks = [Duravz, Frollexy]

    MeleeHealers = [Hevansheal, Mewmonkas]
    RangeHealers = [Kyttn, Seraphemia]
    Healers = MeleeHealers + RangeHealers

    MeleeDPS = [
        Asianbigpump,
        Sanzensekai,
        Felthpot,
        Gunnær,
        Inenta,
        Kyreoss,
        Warkami,
        Wendywoo,
        Zargrul,
        Zaur,
    ]

    RangeDPS = [
        Bartemaeus,
        Cowflaps,
        Maranca,
        Sobura,
        Sossboy,
        Teggyg,
        Thefranchise,
        Zef,
    ]

    DPS = MeleeDPS + RangeDPS
    Melee = MeleeDPS + MeleeHealers
    Range = RangeDPS + RangeHealers


def players_to_str(players):
    result = ""
    for player in players:
        result += f"{player} "
    result += "\n"
    return result


def print_response(response):
    print(json.dumps(response.json(), indent=2))
