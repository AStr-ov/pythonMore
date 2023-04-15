'''Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''


class Animal:
    def __init__(self, name):
        self.name = name

    characteristic = 'Живое существо'


class Fish(Animal):
    def __init__(self, name, salt_or_fresh):
        super(Fish, self).__init__(name)
        self.salt_or_fresh = salt_or_fresh

    characteristic_fish = 'Дышит жабрами'


class Birds(Animal):
    def __init__(self, name, flying):
        super(Birds, self).__init__(name)
        self.flying = flying

    characteristic_bird = 'Пернатое'


class Factory(Fish):
    def __init__(self, name, salt_or_fresh, size):
        super(Factory, self).__init__(name, salt_or_fresh)
        self.size = size

    dor = Fish('Дорадо', "морская")

    def info(self):
        return f'{self.name}, {self.salt_or_fresh}, {self.size}'


som = Factory('Сом', "пресноводная", 'крупная')

print(som.info())
print(f'{Factory.dor.name}, {Factory.dor.salt_or_fresh}, {Factory.dor.characteristic}, {Factory.dor.characteristic_fish}')
