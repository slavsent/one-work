def find_weekend(number):
    """
    По номеру числа дня недели проверят выходной или нет не учитывая праздники
    :param number: число
    :return: Выходной или нет
    """
    try:
        num_int = int(number)
    except ValueError:
        return 'Вы ввели не число'
    else:
        if num_int == 6 or num_int == 7:
            return 'Да'
        else:
            return 'Нет'


def coordinate_find(x=0, y=0):
    """
    Программа, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
    плоскости, в которой находится эта точка (или на какой оси она находится).
    :param number: x, y
    :return: четверть
    """
    try:
        x = int(x)
        y = int(y)
    except ValueError:
        return 'Вы ввели не числа'
    else:
        if x == 0 and y == 0:
            return 'Центр координат'
        elif x > 0 and y > 0:
            return '1-ая четверть'
        elif x == 0:
            return 'На оси Y'
        elif y == 0:
            return 'На оси Х'
        elif x < 0 and y > 0:
            return '2-ая четверть'
        elif x < 0 and y < 0:
            return '3-я четверть'
        elif x > 0 and y < 0:
            return '4-ая четверть'


def coordinate_diapason_find(number):
    """
    нахождение диапазона х и y по четверти координат
    :param number: число
    :return: диапазон
    """
    try:
        num_int = int(number)
    except ValueError:
        return 'Вы ввели не число или дробь введена не через .'
    else:
        if 0 < num_int < 5:
            if num_int == 1:
                return 'x > 0, y > 0'
            elif num_int == 2:
                return 'x < 0, y > 0'
            elif num_int == 3:
                return 'x < 0, y < 0'
            elif num_int == 4:
                return 'x > 0, y < 0'
        else:
            return 'Нет такой четверти'


def find_length(x1=0, y1=0, x2=0, y2=0):
    """
    Программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
    :param number: x1, y1, x2, y2
    :return: длина между точками
    """
    try:
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

    except ValueError:
        return 'Вы ввели не числа'
    else:
        return round(((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2)) ** 0.5, 2)


def logical_statement():
    """
    Программа для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат
    :return:
    """
    print("¬(x⋁y⋁z) = ¬x⋀¬y⋀¬z Это тоже, что not (x or y or z) = not x and not y and not z")
    res = []
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res.append([i, j, k])
    res_true = 0
    for el in res:
        if (not (el[0] or el[1] or el[2])) == (not el[0] and not el[1] and not el[2]):
            res_true += 1
    if res_true == 8:
        return True
    else:
        return False


if __name__ == '__main__':
    num = input('Введите число: ')
    print(find_weekend(num))

    num = input('Введите число х и y через пробел: ')
    if len(num.split()) == 2:
        print(coordinate_find(num.split()[0], num.split()[1]))
    else:
        print('Неправильный ввод')

    num = input('Введите число х1 y1 x2 y2 через пробел: ')
    if len(num.split()) == 4:
        print(find_length(num.split()[0], num.split()[1], num.split()[2], num.split()[3]))
    else:
        print('Неправильный ввод')

    print(logical_statement())
