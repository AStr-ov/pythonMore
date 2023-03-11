'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве
значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.'''

backpack = dict(Палатка=4, Обувь=2, Одежда=3, Спальник=2, Посуда=2, Инструменты=3,
                Консервы=2, Крупа=1, Макароны=1, Напитки=3, Сладости=2)
max_mass = int(input("Введите максимальную грузоподъемность рукзака: "))
mass_all_things = sum(backpack.values())
print(f"Все вещи -{backpack}\nимеют массу {mass_all_things}  кг")
difference = mass_all_things - max_mass
sum_mass = 0
not_included=[]
print('Лишних - ', difference, "кг")

print('Не влезут: ')
if max_mass >= mass_all_things:
    print(f'Грузоподъемность рюкзака {max_mass}кг, массa всех вещей {mass_all_things}кг.В рюкзак влезут все вещи')
else:
    while sum_mass != difference:
        for k, v in backpack.items():
            if sum_mass + v > difference:
                continue
            else:
                sum_mass += v
                not_included.append(k)
                print(k, v, 'кг')
print(f'В рюкзак грузоподъемностью {max_mass} кг влезут : ')
for i in backpack:
    if i not in not_included:
        print(i, end=', ')
