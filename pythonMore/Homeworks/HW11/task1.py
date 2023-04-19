'''Добавьте ко всем задачам с семинара строки документации
и методы вывода информации на печать.'''
'''Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)'''

import time


class MyString(str):
    '''класc, где в str дополнительно хранятся имя автора строки и время создания'''

    def __new__(cls, text, author):
        '''Метод добавляет к строке автора и время создания'''
        instance = super().__new__(cls, text)
        instance.author = author
        instance.time = time.time()
        return instance

    def __str__(self):
        return f'Текст:  \nАвтор: {self.author}\nВремя создания: {time.time()}'


if __name__ == '__main__':
    a = MyString('Однажды в студеную зимнюю пору', 'Nekrasov')
    print(a)

'''Создайте класс Архив, который хранит пару свойств. Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются
в пару списков-архивов list-архивы также являются свойствами экземпляра'''


class Arc:
    '''Класс,записывает архив значений своих экземпляров '''
    _instance = None

    def __init__(self, num, val):
        self.num = num
        self.val = val

    def __new__(cls, *args, **kwargs):
        '''Архив дописывает значения предыдущего экзнипляра класса'''
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.nums = []
            cls._instance.vals = []
        else:
            cls._instance.nums.append(cls._instance.num)
            cls._instance.vals.append(cls._instance.val)
        return cls._instance

    def __str__(self):
        return f'В архиве следующие значения: {self._instance.nums} {self._instance.vals}'

    def __repr__(self):
        return f'Arc({self._instance.num}, "{self._instance.val}")'


if __name__ == '__main__':
    a = Arc(12, '12345')
    print(a)
    a = Arc(33, 'qaz')
    print(a)
    a = Arc(555, '11qaz333')
    print(a)
    a = Arc(12, "12345")
    print(repr(a))
    a = Arc(12, "12345")
    print(a)
    a = Arc(000, "oOo")
    print(a)

'''Дорабатываем класс прямоугольник из прошлого семинара.
Добавьте возможность сложения и вычитания.
При этом должен создаваться новый экземпляр прямоугольника.
Складываем и вычитаем периметры, а не длинну и ширину.
При вычитании не допускайте отрицательных значений.'''


class Rectangle():
    '''Класс считает периметр и площадь прямоугольников, принимая их стороны.'''

    def __init__(self, len_rec, wid_rec=None):
        self.len_rec = len_rec
        if wid_rec is None:
            self.wid_rec = len_rec
        else:
            self.wid_rec = wid_rec

    def perimetr(self):
        '''Метод подсчета периметра прямоугольника.'''
        return 2 * (self.len_rec + self.wid_rec)

    def area(self):
        '''Метод подсчета площади прямоугольника.'''
        return self.len_rec * self.wid_rec

    def __add__(self, other):
        '''Метод определяет сложение сторон прямоугольников и
        возвращает новый экземпляр со сторонами, полученными в результате этого сложения.'''
        a = self.len_rec + other.len_rec
        b = self.wid_rec + other.wid_rec
        return Rectangle(a, b)

    def __sub__(self, other):
        '''Метод определяет вычитание сторон прямоугольников и
        возвращает новый экземпляр со сторонами, полученными в результате этого вычмтания.'''
        a = abs(self.len_rec - other.len_rec)
        b = abs(self.wid_rec - other.wid_rec)
        return Rectangle(a, b)

    def __repr__(self):
        return f'Rectangle({self.len_rec}, {self.wid_rec})'

    def __str__(self):
        return f'Прямоугольник со сторонами {self.len_rec} и {self.wid_rec} имеет периметр равный {self.perimetr()} и площадь {self.area()}'


if __name__ == '__main__':
    r1 = Rectangle(3, 4)
    r2 = Rectangle(4, 5)
    r3 = r1 + r2
    r4 = r1 - r3
    print(repr(r3))
    print(r4)
