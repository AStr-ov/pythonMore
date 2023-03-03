'''Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''
import math

number = int(input("Введите число: "))
NUMBER = number
SYS = 16
a, b = divmod(number, SYS)
result = ''
while number % SYS:
    if b == 10:
        t = 'a'
    elif b == 11:
        t = 'b'
    elif b == 12:
        t = 'c'
    elif b == 13:
        t = 'd'
    elif b == 14:
        t = 'e'
    elif b == 15:
        t = 'f'
    else:
        t = str(b)
    result = t + result
    number = a
    a, b = divmod(number, SYS)

print('Шестнадцатеричное строковое представление числа',NUMBER,': 0x' + result)
print("Bычислениe функции hex(",NUMBER,")                       :",hex(NUMBER))
print("Ответ программы соответствует вычислению функции hex()" if ('0x' + result) == hex(NUMBER) else
      "Ответ программы не соответствует вычислению функции hex()")
