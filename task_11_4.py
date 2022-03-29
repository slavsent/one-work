class MyErr(Exception):
    pass


class Equipment:
    def __init__(self, name, company):
        self.name = name
        self.company = company


class Printer(Equipment):
    def __init__(self, name, company, printer_type, printer_color):
        super().__init__(name, company)
        self.printer_type = printer_type
        self.printer_color = printer_color

    def __str__(self):
        return f'{self.name} {self.company} {self.printer_type} {self.printer_color}'


class Scanner(Equipment):
    def __init__(self, name, company, scanner_color):
        super().__init__(name, company)
        self.scanner_color = scanner_color

    def __str__(self):
        return f'{self.name} {self.company} {self.scanner_color}'


class Xerox(Equipment):
    def __init__(self, name, company, xerox_color, *xerox_param):
        super().__init__(name, company)
        self.xerox_param = list(xerox_param)
        self.xerox_color = xerox_color

    def __str__(self):
        return f'{self.name} {self.company} {self.xerox_color} {" ".join(self.xerox_param)}'


class Computer(Equipment):
    def __init__(self, name, company, computer_os, *computer_param):
        super().__init__(name, company)
        self.computer_param = list(computer_param)
        self.computer_os = computer_os

    def __str__(self):
        return f'{self.name} {self.company} {self.computer_os} {" ".join(self.computer_param)}'


class Warehouse:
    equipments = {}
    list_to_transactions = []

    def __init__(self, name_warehouse):
        self.name_warehouse = name_warehouse

    def to_take(self, to_date, equip, quantity, name_provider):
        try:
            if not isinstance(quantity, int):
                raise MyErr('Количество товара должно быть числом')
        except MyErr as err:
            print(err)
        else:
            if equip not in self.equipments:
                self.equipments[equip] = quantity
            else:
                self.equipments[equip] += quantity
            self.list_to_transactions.append([to_date, equip, quantity, name_provider, 'add'])

    def to_giv(self, to_date, equip, quantity, name_dep):
        try:
            if not isinstance(quantity, int):
                raise MyErr('Количество товара должно быть числом')
        except MyErr as err:
            print(err)
        else:
            if equip not in self.equipments:
                print(f'Товара {equip} нет на складе')
            else:
                if (self.equipments[equip] - quantity) < 0:
                    print(f'Товара {equip} в таком количеству нет, есть: {self.equipments[equip]}')
                else:
                    self.equipments[equip] -= quantity
            self.list_to_transactions.append([to_date, equip, quantity, name_dep, 'sub'])

    def __str__(self):
        res = ''
        for key in self.equipments:
            res += f'{key} количество {self.equipments[key]} \n'
        return res

    def view_transactions(self):
        res = ''
        for el in self.list_to_transactions:
            res += f'{el[0]} {el[1]} {el[2]} {el[3]} {el[4]} \n'
        return res


comp_1 = Computer('PC', 'Aser', 'Windows', 'ОП 4Гб', 'процессор Intel Core i7')
comp_2 = Computer('Notebook', 'Apple', 'Ios', 'ОП 8Гб', 'процессор Intel Core i7')
printer_1 = Printer('Printer', 'HP', 'laser', 'Black')
printer_2 = Printer('Printer', 'Canon', 'jet', 'Color')
print(comp_1)
print(comp_2)
print(printer_1)
print(printer_2)

sklad_1 = Warehouse('Основной')
sklad_1.to_take('20-1-2022', comp_1, 5, 'Ivanov')
sklad_1.to_take('20-1-2022', comp_1, 6, 'Sidorov')
sklad_1.to_take('20-1-2022', printer_1, 4, 'Ivanov')
sklad_1.to_take('20-1-2022', printer_2, 2, 'Petrov')
sklad_1.to_take('20-1-2022', printer_2, 'p', 'Petrov')
sklad_1.to_giv('20-1-2022', comp_1, 1, 'Shop on Dmitrovka')

print(sklad_1)
print(sklad_1.view_transactions())
