'''
Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.
'''
import json


def convert(old_file: str, new_file: str) -> None:
    d = {}
    with open(old_file, 'r', encoding='utf-8') as f:
        for line in f:
            s = line.split(',')
            d[s[0].capitalize()] = float(s[1])
        with open(new_file, 'w', encoding='utf-8') as f:
            json.dump(d, f, indent=2)  # indent=2 - перенос на новую строку


'''Напишите функцию, которая в бесконечном цикле запрашивает:
имя, личный идентификатор и уровень доступа (от 1 до 7).
После каждого ввода добавляйте новую информацию в JSON файл.
Пользователи группируются по уровню доступа.
Идентификатор пользователя выступает ключём для имени.
Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
При перезапуске функции уже записанные в файл данные должны сохраняться.'''


def user_data() -> None:
    while True:
        name, id, level = input('Your name: '), input('Your ID: '), int(input('Your access level: '))
        dic = {}
        with open('data_users', 'w', encoding='utf-8') as f:
            dic[id] = name
            f.writelines(dic, level)


user_data()


def ident(name_file: str):
    dic = {}
    second = {}
    with open(name_file, 'a', encoding='utf-8') as op:
        json.dump(dic, op)
    with open(name_file, 'r', encoding='utf-8') as f:  # чтение файла
        data = json.load(f)  # запись данных в файл

    dic = data  # сохранение
    print(type(dic))
    print(dic)
    while True:
        name = input("введите имя ")
        if name == '':  # выход из цикла
            break

        id = int(input("введите личный идентификатор "))
        lev = int(input('введите уровень доступа (от 1 до 7) '))
        second = {id: name}  # словарь в словаре с идент lev

        if dic.get(lev) is None:  # проверка на уникальность ключа
            dic[lev] = second
        else:
            k = dic.get(lev)
            k.update(second)

    with open(name_file, 'a', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    convert('res_f', 'j_res')
    user_data()
    ident('ident.json')
