class Person:
    name: str
    age: int
    gender: list

    def __init__(self, name, _gender="деб"):
        self.name = name
        self._gender = _gender
        self.__age = 0
        print("Лунтик")

    def talk(self):
        print("э, как рулить")

    def __del__(self):
        print("обамка")

    def sing(self):
        print("🎵🎵🎵🎵")


class Dancer(Person):
    fly: bool
    dance: bool

    def __init__(self, name, fly, _gender="круассан"):
        self.dance = True
        self.fly = fly
        super().__init__(name, _gender)


person1 = Person("Антон")
print(person1._gender, person1.age, person1.name)
person2 = Person("Тимоша")
print(person2.name, person2._gender)
person1.talk()
person2.sing()
person3 = Dancer("Календарь", True)
print(person3.fly)
person3.talk()
