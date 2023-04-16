'''Доработаем задачи 5. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов)
и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''


class Animal:
    def __init__(self, name):
        self.name = name

    characteristic = 'Живое существо'


class Fish(Animal):
    def __init__(self, name, type_water):
        super(Fish, self).__init__(name)
        self.type_water = type_water

    def info_fish(self):
        return f'{self.name}, {self.type_water}'

    characteristic_fish = 'Дышит жабрами'


class Birds(Animal):
    def __init__(self, name, flying):
        super(Birds, self).__init__(name)
        self.flying = flying

    def info_bird(self):
        return f'{self.name}, {self.flying}'

    characteristic_bird = 'Пернатое'


class Factory:
    def __init__(self, class_name, name, type_water=None, flying=None):
        self.class_name = class_name
        self.name = name
        self.type_water = type_water
        self.flying = flying

    def ident(self):
        if self.class_name == 'Fish':
            inst = Fish(self.name, self.type_water)
        if self.class_name == 'Birds':
            inst = Birds(self.name, self.flying)
        return inst


if __name__ == '__main__':
    t = Factory('Fish', 'Macrel', "Sea")
    macrel = t.ident()
    t = Factory('Birds', 'Chicken', None, 'Not fly')
    chicken = t.ident()
    print(f'{type(macrel)= }, {macrel.info_fish()}, {macrel.characteristic_fish}, {macrel.characteristic}')
    print(f'{type(chicken)= }, {chicken.info_bird()}, {chicken.characteristic_bird}, {chicken.characteristic}')
