'''Создайте класс Матрица. Добавьте методы для:
вывода на печать,
сравнения,
сложения,
*умножения матриц'''


class Matrix:
    '''Класс для сравнения, сложения матриц и вывода на печать.'''

    def __init__(self, matrix: []):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row))
                         for row in self.matrix)

    def size(self):
        '''Метод подсчета элементов матрицы.'''
        count_row = len(self.matrix)
        count_col = len(self.matrix[0])
        return count_row * count_col

    def val_matrix(self):
        '''Метод подсчета суммы значений элементов матрицы.'''
        val = 0
        for i in self.matrix:
            for j in i:
                val += j
        return val

    def __gt__(self, other):
        '''Метод сравнения суммы значений элементов двух матриц для матриц с одинаковым количеством элементов.'''
        if self.size() == other.size():
            return self.val_matrix() > other.val_matrix()
        else:
            return f'Некорректно сравнивать матрицы разных размеров'

    def __add__(self, other):
        '''Метод сложения двух матриц.'''
        res = self.matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                res[i][j] = self.matrix[i][j] + other.matrix[i][j]

        return res


if __name__ == '__main__':
    a = Matrix([[1, 1, 1, 1],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [2, 2, 2, 2],
                [1, 2, 3, 8]])
    b = Matrix([[1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2],
                [4, 4, 4, 4, 4]])
    c = Matrix([[1, 1, 1, 1],
                [2, 2, 2, 2],
                [1, 2, 1, 2],
                [1, 2, 1, 2],
                [3, 1, 2, 0]])

    print(c)
    print(a < b)
    print(c > a)
    print(c < a)
    print(f'матрица \n{a}\n+ матрица  \n{c}\n= \n{Matrix(a + c)}')
    print(help(Matrix))