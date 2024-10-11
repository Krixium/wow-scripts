from common import Player, PlayerClass, Role, players_to_str

me = Player("Zaur", PlayerClass.Warrior, Role.Tank)

# genenral
rally = 97462

# prot
last_stand = 12975
shield_wall = 871
spell_block = 392966
spell_reflect = 23920


def seconds(n):
    return n


def minutes(n):
    return seconds(60) * n


class Entry:
    def __init__(self, time) -> None:
        self._time = time
        self._ids = []
        self._notes = []

    def spell(self, id):
        self._ids.append(int(id))
        return self

    def note(self, note):
        self._notes.append(note)
        return self

    def __str__(self) -> str:
        result = f"{{time:{self._time}}} "
        for id in self._ids:
            result = f"{result}{me} {{spell:{id}}}  "
        for note in self._notes:
            result = f"{result}{me} {{text}}{note}{{/text}}  "
        return result


note_entries = [
    Entry(seconds(10)).spell(rally).spell(shield_wall).spell(last_stand).spell(spell_block).spell(spell_reflect).note("this is a test"),
]


def generate_personal_note():
    for entry in note_entries:
        print(entry)


if __name__ == "__main__":
    generate_personal_note()
