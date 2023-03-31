'''Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.'''

count = 0


def riddle(text: str, answer: list, time: int) -> int:
    print(text, "Что это? ")
    global count
    for i in range(1, time + 1):
        ans = input(f'{i}-я попытка. Ваш ответ: ')
        if ans in answer:
            count += 1
            print(f'Угадано с {i} попытки')
            return count
    print(f'Эту загадку не угадал, попытки закончились')


def data_riddle(d: dict):
    try_count = int(input(f"Угадай загадки.\nСколько попыток тебе надо на каждую? "))
    for quest, answer in d.items():
        riddle(quest, answer, try_count)
    return (f'Из {len(d.keys())} загадок угадано  {count}')


d = {'Зимой и летом одним цветом. ': ['елка', "ель", "ёлка", "Елка", "Ель", "Ёлка"]
    , "Висит груша - нельзя скушать. ": ['лампа', "лампочка", 'Лампа', "Лампочка"]
    , "Весной в землю зарывали, а по осени копали. ": ['картофель', "картошка", 'Картофель', "Картошка"]
    , "Хоть и день, и ночь идём, yикуда мы не уйдём. ": ['часы', "часики", 'Часы', "Часики"]
    , "Зубы остры, да не волк, я дрова готовлю впрок. ": ['пила', "ножевка", 'Пила', "Ножевка"]
    , "Он протопал по дорожке, Мы теперь намочим ножки. ": ["дождь", "дождик", "Дождь", "Дождик"]}

print(data_riddle(d))
