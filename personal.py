from common import Player, PlayerClass, Role, players_to_str

me = Player("Zaur", PlayerClass.Warrior, Role.Tank)

# genenral
rally = 97462

# prot
last_stand = 12975
shield_wall = 871
spell_block = 392966


def seconds(n):
    return n


def minutes(n):
    return seconds(60) * n


class Entry:
    def __init__(self, time) -> None:
        self._time = time
        self._id = 0
        self._note = ""

    def spell(self, id):
        assert self._note == ""
        self._id = int(id)
        return self

    def note(self, s):
        assert self._id == 0
        self._note = s
        return self

    def __str__(self) -> str:
        if self._id == 0 and self._note != "":
            return f"{{time:{self._time}}} {me} {{text}}{self._note}{{/text}}  "
        elif self._id != 0 and self._note == "":
            return f"{{time:{self._time}}} {me} {{spell:{self._id}}}  "
        else:
            return ""


note_entries = [
    Entry(seconds(10)).spell(shield_wall),
    Entry(seconds(15)).note("this is a test"),
]


def generate_personal_note():
    for entry in note_entries:
        print(entry)


if __name__ == "__main__":
    generate_personal_note()
