'''Создайте модуль и напишите в нём функцию, которая получает на вход дату
в формате DD.MM.YYYY Функция возвращает истину, если дата может существовать
или ложь, если такая дата невозможна.
Для простоты договоримся, что год может быть в диапазоне [1, 9999].
Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
Проверку года на високосность вынести в отдельную защищённую функцию.'''

__all__ = ['leap_year', 'true_date']


def leap_year(y: int) -> bool:
    if not y % 4 and y % 100 or not y % 400:
        return True
    else:
        return False


def true_date(date: str) -> bool:
    day, month, year = date.split('.')
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
    if 0 < int(year) <= 9999:
        if 0 < int(month) < 13:
            if int(month) in month_31 and 0 < int(day) <= 31 \
                    or int(month) in month_30 and 0 < int(day) <= 30 \
                    or int(month) == 2 and 0 < int(day) <= 28 \
                    or leap_year(int(year)) and int(month) == 2 and 0 < int(day) <= 29:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    print(f'29.02.2000 - {true_date("29.02.2000")}')
    print(f'29.02.1900 - {true_date("29.02.1900")}')
    print(f'29.02.2001 - {true_date("29.02.2001")}')
    print(f'29.02.2016 - {true_date("29.02.2016")}')
    print(f'31.04.2016 - {true_date("31.04.2016")}')
    print(f'31.14.2016 - {true_date("31.14.2016")}')
    print(f'01.13.2022 - {true_date("01.13.2022")}')
    print(f'-01.11.2200 - {true_date("-01.11.2200")}')
    print(f'01.-11.2000 - {true_date("01.-11.2000")}')
    print(f'01.01.1 - {true_date("01.01.1")}')
    print(f'31.12.9999 - {true_date("31.12.9999")}')
    print(f'32.12.2022 - {true_date("32.12.2022")}')
