'''Напишите программу, которая получает целое число и возвращает его
шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''
number = int(input("Введите число: "))
NUMBER = number
SYS = 16
result = ''
while number > 0:
    rem = number % SYS
    if rem == 10:
        letter = 'a'
    elif rem == 11:
        letter = 'b'
    elif rem == 12:
        letter = 'c'
    elif rem == 13:
        letter = 'd'
    elif rem == 14:
        letter = 'e'
    elif rem == 15:
        letter = 'f'
    else:
        letter = str(rem)
    result = str(letter) + result
    number = number // SYS
print('Шестнадцатеричное строковое представление числа',NUMBER,': 0x' + result)
print("Bычислениe функции hex(",NUMBER,")                       :",hex(NUMBER))
print("Ответ программы соответствует вычислению функции hex()" if ('0x' + result) == hex(NUMBER) else
      "Ответ программы не соответствует вычислению функции hex()")
