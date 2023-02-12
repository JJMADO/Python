class Warrior:
    health: int
    attack: int

    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def who_is(self):
        return "Warrior"


class Knight(Warrior):

    def __init__(self):
        super(Knight, self).__init__()
        self.attack = 7

    def who_is(self):
        return "Knight"


class Army:

    def __init__(self):
        self.unit = []

    def add_units(self, army, count):
        for i in range(count):
            self.unit.append(army)


class Battle:

    def fight(self, p1, p2):
        if p1.attack == 0 or p2.attack == 0:
            return "Битвы не будет(("
        while True:
            if p1.is_alive():
                if p1.who_is() == "Vampire":
                    pass
                p2.health -= p1.attack
            else:
                return False
            if p2.is_alive():
                if p1.who_is() == "Defender":
                    p1.defense -= p2.attack
                    if p1.defense < 0:
                        p1.health += p1.defense
                        p1.defense = 0
                else:
                    p1.health -= p2.attack
            else:
                return True

    def battle(self, army1, army2):
        while len(army1) != 0 and len(army2) != 0:
            if self.fight(army1[0], army2[0]):
                army2.pop(0)
            else:
                army1.pop(0)
        if len(army1) != 0:
            return False
        else:
            return True


class Defender(Warrior):

    def __init__(self):
        super(Defender, self).__init__()
        self.attack = 3
        self.defense = 2
        self.health += 10

    def who_is(self):
        return "Defender"


class Vampire(Warrior):

    def __init__(self):
        super(Vampire, self).__init__()
        self.health -= 10
        self.attack = 4
        self.vampirism = 50

    def who_is(self):
        return "Vampire"


d1 = Defender
v1 = Vampire
army_w = Army()
army_w.add_units(Defender, 4)
army_w.add_units(Warrior, 10)
# print(army_w.unit)
army_k = Army()
army_k.add_units(Vampire, 4)
army_k.add_units(Knight, 10)

b = Battle()

# print(b.battle(army_w.unit, army_k.unit))
