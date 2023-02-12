class Potato:

    number: int
    age: int

class gardenbed:


    def __init__(self, number):
        self.number = number
        self.age = 0

    def grow(self):
        self.age += 1
        
    def info(self):
        print(f"Картошка порядковый номер {self.number}. "
              f"Мой возраст уже {self.age}")


makar = Potato(1)
makar2 = Potato(2)