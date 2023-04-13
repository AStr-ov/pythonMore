'''Дорабатываем задачу 1.
Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.'''
import random

def check(funk):
    def wrapper(a: int, count: int):

        if not 0 < a < 101:
            a = random.randint(1, 101)
        if not 0 < count < 11:
            count = random.randint(1, 11)
        result = funk(a, count)
        return result

    return wrapper


@check
def deco(a: int, count: int) -> Callable[[], None]:
    def ugadai() -> None:

        for i in range(count):
            num = int(input('Введите число 1 - 100: '))
            if num > a:
                print('Ваше число больше')
            elif num < a:
                print('Ваше число меньше')
            else:
                print('Вы угадали')
                break

    return ugadai


if __name__ == '__main__':
    game = deco(204, 22)
    game()
