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

    def ident(class_name, name, type_water=None, flying=None):
        if class_name == 'Fish':
            inst = Fish(name, type_water)
        if class_name == 'Birds':
            inst = Birds(name, flying)
        return inst


if __name__ == '__main__':
    catfish = Factory.ident('Fish', 'Catfish', "River", None)
    macrel = Factory.ident('Fish', 'Macrel', "Sea", None)
    eagle = Factory.ident('Birds', 'Eagle', None, 'Fly')
    heck = Factory.ident('Fish', 'Heck', "Sea", None)
    chicken = Factory.ident('Birds', 'Chicken', None, 'Not fly')

    print(f'{type(eagle)= }, {eagle.info_bird()}, {eagle.characteristic_bird}, {eagle.characteristic}')
    print(f'{type(heck)= }, {heck.info_fish()}, {heck.characteristic_fish}, {eagle.characteristic}')
    print(f'{type(chicken)= }, {chicken.info_bird()}, {chicken.characteristic_bird}, {eagle.characteristic}')
    print(f'{type(catfish)= }, {catfish.info_fish()}, {catfish.characteristic_fish}, {eagle.characteristic}')
