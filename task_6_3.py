import sys


def make_list_data(file_name):
    line_num = file_name.readline()
    list_data_num = []
    while line_num:
        list_data_num.append(line_num.split('\n')[0])
        line_num = file_name.readline()
    return list_data_num


with open('users.csv', 'r') as file_1:
    with open('hobby.csv', 'r') as file_2:
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

print(dict_datas)
with open('dict_task.csv', 'w') as file_3:
    for key in dict_datas.keys():
        file_3.write("%s,%s\n" % (key, dict_datas[key]))

with open('users_hobby.txt', 'w', encoding='utf-8') as file_4:
    for key, val in dict_datas.items():
        if val != None:
            value = ','.join(val)
            str_dat = f'{key}: {value} \n'
        else:
            str_dat = f'{key}: None \n'
        file_4.write(str_dat)
