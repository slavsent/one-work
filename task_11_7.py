class MyErr(Exception):
    pass


class ComplexNum:
    def __init__(self, *j_num):
        self.j_num = list(j_num)

    def __str__(self):
        if ComplexNum.verify(self.j_num) == 'Ошибка ввода данных':
            return 'Данные введены не верно все аргументы должны быть числа'
        else:
            if len(self.j_num) == 1:
                return f'Комплексное число - {self.j_num[0]}j'
            else:
                x = sum(self.j_num[:(len(self.j_num) - 1)])
                return f'Комплексное число - ({x} + {self.j_num[-1]}j)'

    @staticmethod
    def verify(j_num):
        try:
            for el in j_num:
                if (not isinstance(el, int)) and (not isinstance(el, float)):
                    raise MyErr('Ошибка ввода данных')
        except MyErr as err:
            print(err)
            return "Ошибка ввода данных"

    def __add__(self, other):
        if ComplexNum.verify(self.j_num) == 'Ошибка ввода данных':
            return 'Данные введены не верно все аргументы должны быть числа'
        elif ComplexNum.verify(other.j_num) == 'Ошибка ввода данных':
            return 'Данные введены не верно все аргументы должны быть числа'
        else:
            if len(self.j_num) == 1:
                arg_2 = self.j_num[0]
                arg_1 = 0
            else:
                arg_1 = sum(self.j_num[:(len(self.j_num) - 1)])
                arg_2 = self.j_num[-1]
            if len(other.j_num) == 1:
                arg_4 = other.j_num[0]
                arg_3 = 0
            else:
                arg_3 = sum(other.j_num[:(len(other.j_num) - 1)])
                arg_4 = other.j_num[-1]
            return ComplexNum(arg_1 + arg_3, arg_2 + arg_4)

    def __mul__(self, other):
        if ComplexNum.verify(self.j_num) == 'Ошибка ввода данных':
            return 'Данные введены не верно все аргументы должны быть числа'
        elif ComplexNum.verify(other.j_num) == 'Ошибка ввода данных':
            return 'Данные введены не верно все аргументы должны быть числа'
        else:
            if len(self.j_num) == 1:
                arg_2 = self.j_num[0]
                arg_1 = 0
            else:
                arg_1 = sum(self.j_num[:(len(self.j_num) - 1)])
                arg_2 = self.j_num[-1]
            if len(other.j_num) == 1:
                arg_4 = other.j_num[0]
                arg_3 = 0
            else:
                arg_3 = sum(other.j_num[:(len(other.j_num) - 1)])
                arg_4 = other.j_num[-1]
            if arg_1 == 0:
                if arg_3 == 0:
                    return f'Получилось число - {-1 * arg_2 * arg_4}'
                else:
                    return ComplexNum(-1 * arg_2 * arg_4, arg_3 * arg_2)
            else:
                if arg_3 == 0:
                    return ComplexNum(-1 * arg_2 * arg_4, arg_1 * arg_4)
                else:
                    return ComplexNum((-1 * arg_2 * arg_4 + arg_1 * arg_3), (arg_3 * arg_2 + arg_1 * arg_4))


num_1 = ComplexNum(6, 5)
print(num_1)
num_2 = ComplexNum(4)
print(num_2)
num_3 = ComplexNum('p', 5)
print(num_3)
num_4 = ComplexNum(6, 5, 9)
print(num_4)
num_5 = ComplexNum(2)
print(num_1 + num_4)
print(num_1 + num_2)
print(num_1 * num_4)
print(num_1 * num_2)
print(num_5 * num_2)
print(num_3 + num_2)
