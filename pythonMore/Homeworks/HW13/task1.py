'''Возьмите 1-3 задачи из тех, что были на прошлых
семинарах или в домашних заданиях. Напишите к ним
классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.
'''


class NotNegative(Exception):
    def __str__(self):
        return (f'Сторона прямоугольника не может иметь отрицательное значение')


class Rectangle():
    def __init__(self, len_rec, wid_rec=None):
        self.len_rec = len_rec
        if self.len_rec == 0:
            raise NotNegative
        if wid_rec is None:
            self.wid_rec = len_rec
        else:
            self.wid_rec = wid_rec
        if self.wid_rec == 0:
            raise NotNegative

    def perimetr(self):
        return 2 * (self.len_rec + self.wid_rec)

    def area(self):
        return self.len_rec * self.wid_rec


if __name__ == '__main__':
    z = Rectangle(3, 4)
    print(f"P={z.perimetr()}, S={z.area()}")
    # z1 = Rectangle(0, 4)
    z2 = Rectangle(3, 0)
    #print(f"P={z1.perimetr()}, S={z.area()}")
    print(f"P={z2.perimetr()}, S={z.area()}")
