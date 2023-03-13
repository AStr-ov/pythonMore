'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.'''


def dic(**kwargs) -> dict:
    changeable = [list, bytearray, frozenset, dict]
    my_d = {}
    for key, value in kwargs.items():
        if type(value) in changeable:
            my_d[str(value)] = key
        else:
            my_d[value] = key
    return my_d


print(dic(dict={'one': 42, 'two': 3.14, 'ten': 'Hello world!'}, fr=frozenset((1, 2, 5)),
          a=((1, 2, 3, "Hello")), two=22, c=True, list=[1, 2, 3],ten=0.01))
