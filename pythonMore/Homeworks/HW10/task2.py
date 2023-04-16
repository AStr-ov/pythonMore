'''Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных),
которые вы уже решали. Превратите функции в методы класса, а параметры в свойства.
Задачи должны решаться через вызов методов экземпляра.'''


class Equation:
    def __init__(self, a: int, b: int, c: int):
        self.a = a
        self.b = b
        self.c = c

    def solution(self):
        d = (self.b ** 2 - (4 * self.a * self.c))
        if d < 0:
            return None
        else:
            x1 = (-self.b + d ** 0.5) / (2 * self.a)
            x2 = (-self.b - d ** 0.5) / (2 * self.a)
            return f'{x1= }, {x2= }'


if __name__ == '__main__':
    ans = Equation(1, 2, -3)
    print(ans.solution())
