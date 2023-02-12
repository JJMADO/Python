import random


class Warrior:
    name = str
    health = int
    attack = int

    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.attack = random.randint(5, 10)

    def is_alive(self):
        return (True if self.health > 0 else False)

    def attack_do(self):
        if random.randint(1, 3) == 1:
            return self.attack
        elif random.randint(1, 2) == 2:
            return self.attack + random.randint(1, 2)
        else:
            return 0


class Knight(Warrior):

    def __init__(self, name, health):
        super().__init__(name, health)
        self.attack += random.randint(0, 3)
        print("СОЛДАТ СОЗДАН")

    def attack_do(self):
        print("Атака не будет")
        return 0



def fight(f1, f2):
    f2.health -= f1.attack_do()
    print(f"Атака произошла, Здоровье {f2.name} = {f2.health}")

if __name__ == '__main__':

    w1 = Warrior("Ronald", 50)
    print(w1.is_alive())
    k2 = Knight("Medved", 50)
    print(k2.health)
    while w1.is_alive() and k2.is_alive():
        fight(w1, k2)
        if k2.is_alive():
            fight(k2, w1)
    print(f"Победил {k2.name}" if k2.is_alive() else f"Победил {w1.name}")
