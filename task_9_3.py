class Worker:
    _income = {}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income['wage'] = wage
        self._income['bonus'] = bonus


class Position(Worker):
    def get_full_name(self):
        print(f'ФИО: {self.name} {self.surname} должность: {self.position}')

    def get_total_income(self):
        income_all = self._income['wage'] * (1 + self._income['bonus'] / 100)
        print(f'ФИО: {self.name} {self.surname} доход: {income_all:.2f}')


class_1 = Position('Иван', 'Петров', 'Бухгалтер', 100000, 10)
print(class_1.name, class_1.surname, class_1.position, class_1._income)
class_1.get_full_name()
class_1.get_total_income()
