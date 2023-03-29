'''Напишите однострочный генератор словаря, который принимает на вход три списка
одинаковой длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии'''


name = ['Иванов', 'Петрова', 'Сидоров', 'Егорова', 'Васильев', 'Сергеева', 'Александров', 'Владимиров']
sal = [10000, 10000, 15000, 12000, 20000, 55000, 25000, 32000]
bonus = ['10.25%', '15%', '10%', '9.5%', '9%', '5.5%', '8.5%', '7.2%']

d = {n: s * float(b.replace('%', '')) / 100 for n, s, b in zip(name, sal, bonus)}

print(d)
