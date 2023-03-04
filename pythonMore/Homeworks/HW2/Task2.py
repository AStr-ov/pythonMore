'''Напишите программу, которая принимает две строки вида “a/b”
- дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.'''
import fractions
import math

num1, num2 = input('Введите первую простую дробь вида "a/b": '), \
             input('Введите вторую простую дробь вида "a/b": ')

sep1 = num1.find("/")
sep2 = num2.find("/")

nom1 = int(num1[:sep1])      # числитель первой дроби
nom2 = int(num2[:sep2])      # числитель второй дроби
den1 = int(num1[sep1 + 1:])  # знаменатель первой дроби
den2 = int(num2[sep2 + 1:])  # знаменатель второй дроби

nom_sum = (nom1 * den2 + nom2 * den1)          # числитель суммы дробей
den_sum = (den1 * den2)                        # знаменатель суммы дробей
gcd_sum = math.gcd(nom_sum, den_sum)           # наибольший общий делитель суммы дробей
gcd_mult = math.gcd(nom1 * nom2, den1 * den2)  # наибольший общий делитель произведения дробей

# print(num1,' + ',num2, ' = ' + str(nom_sum // gcd_sum) + '/' + str(den_sum // gcd_sum))
# print(num1,'*',num2, ' = ' + str(nom1 * nom2 // gcd_mult) + '/' + str(den1 * den2 // gcd_mult))
summ = str(nom_sum // gcd_sum) + '/' + str(den_sum // gcd_sum)
mult = str(nom1 * nom2 // gcd_mult) + '/' + str(den1 * den2 // gcd_mult)
s = fractions.Fraction(nom1, den1) + fractions.Fraction(nom2, den2)
m = fractions.Fraction(nom1, den1) * fractions.Fraction(nom2, den2)

print(num1, ' + ', num2, ' = ' + summ)
print(fractions.Fraction(nom1, den1) + fractions.Fraction(nom2, den2))
print(num1, ' * ', num2, ' = ' + mult)
print(fractions.Fraction(nom1, den1) * fractions.Fraction(nom2, den2))
print("Ответ программы вычисления суммы: " + summ + " соответствует вычислению функции "
                                                    "fractions() :" + str(s) if (
            summ == str(s)) else "Ответ программы не соответствует вычислению функции fractions()")
print("Ответ программы вычисления произведения: " + mult + " соответствует вычислению функции "
                                                           "fractions() :" + str(m) if (
            summ == str(s)) else "Ответ программы не соответствует вычислению функции fractions()")
