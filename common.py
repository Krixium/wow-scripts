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
    Froll = Player("Frollexy", PlayerClass.DeathKnight, Role.Tank)
    Zaur = Player("Zaur", PlayerClass.Warrior, Role.Tank)
    Zaurdk = Player("Zaurdk", PlayerClass.DeathKnight, Role.Tank)

    Fotem = Player("Fotem", PlayerClass.Shaman, Role.Healer)
    Jenn = Player("Kyttn", PlayerClass.Druid, Role.Healer)
    Mewmonkas = Player("Mewmonkas", PlayerClass.Monk, Role.MeleeHealer)
    Mord = Player("Melzrynen", PlayerClass.Evoker, Role.Healer)
    Patch = Player("Patchemup", PlayerClass.Priest, Role.Healer)

    Bug = Player("Bugser", PlayerClass.Rogue, Role.Melee)
    Horn = Player("Hornstarlet", PlayerClass.DemonHunter, Role.Melee)
    Inenta = Player("Inenta", PlayerClass.Warrior, Role.Melee)
    Kyreoss = Player("Kyreoss", PlayerClass.Paladin, Role.Melee)
    Zargrul = Player("Zargruldk", PlayerClass.DeathKnight, Role.Melee)
    Zerg = Player("Zërgpöp", PlayerClass.Monk, Role.Melee)
    Zwarg = Player("Zwarg", PlayerClass.Shaman, Role.Melee)

    Jordan = Player("Bartemaeus", PlayerClass.Warlock, Role.Range)
    Doug = Player("Sincrum", PlayerClass.Mage, Role.Range)
    Jump = Player("Jumpskillz", PlayerClass.Hunter, Role.Range)
    David = Player("Maranca", PlayerClass.Warlock, Role.Range)
    Musty = Player("Redmustard", PlayerClass.Warlock, Role.Range)
    Nik = Player("Teggyg", PlayerClass.Druid, Role.Range)
    Soss = Player("Sossboy", PlayerClass.Mage, Role.Range)
    Fran = Player("Thefranchise", PlayerClass.Hunter, Role.Range)
    Zac = Player("Zacían", PlayerClass.Hunter, Role.Range)

    Tanks = [Froll, Zaur, Zaurdk]

    MeleeHealers = [Mewmonkas]
    RangeHealers = [Fotem, Jenn, Mord, Patch]
    Healers = MeleeHealers + RangeHealers

    MeleeDPS = [Bug, Horn, Inenta, Kyreoss, Zargrul, Zerg, Zwarg]

    RangeDPS = [Jordan, Doug, Jump, David, Musty, Nik, Soss, Fran, Zac]

    DPS = MeleeDPS + RangeDPS
    Melee = MeleeDPS + MeleeHealers
    Range = RangeDPS + RangeHealers


def players_to_str(players):
    result = ""
    for player in players:
        result += f"{player} "
    return result


def print_response(response):
    print(json.dumps(response.json(), indent=2))
