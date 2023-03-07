'''Пользователь вводит строку текста.
✔ Подсчитайте сколько раз встречается
каждая буква в строке без использования
метода count и с ним.
✔ Результат сохраните в словаре, где ключ —
символ, а значение — частота встречи
символа в строке.'''

text = input('Введите с троку текста:')
chars = text.replace(' ', '').replace('-', '').replace(',', '') \
    .replace('.', '').replace('!', '').replace('?', '')
# c count
dict1 = {}
for i in chars:
    dict1.setdefault(i, chars.count(i))
print(dict1)
# без count
dict2 = {}
dict3 = {}
for i in chars:
    t = dict2.setdefault(i, list())
    t.append(i)
print(dict2)
for i, j in dict2.items():
    dict3.setdefault(i, len(j))
print(dict3)
