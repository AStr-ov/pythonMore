'''В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку.'''

text = 'This is a Wiki page. Users with edit rights can edit it. You are, therefore, ' \
       'free to (in fact, encouraged to) add details of material that other Python users ' \
       'will find useful. It is not an advertising page and is here to serve the whole Python ' \
       'community. Users who continually edit pages to give their own materials (particularly ' \
       'commercial materials) prominence, or spam the listing with multiple entries which ' \
       'point to resources with only slightly altered material, may subsequently find their ' \
       'editing rights disabled. You have been warned. On a cheerier note - there is a ' \
       'constant stream of new and updated information on Python as the language is exploding ' \
       'in popularity. Only enthusiastic volunteers can keep this page current, so if something ' \
       'helps you, feel free to link it here.'

words = text.lower().replace('(','').replace(')','').replace('-','').split()
word_count = {}
for i in words:
    if words.count(i) > 1:
        word_count.setdefault(i, words.count(i))
print('В тексте -', len(words), 'слов')
print(f'Количество повторений слов в тексте- {word_count}')
print(f'10 наиболее часто встречающихся в тексте слов: {sorted(word_count, key=word_count.get, reverse=True)[:10]}')
