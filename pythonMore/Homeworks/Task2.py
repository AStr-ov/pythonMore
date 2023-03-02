'''Напишите код, который запрашивает число и сообщает является ли оно простым
или составным. Используйте правило для проверки:
“Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.'''
MIN_NUM = 1
MAX_NUM = 100000
PRIEM_EXCEPTION = 2
flag = True
print("Введите число от", MIN_NUM, " до", MAX_NUM, ": ")
n = int(input())
while n < MIN_NUM or n > MAX_NUM:
    print("Введите число от", MIN_NUM, " до", MAX_NUM, ": ")
    n = float(input())
    if n < MIN_NUM or n > MAX_NUM:
        print("Ваше число не входит в диапазон от", MIN_NUM, " до", MAX_NUM)

else:
    if n % 2 == 0 and n > PRIEM_EXCEPTION:
        flag = False
    for i in range(3, int(n**0.5+1), 2):
        if n % i == 0:
            flag = False
            break
    print(int(n), "- Простое число" if flag == True else " - Составное число")
