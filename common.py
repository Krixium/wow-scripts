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
        self._name = name
        self._playerClass = playerClass
        self._role = role

    def name(self, colored=True):
        if colored:
            return f"|c{self._playerClass}{self._name}|r"
        else:
            return f"{self._name}"

    def __str__(self):
        return self.name(colored=True)

def players_to_str(players, colored=True):
    result = ""
    for player in players:
        result += f"{player.name(colored)} "
    return result


def print_response(response):
    print(json.dumps(response.json(), indent=2))
