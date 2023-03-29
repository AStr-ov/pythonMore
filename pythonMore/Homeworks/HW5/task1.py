''' Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'''

import re


def file_way(s: str) -> tuple():
    *way, name, type_ = re.split('[\\\.]', s)
    way = '\\'.join(way)
    return (way, name, type_)


print(file_way(r'C:\Users\StrAV\Documents\высшая и первая категории Uchitel_perechen.pdf'))
