

def write_bekery(sum_sell):
    """
    Добавление данных в файл продаж
    :param sum_sell: новое значение с суммой продаж
    :return: файл с добавленной записью
    """
    with open('bakery.csv', 'a+') as f:
        f.seek(0)
        line = f.readline()
        if line == '':
            f.write(f'1 {sum_sell}\n')
        else:
            while line:
                last_line = line
                line = f.readline()
            f.write(f'{int(last_line.split()[0])+1} {sum_sell}\n')

def read_bekery(param_1=None, param_2=None):
    """
    Получение данных с файла продаж если параметров нет то выводятся все данные
    :param param_1: либо с какого номера записи выводить если нет второго параметра иначе номер записи
    :param param_2: номер записи который выводить
    :return:
    """
    with open('bakery.csv', 'r') as f:
        if param_1 == None and param_2 == None:
            line = f.readline()
            if line == '':
                print('Данных пока нет')
            else:
                while line:
                    print(line.split()[1])
                    line = f.readline()
        elif param_2 == None:
            line = f.readline()
            if line == '':
                print('Данных пока нет')
            else:
                while line:
                    if int(line.split()[0]) >= int(param_1):
                        print(line.split()[1])
                    line = f.readline()
        else:
            if param_1 == None:
                param_1 = 1
            line = f.readline()
            if line == '':
                print('Данных пока нет')
            else:
                while line:
                    if int(line.split()[0]) == int(param_1) or int(line.split()[0]) == int(param_2):
                        print(line.split()[1])
                    line = f.readline()

def edit_bekery(param_1=None, param_2=None):
    """
    редактирования файла продаж с помощью списка
    :param param_1: номер записи
    :param param_2: новое значение
    :return: измененный файл
    """
    key_param_1 = 0
    with open('bakery.csv', 'r') as f:
        if param_1 == None or param_2 == None:
            print('Данных для редактирование не достаточно')
        else:
            line = f.readline()
            if line == '':
                print('Данных пока нет')
            else:
                data_list = []
                while line:
                    if int(line.split()[0]) == int(param_1):
                        data_list.append(line.replace(line.split()[1], str(param_2)))
                        key_param_1 = 1
                    else:
                        data_list.append(line)
                    line = f.readline()
    if key_param_1 == 0:
        print(F'Записи с номером {param_1} нет')
    else:
        with open('bakery.csv', 'w') as f:
            for line in data_list:
                f.write(line)

def edit_bekery_new(param_1=None, param_2=None):
    """
    редактирования списка продаж с помощью создания кэш файла
    :param param_1: номер строки
    :param param_2: новое значение
    :return: измененный файл
    """
    key_param_1 = 0
    with open('bakery.csv', 'r') as f, open('bakery_kash.csv', 'w') as fkash:
        if param_1 == None or param_2 == None:
            print('Данных для редактирование не достаточно')
        else:
            line = f.readline()
            if line == '':
                print('Данных пока нет')
            else:
                while line:
                    if int(line.split()[0]) == int(param_1):
                        fkash.write(line.replace(line.split()[1], str(param_2)))
                        key_param_1 = 1
                    else:
                        fkash.write(line)
                    line = f.readline()
    if key_param_1 == 0:
        print(F'Записи с номером {param_1} нет')
    else:
        with open('bakery.csv', 'w') as f, open('bakery_kash.csv', 'r') as fkash:
            line = fkash.readline()
            while line:
                f.write(line)
                line = fkash.readline()



if __name__ == '__main__':
    #write_bekery(303)
    #read_bekery(2, 4)
    #edit_bekery(2, 33)
    edit_bekery_new(2, 77)

