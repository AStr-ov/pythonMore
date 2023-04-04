'''Напишите функцию, которая заполняет файл (добавляет в конец)
случайными парами чисел.
Первое число int, второе - float разделены вертикальной чертой.
Минимальное число - -1000, максимальное - +1000.
Количество строк и имя файла передаются как аргументы функции.'''

import random


def ff(count: int, file_name: str):
    with open(file_name, 'a') as f:
        for i in range(count):
            f.write(f'{str(random.randint(-1000, 1001))}|{str(random.uniform(-1000, 1001))}\n')


ff(4, 'file1')

'''Напишите функцию, которая генерирует псевдоимена.
Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, 
среди которых обязательно должны быть гласные.
Полученные имена сохраните в файл.'''


# #   A-Z  65-96;  a -z  97 -122
def pseudo_name():
    vowel = [97, 101, 105, 111, 117, 121]
    s = ''
    for i in range(random.randint(4, 7)):
        if i % 2:
            s += chr(random.choice(vowel))
        else:
            s += chr(random.randint(97, 122))

    with open('f2.txt', 'a', encoding='utf-8') as f:
        f.write(str.capitalize(s) + '\n')


pseudo_name()

'''Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало.'''


def res_file(text: str, digit: str, res: str):
    with open(text, 'r', encoding='utf-8') as f1, open(digit, 'r', encoding='utf-8') as f2, \
            open(res, 'a', encoding='utf-8') as f3:
        len_name = sum(1 for _ in f1)
        len_digit = sum(1 for _ in f2)
        for _ in range(max(len_digit, len_name)):
            name = f1.readline()
            if name == '':
                f1.seek(0)
                name = f1.readline()
            name = name[:-1]
            num = f2.readline()
            if num == '':
                f2.seek(0)
                num = f2.readline()
            num1, num2 = num.split('|')
            num = num[:-1]
            res_mult = int(num1) * float(num2)
            if res_mult < 0:
                f3.write(f'{name.lower()}, {abs(res_mult)}\n')
            else:
                f3.write(f'{name.upper()}, {round(res_mult)}\n')


res_file('f2.txt', 'file1', 'res_f')
