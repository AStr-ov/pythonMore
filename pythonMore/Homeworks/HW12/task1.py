'''Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании
экземпляра. Другие предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
'''
import json
from statistics import mean

class Descriptor:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.name, value)

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'{self.name} должно состоять только из букв')
        if not value.isalpha():
            raise TypeError(f'{self.name} должно состоять только из букв')
        if not value.istitle():
            raise TypeError(f'{self.name} долно начинаться с заглавной буквы')


class Student:
    first_name = Descriptor()
    last_name = Descriptor()

    def __init__(self, first_name: str, last_name: str, discipline: list, grades: list, test_results: list):
        with open('discipline.json', 'r', encoding='utf-8') as f:
            if discipline in json.load(f):
                self.discipline = discipline
            else:
                raise ValueError(f'{discipline} нет в списке предметов ')
        self.first_name = first_name
        self.last_name = last_name
        self.grade = grades
        self.test_results = test_results
        min_grade = 2
        max_grade = 5
        min_test = 0
        max_test = 100
        for i in grades:
            if not isinstance(i, int):
                raise TypeError(f'Оценка не может быть {i} только целым числом')
            if not min_grade <= i <= max_grade:
                raise ValueError(f'Оценка не может быть {i}, только от {min_grade} до {max_grade}')
        for i in test_results:
            if not isinstance(i, int):
                raise TypeError(f'Результат теста не может быть {i}, только целым числом')
            if not min_test <= i <= max_test:
                raise ValueError(f'Результат теста не может быть {i}, только от {min_test} до {max_test}')

    def __str__(self):
        return f'{self.first_name} {self.last_name}\nпо предмету {self.discipline}-\nоценки: {self.grade},' \
               f' \nрезультаты тестов: {self.test_results},со средним балом - {round(mean(self.test_results),2)}'


if __name__ == '__main__':
    s1 = Student('Ivan', 'Petrov', 'Math', [2, 3, 5, 5], [100, 88, 94, 66])
    #s2 = Student('Egor', 'Ivanov', 'Python', [4, 5, 5], [89, 88, 94])
    #s3 = Student('egor', 'Egorov', 'History', [4, 5, 5], [89, 88, 94])
    #s4 = Student('Egor', 'egorov', 'History', [4, 5, 5], [89, 88, 94])
    #s5 = Student('Egor', 'Eegorov', 'History', [4, 6, 5], [89, 88, 94])
    #s6 = Student('Egor', 'Sidorov', 'History', [4, 5], [89, 88, -94])
    print(s1)
