'''Урок 9. Декораторы
Напишите следующие функции:
Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.'''
import csv
import json
import random
from typing import Callable


def dec(func: Callable):
    def wrapper():
        with open('nums.csv', 'r', newline='', encoding='utf-8') as f:
            line = csv.reader(f)
            res = []
            for i in line:
                a, b, c = int(i[0]), int(i[1]), int(i[2])
                res.append(f'if {a= },{b= },{c= }:  {func(a, b, c)}')
            return res

    return wrapper


def dec2(func: Callable):
    def wrapper():
        result = func()
        with open('file.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2)

    return wrapper


@dec2
@dec
def equation(a: int, b: int, c: int):
    d = (b ** 2 - (4 * a * c))
    if d < 0:
        return None
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return f'{x1= }, {x2= }'


def csv_file():
    with open('nums.csv', "w", newline='', encoding='utf-8') as f_csv:
        w = csv.writer(f_csv, quoting=csv.QUOTE_ALL)
        count_rows = random.randint(100, 1000)  # количество генерируемых строк файла
        for _ in range(count_rows):
            nums = []
            for i in range(3):
                num = random.randint(-10, 10)
                if num == 0:
                    num = random.randint(1, 10)
                nums.append(num)
            w.writerow(nums)


if __name__ == '__main__':
    csv_file()
    equation()
