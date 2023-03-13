'''Напишите функцию для транспонирования матрицы'''


def trans_matrix(a: list) -> list:
    res = []
    rows = zip(*a)
    for i in rows:
        res.append(list(i))
    return res


matrix = [[1, 2, 3, 4, 5, ], [6, 7, 8, 9, 10]]
print(trans_matrix(matrix))
