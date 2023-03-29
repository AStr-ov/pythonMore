'''Создайте функцию генератор чисел Фибоначчи'''


def fibonachi(n):
    a = 1
    b = a
    for i in range(n):
        c = a + b
        yield a
        a = b
        b = c


print(*fibonachi(int(input('Введите желаемое количество чисел Фибоначчи: '))))
