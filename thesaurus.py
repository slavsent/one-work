def thesaurus(list_name):
    """
    Функция преоброзования списка имен в словарь
    :param list_name: список имен
    :return: словарь где ключ первая буква имени, а значении имена на эту букву
    """
    list_name_sort = sorted(list_name)
    dict_name = {}
    for name in list_name_sort:
        if name[0] in dict_name:
            dict_name[name[0]].append(name)
        else:
            dict_name[name[0]] = []
            dict_name[name[0]].append(name)
    return print(dict_name)


name_list = ['Ян', 'Клава' , 'Иван', 'Мария', 'Петр', 'Илья']
thesaurus(name_list)

def thesaurus_adv(list_name):
    """
    Функция преоброзования списка имен в словарь
    :param list_name: список имен
    :return: словарь где ключ первая буква имени, а значении имена на эту букву
    """
    list_name_sort = sorted(list_name)
    dict_name = {}
    for name in list_name_sort:
        if name.split()[1][0] in dict_name:
            if name.split()[0][0] in dict_name[name.split()[1][0]]:
                dict_name[name.split()[1][0]][name.split()[0][0]].append(name)
            else:
                dict_name[name.split()[1][0]][name.split()[0][0]] = []
                dict_name[name.split()[1][0]][name.split()[0][0]].append(name)
        else:
            dict_name[name.split()[1][0]] = {}
            dict_name[name.split()[1][0]][name.split()[0][0]] = []
            dict_name[name.split()[1][0]][name.split()[0][0]].append(name)

    dict_name_sort = sorted(dict_name.items(), key=lambda x: x[0])
    return print(dict(dict_name_sort))


name_fam_list = ['Ян Петров', 'Клава Иванова' , 'Иван Михайлов', 'Мария Савельева', 'Петр Смирнов', 'Илья Иванов']
thesaurus_adv(name_fam_list)