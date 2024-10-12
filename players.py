from common import Player, PlayerClass, Role


Froll = Player("Frollexy", PlayerClass.DeathKnight, Role.Tank)
Zaur = Player("Zaur", PlayerClass.Warrior, Role.Tank)
Zaurdk = Player("Zaurdk", PlayerClass.DeathKnight, Role.Tank)

Andrew = Player("Fotem", PlayerClass.Shaman, Role.Healer)
Jenn = Player("Kyttn", PlayerClass.Druid, Role.Healer)
Mew = Player("Mewmonkas", PlayerClass.Monk, Role.MeleeHealer)
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

MeleeHealers = [Mew]
RangeHealers = [Andrew, Jenn, Mord, Patch]
Healers = MeleeHealers + RangeHealers

MeleeDPS = [Bug, Horn, Inenta, Kyreoss, Zargrul, Zerg, Zwarg]

RangeDPS = [Jordan, Doug, Jump, David, Musty, Nik, Soss, Fran, Zac]

DPS = MeleeDPS + RangeDPS
Melee = MeleeDPS + MeleeHealers
Range = RangeDPS + RangeHealers
