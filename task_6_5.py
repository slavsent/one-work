import sys


def make_list_data(file_name):
    """
    создает из файла список строк
    :param file_name: файл
    :return: список с данными
    """
    line_num = file_name.readline()
    list_data_num = []
    while line_num:
        list_data_num.append(line_num.split('\n')[0])
        line_num = file_name.readline()
    return list_data_num

def make_file_fiohobby(file_fio, file_hobby, file_res):
    """
    из двух файлов csv с перечнем фамилий и хобби создает объединенный файл
    :param file_fio: файл с фамилиями именами и отчествами через ,
    :param file_hobby: файл хобби через ,
    :param file_res: результирующий файл
    :return: файл в тойже директории
    """
    with open(file_fio, 'r') as file_1:
        with open(file_hobby, 'r') as file_2:
            dict_datas = {}
            list_data_fio = make_list_data(file_1)
            list_data_hob = make_list_data(file_2)
            if len(list_data_hob) > len(list_data_fio):
                sys.exit(1)
            else:
                for i, el in enumerate(list_data_fio):
                    if i > len(list_data_hob) - 1:
                        dict_datas[el] = None
                    else:
                        dict_datas[el] = list_data_hob[i].split(',')


    with open(file_res, 'w', encoding='utf-8') as file_4:
        for key, val in dict_datas.items():
            if val != None:
                value = ','.join(val)
                str_dat = f'{key}: {value} \n'
            else:
                str_dat = f'{key}: None \n'
            file_4.write(str_dat)

if __name__ == '__main__':
    make_file_fiohobby('users.csv', 'hobby.csv', 'users_hobby.txt')