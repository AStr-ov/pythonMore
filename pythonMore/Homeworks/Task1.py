'''2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы
двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''


a,b,c = int(input("Введите значение стороны а: ")),int(input("Введите значение стороны b: ")),\
        int(input("Введите значение стороны c: "))
if a + b > c and a + c > b and b + c > a:
    print("Треугольник со сторонами ", a,',', b,',', c, " существует.")
    if a == b and a == c:
        print("Это равносторонний треугольник.")
    elif a == b and a != c:
        print("Это равнобедренный треугольник.")
    else:
        print("Это разносторонний треугольник.")
else:
    print("Треугольник со сторонами ", a,',', b,',', c, " не существует.")

